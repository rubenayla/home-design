#!/usr/bin/python2
#
# Copyright 2018 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

"""Implementation of a CSV data source that is backed by sqlite.

Assumes that the parameters for each column are encoded in the header row as
follows:

column1_id[key1=value1;key2=value2;key3=value3;....],column2_id[...],...

A local sqlite instance is used to aggregate and filter the data as
required by the DataSource interface.
"""
from __future__ import print_function


__author__ = 'Benjamin Yolken <yolken@google.com>'

import csv
import os
import re
import shutil
import sqlite3
import string
import tempfile

import csv_utilities
import data_source


# Mapping from DSPL to sqlite data types
_DSPL_TYPE_TO_SQLITE_TYPE = {
    'string': 'text',
    'integer': 'integer',
    'float': 'real',
    'date': 'text',
    'boolean': 'text'}


def _CleanDBValue(value, data_type):
  """Clean the argument value for import into sqlite.

  TODO(yolken): Make this more sophisticated, particularly for integer and
                float values.

  Args:
    value: A value from the table
    data_type: The DSPL data type for the value

  Returns:
    A cleaned value that will be accepted by sqlite
  """
  cleaned_value = value.strip()

  if data_type == 'string' or data_type == 'date':
    # Escape single quotes
    cleaned_value = cleaned_value.replace('\'', '\'\'')

    # Add quotation marks around value
    return '\'%s\'' % cleaned_value
  elif data_type == 'integer' or data_type == 'float':
    # Remove dollar symbols
    return re.sub('[\$\,]', '', cleaned_value)
  else:
    return cleaned_value


class CSVDataSourceSqlite(data_source.DataSource):
  """A DataSource around a single CSV file, backed by a sqlite instance."""

  def __init__(self, csv_file, verbose=True):
    """Populate a CSVDataSourceSqlite object based on a CSV file.

    Note that the caller is responsible for closing the csv_file.

    Args:
      csv_file: A file-like object, opened for reading, that has CSV data in it
      verbose: Print out status messages to stdout

    Raises:
      DataSourceError: If CSV isn't properly formatted
    """
    self.sqlite_dir = tempfile.mkdtemp()
    self.verbose = verbose
    self.column_bundle = csv_utilities.ConstructColumnBundle(csv_file, verbose)

    num_columns = self.column_bundle.GetNumColumns()

    # Set up sqlite table to store data
    columns_string = (
        ','.join(
            ['%s %s' % (column.column_id,
                        _DSPL_TYPE_TO_SQLITE_TYPE[column.data_type])
             for column in self.column_bundle.GetColumnIterator()]))

    if self.verbose:
      print('\nCreating sqlite3 table: %s' % (columns_string))

    self.sqlite_connection = sqlite3.connect(
        os.path.join(self.sqlite_dir, 'db.dat'))
    cursor = self.sqlite_connection.cursor()
    cursor.execute('create table csv_table (%s)' % (columns_string))

    if self.verbose:
      print('Adding CSV data to SQLite table')

    body_csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    next(body_csv_reader)

    for r, row in enumerate(body_csv_reader):
      transformed_row_values = []

      # Ignore blank rows
      if row:
        if len(row) != num_columns:
          raise data_source.DataSourceError(
              'Number of columns in row %d (%d) does not match number '
              'expected (%d)' % (r + 2, len(row), num_columns))

        skip_row = False

        for v, row_value in enumerate(row):
          column = self.column_bundle.GetColumnByOrder(v)

          # Handle dropif_val and zeroif_val parameters
          if 'dropif_val' in column.internal_parameters:
            if row_value == column.internal_parameters['dropif_val']:
              skip_row = True
              break
          elif 'zeroif_val' in column.internal_parameters:
            if row_value == column.internal_parameters['zeroif_val']:
              row_value = '0'

          transformed_row_values.append(
              _CleanDBValue(
                  row_value, column.data_type))

        if skip_row:
          continue

        # Add row to sqlite table
        transformed_values_str = ','.join(transformed_row_values)

        try:
          cursor.execute('insert into csv_table values (%s)' %
                         (transformed_values_str))
        except sqlite3.OperationalError as e:
          raise data_source.DataSourceError(
              'Error putting line %d of input file into database: %s'
              '\n%s' % (r + 2, transformed_values_str, str(e)))

    if self.verbose:
      print('Committing transactions\n')

    self.sqlite_connection.commit()

    cursor.close()

    if self.verbose:
      print('Checking concept hierarchies')

    self._CheckHierarchies()

  def GetColumnBundle(self):
    """Get ColumnBundle object for this data source."""
    return self.column_bundle

  def _CheckHierarchies(self):
    """Make sure that each concept instance has no more than one parent."""
    cursor = self.sqlite_connection.cursor()

    for column in self.column_bundle.GetColumnIterator():
      if column.parent_ref:
        if column.total_val:
          where_clause = (
              'WHERE %s != "%s"' % (column.column_id, column.total_val))
        else:
          where_clause = ''

        query_str = (
            'SELECT %s, COUNT(*) FROM (SELECT DISTINCT %s, %s '
            'FROM csv_table %s) GROUP BY %s' %
            (column.column_id, column.column_id, column.parent_ref,
             where_clause, column.column_id))

        try:
          cursor.execute(query_str)
        except sqlite3.OperationalError as e:
          raise data_source.DataSourceError(
              'Error executing query: %s\n%s' % (query_str, str(e)))

        error_values = []

        for row in cursor:
          if int(row[1]) > 1:
            error_values.append(row[0])

        if error_values:
          raise data_source.DataSourceError(
              'Instances of column %s have multiple parent values: %s' %
              (column.column_id, error_values))

    cursor.close()

  def GetTableData(self, query_parameters):
    """Calculate and return the requested table data.

    Uses sqlite to group and aggregate the raw data from the original CSV.

    Args:
      query_parameters: A QueryParameters object

    Returns:
      A TableData object containing the data for the requested table

    Raises:
      DataSourceError: If query against sqlite instance fails
    """
    if query_parameters.query_type == data_source.QueryParameters.CONCEPT_QUERY:
      # This request is for a concept definition table

      # Filter out total values
      where_statements = []

      for column_id in query_parameters.column_ids:
        column = self.column_bundle.GetColumnByID(column_id)

        if column.total_val:
          where_statements.append('%s != "%s"' % (column.column_id,
                                                  column.total_val))
      if where_statements:
        where_clause = 'WHERE ' + ','.join(where_statements)
      else:
        where_clause = ''

      query_str = (
          'SELECT DISTINCT %s FROM csv_table %s ORDER BY %s' %
          (','.join(query_parameters.column_ids), where_clause,
           ','.join(query_parameters.column_ids)))
    elif query_parameters.query_type == data_source.QueryParameters.SLICE_QUERY:
      # This request is for a slice table
      sql_names = []
      dimension_sql_names = []
      where_statements = []

      time_dimension_id = ''

      # Construct a SQL query that selects all parameters (with the necessary
      # aggregations), groups by non-time dimensions, and orders by all the
      # dimensions, with time last.
      for column_id in query_parameters.column_ids:
        column = self.column_bundle.GetColumnByID(column_id)

        if column.total_val:
          where_statements.append('%s != "%s"' % (column.column_id,
                                                  column.total_val))

        if column.slice_role == 'dimension':
          sql_names.append(column_id)
          dimension_sql_names.append(column_id)

          if column.data_type == 'date':
            time_dimension_id = column_id
        elif column.slice_role == 'metric':
          sql_names.append(
              '%s(%s) AS %s' % (column.internal_parameters['aggregation'],
                                column_id, column_id))

      order_sql_names = (
          [d for d in dimension_sql_names if d != time_dimension_id])

      if time_dimension_id:
        order_sql_names.append(time_dimension_id)

      # Handle total values in non-selected columns
      for column in self.column_bundle.GetColumnIterator():
        if column.column_id not in query_parameters.column_ids:
          if column.total_val:
            where_statements.append(
                '%s = "%s"' % (column.column_id, column.total_val))

      if where_statements:
        where_clause = 'WHERE ' + ','.join(where_statements)
      else:
        where_clause = ''

      query_str = (
          'SELECT %s FROM csv_table %s GROUP BY %s ORDER BY %s' %
          (','.join(sql_names),
           where_clause,
           ','.join(dimension_sql_names),
           ','.join(order_sql_names)))
    else:
      raise data_source.DataSourceError(
          'Unknown query type: %s' % query_parameters.query_type)

    if self.verbose:
      print('Executing query:\n%s\n' % (query_str))

    # Execute the query against the sqlite backend
    cursor = self.sqlite_connection.cursor()

    try:
      cursor.execute(query_str)
    except sqlite3.OperationalError as e:
      raise data_source.DataSourceError(
          'Error executing query: %s\n%s' % (query_str, str(e)))

    query_results = []

    for row in cursor:
      query_results.append(list(row))

    cursor.close()

    return data_source.TableData(rows=query_results)

  def Close(self):
    """Close this data source."""
    self.sqlite_connection.close()
    shutil.rmtree(self.sqlite_dir)

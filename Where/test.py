import numpy as np
import matplotlib.pyplot as plt
import rasterio
import os
print(f'CURRENT WORKING DIRECTORY: {os.getcwd()}')

##### GET THE DATA
# https://earthexplorer.usgs.gov/ (GTOPO30 recommended)
# https://gisgeography.com/free-global-dem-data-sources/
# Path to the GTOPO30 dataset
gtopo30_path = "./data/gt30w020n90.tif"

# Open the GTOPO30 dataset using rasterio
with rasterio.open(gtopo30_path) as dataset:
    height_data = dataset.read(1)

#### INSPECT THE DATA




# Create masks
concave_mask = np.zeros_like(height_data, dtype=bool)
tall_mask = height_data > 500
tall_heights = np.ma.masked_where(~tall_mask, height_data) # True = Mask it!

###################
# ALGORITHMS

max_value = 0  # Initialize maximum value
max_row = -1   # Initialize row index
max_col = -1   # Initialize column index

for row_idx, row in enumerate(height_data):
    for col_idx, point in enumerate(row):
        if not np.ma.is_masked(point) and point > max_value:
            max_value = point
            max_row = row_idx
            max_col = col_idx

print(f"Highest Point: {max_value} meters")
print(f"Coordinates: Row {max_row}, Column {max_col}")










####################

# print(height_data)
# print(tall_mask)
# print(tall_heights)
# Set the mask based on the concave sections you've identified

plt.figure(figsize=(10, 10))
# plt.imshow(height_data, cmap='rainbow') # terrain
plt.imshow(height_data, cmap='rainbow', alpha=0.5)  # Highlighted concave sections
plt.scatter(max_col, max_row, color='red', marker='o', s=50, label='Highest Point')
plt.colorbar(label='Elevation')
plt.title('GTOPO30 Height Map with Highlighted Concave Sections')
plt.show()

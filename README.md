# Home Design

This repository contains the documentation for my home design project. The documentation is built using MkDocs.

## Project Structure

*   `/docs`: Contains the Markdown source files for the MkDocs documentation. All content that should be part of the final website goes here.
*   `/assets`: Holds all the raw files and resources that are *not* part of the documentation website itself, but are related to the project (e.g., CAD files, data files, etc.).
*   `/stuff`: A general-purpose directory for random files and notes that don't fit into the other categories. This directory is not part of the MkDocs build.

# MKDocs

## ✅ Preview locally

```bash
uv venv --python 3.12.3
uv sync
uv run mkdocs serve
# Open http://127.0.0.1:8000 in your browser
```

Or use a specific port:

```bash
uv run mkdocs serve -a 127.0.0.1:8001
```

To build the static site:

```bash
uv run mkdocs build
# Output: site/
```

---

## 🚀 Deploy to GitHub Pages

Recommended (modern): push to `main`. GitHub Actions builds and deploys the site on successful builds using the workflow in `.github/workflows/docs.yml`. This does not use a `gh-pages` branch.

Alternative (legacy): use the MkDocs built-in deploy command, which publishes to a `gh-pages` branch:

```bash
uv run mkdocs gh-deploy --force
```

If you use the legacy method, set GitHub Pages to deploy from the `gh-pages` branch in repo settings.

---

## 📟 PDF Export (optional)

PDF export is disabled by default to speed up builds. To export PDFs explicitly:

```bash
EXPORT_PDF=true uv run mkdocs build
# Outputs: site/pdf/kart-documentation.pdf
```

---


## 🗂 Branch structure

- `main` → Markdown source and tooling
- GitHub Pages → Auto-generated static site via Actions

Do all edits on `main`.

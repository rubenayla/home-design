# Home Design

This repository contains the documentation for my home design project. The documentation is built using MkDocs.

# MKDocs

## ✅ Preview locally

```bash
poetry run mkdocs serve
# Open http://127.0.0.1:8000 in your browser
```

Or use a specific port:

```bash
poetry run mkdocs serve -a 127.0.0.1:8001
```

To build the static site:

```bash
poetry run mkdocs build
# Output: site/
```

---

## 🚀 Deploy to GitHub Pages

```bash
poetry run mkdocs gh-deploy
```

> GitHub Pages must be enabled in the repo settings (branch: `gh-pages`).

---

## 📟 PDF Export (optional)

PDF export is disabled by default to speed up builds. To export PDFs explicitly:

```bash
EXPORT_PDF=true poetry run mkdocs build
# Outputs: site/pdf/kart-documentation.pdf
```

---


## 🗂 Branch structure

- `main` → Markdown source
- `gh-pages` → Auto-generated static site (read-only)

Do all edits on `main`.

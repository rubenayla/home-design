<!-- read in full — kept under 150 lines -->
# Home Design - Agent Guide

This repo contains documentation for a home design project, built with MkDocs.

## .agents/ File System

**Read in full** (loaded every session, kept concise):
- `tasks.md` — Agent task board (TODO / In Progress / Done)

**Consult selectively** (grep, never read in full):
- `error-log.md` — Append-only log of mistakes with root cause and prevention
- `notes.md` — Design decisions, research findings, and rationale
- `../history.md` — Dated log of what happened/was learned (in repo **root**, not `.agents/`, per project convention)

## Project References

- **Site**: MkDocs documentation, deployed via GitHub Actions on push to `main`
- **Stack**: MkDocs + Python (uv)
- **Content**: `/docs/` (Markdown source), `/assets/` (CAD, raw files), `/stuff/` (loose notes)
- **Human tasks**: `tasks.md` in repo root (do not act on items unless explicitly asked)

## Workflow

1. **Before starting**: Read `AGENTS.md` + `.agents/tasks.md`. Grep error-log for relevant entries.
2. **Plan before building** for non-trivial tasks.
3. **Verify your work**: preview MkDocs output, check links, validate visuals.
4. **Commit safety**: `git status` + `git diff` before committing. Never force-push.
5. **Log mistakes**: Append to `.agents/error-log.md` with root cause + prevention.
6. **Temp files go to `/tmp/`**, never in the repo.

## Task Management

Status markers in `.agents/tasks.md`:
- `- [ ]` Ready
- `- [->]` In Progress (with agent ID and date)
- `- [x]` Done (with date)
- `- [!]` Blocked (with reason)

## Useful Commands

```bash
uv run mkdocs serve          # Preview at http://127.0.0.1:8000
uv run mkdocs build          # Build static site to site/
```

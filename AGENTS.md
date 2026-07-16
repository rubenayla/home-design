<!-- read in full — kept under 150 lines -->
# Home Design - Agent Guide

This repo contains documentation for a home design project, built with MkDocs.

## Project Knowledge Files

**Read in full** (loaded every session, kept concise):
- `tasks.md` — The task board, in repo **root** (not `.agents/`)

**Consult selectively** (grep, never read in full):
- `.agents/error-log.md` — Append-only log of mistakes with root cause and prevention
- `.agents/notes.md` — Design decisions, research findings, and rationale
- `history.md` — Dated log of what happened/was learned, in repo **root** (not `.agents/`, per project convention)

## Project References

- **Site**: MkDocs documentation, deployed via GitHub Actions on push to `main`
- **Stack**: MkDocs + Python (uv)
- **Content**: `/docs/` (Markdown source), `/assets/` (CAD, raw files), `/stuff/` (loose notes)
- **Tasks**: `tasks.md` in repo root — the single board (see Task Management below)

## Workflow

1. **Before starting**: Read `AGENTS.md` + root `tasks.md`. Grep error-log for relevant entries.
2. **Plan before building** for non-trivial tasks.
3. **Verify your work**: preview MkDocs output, check links, validate visuals.
4. **Commit safety**: `git status` + `git diff` before committing. Never force-push.
5. **Log mistakes**: Append to `.agents/error-log.md` with root cause + prevention.
6. **Temp files go to `/tmp/`**, never in the repo.

## Task Management

One `tasks.md` per repo, at the root — it is the single board for both the user and agents. There is
intentionally **no `.agents/tasks.md`** in this repo; never create one. Tasks are the project's tasks
regardless of who does them, so a second board only produces duplicates and stale entries. Add
discovered work to root `tasks.md` directly.

Status markers in root `tasks.md`:
- `- [ ]` Ready
- `- [->]` In Progress (with agent ID and date)
- `- [x]` Done (with date)
- `- [!]` Blocked (with reason)

## Useful Commands

```bash
uv run mkdocs serve          # Preview at http://127.0.0.1:8000
uv run mkdocs build          # Build static site to site/
```

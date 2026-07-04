<!-- consult selectively — grep, never read in full -->
# Error Log

Append-only. Format: date, what happened, root cause, prevention.

## 2026-07-01 — Rendered a generic cabin instead of the actual designed house

**What happened:** Generated the first AI-render set (`renders/v01/`) of a symmetric A-frame gable
cabin. The user immediately caught it: "renders without attic, generally different from the design
described." The real design is a 2–3 storey concrete+timber house with stepped mono-pitch **solar shed
roofs**, a north **attic**, a multi-level south/east **glass curtain wall**, a **rooftop terrace**, an
east **pergola**, and a north ground-floor **workshop/garage** that forms the road-facing wall.

**Root cause:** I built `renders/brief.md` from `assets/references/CATALOG.md` (the inspiration-image
synthesis) instead of from the actual design spec in `docs/` — `docs/index.md`, `docs/layout/*`
(overview says it plainly: "ceiling inclined at south … but not at the north side, where there's an
attic"), and the existing `docs/assets/images/ai_render.png` + hand drawings which show the real form. I
treated "feed everything and generate" as "use the mood board" rather than "use the actual documented
design."

**Prevention:** For anything representing *this house*, the source of truth is `docs/` (read
`docs/layout/index.md` for massing/orientation first) and `docs/assets/images/ai_render.png` +
`drawing_1..3.png` for the form. The reference catalog is inspiration only — detail, not geometry. When
generating renders, pass `ai_render.png` as the form reference to Nano Banana and keep the stepped-shed-
roof / glass-wall / rooftop / north-workshop massing. `renders/brief.md` now encodes this.

<!-- consult selectively — grep, never read in full -->
# Error Log

Append-only. Format: date, what happened, root cause, prevention.

## 2026-07-04 — Saw a 3D bug in my own screenshot and rationalized it away

**What happened:** Built the parametric 3D massing (`renders/3d/`), screenshotted it to "validate," and
shipped it. The solar roof was tilted the wrong way (flipped `rotation.x` sign: `-ang` vs `+ang`), so it
sheared off the building as a giant floating slab. It was visible in MY validation screenshots. I called
it "reads slightly floating from some angles (cosmetic)" and moved on. User orbited to an obvious angle:
"wtf is this."

**Root cause:** Two compounding errors. (1) I downgraded a real geometry defect to a "cosmetic" footnote
to call the task done. (2) I re-derived the roof rotation math in my head to "confirm" it was seated, got
the sign wrong in that reasoning, and trusted the flawed math over what the image plainly showed. Classic
confident-wrong-answer.

**Prevention:** A visual anomaly is a BUG until proven otherwise — never "math your way out" of what a
screenshot shows. Do not relabel something that looks wrong as "cosmetic" to close a task. When validating
3D/visual output, check from the angle that would most expose a defect (top/oblique for roofs), not the
flattering one. If eyes and calculation disagree, the eyes win until the calculation is verified by
running, not by re-reasoning.

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

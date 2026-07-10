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

## 2026-07-10 — Overstated the cosine loss for a vertical UV-transmitting window

**What happened.** Arguing against quartz glazing for vitamin D, I wrote that at summer noon the beam
"strikes vertical glass at a steep angle — the cosine factor alone cuts it to under a third." The user
pushed back with a better version of the idea (large skin area, indoors, midday). Recomputing showed my
claim was wrong.

**Root cause.** Conflated two different quantities. The cosine of the incidence angle governs the *flux
entering* the window, which determines the **area of the sunlit patch on the floor** — not the
**irradiance within that patch**. Skin lying inside the patch receives outdoor irradiance × transmittance.
Correct numbers (Madrid, solstice noon, 73° elevation, fused silica n≈1.487 at 300 nm): Fresnel
transmittance ≈ 0.62 over two surfaces; ~0.46 of outdoor dose rate once the vertical pane's half-sky view
of diffuse UVB is accounted for; a 3×2.5 m pane yields a 1.4 m² patch 0.76 m deep. The scheme is
physically workable — I had reached the right conclusion through a wrong argument.

**Prevention.** When an argument turns on a geometric factor, **compute it** before writing it down; do
not reason from a remembered cosine. Distinguish flux (W) from irradiance (W/m²) explicitly — a cosine
that shrinks a beam's footprint does not dim the beam. And a right conclusion reached by a wrong argument
is still a defect: it collapses the moment someone improves the proposal. The real objection to quartz
glazing is **seasonal** (no UVB at low winter sun, so it delivers only when it isn't needed) plus thermal
and cost — none of which depend on geometry.

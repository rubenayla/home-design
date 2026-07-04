# Parametric 3D massing model

Interactive massing model of the house, built from the design in `docs/`. Explore it in 3D and change
dimensions live — a first-principles massing, not a construction model.

## Open it

Just double-click **`index.html`** (or `open renders/3d/index.html`). No server or internet needed — the
libraries (three.js, OrbitControls, dat.gui) are vendored in `vendor/` and it's plain `<script>` tags, so
`file://` works.

## Use

- **Drag** to orbit · **scroll** to zoom · **right-drag** to pan.
- **Sliders** (top-right) change dimensions live: footprint (W–E / N–S), floors, floor height, ground/
  workshop height, roof rise (pitch), south overhang, rooftop-terrace size.
- **Sun** panel moves the light — set azimuth ≈ 180 (south) and it lights the solar roof and casts the
  overhang's shadow, so you can eyeball passive-solar shading. **Show** toggles solar/trees/pergola.
- **N/S/E/W** ground labels keep orientation explicit (solar roof + glass = south; garage = north).

## What it represents (from the docs)

Single continuous volume; mono-pitch roof high at the north (attic) sloping down south, clad in solar;
floor-to-ceiling glass on the south + east; solid concrete north with the ground-floor workshop/garage;
rooftop-terrace pocket set back on the north; east pergola; deciduous fruit trees south, evergreens north.

## Known simplifications (v1)

- Massing only — no interior rooms, no real wall thicknesses or openings besides the garage door.
- The solar roof slab sits *approximately* on the mass (reads slightly floating from some angles).
- Ground floor is one block; the workshop/living split isn't modelled internally.

Refine by editing `index.html` (all geometry is in the `rebuild()` function, parameters in `P`).

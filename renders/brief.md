<!-- consult selectively — the evolving spec that image prompts are generated from -->
# Render brief — Rubén's house

Derived from the **actual design docs** (`docs/index.md`, `docs/layout/*`, `docs/systems.md`,
`docs/glazing.md`) and the existing `docs/assets/images/ai_render.png` + hand drawings — NOT from the
reference-inspiration catalog. Renders live in `renders/vNN/`. Use `ai_render.png` as the form reference.

## Massing / form (get this right — v01 got it wrong)

- **2–3 storeys + a usable rooftop.** Tall rectangular volume, NOT a symmetric gable cabin.
- **Stepped mono-pitch (shed) roofs inclined toward the SOUTH, fully clad in solar panels.** Two roof
  planes at different heights (a taller north block stepping down south). The **north side is vertical
  with an attic** under it — the roof is NOT inclined there.
- **Rooftop terrace** between/beside the roof planes: timber railing, lounge seating, plants, a shade
  structure, fire-pit/hammock/reading spot. The floor/ceiling extends south (shade) and east (covers the
  entrance from rain).
- **South & east façades are floor-to-ceiling curtain-wall glass**, revealing multiple interior levels
  connected by an internal staircase. **Deep roof overhang** over the south glass (blocks high summer
  noon sun, admits low winter sun). Overhang has a drip-cut underside.
- **North = the house is the wall.** No north windows. The ground-floor **workshop/garage** sits right at
  the property's north edge with its **big garage door facing the road**; it buffers road noise and IS
  the north wall (no separate north yard).
- Structure/material: concrete + timber, warm wood accents, lots of glass.
- **Trees:** low **deciduous fruit trees to the south** (seasonal shade, don't block winter sun or the
  panels); **tall evergreens to the north and west** (privacy, wind, never shade panels/winter sun).

## Orientation & site (northern hemisphere, coldish, south-facing hillside)

- House at the **north** edge of the property; ground slopes down to the **south**.
- **Enter at the east** (stairs up to the attic/floors); **cars/workshop at the north** off the road.
- Sun strategy: allow **sunrise (east, through entrance)**, block **noon**, allow some **sunset (west)**.
  Awnings block, inner curtains diffuse. Rooms run long **north–south** so convection distributes heat.
- Off-grid: many solar panels, battery storage, big rainwater collection + filtering, high water tank
  up-north for passive pressure.

## Rooms (for interior views)

- **Workshop + garage** (ground, north, coldest): huge, double-height ("tall workshop" void), concrete
  floor, movable separator between cars and shop, ceiling beams for lifting, dust extraction. Pegboard
  tool wall + huge drawer/assortment-box cabinets + shelving; metalwork (lathe, mill, drill press,
  welding table), woodwork (table saw, router), electronics bench.
- **Entrance** (east, maybe lower level): coats/shoes/keys, EUC charging rack, trash bins, through-wall
  package mailbox, energy dashboard + breakers. The house wall itself holds the mailbox.
- **Kitchen** (west of entrance, storage/fridge to the north): American kitchen, tall **island** with
  sink + tap + backless 3-legged stools on all sides, induction hob in the corner, hanging shelving over
  the island, big deep food shelving by the fridge; openable window with external countertop.
- **Loft workspace** (the "attic"): huge ~90cm adjustable corner **table that wraps the user**, with bin
  holes; **pegboard** with ~32 sockets (Type N + universal + USB-C), shelving wall, smart-home section.
  Overlooks the double-height glazed living volume.
- **Bedroom**: tiny, cozy, tatami + futon on an elevated platform, east-facing (wake with sunrise),
  separate from the loft (noise/light). Carpet tiles.
- **Rooftop**: lounge under the stars, shade structure, fire pit, hammock, plants, sunset/sunrise views.

## View list

- `exterior_south` — hero, south/east glass façade + stepped solar shed roofs + rooftop terrace + east
  pergola, fruit trees + fire pit in front (refine `ai_render.png`).
- `interior_living` — multi-storey glazed living volume with internal staircase, wood + concrete.
- `workshop_garage` — the double-height north workshop/garage with the big door.
- `loft_workspace` — the wrap-around work table + pegboard-with-sockets + shelving, over the glass void.
- `rooftop` — the rooftop terrace at sunset.

## Corrections from v02 feedback (2026-07-03) — get these right in v03

- **Solar vs rooftop are NOT interchangeable — don't flip them.** The big **south-facing inclined roof
  is the SOLAR ARRAY** (that's why it's tilted south — max generation). The **rooftop terrace is a small
  flat pocket set BACK on the higher north part of the roof**, behind/above the solar slope — it must NOT
  occupy the prime south-facing solar surface.
- **Workshop must read as ISOLATED, not open-plan.** It's a sealed enclosed volume (dust, noise, fumes,
  fire) reached from the house only through a door / mudroom-airlock. Do NOT show it open to the living
  space or kitchen — that would spread mess through the house. Its own double-height is fine; the seal
  from living areas is the point.
- **Consistency:** lock ONE correct exterior, then condition every interior/other view on that exact
  image so it's the same building (image-to-image), rather than re-describing from scratch each time.
- `loft_workspace` from v02 is good — keep its character (wrap-around bin-hole table, pegboard-with-
  sockets, shelving wall over the glazed void).
- **Workshop = integrated but sealed** (user decision 2026-07-03): it's the ground-floor north end of the
  same structure, sealed from living by walls + **one internal door** — the point of that door is to park
  the car in the garage and walk straight into the house. In renders just show it enclosed/sealed (no
  open void into living); the door itself doesn't need to be shown precisely.
- **Consistency ceiling (honest):** pure Nano Banana gives *style* consistency, not geometric identity —
  it has no 3D model of the building, so interior and exterior can't be guaranteed to be literally the
  same rooms. Lock a shared palette + the mono-pitch solar-roof ceiling line across all interior prompts
  so they read as one house. True geometric identity would need a 3D massing model (Blender/SketchUp) +
  ControlNet/Blender renders — a bigger step, only if wanted.

## Notes

- v01 (symmetric gable cabin) was generated from `assets/references/CATALOG.md` by mistake — kept for
  reference but does NOT represent the design. v02 got the form right but flipped solar/terrace and
  showed the workshop too open. v03 uses this brief + `ai_render.png` + the corrections above.

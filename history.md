<!-- consult selectively — grep, never read in full -->
# History

Dated log of what happened and what was learned, oldest-first, at topic level.

## 2026-06-29 — Reference album imported and classified; AI-render workflow scoped

**Reference images.** Pulled the shared Google Photos album of home-design inspiration into
`assets/references/` (301 files: 300 photos + `019_VID_20190903_001445.mp4`). All classified by 6
parallel vision subagents into `assets/references/CATALOG.md` (category · what it shows · design idea),
with an 11-theme synthesis on top. User confirmed **no privacy concern** with the images, so they're
safe to commit/publish if wanted. Currently untracked. The 11 recurring design convictions the album
keeps arguing for: small footprint + big vertical volume (lofts/mezzanines/vaults); dissolve-the-wall
glazing toward the view (sliding/bi-fold/frameless) with adjustable shading; passive-solar-first
(sun-angle/overhang sizing, water-column thermal mass, full Köppen-map set) then HRV + ground-source
heat pump; energy independence baked in (rooftop PV + solar-thermal, Tesla Solar Roof, battery, EV
charging); workshop as a first-class room (French-cleat/pegboard walls, labeled bin grids); one modular
see-through storage system (IKEA SAMLA / BrickBox cubes, cubes double as dividers); consolidated low-tech
wet-zones (curbless trays, wall-hung bidet-jet toilets, plumbing along one wall); prefab/modular delivery
(crane/truck onto a stone plinth); three-legged stools everywhere (stable on uneven floors); design
verified against the human body (turning/reach circles in layouts); and a literal first-principles
outlier — a Mars-habitat competition poster. **Gaps to fill next pull:** structural systems/foundations,
real cost/BOM numbers, fire egress, acoustics, off-grid water/septic.

**Google Photos scrape lesson.** An HTML scrape is NOT a complete enumerator for a GPhotos shared album,
especially videos. Photos + video *posters* live on `lh3.googleusercontent.com/pw/...`; actual video
streams live on a different host, `video-downloads.googleusercontent.com/...`. My regex only matched the
`pw` host, so videos were invisible and I wrongly reported the download as "complete." Worse, those
`video-downloads` URLs are short-lived signed links that return 400/500 to plain `curl` even when fresh —
the endpoint needs the browser's JS/session. **Takeaway:** for GPhotos videos use the logged-in Chrome
(osascript) or a Google Takeout export, and never claim a scrape is "complete" when videos are involved.
The one missed item (`IMG_0361.MOV`, a personal clip) was left out at the user's request; full album =
302 items (300 photos + 2 videos), local set = 301.

**AI-render workflow for the house (my proposal, not yet built).** Claude Design (Beta) is a visual-design
canvas (prototype/slides/document/wireframe/animation) — good for a concept *deck* or landing page of the
project, but NOT a CAD tool and NOT a photoreal image generator; it won't render the house. Claude itself
has no native image generation and no image-gen MCP is connected in this session. So the ideal
"feed everything + iterate against the docs" loop needs a dedicated image model, with a clean split of
labor: **the image model owns the pixels; Claude owns the brief, the reference selection, and the
critique-against-docs loop.** Proposed repo structure: `renders/brief.md` (evolving spec distilled from
CATALOG.md's convictions) → user generates in the chosen tool → outputs land in `renders/vNN/` → Claude
critiques each render against the docs (honors passive-solar overhangs? glazed gable? workshop wing?) →
revise brief → repeat.

Tool options, ranked by goal:
- **Geometry-faithful to the actual plan** → Stable Diffusion / Flux + **ControlNet** (condition on a
  floor-plan line drawing via Canny/edges, or a depth map from a rough Blender/SketchUp massing). Only
  path that keeps *your* real layout instead of drifting to stock-render houses. Runs in ComfyUI /
  Automatic1111, local GPU or hosted (Replicate/RunDiffusion). More setup; that's the price of control.
- **Conversational multi-image iteration ("keep the layout, change the roof")** → Gemini image
  (Nano Banana) or GPT-image.
- **Best aesthetics, fast, refs as style** → Midjourney (`--sref`/`--cref`, image prompts); weak on hard
  geometric control, iteration is re-roll not edit.

**ControlNet (one-liner):** a 2023 add-on for diffusion models that locks output geometry to a structural
input you provide (edges / depth / scribble / segmentation) while text controls style — so a floor plan or
massing model becomes a faithful render of *that* building, consistent across angles and material variants.

**User's available tooling (2026-06-29):** has **Gemini Pro, which includes Nano Banana** — so the
cheapest path right now is Nano Banana for conversational ref-based iteration, no extra setup.
**Open question to resolve:** can Claude drive Nano Banana itself (e.g. via a Gemini API / MCP bridge) to
run the generate→critique loop autonomously, or is the human-in-the-loop hand-off (Claude writes brief →
user generates in Gemini → Claude critiques) the practical path? Also unresolved whether ControlNet's
geometry faithfulness is worth the ComfyUI setup over Nano Banana's easier iteration for this project's
stage. Decide before building `renders/`.

## 2026-06-30 — Nano Banana reachable from Claude Code via `agy` (no API key) — CONFIRMED WORKING

Investigated how to actually drive Nano Banana (Gemini image gen) and **verified an end-to-end path that
needs no separate API key** — it reuses the user's existing Google Antigravity / Gemini Pro OAuth.

**What worked (the recommended path):** the `agy` CLI (Google Antigravity CLI, `/opt/homebrew/bin/agy`,
v1.0.10) is already logged into `ruben.jimenezmejias@gmail.com` and has Nano Banana built in. Claude can
generate images straight from Bash in print mode:
```bash
agy --dangerously-skip-permissions --print-timeout 3m0s \
  -p 'Generate an image: <prompt>. Save it as /abs/path/out.png. Then print only the file path.' </dev/null
```
Test on 2026-06-30 produced a correct 1024×1024 PNG (red circle on textured paper) in ~one run. So the
full **generate → critique-against-docs → regenerate loop can be autonomous** — no human hand-off, no key.
Notes: `agy` backgrounds for ~1–2 min per image; it's an agent, so phrase the prompt as "generate AND
save to <abs path>, then print the path". `agy models` lists only text models (Gemini 3.5 Flash, 3.1 Pro,
Claude, GPT-OSS) because image gen is a *tool* it invokes, not a selectable model.

**Two fallback paths (documented, not needed unless the `agy` route breaks):**
- **`nano-banana-antigravity` skill** (github.com/sundial-org/awesome-openclaw-skills,
  `skills/nano-banana-antigravity/scripts/generate_image.py`, 417 lines). Reads a `google-antigravity`
  OAuth *refresh* token, refreshes it at `oauth2.googleapis.com/token`, then POSTs to Google's CloudCode
  API (`cloudcode-pa.googleapis.com`) with `IMAGE_MODEL_PRO` (Nano Banana Pro / Gemini 3 Pro Image),
  falling back to regular Nano Banana. Flags: `-p` prompt, `-f` filename, `-i` input image (repeatable,
  for edits/composites), `-a` aspect ratio (1:1…21:9), `-r` resolution (1K/2K/4K). No API key — BUT it
  expects creds at OpenClaw/opencode paths (`~/.openclaw/...`, `~/.config/opencode/antigravity-accounts.json`);
  the user's token lives in Google's `agy`/`~/.gemini` store, so this script would need its cred-loader
  re-pointed to work. Saved a copy at `/tmp/generate_image.py` during the investigation.
- **Direct Gemini API** via `google-genai` SDK, model id `gemini-2.5-flash-image`. Cleanest/most robust
  but needs a *separate free* API key from aistudio.google.com (free tier ~500 images/day at 1024², a
  different credential from the Gemini Pro subscription). `genai.Client()` reads `GEMINI_API_KEY` from env;
  pass reference images as base64 `image` parts in `interactions.create(...)` for editing/iteration. Each
  paid image ≈ 1290 output tokens ≈ $0.039.

**Nano Banana capabilities relevant to the house loop:** text→image + image editing, fuses up to ~20
reference images while holding subject identity across edits (good for "keep the layout, change the roof"),
SynthID invisible watermark on all output.

**Decision:** use the **`agy` print-mode path** for the `renders/` loop — zero setup, reuses the existing
subscription, fully autonomous. Still TBD whether to feed it a floor-plan/massing image (`-i`-style ref)
for geometry fidelity vs. pure-prompt concept exploration; start with concept exploration.

**Convention note:** this repo (and all of the user's repos) keeps `history.md` in the **repo ROOT**, not
in `.agents/`. Moved here 2026-06-30.

## 2026-07-04 — 3D approach: hand-coded Three.js failed; AI-image→CAD not ready; use floor-plan tools

**What happened.** Built a parametric Three.js massing model (`renders/3d/`, orbit + dimension sliders +
movable sun + N/S/E/W labels). It works for *massing*, but hand-placing boxes by typed coordinates
produced repeated geometry bugs: the solar roof was tilted the wrong way (flipped `rotation.x` sign) and
sheared off as a floating slab; the pergola landed east instead of south; the roof/terrace clipped the
floor. User (rightly) lost confidence that hand-coded geometry scales to a detailed multi-room house with
doors without clashing. See `.agents/error-log.md` 2026-07-04 (I saw the roof bug in my own screenshot and
rationalized it as "cosmetic").

**Investigation — is AI-CAD-from-images ready? Verdict: NO for an editable building model.**
- *Image → editable parametric CAD*: **GenCAD** (MIT, 2026) does exactly this but is research-only (no
  product/API) and needs clean isometric CAD line-drawings, not photos/renders. Not usable.
- *Text/image → parametric CAD*: **Zoo.dev / KittyCAD** is the real leader (free tier, precise B-Rep via
  their KCL language) but scoped to mechanical *parts*; explicitly "not there yet" for complex multi-body
  assemblies and "dimensional accuracy cannot be expected." A house is out of scope. Consensus: hybrid
  AI+human, not autonomous.
- *Image → 3D mesh*: **Meshy / Tripo / Rodin** are fast and mature but output a frozen, non-editable,
  irregular-topology "blob roughly the right shape" — a photo in 3D, not a design.

**What IS ready for rooms/doors/no-clash: floor-plan-based building tools** (building-aware walls/doors/
windows primitives, so geometry can't clash like hand-placed boxes; many export BIM/CAD): **Planner5D**,
**Snaptrude** (BIM), **Drafted** (DXF/GLB/IFC export), **Maket**, **Arcadium 3D** (free). These are WYSIWYG
apps the USER drives — I can't operate them.

**Blender:** a good Blender MCP DOES exist (`ahujasid/blender-mcp` + official `blender.org/lab/mcp-server/`)
— create/modify objects, materials, scene inspection, and **arbitrary Python exec**. It's just NOT
connected in this session's config (servers here: fusion360, kicad, playwright, notion, qmd, gmail/cal/
drive, whatsapp, telegram, voicemode). Even if connected, it wouldn't fix clashing: it's freeform mesh
authoring (same as the Three.js trap), with **no building-aware constraints and no clash detection**.
Fusion 360's MCP (already connected) is better for the "no crash" goal because it exposes
**`check_interference` + `measure_distance`** — programmatic collision verification Blender-MCP lacks.
Blender + **Bonsai (BlenderBIM)** / **Archipack** is real architecture but steep, and driving those
reliably through the MCP's Python exec is brittle. Blender's real value here: rendering/animation of a
model produced elsewhere.

**Decided division of labour:** keep the simple 3D model for **massing/orientation/sun only**; do detailed
rooms/doors in a **floor-plan tool the user drives**; I stay on `docs/`, translating them into a clean
floor-plan spec (per-floor room list, dimensions, adjacencies, orientation) and critiquing output — no
hand-placed geometry.

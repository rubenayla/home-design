# Glass & Shading

The house envelope is largely floor-to-ceiling glass (see [Layout overview](layout/index.md)). That glass is the single biggest path for heat in/out and for light and privacy, so two decisions matter: **what glass to install**, and **how to cover it** for darkness, privacy, and night heat-loss.

For the *automation* that opens/closes the coverings by temperature, see [Systems → HVAC](systems.md).

## Glass

Large glazed walls are a thermal weak point — they gain heat in summer and lose it at night in winter. Choices that help:

- **Double or triple glazing** with an inert gas fill. Triple is worth it for the big north/cold-facing walls; the night heat-loss reduction compounds with whatever shading sits over it.
- **Low-e coatings** to cut radiant loss without darkening the room.
- **Solar-control glazing** on the south/west exposures to limit summer gain, balanced against wanting winter sun (the deciduous fruit trees at the south already do seasonal shading — see [Layout overview](layout/index.md)).

## UV: don't glaze for vitamin D

**Decision: normal glazing. Do not install quartz/fused-silica glass to let UVB in.**

The tempting idea: ordinary glass passes UVA and blocks UVB, so swap it for quartz (which transmits down to ~200 nm) and you'd get the vitamin D without the "bad" UVA. It doesn't work, and the reasoning inverts twice.

**UVB is the more carcinogenic band, not the safe one.** UVA is the milder mutagen per photon. UVB (280–315 nm) is absorbed directly by DNA and forms cyclobutane pyrimidine dimers; per unit energy it is on the order of a thousand times more erythemally effective than UVA. Both contribute to skin cancer. Letting UVB in while UVA still comes through adds the more dangerous band. The "UVA has no benefit" half is also contested — there is evidence that UVA mobilises nitric oxide from stores in the skin and lowers blood pressure, independent of vitamin D.

**Low winter sun carries no UVB anyway.** UVB is filtered by stratospheric ozone, and the ozone path length grows fast as the sun drops. Below roughly 30° solar elevation almost no cutaneous vitamin D synthesis happens — the shorthand is *if your shadow is longer than you are tall, you are making none*. That produces the "vitamin D winter": above about 35° latitude you can stand outside naked at noon in December and synthesise nothing. Since the [location filters](location.md) target 30–60°, the site will almost certainly sit in that band. Quartz glazing would faithfully transmit a winter UVB flux of approximately zero.

**The geometry is *not* the problem — it works, and it's worth being precise about why.** The tempting dismissal is "the cosine factor kills the beam at a vertical pane." That is wrong: the cosine factor governs how much flux *enters*, which sets the **size of the sunlit patch on the floor**, not the irradiance inside it. Skin lying in that patch gets outdoor irradiance × transmittance. At Madrid's summer-solstice noon (73° elevation), a vertical fused-silica pane transmits **~62%** (Fresnel, two surfaces, n≈1.487 at 300 nm); losing half the diffuse skylight to the pane's half-sky view brings the total to roughly **46% of the outdoor dose rate** — about 2.2× the exposure time. A 3 × 2.5 m pane throws a **1.4 m² patch, 0.76 m deep**. You could lie in it. Sunbathing indoors behind quartz is physically sound.

**It fails on season instead, and that is fatal.** The pane only delivers when the sun is high enough to carry UVB — i.e. summer, the season you are *least* likely to be deficient, when incidental outdoor exposure already saturates you and stepping outside costs nothing. In winter, when deficiency actually bites, solar elevation falls below threshold and the pane transmits zero. **It works exactly when it isn't needed and fails exactly when it is.** No amount of glazing engineering fixes that; the filter is stratospheric ozone, not the window.

**And the sun patch is the worst place in the house to put one.** That 0.76 m strip sits against the glass at solar noon in July. Quartz means no low-e, no double glazing, no solar control — a thermal hole in precisely the wall this page says should carry solar-control glazing.

**Dose and risk are the same variable.** A useful vitamin D dose is roughly a third of a minimal erythemal dose over a quarter of the body, a few times a week. Vitamin D synthesis saturates (previtamin D3 photoisomerizes to inert lumisterol and tachysterol, capping at ~10–15% of available 7-dehydrocholesterol); DNA damage does not. So every minute past the plateau is pure risk for zero return — and UVB is the band doing both jobs.

**It also fights every other glass decision on this page.** Fused silica is optical stock, not architectural — orders of magnitude over float glass (unpriced; large panes may not be manufactured at all), no low-e coating, no double glazing, and it conflicts with safety-glazing codes that want tempered or laminated. Quartz also *solarizes*: prolonged short-wavelength exposure builds colour centres that slowly reduce UV transmission, so it degrades at the one job it was bought for.

**Instead:**

- **A screened corner of the [rooftop](layout/rooftop.md)** is the architectural answer, and it is already in the plan. Large-area midday exposure, full sky (so *all* the diffuse UVB, which the window discards), better dose rate than any pane, complete privacy, zero glazing compromise, no extra cost. If the appeal of "indoors" was privacy rather than convenience, build this instead.
- **Vitamin D3, 1000–2000 IU/day.** A few euros a year, settles it — and it is the only option that works in winter.
- **A narrowband 311 nm UVB lamp** (Sperti; Philips TL01 tube) if the appeal was indoor convenience. Quartz envelope, tuned to the previtamin D3 action spectrum, metered dose in ~5 minutes, works in winter and at night, few hundred euros. It dominates a quartz window on every axis.
- **UV-blocking window film** if UVA is the actual worry — normal glass already passes it, so the fix goes on the glass we have.

Reference cutoffs, for the material table in [Reference](reference.md): polycarbonate ~385 nm, acrylic ~375 nm, laminated glass ~380 nm, soda-lime ~320 nm, borosilicate ~300–310 nm, fused quartz ~200 nm. Ordinary glass blocks UV not because of the silica (pure SiO₂ is clear to ~140 nm) but because of trace iron and the sodium/calcium network modifiers.

## Shading & blackout

Goal: full darkness when wanted (sleep, films), privacy at night, and an extra insulating layer over the glass after dark. Options, ranked roughly by how well they actually black out:

1. **Exterior roller shutter (*persiana*)** — best raw blackout, because it covers the whole opening from *outside*; no edge-leak problem. Also adds insulation and security. Costs: mechanical (can break), maintenance, and it's a big external element on a glass wall.
2. **Blackout curtain with side channels** — cheap, simple, soft. A plain curtain leaks light around the edges; a **wrap-around / side-channel track** that seals the perimeter is what makes it genuinely dark. Easy to wash and replace. Best value if done with the channel.
3. **Interior solid shutter (*contraventana* / *postigo* interior)** — hinged solid panels that swing shut over the glass. Durable, wipeable, no fabric to fade, and insulating if the panel is core-filled. Traditional Spanish element, so there's prior art on detailing it.
    - **Catch:** a flat panel butt-fit over flush glass leaks light all around its edges. True blackout needs a built-in **overlap/rebate plus a seal** — otherwise it looks solid but isn't dark.
    - **Catch:** it swings *into* the room, so it needs clear wall/furniture, or you go bifold/pocket (more hardware, more cost).
    - Its real selling point isn't superior darkness — it's durability + insulation + a clean, fabric-free look.

**Rule of thumb:** every *interior* covering (curtain or shutter) is fighting perimeter light leak; the *exterior* persiana avoids that by covering the opening from outside. So for raw darkness: exterior persiana > sealed blackout curtain ≈ well-rebated interior shutter > naive flat shutter or plain curtain. Pick by what else you want from it (insulation, look, security, cost), not by assuming "solid = dark."

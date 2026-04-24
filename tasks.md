# TODO

- kitchen unload dishwasher with 0 steps, no need to move. drawers with holders maybe, or just the over-kitchen thing.

1. Create a Central Glossary

  You have a good list of acronyms in reference.md. As the project grows, you'll likely have more specialized terms. I suggest creating a dedicated glossary.md page.
  This would provide a single, easy-to-find place for all definitions, keeping your other documents cleaner and more focused on their main topic.


- GYM goes at -1, stable temperature and free space for leisure and noise. Could go elsewhere though.
- Add photos about outside wall options: maintenance free, pretty, durable: from Photos.
- add electric shower to bathroom https://youtu.be/jNqdgE4KyEY?si=njrhT6MRI48vuRZq 
    - No wait for hot water, cheaper. It's just better.
- Try rendair.ai
- Pergolas bioclimaticas
- Mid Air woven playground? https://youtube.com/shorts/vfMidFUS3jE?si=zkaldV6lb_U6OpqP
- Wood stove? Nope, we had at home for years and didn't use it. Maybe in the attic, but not inside.
- All the cables and tubing exposed, like a garage tray. Easy maintenance and modification
- Corners seem annoying, but they're the ideal places for tables. Triangle or curvy shaped, go around you.
- Close the kitchen? separate room or some glass, to isolate smoke and noise. But eat there, so keep big.
- Underground pipe for thermal mass? T is constant about 1m below surface.
- Awning (heat) + Curtain (darkness) > Blinds (Noisy when closing at night and break). Window with no coating, let the heat in for winter.
- Add requirements for DANA, ridiculous amounts of water with high speed, depending on placement.
- Develop the score calculation software in `tools/score_calculator.py`.
- Location scoring: layer learned spatial embeddings on top of the climate/horizon/Köppen filters in `docs/location.md`.
    - Stage 1 (regional): existing CHELSA / Köppen / horizon / political filters cut the globe to viable lat/lon regions.
    - Stage 2 (neighborhood): use Google Earth AI embeddings to rank neighborhoods inside surviving regions.
        - **S2Vec** — built environment (buildings, roads, businesses, transit) → predicts income, density, etc. Replaces hand-wavy "free country with powerful economy" with actual neighborhood features.
        - **RS-MaMMUT** — satellite imagery (vegetation, terrain).
        - **PDFM** — population dynamics.
        - Best results in the paper come from fusing S2Vec + satellite embeddings.
    - Lets us express things current filters can't: "quiet but ≤X min from services", "low-rise residential next to a park", as nearest-neighbor queries in embedding space.
    - TODO before committing to it: check whether S2Vec weights / API are publicly available (research paper from Google, Apr 2026). Source: https://x.com/yohaniddawela/status/2047651290432389291
- Si vamos a poner una valla alrededor de la casa, 
- If we're going to put a fence around the house, the house should be part of the fence (part of the perimeter), so we save an extra door to have to open everyday, we save time, and also that space and extra brick. You can look at USA houses with no fence, norway ones where the fence turns inside creating an exposed entrance zone, so the house is not so close to the street, or just make it right there. In cities buildings are huge and it's no problem.
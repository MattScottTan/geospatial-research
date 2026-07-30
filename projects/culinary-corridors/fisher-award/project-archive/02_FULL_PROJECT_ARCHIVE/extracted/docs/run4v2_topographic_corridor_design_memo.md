# Run 4 v2 Topographic/Corridor Design Memo

Created: 2026-04-30

## Goal
Add one defensible geospatial mechanism layer to the East/Southeast Asia focused case without reopening the full project. The enhancement should strengthen the Fisher argument by showing that the strongest residual culinary links can be interpreted through spatial accessibility and corridor context, not only through ingredient similarity.

## Options evaluated

| Option | Feasibility | Fisher value | Risk | Decision |
|---|---:|---:|---:|---|
| Terrain/barrier proxy using a DEM or formal ruggedness surface | Low in this offline run | High if implemented rigorously | High: requires raster access, least-cost choices, and more validation | Defer |
| Coastal/maritime corridor proxy | High | High | Medium: proxy must not be overclaimed as a route model | Selected |
| Boundary/permeability refinement | High | Medium-high | Lower novelty because Run 2 v2 already produced boundary summaries | Fallback/support |
| Path/accessibility proxy using existing coordinates and subregion labels | High | High | Medium: approximate; must be labeled as proxy | Selected with coastal proxy |
| Agroecological/topographic context | Medium-low | Medium-high | Requires crop/climate layers and would widen scope | Defer |

## Selected method
The selected method is a **coastal/maritime corridor-accessibility proxy** for the East/Southeast Asia case. It combines:

1. existing cuisine coordinates and pairwise distance;
2. positive residual cuisine similarity from the filtered Run 2 v2 model;
3. same-subregion/cross-subregion relationship;
4. manual but transparent coastal/island access classes for the six retained East/Southeast Asian cuisines;
5. a conservative barrier proxy for whether the pair is mainland-mainland, peninsula/island, archipelago-mainland, or longer cross-subregion connection.

The output is an exploratory `corridor_accessibility_score` for each East/Southeast Asia cuisine pair. This score is not a historical route model. It is a transparent spatial proxy that asks whether residual links align with plausible accessibility contexts: coastal adjacency, maritime exchange zones, and regional/subregional proximity.

## What this can support
- The East/Southeast Asia residuals are not just a list of ingredient similarities; they can be plotted against spatial accessibility context.
- The strongest links, such as Thai-Vietnamese and Chinese-Korean, sit in high-accessibility same-subregion contexts.
- Filipino links show why maritime/coastal positioning may matter for residual bridge interpretation.

## What this cannot prove
- It cannot prove actual migration, trade, or route history.
- It cannot substitute for a least-cost path, port network, shipping, or historical trade model.
- It cannot establish terrain causality without external topographic data and a formal cost surface.

## Final use recommendation
Use the new figure as a **main supporting figure** if space allows, or as an appendix figure in a tighter StoryMap/poster. It strengthens spatial necessity by showing how residual culinary geography can be compared with corridor/accessibility logic.

# Run 5 Topographic Visual Strategy

Created: 2026-05-01

## Selected primary visual concept
**Relief + residual corridor map for East/Southeast Asia.**

The primary figure will overlay the strongest positive East/Southeast Asia residual cuisine links on a real ETOPO-style relief/coastal background. The map will foreground the spatial form of the focused case: mainland adjacency, peninsula/mainland context, island and maritime positioning, and cross-subregional links.

## Why this improves the submission
The existing Run 4 v2 map already introduced a corridor/accessibility proxy. Run 5 improves the visual communication by making the geography itself visible: seas, islands, peninsulas, mountain/plateau context, and coastlines are immediately legible. This makes the East/Southeast Asia corridor more striking while preserving the non-causal interpretation.

## Primary figure role
Use as a **main supporting figure** immediately after the East/Southeast Asia focused-case figure. It should supplement, not replace, the residual bridge-index figure. The residual bridge-index remains the clearest geospatial-only metric; Run 5 adds topographic/coastal context.

## Fallback visual concept
If relief rendering fails, create a clearly labeled schematic spatial-context map with coastlines, country boundaries, cuisine coordinates, and residual links. Do not call the fallback a topographic map.

## Planned data layers
1. ETOPO relief image from the local Basemap data package.
2. Basemap coastline and country boundary layers.
3. Cuisine coordinates from `data/crosswalks/cuisine_geo_crosswalk.csv`.
4. East/Southeast Asia residual metrics from `data/processed/run4v2_east_se_asia_accessibility_metrics.csv`.
5. Optional annotations for spatial context: South China Sea / maritime context, mainland Southeast Asian adjacency, Korean peninsula/mainland context, Tibetan Plateau/Himalayan barrier context.

## Corridor links to show
Limit the map to the strongest positive residual/corridor-accessibility links to avoid clutter:

- Thai–Vietnamese
- Chinese–Korean
- Filipino–Vietnamese
- Filipino–Thai
- Chinese–Filipino
- Chinese–Japanese
- Chinese–Vietnamese if legibility allows

Line thickness should reflect residual magnitude. Line opacity or color should reflect corridor-accessibility alignment or relation type.

## Claim discipline
The map supports this narrow interpretation: high-residual cuisine pairs can be read in relation to regional, coastal, island, and terrain context. It does **not** prove that terrain, maritime exchange, migration, trade, or historical routes caused the observed residuals.

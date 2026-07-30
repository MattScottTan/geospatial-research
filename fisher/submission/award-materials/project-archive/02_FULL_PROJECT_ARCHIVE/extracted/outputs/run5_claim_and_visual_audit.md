# Run 5 Claim and Visual Audit

Created: 2026-05-01

## Visual clarity check
- **Primary figure exists:** `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`
- **Optional callout exists:** `figures/final_revised/run5_corridor_callout_or_inset.png`
- **Primary map focus:** East/Southeast Asia only; no global clutter.
- **Corridor provenance:** Lines are derived from `data/processed/run4v2_east_se_asia_accessibility_metrics.csv` and selected in `data/processed/run5_east_se_asia_topographic_links_selected.csv`.
- **Coordinates:** Cuisine points use existing project coordinate fields in the Run 4 v2 metrics/crosswalk data.
- **Legend:** The primary map explains line color, line width, and residual meaning.
- **Topographic context:** The map uses the local Basemap ETOPO relief image as relief/coastal context.

## Topographic-data honesty check
- The map is a relief-context map, not a DEM-derived terrain-cost model.
- The caption and insert text distinguish relief/coastline context from least-cost routing.
- The geodata manifest documents the local relief source and states that no external download was performed.

## Claim audit
| Claim | Status | Notes |
|---|---|---|
| East/Southeast Asia residual links become more spatially legible on relief/coastal context. | Safe | Directly supported by the map. |
| Thai–Vietnamese is a compact mainland link. | Safe | Spatial-context description, not causal. |
| Filipino links sit in an island/maritime setting. | Safe | Spatial-context description, not causal. |
| Terrain or maritime routes caused cuisine similarity. | Forbidden | Not made in Run 5 inserts. |
| The map is a measured least-cost route model. | Forbidden | Explicitly denied in captions and inserts. |
| The map strengthens the Fisher spatial-necessity argument. | Safe | It adds a geography-dependent visual interpretation. |

## Submission alignment
The Run 5 map aligns with Fisher spatial necessity because it visually demonstrates that the focused residual links occupy specific coastal, island, peninsula, and relief contexts. The ingredient matrix alone cannot provide this spatial reading.

## Final decision
Use the Run 5 primary map as a **main supporting figure**. Use the optional callout only if space allows. Do not add more maps after this unless a reviewer identifies a specific visual gap.

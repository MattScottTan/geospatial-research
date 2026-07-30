# Run 4 v2 External Geodata Manifest

Created: 2026-04-30

## External geodata used
No new external geospatial or topographic layers were downloaded in this run.

## Why no external raster/route data were used
The Run 4 v2 enhancement is deliberately scoped as a prototype corridor-accessibility proxy. A formal least-cost or terrain-cost model would require additional choices about DEM source, coastline/port network representation, land/sea travel costs, historical period, and validation data. Those choices would widen the project beyond a final improvement pass.

## Proxy inputs used instead
| Input | Artifact | Variables used | Usage note |
|---|---|---|---|
| Focused East/Southeast Asia residual pairs | `data/processed/run2v2_focus_case_results.csv` | cuisine pairs, coordinates, residuals, distance, subregion labels | Core pair-level outcome data |
| Cuisine geography crosswalk | `data/crosswalks/cuisine_geo_crosswalk.csv` | latitude, longitude, mapped place, mapping confidence | Approximate spatial anchors |
| Manual coastal/island class | embedded in `scripts/18_run4v2_topographic_corridor_enhancement.py` | coastal access class, island/archipelago flag, barrier class | Transparent proxy, not measured topography |

## Reliability caveat
The resulting corridor-accessibility score is exploratory. It should be described as a spatial proxy, not as a measured terrain, port, shipping, or least-cost surface.

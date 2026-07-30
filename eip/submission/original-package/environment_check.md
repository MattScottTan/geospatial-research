# Environment Check

Date: 2026-03-14 11:59 AM America/New_York

## Runtime

- Python executable: `/opt/pyvenv/bin/python`
- Python version: `3.13.5`
- Jupyter executable: `/opt/pyvenv/bin/jupyter`
- `latexmk`: `/usr/bin/latexmk`

## Critical package imports

| Package | Status | Version |
|---|---|---:|
| pandas | OK | 2.2.3 |
| numpy | OK | 2.3.5 |
| geopandas | OK | 1.1.2 |
| shapely | OK | 2.1.2 |
| pyogrio | OK | 0.12.1 |
| rasterio | OK | 1.5.0 |
| matplotlib | OK | 3.10.8 |
| scikit-learn | OK | 1.8.0 |
| scipy | OK | 1.17.0 |
| statsmodels | OK | 0.14.6 |
| nbformat | OK | 5.10.4 |
| nbconvert | OK | 7.17.0 |

## Readiness verdict

The local environment is ready for:
- baseline atlas reruns
- report compilation with LaTeX
- notebook generation/execution
- most local figure/table/GIS export work

## Known caveats

- The first `matplotlib` import built the font cache; this is normal but can make the first figure command slower.
- Live ArcGIS Online / StoryMaps assembly is still outside the local environment and requires Harvard login later.
- Any optional use of ArcGIS Pro, StreetMap Premium, or Business Analyst remains a gated, manually executed enhancement rather than a local prerequisite.

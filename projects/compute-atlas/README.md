# compute-atlas

Distance from the world's ~8,000 largest cities to the nearest major AWS / Azure / GCP
region, overlaid with AI research output from OpenAlex (2020–2025). Published as the
StoryMap "Cloudy with a Chance of Compute" (March 2026).

## Assembled from six packages

The original submission was downloaded as six separate "Part N" archives, none complete
on its own. This directory merges them; `../../docs/SOURCE_MANIFEST.md` records which
part each file came from. Notably the pipeline source was in Part 4, the build system in
Part 2, and the data in Part 1.

## Pipeline

`src/pipeline.py` is a staged CLI driven by the `Makefile`:

```bash
make prepare     # build city + cloud-region GeoPackages from data/raw
make access      # geodesic nearest-region distance per city
make openalex    # join the OpenAlex AI overlay
make model_gp    # Gaussian process regression
make model_car   # CAR / GMRF regression
make surfaces    # interpolated raster surfaces
make figures     # report figures
make report      # latexmk -> deliverables/
make all
```

Stack: `numpy`, `pandas`, `geopandas`, `pyogrio`, `shapely`, `scikit-learn`
(`GaussianProcessRegressor`), `scipy.sparse`, `rasterio`, `matplotlib`, `statsmodels`.

`openalex/make_openalex_ai_city_overlay.py` produced `data/raw/openalex_ai_city_overlay.csv`.
It lived outside the submission package entirely (in `Documents/Projects/openalex_overlay`)
and this is its only copy.

`extensions/` holds three later analyses not in the main pipeline: `stage4` causal
extension (matching + stress tests), `stage5` pilot city-year panel with event study, and
`stage6` expanded panel with TWFE and stacked DiD.

## Caveats

Three things to know before reusing any number from here:

1. **The spatial statistics are not in this codebase.** Global Moran's I (I = 0.066,
   p = 0.008) and Getis-Ord Gi\* were computed in ArcGIS Pro. No script here reproduces
   them, and the weights-matrix specification is not recorded anywhere.
2. **`requirements.txt` was missing from the original package.** The root one in this repo
   is reconstructed from the import graph, unpinned.
3. **The StoryMap credits PyMC and GPyTorch, which the pipeline does not import.** It
   uses sklearn's GP and `scipy.sparse` instead. Since the reported GP and CAR distance
   coefficients differ by a factor of four (−0.207 vs −0.052) with no uncertainty
   intervals saved, which implementation produced them is not a bookkeeping detail.

Full detail in [`../../docs/REPRODUCIBILITY_GAPS.md`](../../docs/REPRODUCIBILITY_GAPS.md).

## Data

`data/raw/worldcities.csv` is gitignored pending a licence check — see
[`../../docs/DATA_PROVENANCE.md`](../../docs/DATA_PROVENANCE.md), which also flags that
the StoryMap credits Natural Earth for the city frame while the only city table present
is from SimpleMaps.

`data/processed/` is untracked; `make prepare` regenerates it.

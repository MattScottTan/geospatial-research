# geospatial-research

Consolidated workspace for two geospatial analysis projects and the theoretical
follow-on work that grew out of them.

| Project | Directory | Output |
|---|---|---|
| AI compute accessibility atlas | [`projects/compute-atlas`](projects/compute-atlas) | StoryMap "Cloudy with a Chance of Compute" (Mar 2026) |
| Culinary corridors | [`projects/culinary-corridors`](projects/culinary-corridors) | StoryMap "Salt, Fat, Acid, Distance" (May 2026) |
| Spatial RMT / Bayesian theory | [`theory`](theory) | in progress |

## Layout

```
projects/compute-atlas/       distance-to-cloud vs. OpenAlex AI research output, 8,000 cities
  src/                        pipeline.py (prepare -> access -> openalex -> model -> figures)
  data/raw/                   cloud region coords, Natural Earth, OpenAlex overlay, city frame
  data/processed/             derived GeoPackages (regenerated; not committed)
  report/                     LaTeX report, figures, tables
  extensions/                 stage4 causal, stage5 pilot panel, stage6 expanded panel
  docs/                       stage briefs, ArcGIS guides, audits

projects/culinary-corridors/  ingredient similarity vs. great-circle distance, 20 cuisines
  data/raw/                   cuisine_ingredient_matrix.csv
  versions/
    fisher-submission/        figure builders (cartopy) + build notes
    storymap-v3-balanced/     StoryMap section copy blocks, audits
    storymap-v5/              v5 build instructions + v4 rendered figures
  reports/                    three report PDFs, no stated precedence

theory/                       spatial weights matrices as random band matrices
archive/                      superseded AI-atlas zips, kept for provenance (not committed)
docs/                         provenance, source manifest, reproducibility gaps
scripts/                      repo assembly
```

The culinary project keeps three overlapping packages side by side because none is marked
as superseding the others; see its [README](projects/culinary-corridors/README.md).

## Environment

The geospatial stack (GDAL, GEOS, PROJ) is far easier to install via conda than pip
on Windows. Prefer:

```bash
conda env create -f environment.yml
```

Falling back to pip requires system GDAL already present:

```bash
pip install -r requirements.txt
```

## Reproducibility status

Read [`docs/REPRODUCIBILITY_GAPS.md`](docs/REPRODUCIBILITY_GAPS.md) before trusting any
number in either StoryMap to be regenerable from this repo. Summary:

- **compute-atlas** — the Python pipeline is complete and runnable. The spatial
  statistics reported in the StoryMap (Global Moran's I, Getis-Ord Gi\*) were computed
  in **ArcGIS Pro**, not in this codebase, and have no script here.
- **culinary-corridors** — the figure code is present but reads hardcoded values
  transcribed from earlier figures rather than computing them from the ingredient
  matrix. The Mantel / partial Mantel and Local Moran's I analyses have **no code on
  this machine** in any form.

Both gaps are recoverable; see the doc for what would need to be written.

## Data licensing

See [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md). One input
(`worldcities.csv`, SimpleMaps) has redistribution terms that depend on which tier it
came from, and is excluded from version control until that is confirmed.

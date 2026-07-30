# geospatial-research

Two tracks, deliberately kept apart: **research** that is ongoing, and **prize
submissions** that are finished and must keep reproducing the numbers they published.

```
  research track                     submission track
  ─────────────                      ────────────────
  theory/     RMT / band matrices    eip/      Cloudy with a Chance of Compute
  code/       reusable source        fisher/   Salt, Fat, Acid, Distance
  analysis/   experiments
  tools/      ML techniques
```

Nothing in `eip/` or `fisher/` is imported by the research track, and nothing in the
research track is needed to rebuild either submission. Work on one without disturbing the
other.

## Research track

| Directory | Contents |
|---|---|
| [`theory/`](theory) | Spatial weights matrices as random band matrices — Thouless threshold in 2D, universal bulk vs. non-universal tail, eigenvector localisation and ESF, spectral spatial confounding |
| [`code/`](code) | Reusable library source. Empty; awaiting spectral utilities |
| [`analysis/`](analysis) | Research experiments and simulations. Empty |
| [`tools/`](tools) | Methods and ML techniques worth lifting elsewhere. Empty, with a promotion list |

The submissions are the empirical layer this track draws on — two real datasets with
published statistics that reproduce exactly, which is a better starting position than most
theory work gets.

## Submission track

Each is self-contained: `code/`, `analysis/`, `data/`, `results/`, `submission/`.

### [`eip/`](eip) — AI compute accessibility atlas
Distance from ~8,000 cities to the nearest AWS/Azure/GCP region against OpenAlex AI
research output. Staged pipeline (`make prepare access openalex model_gp model_car
surfaces figures report`), GP and CAR regressions, Moran's I and Getis-Ord Gi\*,
LaTeX report, plus stage 4–6 causal and panel extensions.

### [`fisher/`](fisher) — culinary corridors
Ingredient similarity against great-circle distance across 20 cuisines / 190 pairs.
Mantel and partial Mantel, LISA with a robustness panel, colonial-administration
extension, bridge index. Deterministic at `seed = 42`, 9,999 permutations.

## Environment

```bash
conda env create -f environment.yml     # preferred: GDAL/GEOS/PROJ come from conda-forge
pip install -r requirements.txt         # fallback; needs system GDAL
```

## Provenance and known issues

[`docs/`](docs) holds three files worth reading before trusting any number:
[SOURCE_MANIFEST](docs/SOURCE_MANIFEST.md) (where all 588 files came from across ~20
scattered archives), [DATA_PROVENANCE](docs/DATA_PROVENANCE.md) (licensing), and
[REPRODUCIBILITY_GAPS](docs/REPRODUCIBILITY_GAPS.md) (what reproduces and what doesn't).

Both submissions' spatial statistics now reproduce from this repo. Two documentation
corrections remain open, both recorded in REPRODUCIBILITY_GAPS:

- **eip** — the shipped Gi\* uses a symmetrized binary weights matrix while the methods
  document specifies row standardisation. Moran's I is unaffected (0.065–0.071 across
  schemes); the hot/cold counts are not (7/33 shipped vs. 5/16 documented).
- **eip** — the city frame is SimpleMaps; the published sources section credits Natural
  Earth.

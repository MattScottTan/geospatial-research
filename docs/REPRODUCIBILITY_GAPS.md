# Reproducibility gaps

What the two StoryMaps claim versus what the code on this machine can actually
regenerate. Recorded honestly because both projects are candidates for reuse as the
empirical layer under theory work, and that only works if the provenance is known.

## 1. The spatial statistics: partly recovered

Revised after unpacking `Downloads/EIP All Past Resources/` — see
`../projects/compute-atlas/eip-award/README.md`.

**compute-atlas, Findings 1–2 — code found.** `cloudy_compute_session_export.zip`
contained two scripts, now at `projects/compute-atlas/src/analysis/`:

- `distributional_tests.py` — two-sample KS, Mann-Whitney U, chi-square at 500 km
- `weighted_concentration_tests.py` — activity-weighted distances, Spearman rank correlation

These cover the reported D = 0.30, U = 786,844, χ² = 103.8 and Spearman −0.05.

**compute-atlas, Finding 3 — still no code, but now specified.** Global Moran's I
(I = 0.066, z = 2.86, p = 0.008, n = 319) and Getis-Ord Gi\* remain ArcGIS-only; neither
analysis script imports `libpysal` or `esda`, and the `.aprx` was never downloaded.
However `eip-award/methods/SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` records the weights
specification that I previously listed as unrecorded:

> **K Nearest Neighbors, K = 8, Row standardization**, Euclidean distance on WGS84.

That is enough to reproduce the result in `esda` and compare. The same document explicitly
notes that matching this specification is required to replicate the Python results, so the
choice was deliberate.

**culinary-corridors — still nothing.** The partial Mantel test (r = +0.181, p = 0.022)
and Local Moran's I have no implementation in any language anywhere on this machine. The
EIP archives are compute-atlas material only and add nothing here.

Recovery: port Finding 3 to `esda` using the documented k = 8 row-standardised weights —
now a small, well-defined job. The culinary side still needs the pairwise distance and
dissimilarity matrices rebuilt from `cuisine_ingredient_matrix.csv` from scratch.

## 2. `culinary-corridors/code/figdata.py` is transcribed, not computed

The module docstring says so directly: values are "reproduced from what is already
published in the project's figures." It hardcodes cuisine anchor coordinates read off
earlier PNGs. Two entries are labelled `Anchor_A` and `Anchor_B` with comments saying
their "identity uncertain" and cuisine names "inferred from context."

So the culinary figure builders re-render prior outputs rather than deriving anything
from `cuisine_ingredient_matrix.csv`. There is no code path from the ingredient matrix
to any published figure.

Recovery: write the analysis that was presumably done in run4/run5 (those output
directories are not on this machine either), starting from the ingredient matrix.

## 3. `requirements.txt` is missing from the original package

`requirements-extended.txt` opens with `-r requirements.txt`, which does not exist in
Parts 1–6. The root `requirements.txt` here was reconstructed by reading the import
graph of `src/pipeline.py` and the culinary figure builders. It is therefore a
best-effort reconstruction, not the original pinned environment — no versions were
recorded, so exact-version replication is not possible.

## 4. The StoryMap credits libraries the pipeline does not use

The Sources section lists "GPyTorch and PyMC (spatial regression models)."
`src/pipeline.py` imports neither. It uses
`sklearn.gaussian_process.GaussianProcessRegressor` for the GP and `scipy.sparse` /
`scipy.sparse.linalg` for the CAR/GMRF. Either the PyMC/GPyTorch versions were run in a
notebook that was never saved, or the attribution is wrong.

This matters beyond bookkeeping: the reported GP and CAR distance coefficients
(−0.207 and −0.052) differ by a factor of four, and which implementation produced them
determines whether that gap is a modelling result or an artifact. The StoryMap also
notes it stored posterior point estimates without uncertainty intervals, so there is no
way to tell from the saved outputs whether the two are even distinguishable.

## 5. ArcGIS steps are documented as prose, not code

Buffer creation, projection, spatial joins, and the hosted feature layers were done in
ArcGIS Online / Pro. This is better documented than I first thought — `eip-award/methods/`
holds `ARCGIS_PRO_MASTER_WORKFLOW.md`, a 48 KB `ARCGIS_PRO_CLICK_BY_CLICK_FINDINGS_1_5.md`,
and `ARCGIS_FINAL_INSTRUCTIONS.md`, which together specify the tool settings used. So the
workflow is reconstructible; it just isn't executable. Fully scripting the pipeline still
means reimplementing those steps in `geopandas`.

## Priority if the goal is a reusable empirical base

1. Port Moran's I and Gi\* to `esda` with the documented k = 8 row-standardised weights,
   and check the result against I = 0.066. Removes the ArcGIS dependency from the
   inference path and is now a small job.
2. Rebuild the culinary Mantel analysis from the ingredient matrix — still the largest gap,
   since nothing exists to port.
3. Re-fit the GP and CAR with full posteriors so the factor-of-four coefficient gap can be
   diagnosed.
4. Backfill `figdata.py` from real computation.
5. Correct the city-frame attribution (SimpleMaps, not Natural Earth) — see
   `DATA_PROVENANCE.md`.

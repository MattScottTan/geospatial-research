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

**compute-atlas, Finding 3 — closed. It was never ArcGIS-only.**
`src/pipeline.py` implements both statistics itself, in numpy/scipy:
`compute_global_morans_i` (499 permutations, seed 42) and `compute_local_gi_star`. The
StoryMap's attribution to "the ArcGIS Pro Spatial Statistics toolbox" does not match the
shipped code, and `gis/cities_with_hotspots.geojson` is that code's output.

`src/analysis/spatial_diagnostics_esda.py` ports both to `esda`/`libpysal` and verifies
them. Results reproduce exactly: **I = 0.0661, z = 2.86, p = 0.0080** against the
published 0.066 / 2.86 / 0.008, and Gi\* gives **7 hot spots and 33 cold spots** against
the published 7 and 33. Gi\* z-scores match the shipped GeoJSON with max |diff| = 0.0
across all 319 cities. `esda` independently confirms I to four decimals under every
weighting scheme tested.

**But the weights do not match the documented specification.**
`eip-award/methods/SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md` specifies "K Nearest Neighbors,
K = 8, **Row standardization**". `pipeline.build_knn_graph` builds a kNN graph and then
**symmetrizes it and leaves it binary** — it never row-standardises. Running the
documented specification instead:

| weights | I | p | Gi\* hot | Gi\* cold |
|---|---|---|---|---|
| symmetrized binary (what shipped) | 0.0661 | 0.008 | **7** | **33** |
| symmetrized row-standardised | 0.0654 | 0.010 | 5 | 19 |
| directed kNN binary | 0.0713 | 0.008 | 6 | 21 |
| directed kNN row-standardised (documented spec) | 0.0713 | 0.008 | 5 | 16 |

Moran's I is robust — 0.065 to 0.071, significant at p ≤ 0.01 throughout. The Gi\*
classifications are not: the published counts more than double the cold spots that the
documented specification produces. The hot/cold map in the StoryMap is an artifact of an
undocumented weighting choice, and no reader could reconstruct it from the methods
document.

**culinary-corridors — fully recovered.** Superseded again by
`Downloads/Fisher All Past Resources/`. The complete analysis pipeline was in
`bridges_final_package.zip` and now sits at `projects/culinary-corridors/analysis/`:
`step1_verify_baseline`, `step1b_filter_sweep`, `step1c_validate_residuals`,
`step2_mantel`, `step3_lisa`, `step3b_lisa_robustness`, `step4d_final_figure`,
`build_case_studies`, plus five extension scripts (colonial Mantel and its sensitivity
panel, top-3 permutation, Russian anchor sensitivity, bridge bootstrap).

It imports `esda.moran` and `libpysal.weights`, runs 9,999 permutations at `seed = 42`,
and ships its working matrices (`distance_matrix.npy`, `similarity_matrix.npy`,
`residual_matrix.npy`) alongside the result JSONs. Every published statistic reproduces —
see `../projects/culinary-corridors/fisher-award/README.md` for the claim-by-claim table.

Both projects' spatial statistics are now reproducible from this repo. What remains is not
a missing-code gap but two documentation corrections: the compute-atlas weighting scheme
(above) and the city-frame attribution (§ below).

## 2. `figdata.py` is transcribed — but it is no longer the only path

Still true of the file itself: `versions/fisher-submission/code/figdata.py` hardcodes
cuisine anchor coordinates read off earlier PNGs, with two entries commented as "identity
uncertain."

But it is now a dead end rather than a blocker. The Fisher archives supplied a real
pipeline that computes from `cuisine_ingredient_matrix.csv` through to the figures
(`analysis/step4d_final_figure.py`, `tools/build_fig07_lisa_and_mantel.py`,
`tools/build_fig08_case_studies.py`). Prefer those; treat `figdata.py` as a superseded
early build helper.

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

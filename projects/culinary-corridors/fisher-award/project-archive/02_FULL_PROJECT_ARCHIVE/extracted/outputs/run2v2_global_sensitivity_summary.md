# Run 2 v2 Global Sensitivity Summary

Created: 2026-04-29

## Purpose

This sensitivity check asks whether Run 2's original global residual corridors survive after explicit generic/pantry ingredient removal, IDF weighting, and downweighting of high-prevalence ingredients. The filtered model is not the only correct model; it is a robustness check that reduces platform/staple vocabulary effects.

## Filtered model headline

- Filtered matrix shape: 20 cuisines × 1430 ingredients.
- Original top-20 residual pairs that remain in filtered top-20: 12 of 20.
- Mean absolute residual change across all dyads: 0.0704.
- Median absolute residual change across all dyads: 0.0602.

## Original top residuals

| cuisine_a    | cuisine_b   |   cosine_similarity |   distance_km |   residual_cosine | same_un_region   | same_un_subregion   |
|:-------------|:------------|--------------------:|--------------:|------------------:|:-----------------|:--------------------|
| british      | southern_us |            0.918618 |       6598.91 |          0.39391  | False            | False               |
| irish        | southern_us |            0.895099 |       6390.49 |          0.367602 | False            | False               |
| russian      | southern_us |            0.820853 |       9454.79 |          0.327398 | False            | False               |
| irish        | russian     |            0.852925 |       5974.99 |          0.319586 | True             | False               |
| british      | russian     |            0.849866 |       5613.83 |          0.311108 | True             | False               |
| french       | southern_us |            0.814417 |       7306.55 |          0.298562 | False            | False               |
| brazilian    | spanish     |            0.804487 |       7850.19 |          0.29487  | False            | False               |
| brazilian    | filipino    |            0.711264 |      19317.6  |          0.279904 | False            | False               |
| french       | russian     |            0.798146 |       6221.14 |          0.268315 | True             | False               |
| chinese      | korean      |            0.882952 |       2118.36 |          0.259495 | True             | True                |
| indian       | moroccan    |            0.749411 |       8463.18 |          0.246328 | False            | False               |
| filipino     | jamaican    |            0.691807 |      15983.9  |          0.243984 | False            | False               |
| cajun_creole | spanish     |            0.745102 |       7699.32 |          0.233797 | False            | False               |
| chinese      | japanese    |            0.824796 |       3046.76 |          0.232925 | True             | True                |
| brazilian    | mexican     |            0.733001 |       6928.3  |          0.212526 | True             | False               |

## Filtered top residuals

| cuisine_a   | cuisine_b   |   cosine_similarity |   jaccard_similarity |   distance_km |   residual_cosine | same_un_region   | same_un_subregion   |
|:------------|:------------|--------------------:|---------------------:|--------------:|------------------:|:-----------------|:--------------------|
| british     | southern_us |            0.662864 |             0.472695 |      6598.91  |          0.408458 | False            | False               |
| british     | russian     |            0.643984 |             0.507545 |      5613.83  |          0.370859 | True             | False               |
| thai        | vietnamese  |            0.856119 |             0.608333 |       807.994 |          0.358551 | True             | True                |
| irish       | russian     |            0.606514 |             0.482806 |      5974.99  |          0.340608 | True             | False               |
| french      | russian     |            0.59123  |             0.470529 |      6221.14  |          0.329999 | True             | False               |
| irish       | southern_us |            0.574846 |             0.467028 |      6390.49  |          0.316724 | False            | False               |
| chinese     | korean      |            0.691547 |             0.507883 |      2118.36  |          0.305578 | True             | True                |
| french      | southern_us |            0.544476 |             0.680266 |      7306.55  |          0.301865 | False            | False               |
| russian     | southern_us |            0.512454 |             0.40754  |      9454.79  |          0.299687 | False            | False               |
| filipino    | jamaican    |            0.436427 |             0.432615 |     15983.9   |          0.284454 | False            | False               |
| filipino    | thai        |            0.597862 |             0.46614  |      2261.96  |          0.219488 | True             | True                |
| filipino    | spanish     |            0.405396 |             0.368254 |     11857.3   |          0.218846 | False            | False               |
| filipino    | vietnamese  |            0.637194 |             0.474359 |      1465.16  |          0.208538 | True             | True                |
| british     | french      |            0.661132 |             0.518627 |      1091.33  |          0.198368 | True             | False               |
| brazilian   | filipino    |            0.289997 |             0.419837 |     19317.6   |          0.159958 | False            | False               |
| french      | jamaican    |            0.387111 |             0.391509 |      7769.2   |          0.151609 | False            | False               |
| russian     | spanish     |            0.393626 |             0.426136 |      7019.91  |          0.146382 | True             | False               |
| jamaican    | spanish     |            0.384646 |             0.424689 |      7340.41  |          0.14257  | False            | False               |
| jamaican    | russian     |            0.334493 |             0.383266 |     11157.2   |          0.140895 | False            | False               |
| filipino    | french      |            0.333003 |             0.376481 |     11107.2   |          0.138886 | False            | False               |

## Largest residual changes after filtering

| cuisine_a    | cuisine_b    |   original_residual |   filtered_residual |   residual_change |   original_cosine |   filtered_cosine |
|:-------------|:-------------|--------------------:|--------------------:|------------------:|------------------:|------------------:|
| brazilian    | cajun_creole |           0.185547  |          -0.0451519 |         -0.230699 |          0.710233 |          0.209224 |
| brazilian    | spanish      |           0.29487   |           0.096991  |         -0.197879 |          0.804487 |          0.331292 |
| brazilian    | mexican      |           0.212526  |           0.0335734 |         -0.178953 |          0.733001 |          0.282339 |
| brazilian    | greek        |           0.142549  |          -0.0329612 |         -0.17551  |          0.634198 |          0.1774   |
| brazilian    | indian       |           0.205609  |           0.0329474 |         -0.172662 |          0.660265 |          0.194023 |
| cajun_creole | mexican      |          -0.0602285 |          -0.232446  |         -0.172218 |          0.603914 |          0.207728 |
| brazilian    | moroccan     |           0.145077  |          -0.0233316 |         -0.168409 |          0.664656 |          0.22424  |
| filipino     | japanese     |           0.0529718 |          -0.113109  |         -0.166081 |          0.644118 |          0.229812 |
| brazilian    | italian      |           0.211318  |           0.0454816 |         -0.165837 |          0.708387 |          0.263064 |
| chinese      | japanese     |           0.232925  |           0.0684645 |         -0.16446  |          0.824796 |          0.412352 |
| greek        | spanish      |           0.17892   |           0.0161156 |         -0.162805 |          0.799744 |          0.398577 |
| british      | chinese      |          -0.280293  |          -0.121882  |          0.158411 |          0.23011  |          0.113465 |
| british      | jamaican     |          -0.0510732 |           0.10721   |          0.158283 |          0.464329 |          0.349217 |
| indian       | mexican      |           0.204095  |           0.0478161 |         -0.156279 |          0.656894 |          0.206418 |
| filipino     | vietnamese   |           0.0555234 |           0.208538  |          0.153014 |          0.711021 |          0.637194 |

## Interpretation

The global residual map should remain a **discovery layer only**. Some long-distance Anglo/Southern U.S./European residuals remain prominent even after filtering, so they should be treated as platform-bias diagnostics unless Run 3 adds stronger historical covariates. The filtered model still supports a focused spatial-inference story because the East/Southeast Asia case retains several positive residuals, especially same-subregion or within-Asia links such as Thai--Vietnamese and Chinese--Korean.

# Distance Baseline Model Summary

Input: `data/processed/cuisine_pair_model_table.csv`
Residual output: `data/processed/residual_culinary_corridors.csv`

## Model

`cosine_similarity ~ intercept + log(distance_km)`

This is a distance-only baseline. Residuals are interpreted as exploratory cuisine-similarity deviations from geography, not as causal evidence.

## Coefficients

| term            |   estimate |   std_error |     p_value |
|:----------------|-----------:|------------:|------------:|
| const           |  1.28902   |   0.120792  | 4.35349e-21 |
| log_distance_km | -0.0869069 |   0.0137479 | 1.83734e-09 |

R-squared: 0.1753
N dyads: 190

## Top positive residual culinary corridors

| cuisine_a    | cuisine_b   |   cosine_similarity |   distance_km |   predicted_cosine_distance_only |   residual_cosine | same_un_region   | same_un_subregion   |
|:-------------|:------------|--------------------:|--------------:|---------------------------------:|------------------:|:-----------------|:--------------------|
| british      | southern_us |            0.918618 |      6598.91  |                         0.524708 |          0.39391  | False            | False               |
| irish        | southern_us |            0.895099 |      6390.49  |                         0.527497 |          0.367602 | False            | False               |
| russian      | southern_us |            0.820853 |      9454.79  |                         0.493455 |          0.327398 | False            | False               |
| irish        | russian     |            0.852925 |      5974.99  |                         0.533339 |          0.319586 | True             | False               |
| british      | russian     |            0.849866 |      5613.83  |                         0.538758 |          0.311108 | True             | False               |
| french       | southern_us |            0.814417 |      7306.55  |                         0.515855 |          0.298562 | False            | False               |
| brazilian    | spanish     |            0.804487 |      7850.19  |                         0.509618 |          0.29487  | False            | False               |
| brazilian    | filipino    |            0.711264 |     19317.6   |                         0.43136  |          0.279904 | False            | False               |
| french       | russian     |            0.798146 |      6221.14  |                         0.529831 |          0.268315 | True             | False               |
| chinese      | korean      |            0.882952 |      2118.36  |                         0.623457 |          0.259495 | True             | True                |
| indian       | moroccan    |            0.749411 |      8463.18  |                         0.503084 |          0.246328 | False            | False               |
| filipino     | jamaican    |            0.691807 |     15983.9   |                         0.447823 |          0.243984 | False            | False               |
| cajun_creole | spanish     |            0.745102 |      7699.32  |                         0.511304 |          0.233797 | False            | False               |
| chinese      | japanese    |            0.824796 |      3046.76  |                         0.591872 |          0.232925 | True             | True                |
| brazilian    | mexican     |            0.733001 |      6928.3   |                         0.520475 |          0.212526 | True             | False               |
| brazilian    | italian     |            0.708387 |      9069.64  |                         0.497069 |          0.211318 | False            | False               |
| filipino     | spanish     |            0.683992 |     11857.3   |                         0.473777 |          0.210216 | False            | False               |
| thai         | vietnamese  |            0.916013 |       807.994 |                         0.707221 |          0.208792 | True             | True                |
| brazilian    | indian      |            0.660265 |     14775.3   |                         0.454656 |          0.205609 | False            | False               |
| indian       | mexican     |            0.656894 |     15094.4   |                         0.452799 |          0.204095 | False            | False               |

## Most negative residual pairs

| cuisine_a   | cuisine_b   |   cosine_similarity |   distance_km |   predicted_cosine_distance_only |   residual_cosine | same_un_region   | same_un_subregion   |
|:------------|:------------|--------------------:|--------------:|---------------------------------:|------------------:|:-----------------|:--------------------|
| irish       | thai        |            0.255319 |       9791.13 |                         0.490417 |         -0.235098 | False            | False               |
| chinese     | irish       |            0.266649 |       8149.53 |                         0.506366 |         -0.239717 | False            | False               |
| british     | moroccan    |            0.360787 |       2638.3  |                         0.604381 |         -0.243594 | False            | False               |
| british     | korean      |            0.23408  |       8857.79 |                         0.499123 |         -0.265043 | False            | False               |
| korean      | russian     |            0.320883 |       3253.09 |                         0.586177 |         -0.265294 | False            | False               |
| british     | vietnamese  |            0.218061 |      10033.1  |                         0.488295 |         -0.270234 | False            | False               |
| russian     | thai        |            0.275829 |       5088.13 |                         0.547303 |         -0.271474 | False            | False               |
| british     | chinese     |            0.23011  |       7779.57 |                         0.510403 |         -0.280293 | False            | False               |
| british     | thai        |            0.210649 |       9440.69 |                         0.493584 |         -0.282935 | False            | False               |
| chinese     | russian     |            0.283558 |       2854.61 |                         0.597533 |         -0.313975 | False            | False               |

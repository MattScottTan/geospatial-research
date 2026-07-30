# Run 2 v2 Filtered Distance Baseline Summary

Input matrix: `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`
Residual output: `data/processed/run2v2_residual_culinary_corridors_filtered.csv`

## Model

`filtered_cosine_similarity ~ intercept + log(distance_km)`

Intercept: 1.272702
Log-distance coefficient: -0.115786
R-squared: 0.3553
N dyads: 190

## Top positive residuals after filtering

| cuisine_a   | cuisine_b   |   cosine_similarity |   distance_km |   predicted_cosine_distance_only |   residual_cosine | same_un_region   | same_un_subregion   |
|:------------|:------------|--------------------:|--------------:|---------------------------------:|------------------:|:-----------------|:--------------------|
| british     | southern_us |            0.662864 |      6598.91  |                         0.254406 |          0.408458 | False            | False               |
| british     | russian     |            0.643984 |      5613.83  |                         0.273125 |          0.370859 | True             | False               |
| thai        | vietnamese  |            0.856119 |       807.994 |                         0.497568 |          0.358551 | True             | True                |
| irish       | russian     |            0.606514 |      5974.99  |                         0.265906 |          0.340608 | True             | False               |
| french      | russian     |            0.59123  |      6221.14  |                         0.261231 |          0.329999 | True             | False               |
| irish       | southern_us |            0.574846 |      6390.49  |                         0.258122 |          0.316724 | False            | False               |
| chinese     | korean      |            0.691547 |      2118.36  |                         0.385968 |          0.305578 | True             | True                |
| french      | southern_us |            0.544476 |      7306.55  |                         0.242611 |          0.301865 | False            | False               |
| russian     | southern_us |            0.512454 |      9454.79  |                         0.212767 |          0.299687 | False            | False               |
| filipino    | jamaican    |            0.436427 |     15983.9   |                         0.151973 |          0.284454 | False            | False               |
| filipino    | thai        |            0.597862 |      2261.96  |                         0.378374 |          0.219488 | True             | True                |
| filipino    | spanish     |            0.405396 |     11857.3   |                         0.18655  |          0.218846 | False            | False               |
| filipino    | vietnamese  |            0.637194 |      1465.16  |                         0.428656 |          0.208538 | True             | True                |
| british     | french      |            0.661132 |      1091.33  |                         0.462763 |          0.198368 | True             | False               |
| brazilian   | filipino    |            0.289997 |     19317.6   |                         0.130039 |          0.159958 | False            | False               |
| french      | jamaican    |            0.387111 |      7769.2   |                         0.235502 |          0.151609 | False            | False               |
| russian     | spanish     |            0.393626 |      7019.91  |                         0.247245 |          0.146382 | True             | False               |
| jamaican    | spanish     |            0.384646 |      7340.41  |                         0.242076 |          0.14257  | False            | False               |
| jamaican    | russian     |            0.334493 |     11157.2   |                         0.193597 |          0.140895 | False            | False               |
| filipino    | french      |            0.333003 |     11107.2   |                         0.194117 |          0.138886 | False            | False               |

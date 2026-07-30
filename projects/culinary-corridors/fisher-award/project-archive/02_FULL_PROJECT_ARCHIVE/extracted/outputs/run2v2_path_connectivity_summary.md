# Run 2 v2 Path/Connectivity Proxy Summary

Created: 2026-04-29

## Method

This is an exploratory proxy, not true least-cost routing. Pairs are classified using existing coordinates, UN region/subregion labels, distance, and transparent maritime/coastal cuisine flags. It is useful for asking whether residuals are organized by broad spatial-accessibility classes.

## Mean residual by connectivity proxy class

| connectivity_proxy_class     |   pair_count |   mean_residual |   mean_distance_km |   positive_share |
|:-----------------------------|-------------:|----------------:|-------------------:|-----------------:|
| same_subregion               |           11 |      0.11535    |            1456.18 |         0.727273 |
| long_distance_cross_region   |           21 |      0.0225495  |            9690.91 |         0.619048 |
| long_distance_maritime_proxy |          107 |     -0.00346405 |           10522.4  |         0.411215 |
| same_region_cross_subregion  |           41 |     -0.00920639 |            3454.35 |         0.390244 |
| other_cross_region           |           10 |     -0.0994274  |            2733.64 |         0.2      |

## Top positive residuals by proxy class

| cuisine_a   | cuisine_b   | connectivity_proxy_class     |   cosine_similarity |   distance_km |   residual_cosine | both_maritime_exposed   | east_southeast_asia_bridge   |
|:------------|:------------|:-----------------------------|--------------------:|--------------:|------------------:|:------------------------|:-----------------------------|
| british     | southern_us | long_distance_maritime_proxy |            0.662864 |      6598.91  |          0.408458 | True                    | False                        |
| british     | russian     | same_region_cross_subregion  |            0.643984 |      5613.83  |          0.370859 | False                   | False                        |
| thai        | vietnamese  | same_subregion               |            0.856119 |       807.994 |          0.358551 | True                    | False                        |
| irish       | russian     | same_region_cross_subregion  |            0.606514 |      5974.99  |          0.340608 | False                   | False                        |
| french      | russian     | same_region_cross_subregion  |            0.59123  |      6221.14  |          0.329999 | False                   | False                        |
| irish       | southern_us | long_distance_maritime_proxy |            0.574846 |      6390.49  |          0.316724 | True                    | False                        |
| chinese     | korean      | same_subregion               |            0.691547 |      2118.36  |          0.305578 | True                    | False                        |
| french      | southern_us | long_distance_maritime_proxy |            0.544476 |      7306.55  |          0.301865 | True                    | False                        |
| russian     | southern_us | long_distance_cross_region   |            0.512454 |      9454.79  |          0.299687 | False                   | False                        |
| filipino    | jamaican    | long_distance_maritime_proxy |            0.436427 |     15983.9   |          0.284454 | True                    | False                        |
| filipino    | thai        | same_subregion               |            0.597862 |      2261.96  |          0.219488 | True                    | False                        |
| filipino    | spanish     | long_distance_maritime_proxy |            0.405396 |     11857.3   |          0.218846 | True                    | False                        |
| filipino    | vietnamese  | same_subregion               |            0.637194 |      1465.16  |          0.208538 | True                    | False                        |
| british     | french      | same_region_cross_subregion  |            0.661132 |      1091.33  |          0.198368 | True                    | False                        |
| brazilian   | filipino    | long_distance_maritime_proxy |            0.289997 |     19317.6   |          0.159958 | True                    | False                        |
| french      | jamaican    | long_distance_maritime_proxy |            0.387111 |      7769.2   |          0.151609 | True                    | False                        |
| russian     | spanish     | same_region_cross_subregion  |            0.393626 |      7019.91  |          0.146382 | False                   | False                        |
| jamaican    | spanish     | long_distance_maritime_proxy |            0.384646 |      7340.41  |          0.14257  | True                    | False                        |
| jamaican    | russian     | long_distance_cross_region   |            0.334493 |     11157.2   |          0.140895 | False                   | False                        |
| filipino    | french      | long_distance_maritime_proxy |            0.333003 |     11107.2   |          0.138886 | True                    | False                        |

## Interpretation

The proxy clarifies whether top residuals are mostly same-subregion, same-region/cross-subregion, or long-distance/transregional. It should be used as a Fisher-facing motivation for real path-aware GIS in Run 3, not as evidence of historical route causality.

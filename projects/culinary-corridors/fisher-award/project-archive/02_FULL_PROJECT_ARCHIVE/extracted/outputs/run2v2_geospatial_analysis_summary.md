# Run 2 v2 Geospatial Analysis Summary

Created: 2026-04-29

## Strongest geospatial-only analysis: residual bridge scores

Residual bridge scores are the strongest Run 2 v2 geospatial addition. They aggregate pairwise residual corridors into place-level roles using coordinates, distance, and residual links. This cannot be obtained from ingredient vectors alone because the score depends on which residuals span long distances and which places act as spatial connectors.

### Top bridge-score cuisines

| cuisine      | case_role                                              |   positive_residual_degree |   top20_positive_degree |   long_distance_positive_degree |   long_distance_residual_score |   mean_all_residual |
|:-------------|:-------------------------------------------------------|---------------------------:|------------------------:|--------------------------------:|-------------------------------:|--------------------:|
| russian      | bias_diagnostic                                        |                         13 |                       6 |                              13 |                       2.06178  |          0.0510955  |
| southern_us  | secondary_iberian_atlantic+bias_diagnostic             |                          7 |                       4 |                               7 |                       1.66084  |          0.0478969  |
| filipino     | primary_east_southeast_asia+secondary_iberian_atlantic |                         17 |                       6 |                              13 |                       1.62956  |          0.109758   |
| jamaican     | secondary_iberian_atlantic                             |                         15 |                       4 |                              14 |                       1.47606  |          0.0689648  |
| french       | global_screen_only                                     |                         11 |                       5 |                               7 |                       1.06592  |          0.0504922  |
| british      | bias_diagnostic                                        |                          8 |                       3 |                               6 |                       0.976737 |          0.00969311 |
| spanish      | secondary_iberian_atlantic                             |                         12 |                       3 |                               8 |                       0.945543 |          0.0390869  |
| irish        | bias_diagnostic                                        |                          7 |                       2 |                               5 |                       0.878908 |          0.00310728 |
| italian      | global_screen_only                                     |                          9 |                       0 |                               7 |                       0.700735 |          0.0148886  |
| cajun_creole | secondary_iberian_atlantic                             |                          9 |                       0 |                               9 |                       0.537975 |         -0.0133574  |

## Boundary/permeability check

The boundary check groups dyads by spatial relationship and compares residual strength.

| boundary_class                 |   pair_count |   mean_residual |   median_residual |   mean_similarity |   mean_distance_km |   positive_share |
|:-------------------------------|-------------:|----------------:|------------------:|------------------:|-------------------:|-----------------:|
| iberian_atlantic_interregional |           11 |      0.13871    |        0.114723   |          0.334087 |           11633.8  |         1        |
| same_subregion                 |           11 |      0.11535    |        0.129179   |          0.564818 |            1456.18 |         0.727273 |
| same_region_cross_subregion    |           32 |     -0.00853468 |       -0.0369039  |          0.341347 |            3542.67 |         0.375    |
| east_se_asia_cross_subregion   |            9 |     -0.0115947  |       -0.00631223 |          0.331078 |            3140.29 |         0.444444 |
| other_cross_region             |          127 |     -0.019033   |       -0.0393355  |          0.200939 |            9675.38 |         0.377953 |

## Path/connectivity proxy

The path/connectivity proxy is exploratory. It is useful as a demonstration that spatial-accessibility classes can be tested, but it should not be treated as a true trade-route or migration-route model.

## Fisher insight supported

The amended prototype supports this Fisher-facing insight:

> Cuisine similarity is not just an ingredient-space phenomenon. Its residual structure can be mapped as corridors, bridges, and spatial boundary patterns, which makes the project genuinely geospatial rather than merely a food-data clustering exercise.

## What should be dropped or deferred

- Drop causal route claims from Run 2 v2.
- Defer true least-cost/path-aware routing to Run 3 unless a documented route, port, or cost-surface dataset is staged.
- Defer flavor chemistry unless Pia validates the ingredient-matching strategy.

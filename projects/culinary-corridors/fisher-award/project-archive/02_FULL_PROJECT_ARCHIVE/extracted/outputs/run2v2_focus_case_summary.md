# Run 2 v2 Focused Case Summary

Created: 2026-04-29

## Purpose

This summary separates final inference from the global discovery screen. The East/Southeast Asia case is the primary scoped analysis. The Iberian/Atlantic case is a secondary or diagnostic contrast.


## primary_east_southeast_asia

- Status: strong primary
- Cuisines retained: chinese, filipino, japanese, korean, thai, vietnamese
- Pair count: 15
- Positive residual pairs: 9
- Mean residual: 0.0694
- Median residual: 0.0311
- Mean distance: 2593.7 km

### Top pairs

| cuisine_a   | cuisine_b   |   cosine_similarity |   jaccard_similarity |   distance_km |   residual_cosine | same_un_region   | same_un_subregion   | subregion_relation          |
|:------------|:------------|--------------------:|---------------------:|--------------:|------------------:|:-----------------|:--------------------|:----------------------------|
| thai        | vietnamese  |            0.856119 |             0.608333 |       807.994 |        0.358551   | True             | True                | same_subregion              |
| chinese     | korean      |            0.691547 |             0.507883 |      2118.36  |        0.305578   | True             | True                | same_subregion              |
| filipino    | thai        |            0.597862 |             0.46614  |      2261.96  |        0.219488   | True             | True                | same_subregion              |
| filipino    | vietnamese  |            0.637194 |             0.474359 |      1465.16  |        0.208538   | True             | True                | same_subregion              |
| chinese     | filipino    |            0.475155 |             0.490364 |      3102.76  |        0.133375   | True             | False               | same_region_cross_subregion |
| chinese     | japanese    |            0.412352 |             0.607107 |      3046.76  |        0.0684645  | True             | True                | same_subregion              |
| chinese     | vietnamese  |            0.417332 |             0.583333 |      2458.41  |        0.0486003  | True             | False               | same_region_cross_subregion |
| filipino    | korean      |            0.392031 |             0.437414 |      2630     |        0.0311115  | True             | False               | same_region_cross_subregion |
| korean      | vietnamese  |            0.365951 |             0.490489 |      3110.78  |        0.0244714  | True             | False               | same_region_cross_subregion |
| korean      | thai        |            0.322775 |             0.467609 |      3462.22  |       -0.00631223 | True             | False               | same_region_cross_subregion |

## secondary_iberian_atlantic

- Status: feasible but cautious secondary
- Cuisines retained: brazilian, cajun_creole, filipino, jamaican, mexican, southern_us, spanish
- Pair count: 21
- Positive residual pairs: 13
- Mean residual: 0.0403
- Median residual: 0.0831
- Mean distance: 7757.0 km

### Top pairs

| cuisine_a    | cuisine_b   |   cosine_similarity |   jaccard_similarity |   distance_km |   residual_cosine | same_un_region   | same_un_subregion   | subregion_relation   |
|:-------------|:------------|--------------------:|---------------------:|--------------:|------------------:|:-----------------|:--------------------|:---------------------|
| filipino     | jamaican    |            0.436427 |             0.432615 |      15983.9  |         0.284454  | False            | False               | cross_region         |
| filipino     | spanish     |            0.405396 |             0.368254 |      11857.3  |         0.218846  | False            | False               | cross_region         |
| brazilian    | filipino    |            0.289997 |             0.419837 |      19317.6  |         0.159958  | False            | False               | cross_region         |
| jamaican     | spanish     |            0.384646 |             0.424689 |       7340.41 |         0.14257   | False            | False               | cross_region         |
| cajun_creole | filipino    |            0.289323 |             0.407867 |      13951.4  |         0.121603  | False            | False               | cross_region         |
| filipino     | southern_us |            0.281027 |             0.397737 |      14123.1  |         0.114723  | False            | False               | cross_region         |
| cajun_creole | spanish     |            0.350403 |             0.54113  |       7699.32 |         0.113854  | False            | False               | cross_region         |
| mexican      | spanish     |            0.322676 |             0.573604 |       9025.75 |         0.104532  | False            | False               | cross_region         |
| brazilian    | spanish     |            0.331292 |             0.435185 |       7850.19 |         0.096991  | False            | False               | cross_region         |
| southern_us  | spanish     |            0.330948 |             0.557958 |       7108.56 |         0.0851559 | False            | False               | cross_region         |


## Permitted claims

- The East/Southeast Asia case is the strongest final-scope candidate because enough cuisines are present and the spatial interpretation is coherent.
- The Iberian/Atlantic case is feasible but should be presented cautiously because long-distance residuals are more exposed to platform bias and coarse mapped proxies.
- The Anglo-American/Southern U.S. family is useful as a bias diagnostic and sensitivity-test example.

## Claims to avoid

Do not claim that residual similarity proves historical diffusion, migration, trade, or colonial causation. These are hypotheses to test with explicit external covariates in Run 3.

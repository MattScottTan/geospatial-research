# Run 4 v2 Topographic/Corridor Summary

Created: 2026-04-30

## Enhancement completed
The completed enhancement is a focused **East/Southeast Asia corridor-accessibility proxy**. It supplements the existing distance-residual model by asking whether the strongest residual culinary links sit in spatial contexts that are plausibly more accessible: same-subregion adjacency, coastal/island positioning, shorter distance, maritime/corridor context, and lower transparent barrier flags.

## Key result
The strongest residual links also score highly on the accessibility proxy. The highest alignment pair is **Thai - Vietnamese**, with residual cosine similarity `0.359` and corridor-accessibility score `0.880`. Across the focused case, positive-residual pairs have mean corridor-accessibility score `0.691`; non-positive-residual pairs have mean score `0.576`.

## Top pair results

| cuisine_a   | cuisine_b   |   residual_cosine |   corridor_accessibility_score |   residual_accessibility_alignment | same_un_subregion   |   maritime_corridor_proxy |   terrain_barrier_proxy | proxy_confidence   |
|:------------|:------------|------------------:|-------------------------------:|-----------------------------------:|:--------------------|--------------------------:|------------------------:|:-------------------|
| thai        | vietnamese  |             0.359 |                          0.880 |                              0.316 | True                |                     0.600 |                   0.200 | medium             |
| chinese     | korean      |             0.306 |                          0.757 |                              0.231 | True                |                     0.450 |                   0.250 | medium             |
| filipino    | vietnamese  |             0.209 |                          0.862 |                              0.180 | True                |                     0.750 |                   0.450 | medium             |
| filipino    | thai        |             0.219 |                          0.800 |                              0.176 | True                |                     0.750 |                   0.450 | medium             |
| chinese     | filipino    |             0.133 |                          0.543 |                              0.072 | False               |                     0.750 |                   0.550 | low-medium         |
| chinese     | japanese    |             0.068 |                          0.739 |                              0.051 | True                |                     0.750 |                   0.450 | medium             |
| chinese     | vietnamese  |             0.049 |                          0.518 |                              0.025 | False               |                     0.450 |                   0.600 | low-medium         |
| filipino    | korean      |             0.031 |                          0.592 |                              0.018 | False               |                     0.750 |                   0.600 | low-medium         |

## Interpretation
The result strengthens the Fisher argument because it makes the East/Southeast Asia case more explicitly geospatial. The original residual model showed which cuisine pairs were more similar than distance predicted. This enhancement adds spatial context: the highest residuals are not merely high ingredient similarities; they can be compared with a corridor/accessibility proxy based on geography, subregion, coastal/island context, and barrier classification.

## What can be claimed
- The new figure provides **spatial context** for the East/Southeast Asia residuals.
- It is consistent with the idea that residual food similarity may align with accessible regional or maritime corridors.
- It supports using East/Southeast Asia as the project's strongest focused inference case.

## What cannot be claimed
- This does not prove migration, trade, maritime exchange, or terrain causality.
- The barrier score is not a measured DEM-derived terrain cost.
- The map is a transparent proxy diagram, not a formal historical route model.

## Recommendation for final use
Include `figures/final_revised/run4v2_topographic_corridor_map.png` as a **main supporting figure** after the East/Southeast Asia focused-case figure, or as the first appendix figure if the final StoryMap/poster needs to stay shorter. It should supplement, not replace, the Run 4 hero and bridge-index figures.

# Run 4 Geospatial Upgrade Summary

Created: 2026-04-29

## Upgrade implemented
The implemented upgrade is a **residual bridge-score refinement**. It reads the Run 2 v2 residual bridge-score table and computes a normalized `run4_bridge_index` from five components:

1. number of positive residual links;
2. number of top-20 residual links;
3. mean positive residual strength;
4. long-distance positive residual score;
5. mean residual across all dyads.

## Why this is geospatial
This upgrade cannot be reproduced from ingredient vectors alone. It depends on the distance baseline, mapped cuisine coordinates, long-distance residual structure, and case geography. It asks: **which places become bridge nodes after cuisine similarity is compared against geography?**

## Top bridge-index results

| cuisine     | mapped_place           |   run4_bridge_index | run4_spatial_role                |   positive_residual_degree |   top20_positive_degree |
|:------------|:-----------------------|--------------------:|:---------------------------------|---------------------------:|------------------------:|
| filipino    | Philippines            |            0.863444 | primary_case_bridge              |                         17 |                       6 |
| russian     | Russian Federation     |            0.839174 | global_residual_bridge           |                         13 |                       6 |
| southern_us | Southern United States |            0.691507 | global_residual_bridge           |                          7 |                       4 |
| jamaican    | Jamaica                |            0.68587  | global_residual_bridge           |                         15 |                       4 |
| french      | France                 |            0.653374 | context_bridge_role              |                         11 |                       5 |
| spanish     | Spain                  |            0.532188 | secondary_corridor_or_diagnostic |                         12 |                       3 |
| british     | United Kingdom         |            0.514647 | bias_diagnostic_bridge           |                          8 |                       3 |
| irish       | Ireland                |            0.441666 | bias_diagnostic_bridge           |                          7 |                       2 |

## Interpretation
High bridge-index places are not declared causal origins or historical conduits. They are cuisines whose ingredient similarity remains unexpectedly connected to many other places after the distance baseline. This makes them useful in a Fisher-facing map because they convert a complex residual network into legible spatial roles.

## Limitation
The bridge index is a prototype summary metric. It is not a formal centrality measure on a historical migration/trade network. A stronger future version would use explicit maritime/trade/migration route data and compare bridge scores against those networks.

## Recommended use
Use the bridge-index figure as the key **spatial necessity** visual: it demonstrates that GIS produces a result that non-spatial recipe clustering cannot produce.

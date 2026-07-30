# Stage 4 causal-extension summary

## What was attempted
- Re-estimate the distance relationship with richer geographic and country-level controls.
- Test whether the coefficient survives within-country fixed effects.
- Run a within-country demeaned regression as a direct diagnostic.
- Run doubly robust treatment-effect checks for being very close to compute (<=250 km and <=500 km).

## Core result
- Baseline cross-sectional OLS on the well-matched sample reproduces the original negative sign: -0.220 per additional 1,000 km (p=0.242).
- Once country fixed effects are added, the coefficient becomes 0.151 (p=0.683).
- The within-country demeaned regression gives 0.088 (p=0.787), with demeaned correlation -0.026.
- Matching / weighting estimates are imprecise and unstable across thresholds; none support a clean causal claim.

## Bottom line
The current snapshot supports an association in descriptive and spatial-model terms, but it does not support a credible causal claim once stricter within-place comparisons are used.
A real causal Stage 4 would need a city-year AI outcome and time-stamped cloud-region openings or other exogenous infrastructure shocks.
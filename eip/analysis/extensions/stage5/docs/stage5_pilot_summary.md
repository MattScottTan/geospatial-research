# Stage 5 pilot city-year panel and event-study

## Design actually implemented
- Outcome: annual AI-related works by city, but only from institution IDs present in the project's top-institution file. This is a pilot panel, not a full-city census.
- Treatment: first local AWS region opening for cities within 75 km of a launch location; never-treated controls are cities farther than 75 km from any AWS launch city in the sample window.
- Post indicator uses the first full publication year after launch to avoid partial-year contamination.

## Coverage
- Cities in pilot panel: 18
- Years: 2000-2025
- Treated cities: 9
- Never-treated controls: 9

## Average treatment effect estimates
| model              | subset   |   n_obs |   coef_post_full |   se_post_full |   p_post_full |     ci_low |   ci_high |       r2 |
|:-------------------|:---------|--------:|-----------------:|---------------:|--------------:|-----------:|----------:|---------:|
| TWFE baseline      | all      |     468 |        -0.311469 |       0.260831 |     0.232422  | -0.822698  |  0.199759 | 0.891396 |
| TWFE + city trends | all      |     468 |         0.262773 |       0.150959 |     0.0817384 | -0.0331073 |  0.558654 | 0.9407   |

| model                     | subset        |   n_obs |   coef_post_full |   se_post_full |   p_post_full |    ci_low |   ci_high |       r2 |
|:--------------------------|:--------------|--------:|-----------------:|---------------:|--------------:|----------:|----------:|---------:|
| TWFE baseline             | multi_country |     260 |        -0.448039 |       0.41338  |      0.278435 | -1.25826  |  0.362187 | 0.857916 |
| TWFE + city trends        | multi_country |     260 |         0.210544 |       0.186668 |      0.259359 | -0.155325 |  0.576414 | 0.928952 |
| City FE + country-year FE | multi_country |     260 |        -0.101076 |       0.301455 |      0.737404 | -0.691929 |  0.489777 | 0.943452 |

## Event-study pretrend checks
- Pilot sample pretrend joint p-value: 0.203
- Within-country subset pretrend joint p-value: 0.135

## Interpretation
- This pilot can show whether the sign is directionally consistent in a dynamic panel, but it cannot settle causality because the outcome is a top-institution subset and the treatment is still plausibly endogenous.
- The strongest version here is the within-country subset with country-year comparison logic, which strips out many broad national shocks but still leaves city-specific selection into region openings unresolved.
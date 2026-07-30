# Stage 6 expanded panel: broader city-year causal test

## What this stage does
This stage moves beyond the Stage 5 pilot by expanding the panel to a broader multi-country set of cities and treatment cohorts, then checking whether local cloud-region openings are followed by higher AI-research output in a staggered-adoption panel.

The expanded panel uses annual city-year counts from 2000 to 2025 for a selected sample of 26 cities (13 treated and 13 never-treated controls) across the United States, United Kingdom, France, Japan, South Korea, India, and Switzerland. The outcome is log(1 + annual AI works) constructed from the top-institution city subset. Treatment timing is based on nearby AWS-region launches.

## Sample composition
- 26 cities
- 13 treated cities
- 13 never-treated controls
- 676 city-year observations in the full panel
- 819 observations in the stacked windowed DID comparison

## Main estimates
### Two-way fixed effects panel
- **TWFE baseline:** +0.194 log points, p = 0.504
- **TWFE + city trends:** -0.118 log points, p = 0.673
- **City FE + country-year FE:** +0.574 log points, p = 0.0137

### Cohort-by-cohort DID around launch year
- **2009 cohort (US N. California):** +0.312, p = 0.415
- **2011 cohort (Tokyo):** -0.223, p = 0.0206
- **2016 cohort (London / Seoul):** +0.567, p = 0.0287
- **2017 cohort (Paris):** -0.375, p = 0.0260
- **2018 cohort (Osaka local region):** -0.256, p = 0.452
- **2022 cohort (Hyderabad / Zurich):** -0.001, p = 0.996

### Stacked DID on a common event window [-5, +3]
- **Stacked DID:** +0.020, p = 0.888

## Interpretation
The broader panel does **not** deliver a stable causal effect.

One specification becomes significantly positive once country-year fixed effects are included, but the broader evidence does not line up behind a consistent positive treatment effect:
- the baseline TWFE estimate is positive but imprecise,
- adding city-specific trends flips the sign negative,
- cohort-specific effects are highly heterogeneous, with some positive and some negative significant cohorts,
- the stacked DID estimate over a common event window is essentially zero.

The substantive takeaway is that the cross-sectional story remains much stronger than the causal story. The expanded panel shows that the sign and magnitude of the estimated treatment effect depend heavily on specification and cohort composition.

## Best-read conclusion
The stronger panel design still does not justify the claim that cloud-region openings cause a general rise in city-level AI research output. At most, it suggests that any effect is heterogeneous and context-dependent rather than universal.

## Why this still matters
This stage is still useful because it sharpens the boundary between what the atlas can say confidently and what it cannot. The project remains strong as a spatial diagnosis of compute inequality and AI concentration, but it should not yet be framed as having identified a robust causal effect of local cloud-region openings.

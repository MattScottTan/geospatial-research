# Run 2 Prototype Interpretation

Created: 2026-04-28

## Prototype status

Run 2 successfully moved **Culinary Corridors** from a planning concept to a real-data prototype. The working data spine now includes:

- 39,774 recipes
- 428,249 recipe-ingredient rows
- 20 cuisine labels
- 6,714 raw ingredient strings
- 5,936 normalized ingredient labels
- 1,434 retained non-universal ingredients in the cuisine matrix
- 190 pairwise cuisine dyads

The prototype satisfies the core Fisher-style requirement that GIS/spatial modeling produces an insight: cuisine similarity is not only plotted geographically; it is compared against geographic distance, converted into residuals, and mapped as unexpectedly strong culinary corridors.

## Main preliminary finding

The distance-only baseline finds a negative relationship between geographic distance and cuisine similarity:

- Model: `cosine_similarity ~ log(distance_km)`
- Distance coefficient: -0.0869
- R²: 0.1753
- N dyads: 190

This means geographic distance explains part of the cuisine-similarity structure, but not most of it. That is promising for the project: the most interesting Fisher argument can focus on **where food similarity exceeds geographic expectation**.

## Top positive residual culinary corridors

| cuisine_a    | cuisine_b   |   cosine_similarity |   distance_km |   predicted_cosine_distance_only |   residual_cosine | same_un_region   | same_un_subregion   |
|:-------------|:------------|--------------------:|--------------:|---------------------------------:|------------------:|:-----------------|:--------------------|
| british      | southern_us |            0.918618 |       6598.91 |                         0.524708 |          0.39391  | False            | False               |
| irish        | southern_us |            0.895099 |       6390.49 |                         0.527497 |          0.367602 | False            | False               |
| russian      | southern_us |            0.820853 |       9454.79 |                         0.493455 |          0.327398 | False            | False               |
| irish        | russian     |            0.852925 |       5974.99 |                         0.533339 |          0.319586 | True             | False               |
| british      | russian     |            0.849866 |       5613.83 |                         0.538758 |          0.311108 | True             | False               |
| french       | southern_us |            0.814417 |       7306.55 |                         0.515855 |          0.298562 | False            | False               |
| brazilian    | spanish     |            0.804487 |       7850.19 |                         0.509618 |          0.29487  | False            | False               |
| brazilian    | filipino    |            0.711264 |      19317.6  |                         0.43136  |          0.279904 | False            | False               |
| french       | russian     |            0.798146 |       6221.14 |                         0.529831 |          0.268315 | True             | False               |
| chinese      | korean      |            0.882952 |       2118.36 |                         0.623457 |          0.259495 | True             | True                |
| indian       | moroccan    |            0.749411 |       8463.18 |                         0.503084 |          0.246328 | False            | False               |
| filipino     | jamaican    |            0.691807 |      15983.9  |                         0.447823 |          0.243984 | False            | False               |
| cajun_creole | spanish     |            0.745102 |       7699.32 |                         0.511304 |          0.233797 | False            | False               |
| chinese      | japanese    |            0.824796 |       3046.76 |                         0.591872 |          0.232925 | True             | True                |
| brazilian    | mexican     |            0.733001 |       6928.3  |                         0.520475 |          0.212526 | True             | False               |

These corridors are preliminary, but they show several interpretable families:

1. **Anglo-American / platform-bias corridor.** British–Southern US, Irish–Southern US, British–Irish, and related Russian/French links are strong. Some may reflect real culinary overlap, but some may also reflect the recipe platform's English-language/American bias and generic baking/staple ingredients.
2. **East Asian and Southeast Asian clusters.** Chinese–Korean, Chinese–Japanese, and Thai–Vietnamese are high-value proof-of-concept results because they are geographically and historically plausible.
3. **Mediterranean / Atlantic / colonial-era signals.** Brazilian–Spanish, Brazilian–Italian, Brazilian–Mexican, and Filipino–Spanish-like relationships may be worth testing with colonial, migration, and trade covariates in Run 3.
4. **Spice and ingredient-family corridors.** Indian–Moroccan and Indian–Mexican may reflect spice profiles or shared ingredient families, but they require robustness checks to avoid overinterpretation.

## Overlay result

The Run 2 overlay used UN M49 same-region and same-subregion indicators as a lightweight sanity check. Same-region pairs had positive mean residuals, and same-subregion pairs had a stronger positive mean residual:

- Same UN region: mean residual ≈ 0.041; different region: ≈ -0.016
- Same UN subregion: mean residual ≈ 0.130; different subregion: ≈ -0.008

This supports adding a more substantive explanatory layer in Run 3. However, UN M49 is not a mechanism. Migration, trade, language, colonial history, climate/agriculture, or food-chemistry covariates are needed for the final interpretation.

## Fisher relevance

The prototype has a viable Fisher Prize structure:

1. Define cuisines as ingredient spaces.
2. Measure similarity between places.
3. Compare similarity to geographic distance.
4. Map the unexplained positive residuals.
5. Use migration/trade/history/flavor chemistry to interpret those corridors.

The strongest final visual is likely the residual corridor map, paired with a distance-decay plot and a clustered similarity heatmap. This avoids the weak framing of “a map of foods” and instead presents food as spatial evidence.

## Limitations

- The primary recipe corpus is public and structured, but it is Kaggle/Yummly-derived and should be treated as prototype data unless final-use permissions are clarified.
- Cuisine labels are coarse and not equivalent to countries.
- Coordinates are manually assigned cuisine proxies, not recipe origins.
- The current model uses a distance-only baseline; it does not yet control for language, colonial history, migration, trade, climate, or agriculture.
- Universal and generic ingredients were handled, but ingredient normalization remains subjective.
- Residuals are exploratory and should not be interpreted causally.
- Some high residuals may reflect platform bias rather than true culinary transmission.

## What cannot yet be claimed

The project cannot yet claim that migration, trade, colonial history, or flavor chemistry causes cuisine similarity. It can only claim that the prototype identifies **candidate culinary corridors** that warrant further explanation.

## Recommended interpretation for presentation

Use careful language:

> The prototype shows that cuisine similarity partly decays with geographic distance, but some cuisine pairs are substantially more similar than geography alone predicts. These positive residuals form candidate “culinary corridors” that can be tested against migration, trade, language, colonial history, agriculture, and flavor chemistry in the final Fisher submission.

## Run 3 implication

Proceed with the primary Culinary Corridors project, but treat the global map as the opening frame. For final polish, select 2–4 corridor families for careful interpretation rather than trying to explain every residual line globally.


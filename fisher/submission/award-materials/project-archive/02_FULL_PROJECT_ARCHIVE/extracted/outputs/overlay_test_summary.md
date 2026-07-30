# Overlay Test Summary

Created: 2026-04-28

## Overlay tested

Run 2 tested the official **UN M49 region/subregion** classification as the explanatory overlay. Each cuisine was mapped to a country or regional proxy in `data/crosswalks/cuisine_geo_crosswalk.csv`; each pair then received `same_un_region` and `same_un_subregion` flags.

Source: `https://unstats.un.org/unsd/methodology/m49/overview/`

## Join success

- Pairwise model rows: 190
- Rows with `same_un_region`: 190
- Rows with `same_un_subregion`: 190
- Join success rate: 100% for retained cuisine pairs

## Summary by same UN region

| group   |   n_pairs |   mean_residual |   median_residual |   mean_cosine |
|:--------|----------:|----------------:|------------------:|--------------:|
| False   |       138 |      -0.0155682 |        -0.0220935 |      0.481823 |
| True    |        52 |       0.0413156 |         0.0566694 |      0.652562 |

Welch t-test comparing same-region vs different-region residuals:

- statistic: 2.463
- p-value: 0.0155

## Summary by same UN subregion

| group   |   n_pairs |   mean_residual |   median_residual |   mean_cosine |
|:--------|----------:|----------------:|------------------:|--------------:|
| False   |       179 |     -0.00797129 |       -0.00708183 |      0.511819 |
| True    |        11 |      0.129715   |        0.139329   |      0.800833 |

Welch t-test comparing same-subregion vs not-same-subregion residuals:

- statistic: 4.198
- p-value: 0.0011

## Preliminary interpretation

The overlay is a lightweight sanity check. Same-region and same-subregion pairs have positive mean residuals, but the sample of same-subregion pairs is small and includes obvious close cultural/geographic cuisine clusters such as Thai–Vietnamese, Chinese–Japanese, Chinese–Korean, and British–Irish. This supports keeping an explanatory overlay in Run 3, but it does **not** substitute for migration, trade, language, or colonial-history covariates.

## Limitations

- UN M49 is broad and administrative, not a food-history classification.
- The overlay uses manually documented cuisine-to-place mappings.
- The test is exploratory and does not prove a causal mechanism.
- Run 3 should prioritize UN DESA migration, CEPII language/colonial variables, and/or UN Comtrade food-trade data if the final claim is about movement and exchange.

## Output

- Data: `data/processed/overlay_test_results.csv`
- Figure: `figures/run2_overlay_test_figure.png`

# Run 2 Figure Captions

Created: 2026-04-28

## `figures/run2_cuisine_similarity_heatmap.png`

**Data.** The heatmap uses `data/processed/cuisine_similarity_cosine.csv`, computed from `data/processed/cuisine_ingredient_matrix.csv`. The matrix contains 20 cuisines and 1434 retained normalized ingredients after dropping flagged universal ingredients and globally rare ingredients.

**Method.** Each cuisine is represented by a recipe-prevalence vector over normalized ingredients. Cell values are cosine similarities between cuisine vectors.

**What it shows.** The strongest observed cuisine-similarity clusters include British/Southern US/Irish, Thai/Vietnamese, Chinese/Korean/Japanese, and Italian/Spanish patterns.

**What it does not prove.** It does not prove historical transmission or causal migration/trade effects. The source is platform-biased and cuisine labels are coarse.

**Run 3 improvement.** Add clustering/dendrogram ordering, sensitivity to ingredient downweighting, and comparison to a second recipe source if feasible.

## `figures/run2_distance_decay_plot.png`

**Data.** The plot uses `data/processed/residual_culinary_corridors.csv`, which combines pairwise cuisine similarity with centroid-to-centroid geographic distance.

**Method.** The x-axis is geographic distance between mapped cuisine proxies in kilometers on a log scale. The y-axis is cosine cuisine similarity. The fitted line is the distance-only baseline: `cosine_similarity ~ log(distance_km)`.

**What it shows.** The estimated distance coefficient is negative, and the model has R² ≈ 0.175. Distance helps explain similarity, but it leaves substantial residual structure.

**What it does not prove.** Distance is a baseline, not a full causal model. Coordinate proxies are especially approximate for `southern_us`, `cajun_creole`, and very large cuisines such as Chinese, Indian, and Russian.

**Run 3 improvement.** Replace manual coordinate proxies with CEPII/Natural Earth joins where possible and add language, colonial, migration, trade, and climate covariates.

## `figures/run2_residual_corridor_map.png`

**Data.** The map uses the top positive residual cuisine pairs from `data/processed/residual_culinary_corridors.csv` and coordinates from `data/crosswalks/cuisine_geo_crosswalk.csv`.

**Method.** A residual corridor is a cuisine pair whose observed cosine similarity is higher than predicted by the distance-only model. Line thickness is proportional to positive residual magnitude.

**What it shows.** Top corridors include British–Southern US, Irish–Southern US, Russian–Southern US, Irish–Russian, British–Russian, French–Southern US, Brazilian–Spanish, Brazilian–Filipino, French–Russian, and Chinese–Korean.

**What it does not prove.** The map is a prototype. It does not distinguish true culinary history from dataset/platform bias, generic ingredient effects, or coarse cuisine labels.

**Run 3 improvement.** Use a cleaner basemap, label only defensible corridors, add confidence/error encoding, and compare residuals after additional covariates.

## `figures/run2_overlay_test_figure.png`

**Data.** The figure uses `data/processed/overlay_test_results.csv`, which adds UN M49 same-region and same-subregion flags to cuisine-pair residuals.

**Method.** Bars compare mean residuals for same-region vs different-region pairs and same-subregion vs different-subregion pairs.

**What it shows.** Same UN region pairs have mean residual ≈ 0.041 versus -0.016 for different-region pairs. Same UN subregion pairs have mean residual ≈ 0.130 versus -0.008 for other pairs.

**What it does not prove.** UN M49 regions are administrative/statistical categories, not mechanisms of culinary similarity. This is only a fast sanity check.

**Run 3 improvement.** Replace or supplement the UN M49 overlay with UN DESA migration, UN Comtrade food trade, CEPII language/colonial variables, and/or agriculture/climate similarity.


# Run 3 Handoff Plan

Created: 2026-04-28

## Go / no-go decisions

| Decision area | Recommendation | Rationale |
|---|---|---|
| Primary project | **Go: continue Culinary Corridors** | Run 2 produced a working real-data cuisine-similarity matrix, distance baseline, residual corridor map, and overlay test. |
| Scope | **Keep global frame, but interpret through selected corridor families** | The 20-cuisine prototype is viable, but final claims will be stronger if focused on defensible clusters such as East Asia/Southeast Asia, Mediterranean/Atlantic, Anglo-American, or spice corridors. |
| Fallback project | **Keep available but not necessary yet** | The simpler cuisine-similarity + migration/trade residual version is already embedded in the primary project. |
| Flavor chemistry | **Conditional include** | Include only if Run 3 quickly validates ingredient-to-FlavorDB/FooDB match rates and Pia agrees with the interpretive framing. |
| Fermentation | **Do not centralize** | No strong geocoded fermentation/microbiome layer was established in Run 2. Use only as a short interpretive sidebar if Pia suggests a concrete case. |
| Final format | **ArcGIS StoryMap / web-map-heavy submission with technical appendix** | The strongest outputs are visual/spatial: heatmap, distance-decay plot, residual corridor map, and explanatory overlay maps. |

## Remaining blockers / risks

1. **Recipe data license and platform bias.** The What’s Cooking/Yummly-derived source is excellent for a prototype but should not be treated as final without clarifying use permissions or finding a cleaner source.
2. **Cuisine-to-place mapping uncertainty.** `southern_us`, `cajun_creole`, and broad country labels need caveats and possibly narrowed scope.
3. **Ingredient normalization.** Some aliases remain uncertain and require manual/Pia review.
4. **Explanatory mechanisms not yet modeled.** Run 2 used UN M49 only; migration, trade, language/colonial history, and agriculture/climate remain to be added.
5. **Flavor chemistry not yet matched.** FlavorDB/FooDB was evaluated conceptually but not operationally joined.

## Run 3 concrete task list

1. Verify whether the What’s Cooking/Yummly-derived data can be used in the final Fisher submission; if not, switch to TheMealDB or another documented corpus.
2. Improve the ingredient alias crosswalk for the top 100–300 weighted ingredients, with Pia review where possible.
3. Add sensitivity tests excluding or downweighting generic pantry staples, dairy/baking ingredients, and broad ingredient categories.
4. Replace manual cuisine coordinates with CEPII/Natural Earth-supported country coordinates wherever possible.
5. Add CEPII language/colonial variables if `.xls` parsing or alternate data formats are resolved.
6. Add one serious bilateral explanatory dataset: UN DESA migrant stock or UN Comtrade food/spice/agricultural trade.
7. Refit the dyadic model with distance plus one or two explanatory covariates.
8. Recompute residual corridors after the expanded model.
9. Decide final corridor families: likely East/Southeast Asia, Mediterranean/Atlantic, Anglo-American/diaspora, and spice-profile corridors.
10. Run the FlavorDB/FooDB ingredient-match test and decide whether to include a flavor-chemistry figure.
11. Prepare a Pia review packet with the top residual corridors, top ingredients by cuisine, and the flavor-chemistry decision.
12. Build Fisher-facing figures: polished heatmap, distance-decay plot, residual corridor map, overlay map/table, and optional flavor-chemistry figure.
13. Write the final narrative as a StoryMap or map-heavy report.
14. Create a technical appendix documenting data sources, crosswalks, model formulae, limitations, and reproducibility.
15. Review all claims for overstatement, especially anything implying causality.

## Handoff artifacts from Run 2

- `data/run2_dataset_selection_memo.md`
- `data/run2_data_access_log.md`
- `data/raw/recipe_source_manifest.md`
- `data/crosswalks/ingredient_alias_crosswalk.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `data/processed/cuisine_ingredient_long.csv`
- `data/processed/cuisine_ingredient_matrix.csv`
- `data/processed/cuisine_similarity_cosine.csv`
- `data/processed/cuisine_similarity_jaccard.csv`
- `data/processed/cuisine_pair_model_table.csv`
- `data/processed/residual_culinary_corridors.csv`
- `outputs/distance_baseline_model_summary.md`
- `outputs/overlay_test_summary.md`
- `figures/run2_cuisine_similarity_heatmap.png`
- `figures/run2_distance_decay_plot.png`
- `figures/run2_residual_corridor_map.png`
- `figures/run2_overlay_test_figure.png`
- `docs/flavor_chemistry_feasibility_decision.md`
- `docs/run2_prototype_interpretation.md`

## Exact next input needed from user/Pia

- User: confirm whether final project may use a Kaggle/Yummly-derived prototype dataset if source terms are flagged, or whether a cleaner/opener source is required.
- Pia: review ingredient normalization and advise whether flavor-compound similarity is a defensible secondary layer.


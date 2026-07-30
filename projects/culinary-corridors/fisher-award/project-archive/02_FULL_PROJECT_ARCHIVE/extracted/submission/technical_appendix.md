# Technical Appendix

Created: 2026-04-29

## 1. Reused analysis base

Run 3 reuses the completed Run 2 and Run 2 v2 prototype outputs. It does not redo data acquisition or primary modeling. The key reused files are:

- `data/processed/cuisine_ingredient_long.csv`
- `data/processed/cuisine_ingredient_matrix.csv`
- `data/processed/cuisine_similarity_cosine.csv`
- `data/processed/cuisine_similarity_jaccard.csv`
- `data/processed/cuisine_pair_model_table.csv`
- `data/processed/residual_culinary_corridors.csv`
- `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`
- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `data/processed/run2v2_focus_case_results.csv`
- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`
- `data/processed/run2v2_boundary_permeability_results.csv`
- `data/processed/run2v2_path_connectivity_results.csv`

## 2. Recipe and ingredient preparation

The prototype begins with recipe records containing cuisine labels and ingredient lists. Ingredients are normalized using a rule-based alias crosswalk. The workflow preserves raw ingredient names in the long table and records normalized ingredients for matrix construction.

Core files:

- raw/source notes: `data/raw/recipe_source_manifest.md`
- access/source log: `data/run2_data_access_log.md`
- ingredient alias crosswalk: `data/crosswalks/ingredient_alias_crosswalk.csv`
- cuisine-ingredient long table: `data/processed/cuisine_ingredient_long.csv`

## 3. Cuisine-to-place mapping

Cuisine labels are mapped to coordinate proxies for spatial analysis. This is necessary for distance calculation and corridor mapping, but it is also a source of uncertainty. The final text therefore avoids treating cuisine labels as exact nation-state units.

Core file:

- `data/crosswalks/cuisine_geo_crosswalk.csv`

Each retained cuisine has mapped place, ISO code where applicable, latitude, longitude, mapping confidence, and caveat notes.

## 4. Cuisine vectors and similarity metrics

The cuisine-by-ingredient matrix represents cuisines as vectors of ingredient frequencies or weights. Pairwise cuisine similarity is computed using cosine similarity and a robustness metric inherited from Run 2, including Jaccard similarity.

Core files:

- `data/processed/cuisine_ingredient_matrix.csv`
- `data/processed/cuisine_similarity_cosine.csv`
- `data/processed/cuisine_similarity_jaccard.csv`

The final narrative emphasizes cosine similarity because it is suited to vector comparison and was used in the distance/residual model.

## 5. Generic-ingredient sensitivity model

Run 2 v2 introduced explicit generic-ingredient filtering to reduce the effect of common pantry and recipe-platform vocabulary. The policy labels ingredients for removal, downweighting, retention, or flagging.

Core files:

- `data/crosswalks/run2v2_generic_ingredient_policy.csv`
- `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`
- `outputs/run2v2_global_sensitivity_summary.md`

The final package uses filtered results where possible because they are more defensible than the unfiltered global prototype.

## 6. Distance baseline and residual computation

The core spatial model compares cuisine similarity with geographic distance. The baseline relationship can be summarized as:

```text
cosine_similarity ~ log(distance_km)
```

For each cuisine pair, the model generates a predicted similarity based on distance. The residual is:

```text
residual = observed cosine similarity - predicted cosine similarity from distance-only model
```

Positive residuals identify cuisine pairs that are more similar than a distance-only model predicts.

Core files:

- `data/processed/cuisine_pair_model_table.csv`
- `outputs/distance_baseline_model_summary.md`
- `data/processed/residual_culinary_corridors.csv`
- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `outputs/run2v2_filtered_distance_baseline_summary.md`

## 7. Focused cases

Run 2 v2 locks final inference to scoped cases:

- primary: East/Southeast Asia;
- secondary/diagnostic: Iberian/Atlantic-Pacific.

Core files:

- `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`
- `data/processed/run2v2_focus_case_results.csv`
- `outputs/run2v2_focus_case_summary.md`

The East/Southeast Asia case is the strongest because it has coherent geography, six available target cuisines, and positive residual links after filtering.

## 8. Geospatial-only analyses

Run 2 v2 adds geospatial analyses that cannot be obtained from ingredient vectors alone.

### Residual bridge scores

Bridge scores aggregate pairwise residual links into place-level roles. They depend on mapped coordinates, distance, residuals, and long-distance pair identification.

Core file:

- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`

### Boundary/permeability check

Boundary/permeability groups pairs by spatial relationship and compares residual strength across classes.

Core file:

- `data/processed/run2v2_boundary_permeability_results.csv`

### Path/connectivity proxy

The path/connectivity proxy is exploratory. It uses spatial-accessibility classes rather than true least-cost path or historical route data.

Core file:

- `data/processed/run2v2_path_connectivity_results.csv`

## 9. Final figures

Run 3 creates final figure copies under `figures/final/`:

- `figures/final/final_global_discovery_figure.png`
- `figures/final/final_distance_or_residual_model_figure.png`
- `figures/final/final_east_southeast_asia_case_figure.png`
- `figures/final/final_geospatial_bridge_or_boundary_figure.png`
- `figures/final/final_secondary_or_sensitivity_figure.png`
- `figures/final/final_boundary_permeability_appendix_figure.png`

Captions are in `figures/final/final_figure_captions.md`.

## 10. Reproducibility notes

Run 3 itself mostly packages and relabels existing outputs. The main reproducibility requirement is therefore to preserve the relationship between final figures and their source artifacts. The Run 2 and Run 2 v2 reproducibility logs remain the source for data acquisition, cleaning, similarity computation, and modeling commands.

Run 3 final manifest:

- `outputs/run3_reproducibility_and_manifest.md`

Prior logs:

- `outputs/run2_reproducibility_log.md`
- `outputs/run2v2_reproducibility_log.md`

# Run 4 Data and Source Risk Review

Created: 2026-04-29

| Layer | Source / artifact | Role | Main risk | Fix or disclosure |
|---|---|---|---|---|
| Recipe / ingredient corpus | `data/raw/recipe_source_manifest.md`; Run 2 staged What’s Cooking / Yummly-derived corpus | Core outcome data for ingredient profiles | Platform-mediated and English-language/American-recipe bias; not globally representative | State that global results are a discovery screen. |
| Ingredient normalization | `ingredient_alias_crosswalk.csv`; `run2v2_generic_ingredient_policy.csv` | Converts raw ingredients to normalized features | Alias choices can change similarity values | Show sensitivity filtering; ask Pia to review food-science assumptions. |
| Cuisine geography | `cuisine_geo_crosswalk.csv` | Coordinates and spatial grouping for cuisine labels | Cuisine labels are not exact countries or homogeneous cultures | Use mapping confidence notes; frame as approximate spatial anchor. |
| Similarity matrices | `run2v2_cuisine_ingredient_matrix_filtered.csv`; residual outputs | Measures observed cuisine similarity | Similarity depends on metric and ingredient filtering | Report cosine plus robustness metric; disclose filtering rules. |
| Spatial baseline | Pairwise geographic distance from cuisine coordinates | Establishes expected similarity by distance | Straight-line distance ignores route, ports, barriers, and historical networks | Present as baseline, not complete movement model. |
| Focused cases | `run2v2_focus_case_results.csv` | Supports primary inference and secondary case | Small number of cuisine labels per case | Use modest claims; prioritize case clarity over global causality. |
| Bridge/boundary outputs | bridge scores and boundary/permeability results | Geospatial-only Fisher insight | Prototype-level metric, not formal network or hotspot test | Use as spatial role summary; propose network/least-cost model as extension. |

## Risk effect on Fisher scoring
The data stack is competitive because it integrates recipe/ingredient data, normalized features, geography, distances, residual models, focused cases, and sensitivity checks. The main risk is trust: judges need to see uncertainty clearly enough that the analysis reads as rigorous rather than overextended.

## Required disclosures
- The recipe corpus is a proxy, not a census of global cuisine.
- Cuisine-to-place mapping is approximate.
- Positive residuals are model outputs, not proof of historical mechanism.
- Generic-ingredient filtering is necessary because platform recipes over-represent pantry staples.
- East/Southeast Asia is treated as the strongest focused case because it is spatially coherent in the available labels.

## Exact fix
Add a compact source/limitation panel to the StoryMap, report, or poster. This directly supports the playbook's data documentation criterion.

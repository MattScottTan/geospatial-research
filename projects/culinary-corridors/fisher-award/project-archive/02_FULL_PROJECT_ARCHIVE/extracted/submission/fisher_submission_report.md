# Culinary Corridors: Mapping Food Similarity, Spatial Residuals, and Regional Exchange

Created: 2026-04-29

## Abstract placeholder

See `submission/abstract_and_pitch.md` for the final 150–250 word abstract and oral pitch.

## 1. Introduction

Food is cultural, chemical, historical, and spatial. Ingredients and techniques move through trade, migration, climate zones, ports, borders, and households. This project asks whether cuisine similarity can be analyzed as geographic evidence.

The central question is:

> **When two cuisines are similar, is that similarity mostly explained by geographic distance, or do residual similarities reveal spatial corridors, regional bridges, and boundary patterns that distance alone cannot explain?**

The project uses a global recipe-derived cuisine model as a discovery screen, then narrows interpretation to focused cases where the spatial logic is more defensible. The final scope is global discovery plus an East/Southeast Asia primary case and an Iberian/Atlantic-Pacific secondary case.

## 2. Data

The prototype uses a prepared What’s Cooking / Yummly-derived recipe corpus staged in Run 2. The corpus contains cuisine labels and ingredient lists, which makes it usable for cuisine-vector construction. The project also uses cuisine-to-place coordinate crosswalks, UN M49-style regional/subregional groupings, and Run 2 v2 sensitivity outputs. Source and usage risks are documented in `submission/data_sources_and_limitations.md`.

The dataset is treated as platform-mediated recipe data, not as a representative census of global foodways. This distinction is central to the interpretation.

## 3. Methods

The workflow proceeds in six steps:

1. normalize recipe ingredients;
2. construct cuisine-by-ingredient matrices;
3. calculate pairwise cuisine similarity using cosine similarity and robustness metrics;
4. map each cuisine label to a coordinate proxy with confidence notes;
5. fit a distance-only baseline model;
6. compute and map residuals as candidate culinary corridors.

Run 2 v2 added a generic-ingredient filtering policy so high-frequency staples such as salt, water, sugar, flour, oil, butter, and broad pantry terms do not dominate similarity structure. It also added geospatial-only outputs, especially residual bridge scores and boundary/permeability summaries.

## 4. Global discovery result

![Global discovery figure](../figures/final/final_global_discovery_figure.png)

The global filtered residual map identifies cuisine pairs whose ingredient-profile similarity is higher than a distance-only model predicts. This figure is used as discovery rather than proof. It shows where the model finds candidate culinary corridors, but it does not explain why they exist.

The global result matters because it motivates a narrower question: which residual patterns are coherent enough to interpret spatially?

## 5. Distance baseline and residuals

![Distance or residual model figure](../figures/final/final_distance_or_residual_model_figure.png)

The distance baseline tests whether cuisine similarity declines with geographic distance. The Run 2 v2 filtered model reported a negative log-distance coefficient and an R² of 0.3553. That supports a modest but important claim: geography explains part of cuisine similarity, but not all of it.

The unexplained component—the residual—is the project’s main spatial object. Positive residuals mark cuisine pairs that are more similar than geography alone predicts.

## 6. Primary case: East/Southeast Asia

![East/Southeast Asia case figure](../figures/final/final_east_southeast_asia_case_figure.png)

The East/Southeast Asia focused case includes Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino cuisines. It is the strongest final case because it forms a coherent regional/cross-subregional spatial subset and retains multiple positive residual links after generic-ingredient filtering.

The top filtered residual links include Thai–Vietnamese, Chinese–Korean, Filipino–Thai, Filipino–Vietnamese, and Chinese–Filipino. These support a careful claim: within this subset, cuisine similarity appears spatially organized around regional adjacency and cross-subregional links. The project does not claim a specific historical mechanism has been proven.

## 7. Geospatial bridge scores

![Residual bridge score figure](../figures/final/final_geospatial_bridge_or_boundary_figure.png)

Residual bridge scores aggregate pairwise residuals into place-level roles. Instead of only asking which cuisine pairs are unexpectedly similar, the bridge-score analysis asks which cuisines repeatedly participate in positive residual corridors.

This is the project’s strongest geospatial-only contribution. Ingredient vectors alone can identify similarity, but they cannot identify which places become spatial bridges after controlling for distance. That requires coordinates, distance baselines, residuals, and mapped place-level aggregation.

## 8. Secondary case: Iberian/Atlantic-Pacific corridor hypothesis

![Secondary/diagnostic figure](../figures/final/final_secondary_or_sensitivity_figure.png)

The Iberian/Atlantic-Pacific case illustrates how long-distance residual corridors can suggest spatial histories of exchange. It includes Spanish, Brazilian, Mexican, Filipino, Cajun/Creole, Jamaican, and Southern U.S. labels where available.

This case is visually useful but more interpretively risky. It should be treated as a corridor hypothesis because it is vulnerable to platform bias, broad cuisine labels, and overinterpretation of colonial or maritime histories.

## 9. Limitations

The most important limitations are:

- The recipe corpus is not globally representative.
- Cuisine labels are broad and sometimes regional or diasporic.
- Coordinates are proxies, not exact origins of food traditions.
- Generic ingredients can distort similarity if not filtered.
- Residuals are associations, not causal proof.
- Migration, trade, colonial, and maritime mechanisms remain hypotheses unless explicitly modeled.

These limitations do not invalidate the project. They define the proper scope of the claim.

## 10. Conclusion

Culinary Corridors shows that cuisine similarity can be studied as a geospatial phenomenon. The final claim is not that the model explains world cuisine. The claim is that GIS can reveal a spatial residual structure in food data: candidate corridors, focused regional links, bridge cuisines, and boundary patterns that ingredient analysis alone would miss.

That is the Fisher-facing contribution: the map and spatial model are not decoration. They produce the insight.

## Source and reference note

A complete source list is provided in `submission/references.md`. Data and limitation details are provided in `submission/data_sources_and_limitations.md`. Methods are documented in `submission/technical_appendix.md`.

## Post-audit revision note

This report was reviewed against `outputs/run3_claim_audit_checklist.md`. Language implying causal proof, global representativeness, or exact cuisine-to-nation equivalence has been removed or qualified. Mechanism language is framed as hypothesis or association unless directly computed.

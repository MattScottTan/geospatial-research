# Culinary Corridors: Mapping Where Food Similarity Breaks Distance

**Committee-ready final report for Fisher Award review**  
Created: 2026-04-30

## Abstract

**Culinary Corridors** uses geographic information science to ask when cuisine similarity follows distance and when it breaks distance-based expectation. The project represents cuisines as filtered ingredient profiles, calculates pairwise cuisine similarity, anchors cuisine labels to approximate geographic locations, fits a distance baseline, and maps the residuals: places and cuisine pairs whose similarity is higher than distance alone predicts. The global model is used as a discovery screen, while East/Southeast Asia is treated as the primary focused case because it is the most spatially coherent subset in the available data. A residual bridge-index then aggregates pairwise residual links into mapped place-level roles, and a Run 4 v2 corridor-accessibility proxy adds focused spatial context using subregion, distance, coastal/island position, maritime context, and transparent barrier flags. The project does not claim that the recipe corpus represents all world cuisine, nor does it prove that migration, trade, colonialism, or maritime exchange caused the observed similarities. Its contribution is methodological and cartographic: GIS transforms ingredient similarity into a spatial-inference problem about corridors, bridges, boundaries, and residual geography.

## Executive summary

The central finding is that cuisine similarity is spatially structured but not reducible to straight-line distance. The distance model explains a meaningful portion of similarity, but the residuals reveal candidate culinary corridors: links where observed ingredient similarity exceeds distance-based expectation. The strongest defensible interpretation comes from the East/Southeast Asia focused case, especially high positive residuals such as Thai-Vietnamese and Chinese-Korean. The residual bridge index further shows how pairwise residuals can be aggregated into place-level spatial roles, with Filipino cuisine emerging as a primary-case bridge in the available prototype data.

The most important Fisher-facing point is that the project requires GIS. A non-spatial recipe model can cluster cuisines, but it cannot identify which similarities are unexpected relative to distance, where those residuals occur, whether they form regional corridor patterns, or which places become bridge nodes in residual space.

## Research question

**When does cuisine similarity follow geographic distance, and when does it break distance-based expectation in ways that reveal candidate culinary corridors, bridge regions, or spatial boundary patterns?**

Subquestions:

1. Can cuisines be represented as ingredient profiles and compared quantitatively?
2. Does cuisine similarity decay with geographic distance?
3. Which cuisine pairs are more similar than distance alone predicts?
4. Which focused regional case supports the strongest spatial interpretation?
5. Can residual similarity be mapped as bridge roles or corridor/accessibility patterns that require GIS to detect?

## Problem framing

Food is a global science and culture topic, but similarity among cuisines is not evenly distributed across space. Ingredient repertoires may reflect ecological constraints, proximity, exchange, diaspora, colonial histories, migration, trade, shared techniques, platform bias, or simple pantry overlap. This creates a GIS problem: the interesting object is not only which cuisines are similar, but **where that similarity is spatially expected or spatially surprising**.

The project therefore avoids a decorative 'world food map' framing. Instead, it uses food as spatial evidence. Similarity is first measured in ingredient space, then compared to geographic expectation. The residuals become the central spatial object.

## Fisher Award alignment and prior-winner logic

The Fisher Award strategy materials emphasized five dimensions: innovation/creativity, use of GIS, data complexity/relevance/documentation, analytical approach/execution, and visualization/cartographic communication. Run 4 aligned the project to those dimensions by changing the frame from general food similarity to **residual culinary geography**. The project now follows a winner-like structure:

- a strong spatial question;
- a nontrivial geospatial operation;
- a clear data pipeline;
- a visually led argument;
- cautious interpretation and visible limitations;
- a focused case rather than broad global overclaiming.

The Run 4 internal alignment score improved from 80.8 to 91.9 out of 100. This score is not an official Fisher score; it is an internal diagnostic based on the uploaded strategy packet and the project's own playbook rubric.

## Data

The core data stack includes:

- a staged cuisine-labeled recipe/ingredient corpus;
- normalized ingredient names and an ingredient alias crosswalk;
- a generic-ingredient filtering policy to reduce pantry/platform effects;
- cuisine-to-geography anchors with coordinates, ISO/country-region labels, and mapping-confidence caveats;
- pairwise geographic distances;
- cosine and Jaccard similarity matrices;
- residual culinary-corridor outputs;
- focused East/Southeast Asia and secondary Iberian/Atlantic-Pacific case outputs;
- residual bridge-score and boundary/permeability summaries.

The data-source risk review is explicit: the recipe corpus is a proxy, not a census of global cuisine; cuisine labels are approximate; and positive residuals are model outputs, not historical proof.

## Methods

### 1. Ingredient representation

Each cuisine is represented as a filtered cuisine-by-ingredient vector. Generic pantry ingredients are removed or downweighted through a documented sensitivity policy. This reduces the chance that shared platform vocabulary, such as salt, water, sugar, or generic oils, dominates the similarity measure.

### 2. Cuisine similarity

The project computes pairwise cuisine similarity using cosine similarity and a robustness metric such as Jaccard similarity. These metrics answer the non-spatial question: which cuisines share ingredient profiles?

### 3. Geographic baseline

Cuisine labels are assigned approximate geographic anchors through a crosswalk. For each cuisine pair, the project computes geographic distance and fits a distance-only model:

`similarity_ij = alpha + beta * log(distance_km_ij) + error_ij`

The filtered Run 2 v2 model used 190 cuisine dyads. Its log-distance coefficient was -0.1158 and its R-squared was 0.3553. This is substantively useful: distance matters, but it does not explain everything.

### 4. Residual culinary corridors

The main object is the residual:

`residual_ij = observed_similarity_ij - predicted_similarity_from_distance_ij`

Positive residuals become candidate culinary corridors: cuisine pairs that are more similar than a distance-only geography would predict.

### 5. Focused cases

The global model is a discovery screen. The strongest interpretation comes from East/Southeast Asia because the cuisine labels form a coherent regional geography and include enough cuisines for pairwise comparison: Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino.

### 6. Geospatial-only analyses

The project adds analyses that ingredient clustering alone cannot produce:

- residual corridor maps;
- residual bridge scores, aggregating pairwise residuals into place-level roles;
- boundary/permeability summaries by spatial grouping;
- Run 4 v2 corridor-accessibility proxy for East/Southeast Asia.

## Key findings

### Finding 1: Distance matters, but does not explain all cuisine similarity

The filtered distance model shows a negative log-distance coefficient. Cuisines tend to become less similar as distance increases, but the residuals remain meaningful. This is the project's entry point: food similarity is spatial, but not exhausted by distance.

### Finding 2: The strongest global map is a discovery screen, not a causal model

The global residual map helps identify candidate corridors, but it should not be used to claim global culinary causality. It is valuable because it selects places for focused inquiry.

### Finding 3: East/Southeast Asia is the strongest focused case

Top East/Southeast Asia residuals include:

| cuisine_a   | cuisine_b   |   cosine_similarity |   distance_km |   residual_cosine | subregion_relation          |
|:------------|:------------|--------------------:|--------------:|------------------:|:----------------------------|
| thai        | vietnamese  |               0.856 |       807.994 |             0.359 | same_subregion              |
| chinese     | korean      |               0.692 |      2118.363 |             0.306 | same_subregion              |
| filipino    | thai        |               0.598 |      2261.956 |             0.219 | same_subregion              |
| filipino    | vietnamese  |               0.637 |      1465.159 |             0.209 | same_subregion              |
| chinese     | filipino    |               0.475 |      3102.755 |             0.133 | same_region_cross_subregion |

These links are interpretable as spatial associations within or across coherent subregions, but they are not proof of historical mechanisms.

### Finding 4: Corridor-accessibility context strengthens the focused case

Run 4 v2 adds a proxy corridor/accessibility score for the East/Southeast Asia pairs:

| cuisine_a   | cuisine_b   |   residual_cosine |   corridor_accessibility_score |   terrain_barrier_proxy |   residual_accessibility_alignment |
|:------------|:------------|------------------:|-------------------------------:|------------------------:|-----------------------------------:|
| thai        | vietnamese  |             0.359 |                          0.880 |                   0.200 |                              0.316 |
| chinese     | korean      |             0.306 |                          0.757 |                   0.250 |                              0.231 |
| filipino    | vietnamese  |             0.209 |                          0.862 |                   0.450 |                              0.180 |
| filipino    | thai        |             0.219 |                          0.800 |                   0.450 |                              0.176 |
| chinese     | filipino    |             0.133 |                          0.543 |                   0.550 |                              0.072 |
| chinese     | japanese    |             0.068 |                          0.739 |                   0.450 |                              0.051 |

The highest positive residuals also sit in strong accessibility contexts. Thai-Vietnamese and Chinese-Korean are same-subregion, relatively high-accessibility pairs. Filipino links show why an archipelagic/coastal position may matter for residual bridge interpretation. This is a proxy, not a formal topographic model.

### Finding 5: Bridge scores convert residual links into mapped roles

The residual bridge index is the clearest geospatial-only insight. It turns pairwise residual links into place-level roles:

| cuisine     | mapped_place           |   run4_bridge_index | run4_spatial_role                |
|:------------|:-----------------------|--------------------:|:---------------------------------|
| filipino    | Philippines            |               0.863 | primary_case_bridge              |
| russian     | Russian Federation     |               0.839 | global_residual_bridge           |
| southern_us | Southern United States |               0.692 | global_residual_bridge           |
| jamaican    | Jamaica                |               0.686 | global_residual_bridge           |
| french      | France                 |               0.653 | context_bridge_role              |
| spanish     | Spain                  |               0.532 | secondary_corridor_or_diagnostic |
| british     | United Kingdom         |               0.515 | bias_diagnostic_bridge           |
| irish       | Ireland                |               0.442 | bias_diagnostic_bridge           |

The bridge index cannot be obtained from ingredient vectors alone because it depends on geographic distance, mapped residuals, and place-level aggregation.

### Finding 6: Boundary and permeability checks support spatial structure

Boundary/permeability summaries compare residuals by spatial grouping:

| boundary_class                 |   pair_count |   mean_residual |   median_residual |   mean_similarity |   mean_distance_km |   positive_share |
|:-------------------------------|-------------:|----------------:|------------------:|------------------:|-------------------:|-----------------:|
| iberian_atlantic_interregional |           11 |           0.139 |             0.115 |             0.334 |          11633.784 |            1.000 |
| same_subregion                 |           11 |           0.115 |             0.129 |             0.565 |           1456.179 |            0.727 |
| same_region_cross_subregion    |           32 |          -0.009 |            -0.037 |             0.341 |           3542.672 |            0.375 |
| east_se_asia_cross_subregion   |            9 |          -0.012 |            -0.006 |             0.331 |           3140.293 |            0.444 |
| other_cross_region             |          127 |          -0.019 |            -0.039 |             0.201 |           9675.384 |            0.378 |

These groupings support the idea that residual cuisine similarity has spatial structure. They remain diagnostic rather than causal.

## Figure walkthrough

### Figure 1. Hero spatial argument

![Hero spatial argument](../../figures/final_revised/run4_hero_spatial_argument_figure.png)

This figure shows filtered positive residual culinary corridors after the distance baseline. It introduces the core idea: cuisine similarity sometimes exceeds spatial expectation.

### Figure 2. Residual method

![Residual method](../../figures/final_revised/run4_method_or_model_figure.png)

This figure makes the analytical method legible. Points above the distance trend become positive residual corridors.

### Figure 3. East/Southeast Asia focused case

![East/Southeast Asia focused case](../../figures/final_revised/run4_primary_case_figure.png)

This figure carries the project's strongest inference because it focuses on a coherent regional/cross-subregional geography rather than the entire global corpus.

### Figure 4. Run 4 v2 corridor-accessibility enhancement

![Run 4 v2 topographic/corridor enhancement](../../figures/final_revised/run4v2_topographic_corridor_map.png)

This figure supplements the focused case by comparing residual links to a corridor-accessibility proxy. It uses existing coordinates, subregion labels, distance, coastal/island context, maritime proxy, and transparent barrier flags. It is not a measured topographic or route model.

### Figure 5. Residual bridge-index figure

![Residual bridge index](../../figures/final_revised/run4_geospatial_insight_figure.png)

This figure is the clearest spatial necessity visual. It shows that residual similarity can be aggregated into mapped place-level roles.

### Figure 6. Secondary / limitations figure

![Secondary limitations figure](../../figures/final_revised/run4_secondary_or_limitations_figure.png)

This figure supports the limitations and sensitivity discussion. It should be used as appendix or diagnostic evidence if the final submission needs to be concise.

## Limitations and caveats

1. **Recipe corpus bias.** The recipe corpus is platform-mediated and likely reflects English-language/American recipe conventions. It is not a census of global cuisine.
2. **Cuisine labels are approximate.** A cuisine label is not the same as a nation-state or homogeneous culture. The geography crosswalk uses approximate anchors.
3. **Ingredient normalization is interpretive.** Alias choices and generic-ingredient filtering affect similarity results.
4. **Residuals are associations.** Positive residuals do not prove migration, trade, colonialism, maritime exchange, or topographic causality.
5. **Run 4 v2 accessibility is a proxy.** It is not a DEM-based cost surface, historical route model, or port-network model.
6. **Focused cases are stronger than global claims.** The global map is discovery; the East/Southeast Asia case carries the main interpretation.

## Ethical and data-use considerations

The project should be transparent about data limits and cultural representation. It should avoid implying that a recipe platform speaks for entire cuisines or cultures. It should frame the analysis as a prototype GIS method for exploring food similarity, not as a definitive cultural genealogy.

## Why the project is spatially necessary

Without GIS, the project could only say which cuisines share ingredients. With GIS, it can ask which similarities are expected from distance, which ones are residual, where those residuals occur, whether they form regional structures, and which places become bridge nodes. That transformation from ingredient similarity to residual spatial evidence is the project's core Fisher contribution.

## Recommended submission route

The StoryMap route remains the best final format because the argument is map-led. The static report and PDF are suitable for committee/advisor review or as a backup submission package. The recommended final sequence is:

1. Hero residual-corridor map.
2. Distance/residual method figure.
3. East/Southeast Asia focused case.
4. Run 4 v2 corridor-accessibility figure.
5. Residual bridge-index figure.
6. Limitations/source panel.

## Conclusion

**Culinary Corridors** demonstrates that food can be analyzed as spatial evidence. The project turns recipe ingredients into cuisine profiles, compares cuisine similarity to geographic distance, maps the residuals, and then uses focused regional analysis and residual bridge roles to show that cuisine similarity has a geography beyond simple proximity. Its claims are deliberately modest: the project identifies candidate corridors and bridge roles, not causal histories. Its Fisher strength is that GIS produces the finding.

## Source and artifact notes

Key internal artifacts: `outputs/run2v2_filtered_distance_baseline_summary.md`, `outputs/run2v2_global_sensitivity_summary.md`, `outputs/run2v2_geospatial_analysis_summary.md`, `docs/run4_revised_spatial_thesis_and_scope.md`, `outputs/run4_geospatial_upgrade_summary.md`, `data/run4_data_and_source_risk_review.md`, and `outputs/run4_claim_and_compliance_audit.md`.

Key public source families referenced in the project package include the Harvard Center for Geographic Analysis Fisher Prize pages, Natural Earth/public-domain base map documentation, UN M49 regional classification, UN/FAO-style data portals discussed in the source register, and documented recipe-corpus source notes in `data/raw/recipe_source_manifest.md` and `data/run2_data_access_log.md`.

## Post-audit revision note

This report was checked against the final claim audit. Global results are framed as discovery, focused cases remain non-causal, and the Run 4 v2 topographic/corridor language is explicitly described as a proxy rather than a measured terrain model.

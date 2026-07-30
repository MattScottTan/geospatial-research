# Culinary Corridors — Copy-Paste StoryMap Script

Use this file as the main text source for ArcGIS StoryMaps. Text under **PASTE:** can be pasted directly into the StoryMap. Text under **FIGURE:** tells you which image to upload and where to place it. Captions can be pasted below each figure.

---

## 1. Title / Hero

**Recommended ArcGIS block:** Cover.

**PASTE TITLE:**
Culinary Corridors

**PASTE SUBTITLE:**
Mapping Food Similarity, Spatial Residuals, and Regional Exchange

**PASTE BYLINE:**
Matthew Tan — Fisher Prize submission

**FIGURE:** Upload `figures/final_revised/run4_hero_spatial_argument_figure.png` as the cover image if it crops cleanly. If ArcGIS crops it too aggressively, use a plain cover and place this figure immediately after the opening paragraph as a full-width image.

**PASTE OPENING TEXT:**
Food is often described through culture. This project asks what happens when food is treated as spatial data.

Culinary Corridors uses GIS to compare cuisine similarity against geographic distance. The central question is not simply which cuisines are similar, but where that similarity exceeds what distance alone would predict.

**PASTE CALLOUT:**
Core thesis: cuisine similarity is spatially structured, but not reducible to distance.

---

## 2. Research Question and Problem

**Recommended ArcGIS block:** Text block with one emphasized quote/callout.

**PASTE HEADING:**
The Question

**PASTE BODY:**
The project asks:

**When does cuisine similarity follow geographic distance, and when does it follow corridors, bridges, regions, or boundaries instead?**

A non-spatial food analysis can identify cuisines that share ingredients. GIS adds a different question: are those similarities geographically expected, or are they spatially surprising?

This distinction matters. If two nearby cuisines share ingredients, geography may already explain part of the resemblance. If two cuisines remain highly similar after accounting for distance, that residual similarity becomes a candidate culinary corridor.

**PASTE CALLOUT:**
GIS changes the unit of insight from “similar cuisines” to “spatially unexpected culinary relationships.”

---

## 3. Data and Caveats

**Recommended ArcGIS block:** Text block, then a caution callout.

**PASTE HEADING:**
Turning Food into Spatial Data

**PASTE BODY:**
The analysis begins with a cuisine-labeled recipe dataset. Each cuisine is represented as a filtered ingredient profile: a vector of normalized ingredient frequencies. Raw ingredient names were cleaned and grouped so that similar terms could be compared more consistently.

The project also filters or flags generic pantry ingredients. Ingredients such as salt, water, sugar, oil, pepper, onion, and garlic can inflate similarity because they appear widely across recipes. Removing or downweighting generic terms helps test whether the corridor patterns are more than shared pantry vocabulary.

Each cuisine label is then assigned to an approximate geographic anchor so that cuisine similarity can be compared with geographic distance. These anchors are necessary for spatial analysis, but they are approximate cultural-geographic reference points, not exact national boundaries.

**PASTE CAUTION CALLOUT:**
The recipe corpus is not a census of world cuisine. Cuisine labels are broad, platform-mediated, and geographically approximate. The project uses them as analytical proxies, not as exact representations of cultures or countries.

---

## 4. Spatial Method / Residual Logic

**Recommended ArcGIS block:** Text block followed by full-width image.

**PASTE HEADING:**
The GIS Move: From Similarity to Residual Geography

**PASTE BODY:**
The method has four steps.

First, each cuisine is represented as an ingredient profile. Second, pairwise cuisine similarity is calculated. Third, each cuisine pair is assigned a geographic distance. Fourth, similarity is modeled against distance.

The key output is the residual:

**Residual = observed cuisine similarity − distance-predicted cuisine similarity**

A positive residual means that two cuisines are more similar than a distance-only model predicts. These positive residuals become candidate culinary corridors.

**FIGURE:** Upload `figures/final_revised/run4_method_or_model_figure.png`.

**PASTE CAPTION:**
Cuisine similarity plotted against log geographic distance. The fitted trend is the distance baseline. Points above the trend have positive residuals and become candidate culinary corridors. This figure makes the core GIS operation visible: comparing food similarity to spatial expectation.

**PASTE CALLOUT:**
The map is not just showing cuisine similarity. It is showing where similarity exceeds geographic expectation.

---

## 5. Global Discovery Screen

**Recommended ArcGIS block:** Full-width image plus short explanatory text.

**PASTE HEADING:**
Global Screen: Finding Candidate Corridors

**FIGURE:** Upload or reuse `figures/final_revised/run4_hero_spatial_argument_figure.png`.

**PASTE CAPTION:**
Filtered positive residual culinary corridors after a geographic distance baseline. Blue links highlight the East/Southeast Asia focused case; orange links show global discovery candidates. Line width represents residual strength. The figure shows where food similarity exceeds distance-based expectation; it does not identify historical causes.

**PASTE BODY:**
The global map is a discovery screen. It identifies cuisine pairs whose ingredient similarity is higher than expected after accounting for distance.

This global view is useful because it shows that cuisine similarity has spatial structure. But it is not the strongest place to make final claims. Global recipe data include platform bias, broad cuisine labels, and uneven representation. For that reason, the global result is used to identify candidate corridors, not to prove global culinary history.

**PASTE CAUTION CALLOUT:**
Global = discovery, not proof.

---

## 6. East/Southeast Asia Primary Case

**Recommended ArcGIS block:** Image block or sidecar with figure on the right and text on the left.

**PASTE HEADING:**
Focused Case: East and Southeast Asia

**PASTE BODY:**
The strongest focused interpretation comes from East/Southeast Asia. This case narrows the global screen to a coherent regional geography that includes mainland, coastal, island, and cross-subregional relationships.

The strongest residual links include Thai–Vietnamese, Chinese–Korean, Filipino–Thai, Filipino–Vietnamese, and Chinese–Filipino relationships. These links are not treated as proof of migration, trade, or historical exchange. Instead, they show where cuisine similarity remains spatially meaningful after the distance baseline.

**FIGURE:** Upload `figures/final_revised/run4_primary_case_figure.png`.

**PASTE CAPTION:**
East/Southeast Asia focused case using filtered positive residual cuisine links. Thicker blue links indicate stronger residual similarity after the distance baseline. This is the strongest inference case because it is spatially coherent and avoids relying on the full global network for interpretation.

**PASTE CALLOUT:**
The focused case is where the project moves from global discovery to stronger spatial interpretation.

---

## 7. Run 5 Topographic Corridor Context

**Recommended ArcGIS block:** Large image block. Optional sidecar for the inset/callout.

**PASTE HEADING:**
Making the Corridor Spatially Legible

**PASTE BODY:**
Run 5 adds a relief-context map for the East/Southeast Asia case. The goal is visual and interpretive: to place the strongest residual links over coastlines, islands, peninsulas, relief, and maritime space.

This map does not prove that terrain or maritime movement caused the observed similarities. Instead, it helps make the focused corridor geographically legible. It shows why this case is more than a matrix of ingredients: the residual links sit within a distinctive spatial setting.

**FIGURE:** Upload `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`.

**PASTE CAPTION:**
East/Southeast Asia residual cuisine links over shaded relief and coastal context. The map makes the focused corridor visually legible by placing residual links near coastlines, islands, peninsulas, relief, and maritime space. It is a relief-context map, not a measured least-cost route or causal terrain model.

**OPTIONAL FIGURE:** If the StoryMap layout has room, add `figures/final_revised/run5_corridor_callout_or_inset.png` as a sidecar or optional zoom.

**OPTIONAL CAPTION:**
Corridor callouts showing two focused residual situations: Thai–Vietnamese mainland adjacency and Filipino links in a maritime/island setting. The callouts clarify spatial contexts that are harder to see in the full regional relief map.

**PASTE CAUTION CALLOUT:**
Topography here is context, not causal proof.

---

## 8. Residual Bridge-Index / Geospatial-Only Insight

**Recommended ArcGIS block:** Full-width image followed by concise explanation.

**PASTE HEADING:**
Which Cuisines Become Spatial Bridges?

**PASTE BODY:**
The residual bridge index is the clearest geospatial-only insight in the project.

Instead of asking only which cuisine pairs are unexpectedly similar, the bridge index asks which mapped cuisine anchors repeatedly participate in positive residual links. This turns pairwise similarity into place-level spatial roles.

Ingredient data alone cannot produce this result. The bridge index depends on geographic distance, residuals, mapped positions, and network structure. That is why it is central to the Fisher argument.

**FIGURE:** Upload `figures/final_revised/run4_geospatial_insight_figure.png`.

**PASTE CAPTION:**
Residual bridge index by cuisine. The index aggregates positive residual degree, top-residual participation, mean positive residual strength, long-distance residual score, and mean residual into mapped place-level roles. This cannot be derived from ingredient vectors alone because it depends on geographic distance and the spatial residual network.

**PASTE CALLOUT:**
This is the strongest GIS-only contribution: spatial residuals become mapped bridge roles.

---

## 9. Secondary / Diagnostic Case and Sensitivity

**Recommended ArcGIS block:** Image block plus short caution text.

**PASTE HEADING:**
Secondary Patterns and Sensitivity

**PASTE BODY:**
The project also examines secondary and diagnostic patterns, including longer-distance residual links and boundary/permeability groupings. These results are useful because they test whether residual cuisine similarity has spatial structure beyond the primary case.

They are also the place where caution matters most. Some long-distance residuals may reflect real spatial histories, but they may also reflect recipe-platform bias, broad cuisine labels, shared generic ingredients, or English-language recipe conventions. For that reason, this section is interpreted as diagnostic rather than conclusive.

**FIGURE:** Upload `figures/final_revised/run4_secondary_or_limitations_figure.png`.

**PASTE CAPTION:**
Boundary/permeability diagnostic summarizing mean residual similarity by spatial grouping. Positive values indicate that similarity is higher than distance-only expectation on average. The result supports spatial structure while remaining diagnostic rather than causal.

**PASTE CALLOUT:**
Secondary patterns are hypothesis-generating. The primary inference remains East/Southeast Asia plus the residual bridge analysis.

---

## 10. Limitations and Claim Discipline

**Recommended ArcGIS block:** Text block with bullets and a caution callout.

**PASTE HEADING:**
What This Project Can — and Cannot — Claim

**PASTE BODY:**
This project makes a spatial argument, not a causal historical proof. Its strongest claims are limited to spatial structure, distance residuals, focused-case evidence, and bridge-score insight.

Key limitations:

- The recipe corpus is platform-mediated and is not globally representative.
- Cuisine labels are broad and do not map cleanly to modern nation-states.
- Ingredient normalization involves judgment.
- Generic pantry ingredients can inflate similarity, which is why filtering and sensitivity checks matter.
- Positive residuals are spatial associations, not proof of migration, trade, colonialism, or maritime exchange.
- The Run 5 relief map provides spatial context; it is not a true least-cost path model or causal topographic analysis.

**PASTE CAUTION CALLOUT:**
The project identifies candidate culinary corridors. It does not prove what caused them.

---

## 11. Conclusion and Contribution

**Recommended ArcGIS block:** Text block; optionally repeat the bridge-index or hero figure as a small closing visual if the story feels visually sparse.

**PASTE HEADING:**
Conclusion: Food as Spatial Evidence

**PASTE BODY:**
Culinary Corridors shows how food similarity can become a GIS question. By comparing cuisine similarity against geographic distance, the project identifies where food follows distance, where it breaks distance, and where cuisines become bridge nodes in a residual spatial network.

The project’s contribution is not that it explains all global cuisine. It is that GIS changes the question. Instead of asking only which cuisines are similar, it asks where similarity is geographically expected, where it is spatially surprising, and what mapped roles those residual links create.

**PASTE FINAL SENTENCE:**
GIS transforms cuisine similarity from a list of shared ingredients into a map of residual corridors, bridges, and spatial interpretation.

---

## 12. Sources / PDF Backup Note

**Recommended ArcGIS block:** Text block at the end; add a button or hyperlink if a public PDF URL is available.

**PASTE HEADING:**
Sources, Methods, and Full Report

**PASTE BODY:**
This StoryMap summarizes the Fisher submission package. The full PDF report contains the complete methods, data notes, source limitations, figure sequence, and claim audit.

Primary data and analysis components include a cuisine-labeled recipe/ingredient corpus, ingredient normalization and filtering, cuisine-to-geography anchors, pairwise distance modeling, residual corridor mapping, East/Southeast Asia focused-case analysis, residual bridge-index mapping, boundary/permeability diagnostics, and Run 5 relief-context visualization.

If the submission form allows supporting materials, include the complete PDF report as a backup. If the form accepts only one URL, include the PDF link in this final section of the StoryMap.

**PASTE PDF BACKUP LINE:**
Full technical report: [insert public/shareable PDF link here]

**PASTE FINAL SOURCE NOTE:**
All interpretations are cautious: global results are discovery, focused cases support stronger but non-causal inference, topographic relief is contextual, and the recipe corpus is not treated as globally representative.

---

# Claim-Audit Revision Note

This script was checked against the Run 6 claim-safety audit. No overclaiming edits were required. If new language is added in ArcGIS, preserve the distinction between global discovery, focused inference, spatial context, and non-causal interpretation.

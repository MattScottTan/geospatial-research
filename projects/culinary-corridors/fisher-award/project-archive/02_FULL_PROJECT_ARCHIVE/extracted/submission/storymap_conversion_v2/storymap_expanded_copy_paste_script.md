# Culinary Corridors — Expanded Atlas-Style StoryMap Copy-Paste Script



Use this file as the main copy-paste source for ArcGIS StoryMaps. Each section separates text to paste from editor notes and figure instructions.



---


# 1. Cover / title / subtitle / author note

## PASTE TEXT

# Culinary Corridors

## Mapping Food Similarity, Spatial Residuals, and Regional Exchange

Matthew Tan — Fisher Prize submission

Food is often described through culture, memory, and taste. This project asks what happens when food is treated as spatial evidence.

Culinary Corridors uses GIS to compare cuisine similarity against geographic distance. The central question is not simply which cuisines share ingredients. The question is where that similarity is geographically expected, where it exceeds distance-based expectation, and which cuisines become bridge nodes in a residual geography of food resemblance.

At first glance, this may sound like a project about recipes. It is not. Recipes provide the raw material, but the object of analysis is spatial. The project begins with ingredient profiles, adds geographic distance, calculates residuals, and then maps the resulting corridors, focused cases, topographic contexts, and bridge roles.

## EDITOR NOTE / FIGURE INSTRUCTION

Use `figures/final_revised/run4_hero_spatial_argument_figure.png` as the cover only if ArcGIS crops it cleanly. Otherwise use a simple cover and place the hero figure in Section 6.

## PASTE CALLOUT

> Core thesis: cuisine similarity is spatially structured, but not reducible to distance.

## EDITOR NOTE

Recommended ArcGIS block: Cover. Keep the title large and use the subtitle exactly as written.

---


# 2. Opening contrast and introduction

## PASTE TEXT

# Opening: similar food, different geographies

A cuisine-similarity model can tell us that Thai and Vietnamese cuisines share a strong ingredient relationship. It can also tell us that Chinese and Korean cuisines remain highly similar after a distance adjustment, and that Filipino cuisine participates in several links that cross island and maritime space. But those statements are incomplete until they are mapped.

Thai-Vietnamese appears as a compact mainland Southeast Asian relationship. Chinese-Korean sits inside an East Asian regional setting. Filipino-related links look different: they extend through an island and maritime geography where straight-line distance alone is a weak way to describe spatial connection. These three examples reveal the problem at the heart of the project. The meaning of cuisine similarity changes when we ask where it happens.

Most discussions of food similarity begin with culture, history, taste, or technique. Those are essential, but they do not answer a spatial question: is a similarity expected because two cuisines are near each other, or is it surprising because it remains strong after distance is modeled? A map of shared ingredients alone cannot answer that. It can cluster cuisines, but it cannot say whether a similarity follows geography or breaks it.

This atlas approaches food as a geographic signal. It treats cuisines as ingredient profiles, compares those profiles, models similarity against distance, and then studies the residuals. The residuals are the key. They identify cuisine pairs that are more similar than distance alone predicts. Once mapped, those residuals become candidate culinary corridors.

The project is careful about what that means. A residual corridor is not a proven migration path, trade route, colonial history, or terrain-determined food pathway. It is a spatial association: a place where food similarity exceeds a geographic baseline and therefore deserves focused interpretation. That distinction is central to the project’s claim discipline and to its fit with the Fisher Prize.

The opening is meant to work like the first page of an atlas. It does not ask the reader to trust an abstract model immediately. Instead, it gives the reader three spatial situations to hold in mind: a nearby mainland pair, a regional East Asian pair, and an island-maritime bridge. Those situations make the later figures easier to read because the reader already understands why geography matters.

## PASTE CALLOUT

> The question is not simply “which cuisines are similar?” It is “where is cuisine similarity spatially expected, and where is it surprising?”

This opening contrast also clarifies why the project is better suited to a StoryMap than to a conventional static paper. The reader needs to move from an abstract model to a spatial scene: a mainland link, a regional link, and an island-maritime bridge. In each case, the map changes how the same numerical result is interpreted. The StoryMap format lets the project reveal that shift step by step.

## EDITOR NOTE

Recommended ArcGIS block: Text section with an emphasized quote/callout.

---


# 3. Research question and subquestions

## PASTE TEXT

# Research question

**When does cuisine similarity follow geographic distance, and when does it follow corridors, bridges, regions, or boundaries instead?**

This question breaks into five working subquestions.

First, can cuisines be represented as ingredient profiles in a way that is systematic enough for comparison? The project answers this by turning cuisine-labeled recipes into cuisine-by-ingredient vectors.

Second, which cuisines are similar in ingredient space? This is the non-spatial baseline: a cuisine-similarity matrix based on normalized ingredient profiles.

Third, does cuisine similarity decline with geographic distance? If nearby cuisines are often similar, then a raw similarity score is not enough. We need to know how much similarity is already explained by proximity.

Fourth, which cuisine pairs are more similar than distance predicts? These positive residuals become the candidate culinary corridors.

Fifth, which focused regional cases and place-level bridge roles are most interpretable once the residuals are mapped? This is where the project moves from global discovery to spatial inference.

Together, these questions turn food similarity into a GIS problem. The unit of analysis is not just the ingredient list. It is the relationship between ingredient similarity, geographic expectation, mapped residuals, and regional context.

## PASTE CALLOUT

> GIS changes the unit of insight from “similar cuisines” to “spatially unexpected culinary relationships.”

## EDITOR NOTE

Recommended ArcGIS block: Text block with bold research question.

---


# 4. Why food can be treated as spatial data

## PASTE TEXT

# Why food can be treated as spatial data

Food is local, mobile, ecological, social, and historical. Ingredients are grown in environments, moved through trade and migration, adapted through technique, and written into recipes that circulate through platforms. That makes food a rich but complicated spatial signal.

This project does not claim that a recipe corpus captures everything about a cuisine. A cuisine is not a country, and a cuisine label is not a precise polygon. But even an imperfect cuisine-labeled recipe dataset can be used as a structured proxy if the limits are visible. The project therefore treats cuisine labels as approximate cultural-geographic anchors, not as exact representations of nations or communities.

The spatial question emerges because similarity is not evenly distributed. Some similarities are unsurprising: neighboring cuisines may share crops, markets, climate zones, techniques, or regional histories. Other similarities are less expected, especially when two cuisines are distant or separated by water, terrain, or subregional boundaries. The goal is not to explain every similarity historically. The goal is to build a spatial screen that shows where similarity is expected and where it becomes interesting.

The data pipeline makes this possible. Recipes are grouped by cuisine label. Ingredients are normalized so that closely related labels can be compared. Generic pantry terms are removed or downweighted so that common recipe vocabulary does not dominate the result. Each cuisine is then represented as a vector of ingredient frequencies.

At that point, the project has a food dataset. It becomes a GIS project only after geography is added: cuisine anchors, pairwise distances, residual modeling, corridor maps, focused regional cases, bridge scores, and relief context. The difference matters. A recipe model can say that two cuisines are similar. A GIS model can say whether that similarity is spatially expected.

This is also why the project uses several kinds of maps rather than one. The global residual map shows where candidates appear. The focused regional map shows where interpretation is most defensible. The relief map shows how the same links sit within terrain, coastlines, islands, and maritime space. The bridge-index map shows which cuisine anchors repeatedly participate in unexpected residual links. Each map answers a different spatial question.

## PASTE CALLOUT

> Ingredient similarity is the input. Residual geography is the finding.

The project therefore treats cuisine similarity as a layered signal. At one layer, ingredients record recipe vocabulary. At another, geography records distance and spatial context. At a third, residuals record where the first two layers do not line up neatly. The value of the analysis comes from comparing these layers rather than treating any single layer as complete.

## EDITOR NOTE

Recommended ArcGIS block: Text block. Use this section before methods to justify the project’s spatial premise.

---


# 5. How the culinary atlas works

## PASTE TEXT

# How the culinary atlas works

The atlas is built in four stages.

**Stage 1: Build cuisine profiles.** The project starts with a cuisine-labeled recipe dataset derived from the What’s Cooking / Kaggle-Yummly family of data. The prototype retained 39,774 recipes, 428,249 recipe-ingredient rows, 20 cuisine labels, and 5,936 normalized ingredient labels. These figures describe prototype coverage, not population-level representativeness. Each cuisine is converted into a filtered ingredient profile: a vector that records how frequently normalized ingredients appear in that cuisine’s recipes.

**Stage 2: Measure cuisine similarity.** Cuisine profiles are compared using cosine similarity, with Jaccard similarity used as a robustness check. Cosine similarity asks whether two cuisine profiles point in a similar direction in ingredient space. Jaccard similarity asks how much overlap exists in the set of retained ingredients. Together, these metrics answer the non-spatial question: which cuisines share ingredient repertoires?

**Stage 3: Add geography.** Each cuisine label is assigned an approximate geographic anchor. These anchors are necessary for a global comparison, but they are not treated as exact nation-state locations. For each cuisine pair, the project calculates geographic distance and creates a dyadic table with cuisine pair, similarity, distance, and regional metadata.

**Stage 4: Model residual corridors.** Cuisine similarity is modeled against log geographic distance. The filtered distance model used 190 cuisine dyads and returned a negative log-distance coefficient of -0.1158 with an R-squared of 0.3553. This means distance explains a meaningful share of cuisine similarity, but not all of it. The unexplained part is the residual:

**Residual = observed cuisine similarity − distance-predicted cuisine similarity**

Positive residuals identify cuisine pairs that are more similar than distance alone predicts. These are the candidate culinary corridors. The global map identifies candidates; the focused East/Southeast Asia case provides the strongest spatial interpretation; the residual bridge index converts pairwise residuals into mapped place-level roles; and the Run 5 relief map adds topographic and coastal context for the strongest focused case.

The method is intentionally transparent. It does not try to infer hidden history from food data alone. It asks a narrower and more defensible question: where does food similarity exceed geographic expectation?

The staged design also protects the project from overinterpretation. At no point does the model jump directly from ingredients to historical explanation. It first asks a measurable spatial question, then uses the maps to decide where interpretation is reasonable. This is why the StoryMap can be comprehensive without becoming speculative.

## PASTE CALLOUT

> A cuisine pair becomes a candidate corridor only after ingredient similarity is compared with geographic distance.

The staged workflow is also designed to be auditable. Each stage creates an object that can be inspected: a cuisine-ingredient matrix, a similarity matrix, a distance-pair table, a residual-corridor table, and then a map. This matters for Fisher because the maps are not decorative outputs added after the analysis; they are the visible form of the spatial comparison.

## EDITOR NOTE

Recommended ArcGIS block: Long text section, preferably broken into four short subsections or a sidecar with four panels.

---


# 6. Global discovery screen

## PASTE TEXT

# Global discovery screen

The global map is the starting point of the atlas. It uses all 20 retained cuisine labels to identify positive residual culinary corridors: cuisine pairs whose observed ingredient similarity exceeds the similarity predicted by geographic distance alone.

This view is intentionally broad. It shows the project’s full comparison frame, makes the residual concept visible, and identifies candidate patterns for focused analysis. Blue links highlight the East/Southeast Asia focused case. Orange links show other global discovery candidates. The map is useful because it reveals that food similarity is not distributed as a simple geography of proximity.

The global screen must be read carefully. Some long-distance residuals may reflect meaningful spatial histories, but others may reflect recipe-platform bias, English-language recipe conventions, generic ingredient patterns, or coarse cuisine labels. For that reason, the global map is not treated as proof of global culinary exchange. It is a discovery layer.

The map changes the project’s question. Instead of asking whether two cuisines are similar in the abstract, it asks whether that similarity is spatially unexpected. That is the first major GIS contribution of the project. The lines on the map are not routes. They are residual relationships: model outputs that identify where the spatial baseline is exceeded.

The rest of the StoryMap follows those residuals into more defensible settings. First, the distance model explains how the residuals are calculated. Then the East/Southeast Asia case narrows the map to a coherent regional geography. Finally, the bridge-index and topographic-context figures show how residuals can become place-level and corridor-level spatial insights.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload or reuse `figures/final_revised/run4_hero_spatial_argument_figure.png`.

## PASTE CAPTION

This map shows cuisine pairs whose observed ingredient similarity is higher than the distance-only model predicts. Blue links foreground the East/Southeast Asia focused case, while orange links show candidate residual corridors from the broader global screen. Line width represents residual strength. The figure introduces the core spatial idea: the project is not simply mapping similar cuisines, but mapping where similarity exceeds geographic expectation.

## PASTE CALLOUT

> Global = discovery, not proof. The map identifies candidate corridors for focused analysis.

## EDITOR NOTE

Recommended ArcGIS block: Full-width image followed by explanation. This should feel like the first major map of the atlas.

---


# 7. Finding 1: distance matters, but incompletely

## PASTE TEXT

# Finding 1: distance matters, but incompletely

The first analytical question is whether cuisine similarity is related to geographic distance. If distance explains everything, then the project would mostly be a map of proximity. If distance explains nothing, then the geography would be weak. The actual result sits between those extremes.

The filtered distance model relates pairwise cuisine similarity to log geographic distance across 190 cuisine dyads. The model returns a negative log-distance coefficient of -0.1158 and an R-squared of 0.3553. In plain language, cuisines tend to become less similar as distance increases, but distance does not explain all similarity.

This finding matters because it creates the residual space. The model establishes a spatial expectation: given two cuisine anchors and their distance apart, how similar should the model expect them to be? A cuisine pair above the fitted trend is more similar than that distance-only expectation. A cuisine pair below the trend is less similar than expected.

The method figure makes this visible. The fitted line is the distance baseline. The points above the line are the positive residuals. Those points become the candidate culinary corridors.

This is the project’s central GIS move. A non-spatial recipe model can cluster cuisines by shared ingredients, but it cannot define “unexpected” similarity. The unexpectedness only appears after similarity is compared with a spatial baseline. That is why the residual is more important than the raw similarity score.

The model is not causal. It does not claim that distance causes or prevents culinary similarity. It simply establishes a geographic expectation, then maps where observed similarity exceeds that expectation. The significance of the result is interpretive and spatial: cuisine similarity has a distance structure, but that structure leaves meaningful residuals.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `figures/final_revised/run4_method_or_model_figure.png`.

## PASTE CAPTION

The scatterplot shows how the project turns ingredient similarity into spatial analysis. The fitted line is the distance baseline: the model’s estimate of how similar two cuisines should be given their geographic separation. Points above that line have positive residuals, meaning observed similarity is higher than distance alone predicts. Those residuals are the project’s central spatial object.

## PASTE CALLOUT

> The key object is not the similarity score. It is the residual: observed similarity minus distance-predicted similarity.

## EDITOR NOTE

Recommended ArcGIS block: Image plus explanatory text. This is the main methods/result bridge.

---


# 8. Finding 2: residuals reveal candidate culinary corridors

## PASTE TEXT

# Finding 2: residuals reveal candidate culinary corridors

Once the distance baseline is fitted, each cuisine pair has an observed similarity, a predicted similarity, and a residual. Positive residuals are the pairs where observed similarity is higher than the distance-only model predicts.

This residual framing matters because it avoids a common problem in cultural mapping. Raw similarity can be misleading. Nearby cuisines may look similar because they are near; distant cuisines may look surprising because the map makes distance visually dramatic. The residual model creates a consistent comparison. It asks the same question for every pair: how much does observed similarity exceed or fall short of the distance-based expectation?

The term “culinary corridor” is therefore used carefully. It does not mean that the model has discovered a historical route. It means that the model has identified a spatially unexpected similarity worth investigating. Some residual corridors may align with regional adjacency, shared environments, maritime/coastal context, or historical exchange. Others may be artifacts of the recipe platform, generic ingredient vocabulary, or broad cuisine labels.

This is why the project separates global discovery from focused inference. The global residual map is powerful because it surfaces candidates. But the strongest claims come only after narrowing to a coherent case, checking generic-ingredient sensitivity, and interpreting the result through geography rather than historical speculation.

The filtered sensitivity analysis helps here. The model explicitly removed or downweighted generic pantry ingredients and recalculated residuals. Twelve of the original top 20 residual pairs remained in the filtered top 20, showing that the residual structure does not disappear when generic terms are handled more conservatively. At the same time, several global links changed, confirming that platform and pantry effects matter and should remain visible in the interpretation.

The result is a disciplined workflow: global residuals identify candidate corridors; focused cases decide which candidates are spatially interpretable.

For a Fisher audience, this is the point to emphasize: the map is not an illustration of a conclusion reached somewhere else. The residual is created by a spatial operation, and the map is where that operation becomes interpretable. Without the geographic baseline, there is no residual corridor to map.

## PASTE CALLOUT

> A residual corridor is a model-defined candidate for spatial interpretation, not a historical route.

This is also why the project does not rely only on a single beautiful map. A residual line becomes meaningful only because it sits inside a chain of evidence: ingredient normalization, similarity measurement, geographic anchoring, distance modeling, and focused interpretation. The StoryMap should make that chain visible so the reviewer can see how the figure was produced.

## EDITOR NOTE

Recommended ArcGIS block: Text block after the method figure. Optional: reuse a cropped/global portion of the hero figure if the StoryMap needs visual pacing.

---


# 9. Finding 3: East/Southeast Asia is the strongest focused case

## PASTE TEXT

# Finding 3: East/Southeast Asia is the strongest focused case

The global screen identifies many candidate residuals, but the strongest interpretation comes from a focused regional case. East/Southeast Asia is the primary case because it combines enough retained cuisine labels with a coherent geography: Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino.

The focused model retains 15 cuisine pairs. Nine have positive residuals. The strongest positive residuals are Thai-Vietnamese, Chinese-Korean, Filipino-Thai, Filipino-Vietnamese, and Chinese-Filipino. These pairs do not all represent the same kind of geography. Thai-Vietnamese is a compact mainland Southeast Asian link. Chinese-Korean sits inside an East Asian regional setting. Filipino-related links extend through an island and maritime context.

That variation is why the case is useful. It lets the StoryMap compare different spatial situations inside a manageable regional frame. The question is not whether all East/Southeast Asian cuisines are similar. The question is how the positive residual links become interpretable once they are mapped against regional adjacency, subregion, coastlines, islands, and distance.

This focused case also reduces the risk of global overclaiming. The full global model includes long-distance links that may be interesting, but they are more exposed to platform bias and broad cuisine-label uncertainty. East/Southeast Asia offers a more controlled setting where the geography is coherent enough to support stronger, though still non-causal, interpretation.

The map should be read as a residual network. Thicker links indicate stronger positive residual similarity after the distance baseline. The figure does not prove why those similarities exist. It shows where the spatial residuals are concentrated and which relationships deserve interpretation.

This is where the project moves from “global discovery” to “focused inference.” The map is still cautious, but it is the strongest case for the Fisher submission because it lets the reviewer see the spatial pattern rather than only read a table of cuisine pairs.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `figures/final_revised/run4_primary_case_figure.png`.

## PASTE CAPTION

This focused map narrows the global discovery screen to the strongest regional case. It highlights positive residual links among Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino cuisine anchors. Because the subset is geographically coherent and contains enough cuisines for pairwise comparison, it supports the strongest non-causal spatial interpretation in the project.

## PASTE CALLOUT

> The focused case carries the strongest interpretation because it is spatially coherent and still visibly map-based.

## EDITOR NOTE

Recommended ArcGIS block: Sidecar or full-width map with text. This should be one of the central StoryMap sections.

---


# 10. Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible

## PASTE TEXT

# Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible

Run 5 adds a relief-context map for the East/Southeast Asia focused case. This map is not a new causal model. It is a cartographic and interpretive layer that makes the corridor visually legible.

The focused residual links sit in different spatial settings. Thai-Vietnamese appears as a mainland Southeast Asian link across a relatively compact regional space. Chinese-Korean appears in a mainland/peninsula East Asian setting. Filipino-related links sit in an island and maritime geography, crossing the South China Sea and western Pacific context rather than following a simple contiguous land relationship.

A table or matrix can list these pairs, but it cannot show the spatial situations that make them different. The shaded-relief map gives the reviewer an immediate visual sense of the geography around the links: coastlines, islands, peninsulas, mountain and relief patterns, and maritime space. That matters because the project is not only measuring similarity. It is asking how similarity becomes spatially interpretable.

The map should be used carefully. It does not prove that topography caused the observed similarities. It does not reconstruct historical food routes. It is not a least-cost path model, port network, trade model, or migration model. Its role is to provide spatial context for the strongest focused case.

Even with that caution, the figure strengthens the Fisher argument. It shows why a geospatial presentation adds value beyond an ingredient matrix. The same residual links become easier to understand when they are placed in a real regional geography. The viewer can see why mainland adjacency, island setting, and maritime space matter as context, even though the project does not convert them into causal claims.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`. Optional sidecar: `figures/final_revised/run5_corridor_callout_or_inset.png` if the layout has room.

## PASTE CAPTION

This relief-context map places the strongest East/Southeast Asia residual links over terrain, coastlines, islands, peninsulas, and maritime space. It helps the viewer read Thai-Vietnamese as a compact mainland link, Chinese-Korean as a regional East Asian link, and Filipino links as island/maritime relationships. The map strengthens the spatial interpretation of the focused case without claiming that terrain or maritime movement caused the similarities.

## PASTE CALLOUT

> Relief and coastline are context, not proof. The map makes the corridor legible; it does not identify the cause of the residuals.

## EDITOR NOTE

Recommended ArcGIS block: Full-width image. Place immediately after the East/Southeast Asia focused-case section.

---


# 11. Finding 5: residual bridge scores identify spatial bridge roles

## PASTE TEXT

# Finding 5: residual bridge scores identify spatial bridge roles

The residual bridge index is the clearest geospatial-only insight in the project.

Pairwise residuals are useful, but they can become a list of links. The bridge index asks a different question: which cuisine anchors repeatedly participate in positive residual relationships? Instead of treating each pair separately, it aggregates residual links into mapped place-level roles.

The index combines several pieces of information: positive residual degree, top-residual participation, mean positive residual strength, long-distance residual score, and mean residual. The result is a map of bridge roles in the residual culinary network. Filipino cuisine emerges as a primary-case bridge in the prototype data, while several other cuisines appear as global or diagnostic bridge roles.

This is not the same as saying that a cuisine is historically responsible for linking others. A bridge score is a spatial-network position, not a causal identity. It means that, after distance is modeled, that cuisine anchor participates in multiple unexpectedly strong residual links.

This is also where the project most clearly requires GIS. Ingredient vectors alone can tell us which cuisines are similar. They cannot tell us which mapped cuisines repeatedly exceed distance-based expectation, nor can they translate those residuals into place-level bridge roles. The bridge index depends on the combination of ingredient similarity, geographic distance, residual modeling, mapped anchors, and network aggregation.

For the Fisher submission, this figure should be treated as a centerpiece. The global map introduces residual corridors. The East/Southeast Asia map provides the focused case. The topographic map makes that case visually legible. The bridge-index figure shows the deeper spatial insight: residual links create mapped roles.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `figures/final_revised/run4_geospatial_insight_figure.png`.

## PASTE CAPTION

The residual bridge index converts pairwise residual links into place-level spatial roles. It combines positive residual degree, top-residual participation, mean residual strength, long-distance residual score, and mean residual into a mapped index. This is the clearest spatial-necessity result: ingredient vectors alone can identify similar cuisines, but only GIS can show which mapped cuisine anchors repeatedly bridge residual similarities after distance is modeled.

## PASTE CALLOUT

> Ingredient data can identify resemblance; GIS identifies residual bridge roles.

## EDITOR NOTE

Recommended ArcGIS block: Full-width image with an emphasized text callout. This is the strongest spatial-necessity section.

---


# 12. Cuisine-pair vignettes

## PASTE TEXT

# Three cuisine-pair vignettes

Global maps and residual indices show structure, but individual pairs make the pattern concrete. These vignettes are not historical explanations. They are examples of how the residual method creates different spatial readings.

These vignettes should be read as examples of spatial reasoning rather than miniature historical essays. Each one begins with a measured residual, then asks what kind of geography surrounds that residual. The result is a set of cautious readings: one mainland, one regional, one maritime/island, and one optional diagnostic long-distance case.

## Thai–Vietnamese: a mainland adjacency case

Thai-Vietnamese is the strongest positive residual in the East/Southeast Asia focused case. Its cosine similarity is 0.856, the pairwise distance is approximately 808 km, and the residual is 0.359. This means the observed similarity is much higher than the distance-only model predicts.

Spatially, this pair is the cleanest focused-corridor example. It sits within mainland Southeast Asia and is classified as same-subregion in the project outputs. The Run 5 relief map makes this easy to read: the link is compact, regional, and visually coherent. The project can safely say that the residual is consistent with a focused mainland corridor context. It should not claim that the model proves a particular diffusion pathway or historical mechanism.

## Chinese–Korean: a regional proximity case

Chinese-Korean is another high positive residual, with cosine similarity of 0.692, distance of approximately 2,118 km, and residual of 0.306. The pair sits inside the East Asian subregion and appears as a strong regional link after the distance baseline.

This vignette shows why residuals are better than raw similarity alone. The pair is not simply marked as similar; it is similar relative to what the distance model would predict. Mapped regionally, it appears as a focused East Asian relationship rather than a scattered global anomaly. The interpretation should remain spatial and non-causal: the model identifies a strong residual association inside a coherent regional setting.

## Filipino links: island and maritime bridge context

Filipino-related links are important because they complicate a simple land-distance story. Filipino-Thai has residual 0.219; Filipino-Vietnamese has residual 0.209; Chinese-Filipino has residual 0.133. These links place Filipino cuisine in a different spatial situation from Thai-Vietnamese or Chinese-Korean. They sit in an archipelagic and maritime context.

The Run 5 relief map helps here. It shows why the Filipino links are not visually legible as simple land adjacency. They cross island and maritime space, making them better understood as residual relationships that require coastal and maritime context. The residual bridge index reinforces this by identifying Filipino cuisine as a primary-case bridge in the prototype data.

The safe claim is that Filipino cuisine occupies a bridge role in the residual spatial network and that its links are more interpretable when mapped in island/maritime context. The unsafe claim would be that the model proves maritime exchange caused those similarities. The StoryMap should keep that distinction explicit.

## Optional diagnostic vignette: Iberian / Atlantic-Pacific links

The secondary Iberian/Atlantic-Pacific case includes longer-distance residual links involving cuisines such as Filipino, Spanish, Brazilian, Mexican, Cajun/Creole, Jamaican, and Southern U.S. These links are visually and conceptually interesting because they raise questions about long-distance culinary resemblance.

They should remain diagnostic. The distances are larger, the labels are broader, and the risk of recipe-platform bias is higher. The value of this case is not proof. Its value is to show that the residual method can surface hypotheses for future work, while the final submission keeps its strongest interpretation anchored in East/Southeast Asia.

## PASTE CALLOUT

> The vignettes turn residual pairs into readable spatial situations: mainland adjacency, regional proximity, and island/maritime bridge context.

The common thread across these vignettes is that residuals are not self-interpreting. A number tells us that observed similarity exceeds a distance expectation. A map tells us what kind of spatial situation the residual occupies. The vignettes are included so the judge can see how the project moves from a ranked table of links to a set of geographic readings.

## EDITOR NOTE

Recommended ArcGIS block: Scrolling text section after bridge-index figure, or sidecar with one panel per vignette. Optional diagnostic vignette may be omitted if the StoryMap feels long.

---


# 13. Secondary / diagnostic case and sensitivity

## PASTE TEXT

# Secondary / diagnostic case and sensitivity

The secondary case helps the project show discipline. It includes longer-distance and cross-region residual patterns, especially in the Iberian/Atlantic-Pacific family. Some of these links are suggestive, but they are not the strongest basis for final claims.

This section has two purposes. First, it shows that residual cuisine similarity has structure beyond one focused region. Second, it shows why the project does not overclaim. Long-distance residuals are harder to interpret because they may reflect platform bias, broad recipe categories, shared generic ingredients, or English-language recipe conventions.

The sensitivity work is therefore part of the argument, not an appendix afterthought. The project filters generic ingredients and compares original and filtered residuals. The filtered model still supports the East/Southeast Asia focused case, but it also shows that some global residual patterns change when generic pantry vocabulary is handled more conservatively.

The boundary/permeability diagnostic extends this caution. It compares mean residual similarity across spatial groupings such as same subregion, same region but cross-subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other cross-region groupings. The result supports the idea that residuals have spatial structure, but it does not identify a causal mechanism.

This section should appear near the end of the StoryMap because it shows methodological maturity. The project is not hiding inconvenient uncertainty. It is using uncertainty to explain why the final interpretation is scoped: global discovery identifies candidates, East/Southeast Asia carries the main inference, and secondary patterns remain diagnostic.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `figures/final_revised/run4_secondary_or_limitations_figure.png`.

## PASTE CAPTION

This diagnostic figure compares residual similarity across spatial groupings such as same subregion, cross-subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other cross-region links. It supports the idea that residual cuisine similarity has spatial structure, while also showing why the broad global result should remain a discovery screen rather than a causal explanation.

## PASTE CALLOUT

> Secondary patterns are hypothesis-generating. They support future research questions, not final causal claims.

## EDITOR NOTE

Recommended ArcGIS block: Image plus text. This section can be shortened if the StoryMap becomes too long, but keep the claim discipline.

---


# 14. What this proves, and what it does not prove

## PASTE TEXT

# What this proves, and what it does not prove

The project makes a spatial argument, not a causal historical argument.

It can strongly claim that cuisine similarity is spatially structured. The distance model shows that similarity is related to geographic distance, but not fully explained by it. Positive residuals identify candidate culinary corridors. East/Southeast Asia is the strongest focused case. Residual bridge scores produce a spatial insight that ingredient clustering alone cannot produce. The Run 5 relief map makes the focused corridor more visually legible.

It can cautiously say that selected residual patterns are consistent with regional adjacency, corridor plausibility, island/maritime context, or possible exchange histories. These are interpretations to investigate, not mechanisms proven by the model.

It cannot claim that migration caused the observed similarities. It cannot claim that trade, colonialism, empire, maritime routes, or terrain caused the observed similarities. It cannot claim that the recipe corpus represents all world cuisines. It cannot treat cuisine labels as exact nation-states. It cannot treat the relief map as a least-cost path model or causal topographic analysis.

Those limits are not weaknesses. They are what make the project defensible. A weaker project would overread the residuals as historical truth. This project treats them as spatial evidence: model-defined relationships that become meaningful when mapped, scoped, and interpreted carefully.

The final contribution is therefore methodological and cartographic. GIS transforms a recipe corpus into a map of spatial expectations, residuals, corridors, focused cases, and bridge roles. The project shows how food can be analyzed as a spatial signal without pretending that the signal is complete or causal on its own.

## PASTE CALLOUT

> Strong claim: residuals reveal spatial structure. Cautious claim: some residuals are consistent with exchange contexts. Forbidden claim: the model proves the cause.

## EDITOR NOTE

Recommended ArcGIS block: Text block with strong/cautious/forbidden claim callout.

---


# 15. Sources, methods, and reproducibility

## PASTE TEXT

# Sources, methods, and reproducibility

This StoryMap summarizes a larger technical workflow documented in the PDF backup and internal project artifacts.

The recipe and ingredient pipeline uses a staged cuisine-labeled recipe corpus derived from the What’s Cooking / Kaggle-Yummly data family and prepared recipe source notes. Ingredients were normalized with an alias crosswalk, and generic pantry terms were removed or downweighted in sensitivity checks. The recipe corpus is treated as a platform-mediated proxy, not as a representative census of world cuisine.

The geography pipeline uses cuisine-to-place anchor points, pairwise geographic distances, UN M49-style regional groupings where relevant, and public map/relief sources for visualization. Natural Earth-style boundary and base-map data support the cartographic context. The Run 5 topographic corridor figure uses relief/coastal context from a local Basemap ETOPO-style relief image. It is a relief-context visualization, not a new elevation model or least-cost routing analysis.

The analysis pipeline was implemented with Python for data preparation, similarity computation, residual modeling, and figure generation. The StoryMap is designed for ArcGIS StoryMaps as the final presentation format. The PDF report remains the technical backup, with more detail on data sources, methods, limitations, and final figure sequence.

Key source families include Harvard Center for Geographic Analysis Fisher Prize pages, What’s Cooking / Kaggle-Yummly recipe data notes, Natural Earth public-domain map data, UN M49 statistical region definitions, Basemap/ETOPO relief context, and the project’s Run 2 through Run 6 internal artifacts.

ChatGPT was used for guidance, drafting, organization, and formatting of the project materials. The analytical results, figures, and claim hierarchy are documented in the project artifacts and should be checked through the final PDF and StoryMap QA materials before submission.

For the final StoryMap, the sources section should be visible but not overwhelming. The most important message is that every major visual has a traceable input family and that the limitations are not hidden. If a reviewer wants the full file-level record, the technical PDF and reproducibility manifests provide that backup.

## PASTE CALLOUT

> The PDF backup contains the technical report; the StoryMap presents the map-led argument.

The reproducibility standard for the StoryMap is practical rather than archival. A reviewer should be able to trace each major visual to its input family and method: recipe corpus to ingredient matrix, ingredient matrix to similarity, similarity and coordinates to residuals, residuals to focused maps, and residuals plus mapped positions to bridge roles. The PDF backup preserves the fuller file-level audit.

## EDITOR NOTE

Recommended ArcGIS block: Sources/methods text near the end. Include source hyperlinks if possible in ArcGIS.

---


# 16. Conclusion and final contribution

## PASTE TEXT

# Conclusion: food as spatial evidence

Culinary Corridors shows how food similarity can become a GIS question.

A conventional recipe analysis can identify shared ingredients. This project asks what happens when those similarities are compared with geographic expectation. The result is a residual geography of food resemblance: places where cuisine similarity follows distance, places where it exceeds distance, and cuisines that become bridge nodes in the residual network.

The strongest result is not a claim that the model explains global cuisine. It does not. The strongest result is that GIS changes the question. It makes it possible to separate raw similarity from spatially unexpected similarity, to move from a global discovery map into a focused regional case, and to translate pairwise residuals into mapped bridge roles.

East/Southeast Asia is the clearest case because its residual links are spatially coherent and visually interpretable. The Run 5 relief map adds corridor context by placing those links over coastlines, islands, peninsulas, terrain, and maritime space. The residual bridge index adds the deeper GIS insight by showing which cuisines occupy bridge positions after the distance baseline.

The project’s final claim is deliberately modest but spatially strong: cuisine similarity is geographically structured, but not reducible to distance. By mapping residuals, the project reveals candidate culinary corridors and bridge roles that cannot be seen from ingredient lists alone.

## PASTE CALLOUT

> Final takeaway: GIS transforms cuisine similarity from a list of shared ingredients into a map of residual corridors, bridges, and spatial interpretation.

## EDITOR NOTE

Recommended ArcGIS block: Closing text. Consider repeating a small version of the bridge-index or hero figure only if the StoryMap feels visually sparse.

---


# 17. PDF backup / technical report note

## PASTE TEXT

# Technical report and PDF backup

This StoryMap is the primary Fisher-facing presentation because the project is map-led. A complete PDF report is available as the technical backup. It includes the full investigation history, data stack, methods, findings, figure sequence, claim hierarchy, limitations, source notes, and practical submission guidance.

If the Fisher submission form accepts both a StoryMap URL and a PDF, submit the StoryMap as the main artifact and include the PDF as supporting documentation. If the form accepts only one URL, submit the StoryMap URL and include a clearly visible PDF backup link in the final section of the StoryMap. If the form accepts only one file, submit the PDF and include the StoryMap URL prominently near the beginning of the report.

Before final submission, check that all figures display correctly on desktop and mobile, all captions are visible, all source notes are included, the PDF link opens in a private/incognito browser, and no section claims causal proof from migration, trade, colonialism, terrain, or maritime routes.

## PASTE CALLOUT

> Recommended submission route: StoryMap primary, PDF backup.

## EDITOR NOTE

Recommended ArcGIS block: Final section with button/link to PDF if a public PDF URL is available.

---

# Culinary Corridors — Regionally Balanced Expanded StoryMap Copy-Paste Script

Use this file as the main v3 copy-paste source. It revises the Run 6 v2 StoryMap so the project reads as a global GIS method with a selected East/Southeast Asia focused case and a mandatory Iberian/Atlantic-Pacific diagnostic comparison.

---

# 1. Cover / title / subtitle / author note

## PASTE TEXT

# Culinary Corridors

## Mapping Food Similarity, Spatial Residuals, and Regional Exchange

Matthew Tan — Fisher Prize submission

Food is often described through culture, memory, and taste. This project asks what changes when food is treated as spatial evidence.

Culinary Corridors uses GIS to compare cuisine similarity against geographic distance. The central question is not simply which cuisines share ingredients. The question is where that similarity is geographically expected, where it exceeds distance-based expectation, and which cuisines become bridge nodes in a residual geography of food resemblance.

At first glance, this may sound like a project about recipes. It is not. Recipes provide the raw material, but the object of analysis is spatial. The project begins with ingredient profiles, adds geographic distance, calculates residuals, and then maps the resulting corridors, focused cases, topographic contexts, and bridge roles.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_hero_spatial_argument_figure.png`. Recommended ArcGIS block: Cover. Use a simple cover if ArcGIS crops the hero figure awkwardly. Otherwise use the hero residual-corridor image as the cover image.

## PASTE CALLOUT

> Core thesis: cuisine similarity is spatially structured, but not reducible to distance.

---

# 2. Opening contrast and introduction

## PASTE TEXT

# Opening: similar food, different geographies

A cuisine-similarity model can tell us that Thai and Vietnamese cuisines share a strong ingredient relationship. It can also tell us that Chinese and Korean cuisines remain highly similar after a distance adjustment, and that Filipino cuisine participates in several links that cross island and maritime space. But those statements are incomplete until they are mapped.

Thai–Vietnamese appears as a compact mainland Southeast Asian relationship. Chinese–Korean sits inside an East Asian regional setting. Filipino-related links look different: they extend through an island and maritime geography where straight-line distance alone is a weak way to describe spatial connection. These examples reveal the problem at the heart of the project: the meaning of cuisine similarity changes when we ask where it happens.

Most discussions of food similarity begin with culture, history, taste, or technique. Those are essential, but they do not answer a spatial question. If two cuisines are similar, is that similarity expected because the cuisines are near each other? Or is it surprising because it remains strong after distance is modeled?

This atlas approaches food as a geographic signal. It treats cuisines as ingredient profiles, compares those profiles, models similarity against distance, and then studies the residuals. The residuals are the key. They identify cuisine pairs that are more similar than distance alone predicts. Once mapped, those residuals become candidate culinary corridors.

The opening examples come from East/Southeast Asia because that region becomes the strongest focused case later in the atlas. But the project does not start there. It starts with a broader global prototype and then narrows to the case where the spatial evidence is most interpretable. That distinction is important: this is a global GIS method with a selected focused case, not an Asia-only cuisine study.

The project is careful about what a residual corridor means. A residual corridor is not a proven migration path, trade route, colonial history, or terrain-determined food pathway. It is a spatial association: a relationship where food similarity exceeds a geographic baseline and therefore deserves focused interpretation. That distinction is central to the project’s claim discipline and to its fit with the Fisher Prize.

## EDITOR NOTE

Recommended ArcGIS block: Text section with one highlighted quote/callout. Keep paragraphs short for StoryMap pacing.

## PASTE CALLOUT

> The question is not simply “which cuisines are similar?” It is “where is cuisine similarity spatially expected, and where is it surprising?”

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

Fifth, which focused regional cases, secondary diagnostic comparisons, and place-level bridge roles become most interpretable once the residuals are mapped?

Together, these questions turn food similarity into a GIS problem. The unit of analysis is not just the ingredient list. It is the relationship between ingredient similarity, geographic expectation, mapped residuals, regional context, and comparative diagnostic evidence.

## EDITOR NOTE

Recommended ArcGIS block: Text block with the research question in bold or as a quote.

## PASTE CALLOUT

> GIS changes the unit of insight from “similar cuisines” to “spatially unexpected culinary relationships.”

---

# 4. Why food can be treated as spatial data

## PASTE TEXT

# Why food can be treated as spatial data

Food is local, mobile, ecological, social, and historical. Ingredients are grown in environments, moved through markets, adapted through technique, and written into recipes that circulate through platforms. That makes food a rich but complicated spatial signal.

This project does not claim that a recipe corpus captures everything about a cuisine. A cuisine is not a country, and a cuisine label is not a precise polygon. “Chinese,” “Mexican,” “Brazilian,” or “Southern U.S.” are broad culinary labels, not exact spatial units. The project therefore treats cuisine labels as approximate cultural-geographic anchors, not as exact representations of nations or communities.

The spatial question emerges because similarity is not evenly distributed. Some similarities are unsurprising: neighboring cuisines may share crops, markets, climate zones, techniques, or regional histories. Other similarities are less expected, especially when two cuisines are distant or separated by water, terrain, or subregional boundaries. The goal is not to explain every similarity historically. The goal is to build a spatial screen that shows where similarity is expected and where it becomes interesting.

The data pipeline makes this possible. Recipes are grouped by cuisine label. Ingredients are normalized so that related ingredient strings can be compared. Generic pantry terms are removed or downweighted so that common recipe vocabulary does not dominate the result. Each cuisine is then represented as a vector of ingredient frequencies.

At that stage, the project has a food dataset. It becomes a GIS project only when the ingredient profiles are connected to geography: cuisine anchors, pairwise distances, residuals, corridor maps, focused cases, boundary diagnostics, topographic context, and bridge roles.

## EDITOR NOTE

Recommended ArcGIS block: Text section. Consider a side note titled “Scope note” with the cuisine-label caveat.

## PASTE CALLOUT

> Scope note: cuisine labels are approximate cultural-geographic anchors, not exact countries.

---

# 5. How the culinary atlas works

## PASTE TEXT

# How the culinary atlas works

The atlas is built in four stages. The stages are intentionally transparent because the project’s argument depends on showing how food data becomes spatial evidence.

**Stage 1: Build cuisine profiles.** The project begins with cuisine-labeled recipes. Each recipe has a cuisine label and a list of ingredients. The raw ingredient strings are preserved, then normalized so that closely related ingredient names can be compared. Recipes are then grouped by cuisine label, producing a cuisine-by-ingredient matrix.

**Stage 2: Measure culinary similarity.** Each cuisine is represented as an ingredient-frequency vector. Pairwise cuisine similarity is computed using cosine similarity, with robustness checks from other similarity measures. This produces a matrix of cuisine resemblance. At this stage, the analysis can say which cuisines share ingredients, but it cannot yet say whether those similarities are geographically expected.

**Stage 3: Add geography.** Each cuisine label is assigned an approximate geographic anchor. This step is imperfect but necessary. The project uses those anchors to calculate pairwise geographic distance. Distance then becomes a baseline expectation: if geography matters, nearby cuisines should often be more similar than distant cuisines.

**Stage 4: Calculate residual culinary corridors.** The project models cuisine similarity against geographic distance and asks how much similarity is expected for each cuisine pair. The residual is the difference between observed similarity and predicted similarity from distance:

**Residual = observed cuisine similarity − predicted similarity from geographic distance.**

A positive residual means a pair is more similar than distance alone predicts. Those positive residuals are mapped as candidate culinary corridors.

The atlas then uses those residuals in three ways. First, the global discovery screen identifies candidate corridors across the whole prototype. Second, focused cases examine where the residuals are most interpretable. Third, residual bridge scores aggregate pairwise residuals into mapped place-level roles.

This design is why the project is not simply “a map of food.” The maps are not decorative. The GIS workflow produces the central object of interpretation: spatial residuals.

## EDITOR NOTE

Recommended ArcGIS block: Text section. Use the residual equation as an emphasized block or quote.

## PASTE CALLOUT

> Residuals are the hinge of the project: they turn ingredient resemblance into a spatial question.

---

# 6. Global discovery screen

## PASTE TEXT

# Global discovery screen: the atlas begins broadly

The first map is a global discovery screen. It shows candidate residual culinary corridors: cuisine pairs whose ingredient similarity is higher than the distance-only model predicts. This is the broadest layer of the project. It is where the atlas asks, across the available cuisine labels, where food resemblance appears spatially unexpected.

The global view matters because it prevents the project from becoming a preselected regional story. East/Southeast Asia is not chosen first and justified afterward. It emerges as the strongest focused case after the broader screen reveals which residual patterns are most spatially coherent and interpretable.

The global map should be read carefully. The lines do not represent historical routes. They are not proof of migration, trade, empire, or culinary diffusion. They are model-defined links: places where observed ingredient similarity exceeds geographic expectation. In that sense, the map is a discovery layer. It shows where to look next.

Several kinds of patterns appear in the global screen. Some residuals are regional and compact, suggesting that distance alone does not capture the full structure of local or subregional cuisine relationships. Others are longer-distance, including Atlantic- and Pacific-linked patterns that are visually intriguing but more difficult to interpret. Some may reflect historical exchange; others may reflect recipe-platform bias, broad cuisine labels, or shared pantry vocabulary.

This is why the project uses a two-level interpretation. The global screen identifies candidates, while focused sections evaluate which candidates can support stronger claims. East/Southeast Asia carries the strongest focused inference. Iberian/Atlantic-Pacific is retained as a mandatory non-Asia diagnostic comparison. The distinction is not a weakness; it is the project’s main source of discipline.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_hero_spatial_argument_figure.png`. Recommended ArcGIS block: Full-width image. Place the hero residual-corridor figure here if it was not used as cover.

## PASTE CAPTION

The global discovery figure maps candidate residual culinary corridors: cuisine pairs whose ingredient similarity exceeds what geographic distance alone predicts. This map is a screening layer, not a causal history. It shows where residual similarity becomes spatially interesting and motivates the focused cases that follow.

## PASTE CALLOUT

> Global discovery does not prove a mechanism. It identifies where spatially unexpected resemblance deserves closer analysis.

---

# 7. Finding 1: distance matters, but incompletely

## PASTE TEXT

# Finding 1: distance matters, but incompletely

A raw cuisine-similarity matrix can show that two cuisines share ingredients, but it cannot tell us whether that similarity is surprising. For that, the project needs a geographic baseline.

The distance model asks whether cuisine similarity changes as geographic distance increases. If nearby cuisines tend to be more similar, then distance explains part of the pattern. If some distant pairs remain highly similar, or some nearby pairs are less similar than expected, those differences become analytically important.

The model is intentionally simple. It estimates cuisine similarity as a function of log geographic distance. The goal is not to produce a final causal model of cuisine formation. The goal is to create a transparent baseline so the project can ask which similarities exceed spatial expectation.

This is where the residual logic begins. For each cuisine pair, the model produces a predicted similarity based on distance. The observed similarity is then compared to the predicted value. Positive residuals identify pairs that are more similar than distance alone predicts. Negative residuals identify pairs that are less similar than expected.

The figure in this section explains that logic visually. It shows the distance baseline and the gap between expected and observed similarity. That gap is the core of the atlas. Without it, the project would only rank similar cuisines. With it, the project can map spatial surprise.

The finding is modest but important: geography matters, but geography does not explain everything. That incomplete relationship is exactly what makes residual corridors meaningful.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_method_or_model_figure.png`. Recommended ArcGIS block: Image plus text. This is the key methods/result bridge.

## PASTE CAPTION

The residual method compares observed ingredient similarity with similarity predicted from geographic distance. Positive residuals are cuisine pairs that are more similar than the distance baseline predicts. The project maps those positive residuals as candidate culinary corridors.

## PASTE CALLOUT

> The model does not explain cuisine history. It creates a spatial expectation against which cuisine similarity can be compared.

---

# 8. Finding 2: residuals reveal candidate culinary corridors

## PASTE TEXT

# Finding 2: residuals reveal candidate culinary corridors

The central result of the project is not that some cuisines are similar. The central result is that some cuisines are more similar than a distance baseline predicts. Those residuals create the project’s candidate culinary corridors.

A corridor in this atlas is not a route drawn from historical evidence. It is a mapped residual relationship. The term “corridor” is used because the relationships are spatial, directional in appearance, and interpretable only when geography is added. But the project avoids treating them as proven pathways.

The residual map does two things. First, it filters the cuisine-similarity matrix through geography. A pair must exceed distance-based expectation to become interesting. Second, it turns numerical residuals into a map. Once mapped, the same residual can be read differently depending on its spatial situation: a mainland adjacency, an island-maritime bridge, a regional proximity pattern, or a long-distance diagnostic link.

This is where the project’s global scope matters. The global screen shows that residual similarity is not confined to one part of the world. It includes compact regional links and longer-distance diagnostic links. But the screen also shows why the project cannot make every region equally central. Some links are easier to interpret spatially than others; some are more vulnerable to data bias; some require more historical or trade covariates than this prototype includes.

Therefore, the project does not pretend that every residual is equally meaningful. It uses the global screen to select focused cases. East/Southeast Asia becomes the strongest focused case because its residuals sit in a coherent regional geography. Iberian/Atlantic-Pacific becomes the required non-Asia diagnostic case because it demonstrates how the method surfaces long-distance hypotheses while demanding greater caution.

## EDITOR NOTE

Recommended ArcGIS block: Text section or transition before focused cases. If the StoryMap feels text-heavy, use this as a shorter transition.

## PASTE CALLOUT

> A residual corridor is a candidate spatial relationship, not a proven historical route.

---

# 9. From global screen to focused case: why East/Southeast Asia carries the strongest inference

## PASTE TEXT

# From global screen to focused case: why East/Southeast Asia carries the strongest inference

The strongest focused case in the prototype is East/Southeast Asia. This is not because the project is only about Asia. It is because the global residual screen needs to be narrowed to the place where the spatial evidence is strongest.

A good focused case needs several qualities. It needs enough retained cuisine labels to compare. It needs positive residual links that survive the filtering and residual workflow. It needs a coherent geography rather than a scattered set of unrelated labels. It also needs a map that helps interpret the residuals rather than merely displaying them.

East/Southeast Asia fits those requirements better than the other candidate cases. The retained cuisines include Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino. The strongest residual links include both mainland and maritime/island situations. Thai–Vietnamese appears as a compact mainland Southeast Asian link. Chinese–Korean appears as a regional East Asian link. Filipino-related links introduce island and maritime context.

The focused-case map does not claim that the model explains the history of these cuisines. Instead, it shows why the region is analytically useful. The residual links can be read in relation to mainland adjacency, regional proximity, archipelagic geography, coastlines, and maritime space. Those spatial contexts make the focused case more interpretable than a global network of lines.

This section is the main inference section of the StoryMap. The global screen identifies candidates; East/Southeast Asia demonstrates how residual cuisine similarity can become a readable spatial pattern.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_primary_case_figure.png`. Recommended ArcGIS block: Image plus text. The heading intentionally frames Asia as a selected focused case rather than the whole project.

## PASTE CAPTION

The East/Southeast Asia focused-case map shows the strongest regional residual links in the prototype. It is the primary inference case because its residuals sit inside a coherent spatial setting with mainland, island, coastal, and regional structure.

## PASTE CALLOUT

> East/Southeast Asia is not the whole project. It is the focused case where the global residual method produces the most defensible spatial interpretation.

---

# 10. Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible

## PASTE TEXT

# Finding 4: terrain, coastlines, islands, and maritime space make the corridor legible

The East/Southeast Asia focused case becomes more visually and geographically legible when the residual links are placed over relief, coastlines, islands, and maritime space. This is the purpose of the Run 5 topographic corridor map.

The map does not add a new causal model. It does not estimate least-cost paths, reconstruct historical trade routes, or prove that terrain caused cuisine similarity. Instead, it provides spatial context for the residual links already identified by the cuisine-similarity and distance model.

That context matters because not all residual links occupy the same kind of geography. Thai–Vietnamese appears as a compact mainland link. Chinese–Korean appears as a regional East Asian link. Filipino-related links cross island and maritime space. A flat matrix makes these all look like rows and columns. A relief and coastline map makes their spatial differences visible.

The map also helps the StoryMap communicate visually. The viewer can see mainland Southeast Asia, the Korean peninsula, the Japanese archipelago, the Philippines, coastlines, shallow seas, and regional terrain in one frame. The corridor links become part of a landscape rather than abstract pairwise edges.

The safe interpretation is that the strongest East/Southeast Asia residuals sit within legible regional, coastal, island, and maritime contexts. The unsafe interpretation would be to say that the relief map proves a mechanism. The map strengthens the spatial reading, but the project’s causal claims remain intentionally limited.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run5_east_se_asia_topographic_corridor_map.png`. Recommended ArcGIS block: Large image, preferably full-width or sidecar. Use after the East/Southeast Asia focused-case section.

## PASTE CAPTION

The Run 5 relief map places the strongest East/Southeast Asia residual links over topographic, coastal, island, and maritime context. It makes the corridor visually legible but does not claim that terrain or maritime routes caused the observed cuisine similarities.

## PASTE CALLOUT

> The relief map provides spatial context, not causal proof.

---

# 11. Finding 5: residual bridge scores identify spatial bridge roles

## PASTE TEXT

# Finding 5: residual bridge scores identify spatial bridge roles

Pairwise residuals are useful, but they can become a list of links. The bridge index asks a different question: which cuisine anchors repeatedly participate in positive residual relationships?

Instead of treating each pair separately, the bridge-index analysis aggregates residual links into place-level spatial roles. It combines positive residual degree, participation in top residual links, mean residual strength, long-distance residual score, and average residual behavior. The result is a map of bridge roles in the residual culinary network.

This is not the same as saying that a cuisine historically caused or transmitted other cuisines. A bridge score is a spatial-network position, not a causal identity. It means that, after distance is modeled, that cuisine anchor participates in multiple unexpectedly strong residual links.

This is also where the project most clearly requires GIS. Ingredient vectors alone can tell us which cuisines are similar. They cannot tell us which mapped cuisines repeatedly exceed distance-based expectation, nor can they translate those residuals into place-level bridge roles. The bridge index depends on ingredient similarity, geographic distance, mapped anchors, residual modeling, and network aggregation.

For the Fisher submission, this figure should be treated as a centerpiece. The global map introduces residual corridors. The East/Southeast Asia map provides the strongest focused case. The topographic map makes that case visually legible. The bridge-index figure shows the deeper spatial insight: residual links create mapped roles.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_geospatial_insight_figure.png`. Recommended ArcGIS block: Full-width image with an emphasized callout. This is the strongest spatial-necessity section.

## PASTE CAPTION

The residual bridge index converts pairwise residual links into place-level spatial roles. Ingredient vectors alone can identify similar cuisines, but only GIS can show which mapped cuisine anchors repeatedly bridge residual similarities after distance is modeled.

## PASTE CALLOUT

> Ingredient data can identify resemblance; GIS identifies residual bridge roles.

---

# 12. Cuisine-pair vignettes

## PASTE TEXT

# Cuisine-pair vignettes

Global maps and residual indices show structure, but individual pairs make the pattern concrete. These vignettes are not historical explanations. They are examples of how the residual method creates different spatial readings.

Each vignette begins with a residual relationship and then asks what kind of geography surrounds it. The point is not to turn a pair into a complete food history. The point is to show how maps change the interpretation of cuisine similarity.

## Thai–Vietnamese: a mainland adjacency case

Thai–Vietnamese is the cleanest mainland example in the East/Southeast Asia focused case. The relationship appears as a strong positive residual, meaning the observed ingredient similarity is higher than the distance-only model predicts.

Spatially, the pair is compact and regional. It sits within mainland Southeast Asia and is easier to read as a focused corridor than a long-distance global anomaly. The Run 5 relief map makes this visible because the link appears within a coherent mainland setting rather than across scattered global space.

The safe claim is that Thai–Vietnamese provides a strong mainland adjacency example of residual cuisine similarity. The unsafe claim would be that the model proves a specific historical diffusion route.

## Chinese–Korean: a regional proximity case

Chinese–Korean provides a second kind of focused example. The pair sits inside an East Asian regional setting and remains strong after the distance baseline. It is not simply a raw similarity result; it is a similarity that exceeds a geographic expectation.

This vignette shows why residuals matter. A similarity matrix can say that two cuisines resemble one another. A residual map can say that the resemblance is stronger than expected after distance is considered and can place that resemblance inside a regional geography.

The safe claim is that Chinese–Korean is a strong residual association inside a coherent East Asian setting. The project does not claim to explain the mechanism behind that association.

## Filipino links: island and maritime bridge context

Filipino-related links are important because they complicate a simple land-distance story. They sit in an archipelagic and maritime context rather than a compact mainland setting.

The Run 5 relief map helps here. It shows why Filipino links are not visually legible as simple land adjacency. They cross island and maritime space, making them better understood as residual relationships that require coastal and maritime context. The bridge-index figure reinforces this by showing how some cuisine anchors participate in multiple unexpected residual relationships.

The safe claim is that Filipino cuisine occupies a bridge role in the residual spatial network and that its links are more interpretable when mapped in island/maritime context. The unsafe claim would be that the model proves maritime exchange caused those similarities.

## Iberian/Atlantic-Pacific: a mandatory non-Asia diagnostic case

The non-Asia diagnostic case includes longer-distance residual patterns involving Iberian, Atlantic, and Pacific-linked cuisine labels such as Spanish, Brazilian, Mexican, Filipino, Cajun/Creole, Jamaican, and Southern U.S. where available in the prototype. These links are visually and conceptually important because they show that the residual method does not only surface Asian regional structure.

This case must be read differently from the East/Southeast Asia focused case. The distances are larger, the cuisine labels are broader, and the risk of recipe-platform bias is higher. The value of the diagnostic case is therefore not proof. Its value is to show that the residual method can surface long-distance corridor hypotheses that deserve future investigation.

The safe claim is that the Iberian/Atlantic-Pacific material is hypothesis-generating and helps test the generality of the residual method. The unsafe claim would be that the prototype proves a specific Atlantic or colonial food pathway. This vignette is included precisely to show that the project is global in method but disciplined in inference.

## EDITOR NOTE

Recommended ArcGIS block: Sidecar or scrolling text. Use one panel per vignette if possible. Make the Iberian/Atlantic-Pacific vignette mandatory, not optional.

## PASTE CALLOUT

> The vignettes turn residual pairs into spatial situations: mainland adjacency, regional proximity, island/maritime bridge context, and non-Asia diagnostic comparison.

---

# 13. Mandatory non-Asia diagnostic case and sensitivity

## PASTE TEXT

# Mandatory non-Asia diagnostic case and sensitivity

The StoryMap would be weaker if it only presented the East/Southeast Asia case. The global screen shows that the residual method produces patterns beyond one region, and the submission should make that visible. The Iberian/Atlantic-Pacific diagnostic case does that work.

This case includes longer-distance and cross-region residual patterns, especially in an Iberian/Atlantic-Pacific family of cuisine labels. These patterns are visually compelling because they raise questions about long-distance culinary resemblance. They are also more difficult to interpret than the East/Southeast Asia focused case.

The reason is methodological. Long-distance residuals are more exposed to confounding from recipe-platform bias, broad cuisine labels, English-language recipe conventions, and shared generic ingredients. A recipe dataset may represent “Spanish,” “Brazilian,” or “Mexican” cuisine through a platform-specific lens. It may also overrepresent pantry ingredients or popular recipe categories. The project therefore keeps this case diagnostic.

That does not make the case unimportant. It shows that the residual method can surface non-Asian hypotheses and that the global model is not merely a pretext for an Asian regional study. It also shows why scope discipline matters. Some residuals are strong enough to motivate focused interpretation; others are best used as future-research signals.

The sensitivity and boundary/permeability figure supports this point. It compares residual behavior across spatial groupings, including same-subregion, cross-subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other cross-region categories. The result supports the idea that residual cuisine similarity has spatial structure, while also showing why not every grouping should carry the same inferential weight.

The conclusion from this section is deliberately balanced: the project is global in method, focused in inference, and diagnostic in its treatment of non-Asia long-distance cases.

## EDITOR NOTE / FIGURE INSTRUCTION

Upload `run4_secondary_or_limitations_figure.png`. Recommended ArcGIS block: Image plus text. Use the secondary/limitations figure as the required non-Asia diagnostic visual.

## PASTE CAPTION

The secondary/limitations figure compares residual similarity across spatial groupings, including East/Southeast Asia cross-subregion and Iberian/Atlantic interregional diagnostics. It supports the idea that residual cuisine similarity has spatial structure, while showing why broader non-Asia cases should remain diagnostic rather than causal.

## PASTE CALLOUT

> The non-Asia diagnostic case keeps the project global without overstating what the current evidence can prove.

---

# 14. Why Europe and Atlantic-linked material remain diagnostic, not primary

## PASTE TEXT

# Why Europe and Atlantic-linked material remain diagnostic, not primary

Europe and Atlantic-linked cuisines do appear in the global residual screen and in the Iberian/Atlantic-Pacific diagnostic layer. They are important to the project because they show that the method can surface long-distance residual patterns outside East/Southeast Asia. But they are not treated as a second primary focused case.

That is a methodological choice, not an omission. A focused case needs more than interesting residuals. It needs a coherent regional geography, enough retained labels, stable interpretation after sensitivity checks, and a visual structure that helps the map carry the argument. East/Southeast Asia meets those requirements most clearly in the current prototype.

The Europe/Atlantic-linked material is more exposed to interpretive risks. Some cuisine labels are broad. Some long-distance similarities may reflect platform-specific recipe vocabulary. Some patterns may be influenced by shared generic ingredients or English-language representations of cuisine. Without additional covariates for migration, trade, colonial history, language, or ingredient flows, the prototype should not elevate those links to the same inferential level as the primary case.

This does not mean the Europe/Atlantic material is weak or irrelevant. It is useful precisely because it shows what the residual method can generate next: a future focused case with additional covariates, more refined cuisine labels, and more specific historical or trade data. In the current submission, it functions as a diagnostic comparison and a boundary on the project’s claims.

The project therefore stays honest: East/Southeast Asia is the strongest focused inference case; Iberian/Atlantic-Pacific is the required non-Asia diagnostic comparison; and Europe-linked residuals remain promising but not fully analyzed as a focused regional model.

## EDITOR NOTE

Recommended ArcGIS block: Callout or short text section after the non-Asia diagnostic figure. This paragraph directly answers the regional-balance concern.

## PASTE CALLOUT

> Europe/Atlantic-linked residuals are included, but not overbuilt. They are diagnostic signals for future focused analysis.

---

# 15. What this proves, and what it does not prove

## PASTE TEXT

# What this proves, and what it does not prove

The project makes a spatial argument, not a causal historical argument.

It can strongly claim that cuisine similarity is spatially structured. The distance model shows that similarity is related to geographic distance, but not fully explained by it. Positive residuals identify candidate culinary corridors. East/Southeast Asia is the strongest focused case. Residual bridge scores produce a spatial insight that ingredient clustering alone cannot produce. The Run 5 relief map makes the focused corridor more visually legible.

It can cautiously say that selected residual patterns are consistent with regional adjacency, corridor plausibility, island/maritime context, or possible exchange histories. It can cautiously say that Iberian/Atlantic-Pacific residuals are useful diagnostic signals for future non-Asia work.

It cannot claim that migration caused the observed similarities. It cannot claim that trade, colonialism, empire, maritime routes, or terrain caused the observed similarities. It cannot claim that the recipe corpus represents all world cuisines. It cannot treat cuisine labels as exact nation-states. It cannot treat the relief map as a least-cost path model or causal topographic analysis. It cannot claim that Europe has been fully analyzed as a focused regional case.

Those limits are not weaknesses. They are what make the project defensible. A weaker project would overread the residuals as historical truth. This project treats them as spatial evidence: model-defined relationships that become meaningful when mapped, scoped, and interpreted carefully.

The final contribution is methodological and cartographic. GIS transforms a recipe corpus into a map of spatial expectations, residuals, corridors, focused cases, diagnostic comparisons, and bridge roles. The project shows how food can be analyzed as a spatial signal without pretending that the signal is complete or causal on its own.

## EDITOR NOTE

Recommended ArcGIS block: Text section with strong/cautious/forbidden claims visually separated if possible.

## PASTE CALLOUT

> Strong claim: spatial structure. Cautious claim: corridor hypotheses. Forbidden claim: causal proof.

---

# 16. Sources, methods, and reproducibility

## PASTE TEXT

# Sources, methods, and reproducibility

This project uses a cuisine-labeled recipe corpus as the food-data foundation. Recipes are transformed into cuisine-by-ingredient profiles through ingredient normalization and generic-ingredient filtering. The analysis then calculates cuisine similarity, maps cuisine labels to approximate geographic anchors, computes pairwise distance, models similarity against distance, and maps residuals.

The final maps and figures draw on the project’s processed cuisine-similarity outputs, distance/residual model outputs, focused East/Southeast Asia results, residual bridge-index outputs, secondary/diagnostic sensitivity summaries, and Run 5 topographic/relief visualization work. The Run 5 relief map uses documented topographic/coastal context as a visual layer, but it is treated as spatial context rather than a causal model.

The workflow was developed through Python-based data processing and figure generation, with ArcGIS StoryMaps used as the final presentation format. The PDF report remains the technical backup and includes the fuller methodology, figures, limitations, and source notes.

Several limitations are central to the interpretation. The recipe corpus is not globally representative. Cuisine labels are broad and cannot be treated as precise countries. Ingredient normalization requires judgment. Generic pantry ingredients can inflate similarity, which is why filtering and sensitivity checks matter. Cuisine-to-place mapping is approximate. Residuals identify spatially unexpected resemblance, not causality. Topographic context improves visual interpretation but does not prove terrain or maritime pathways caused the patterns.

The StoryMap is designed to be readable on its own, while the PDF report provides the deeper technical version. Together, they present the project as a map-led Fisher submission with transparent limitations.

## EDITOR NOTE

Recommended ArcGIS block: Sources/methods panel near the end. Link to PDF backup if possible.

## PASTE CALLOUT

> The PDF report is the technical companion; the StoryMap is the map-led submission narrative.

---

# 17. Conclusion and final contribution

## PASTE TEXT

# Conclusion: what GIS changes

Culinary Corridors began with a simple question: which cuisines are similar? GIS changes that question.

The project does not stop at ingredient resemblance. It asks whether resemblance follows geographic distance, where it exceeds distance-based expectation, which residuals become readable as focused corridors, and which cuisine anchors become bridge nodes in a mapped residual network.

The global discovery screen shows that candidate residual corridors appear across the prototype. The East/Southeast Asia case shows where those residuals become most spatially interpretable. The Run 5 relief map makes that focused corridor visually legible through terrain, coastlines, islands, and maritime space. The residual bridge index turns pairwise links into mapped roles. The Iberian/Atlantic-Pacific diagnostic case keeps the project global while preserving claim discipline.

The strongest contribution is not a claim that food similarity has one cause. It is a method for making food similarity geographically explicit. By combining ingredient profiles, distance baselines, residuals, focused cases, topographic context, and diagnostic comparisons, the project shows how cuisine can be read as spatial evidence.

The final takeaway is this: cuisine similarity is not only a cultural pattern. It is also a geographic pattern. GIS helps reveal where that pattern follows distance, where it breaks distance, and where it forms corridors and bridge roles that would be difficult to see from recipes alone.

## EDITOR NOTE

Recommended ArcGIS block: Closing section. Use one final callout or return to the hero map if desired.

## PASTE CALLOUT

> GIS changes the question from “which cuisines are similar?” to “where does similarity exceed geographic expectation?”

---

# 18. PDF backup / technical report note

## PASTE TEXT

# Technical report and backup materials

This StoryMap is the primary Fisher-facing narrative. A complete PDF report is available as the technical companion. The PDF contains the full investigation history, data pipeline, figure sequence, methodology, limitations, claim hierarchy, and practical submission notes.

Use the PDF if the submission form requires a file upload, if a reviewer asks for technical detail, or if the StoryMap link cannot be accessed. If the form allows both, submit the StoryMap link as the main project and include the PDF as a supporting document.

## EDITOR NOTE

Recommended ArcGIS block: Final note or button/link block. Add a public/shareable PDF link after uploading the PDF to a stable location.

## PASTE CALLOUT

> Recommended submission route: StoryMap first, PDF backup second.

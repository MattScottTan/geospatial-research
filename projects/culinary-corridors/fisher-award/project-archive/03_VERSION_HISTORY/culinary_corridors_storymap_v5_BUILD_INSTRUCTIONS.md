# Culinary Corridors — StoryMap v5 Build Instructions
**Single-file build guide. Open this file, work top to bottom, paste as you go.**

Matthew Tan — Fisher Prize submission
Version: v5 (v4 with rebuilt geospatial figures)

---

## What changed from v4

Four of the six figures were rebuilt with proper cartographic tooling (cartopy + Natural Earth) so the project actually looks geospatial instead of like scatter plots on lat/long axes.

1. **Hero figure (Section 6) — full rebuild.** Now a real Robinson-projection world map with land/ocean basemap, country borders, great-circle residual lines (not straight lat/long segments), labeled cuisine anchors, and an on-figure corpus-coverage caveat.
2. **Primary case figure (Section 9) — full rebuild.** Now a real East/SE Asia regional map with country fills, coastlines, rivers, lakes, lat/long graticule, geographic context labels (China, Japan, South China Sea, etc.). Residual links are color-coded by type (mainland adjacency, regional proximity, island/maritime) with line width proportional to residual strength. A side panel ranks the top 5 residual links with values.
3. **Bridge-index figure (Section 11) — full rebuild.** Two-panel: world map with bridge nodes sized by score and color-coded by region (blue = Asian, orange = non-Asian), plus the bar chart on the right with the headline "← only Asian in top 10" annotation. The non-Asian dominance is now visually obvious at a glance.
4. **Secondary/limitations figure (Section 13) — full rebuild.** Same data, but cleaner typography, color-coded bars (headline Iberian/Atlantic in saturated orange, others in muted tones), n labels in their own column, callout pointing to the headline finding.

Two figures kept as-is:
- **Method scatter (Section 7)** — kept unchanged because the plotted points are the project's real similarity-vs-distance data; rebuilding without that data would have meant synthetic points.
- **Run 5 topographic corridor map (Section 10)** — already excellent; no changes.

What did **not** change: the script text, section structure, claim discipline, word counts, or QA checklist. Only the figures (and their captions/alt text) were updated.

---

## What changed from v3 → v4 (carried over)

1. Cover is text-only ("Minimal" cover type in ArcGIS). Hero figure moved to Section 6.
2. Hero figure caption rewrites the corpus-sparseness as a corpus property, not a finding.
3. Section 11 expanded to ~280 words with the 9-of-10-non-Asian bridge finding stated explicitly.
4. Vignettes rebalanced; Iberian/Atlantic-Pacific extended with figure data (mean residual ≈ 0.14, n=11).
5. Caveats consolidated into Section 15.

Total length: ~3,935 words.

---

## Pre-flight: get these ready before you start

### Figures (have all six on your desktop, named exactly)

| # | Filename | Goes in |
|---|---|---|
| 1 | `v4_01_hero_world_corridors.png` | Section 6 |
| 2 | `v4_02_method_residual_baseline.png` | Section 7 |
| 3 | `v4_03_primary_case_regional_map.png` | Section 9 |
| 4 | `v4_04_topographic_corridor_map.png` | Section 10 |
| 5 | `v4_05_bridge_index_map_and_chart.png` | Section 11 |
| 6 | `v4_06_secondary_residuals_by_grouping.png` | Section 13 |

### Account
Sign in to **storymaps.arcgis.com** with your Harvard ArcGIS Online account. Click **+ New story → Start from scratch**.

---

## How to read this file

For each section below you'll see:

> **➤ ArcGIS action:** what to click in the editor
> **➤ Block type:** which block to add from the `+` menu
> **➤ PASTE:** the exact text to copy in
> **➤ CALLOUT (Quote block):** the highlighted callout to add after the text
> **➤ FIGURE:** image upload, caption, and alt text (only on sections that have one)

ArcGIS StoryMaps adds blocks using the floating **`+`** button that appears between paragraphs when you hover. The block menu offers: Text, Heading, Button, Image, Video, Map, Embed, Code, Quote, Separator, Sidecar, Slideshow, Swipe, Timeline, Table.

You will only need: **Heading, Text, Image, Quote, Separator**.

---

# COVER (Section 1)

> **➤ ArcGIS action:** This is the top of the story. ArcGIS auto-creates the cover when you start a new story.
> **➤ Cover type:** Click the cover area, then in the right-hand panel choose **"Minimal"** as the cover design (no media). If "Minimal" isn't visible, choose the layout option without a background image.
> **➤ Title field — paste:**

```
Culinary Corridors
```

> **➤ Subtitle field — paste:**

```
Mapping food similarity, spatial residuals, and regional exchange
```

> **➤ Byline field — paste:**

```
Matthew Tan — Fisher Prize submission
```

> **➤ After the cover, click `+` and add a Text block. PASTE:**

```
Food is usually described through culture, memory, and taste. This project asks what changes when food is treated as spatial evidence.

Culinary Corridors uses GIS to compare cuisine similarity against geographic distance. The question is not which cuisines share ingredients — it is where that similarity is geographically expected, where it exceeds distance-based expectation, and which cuisines become bridge nodes in a residual geography of food resemblance.

The maps are not decorative. They are the analytical product.
```

> **➤ Click `+` → add a Quote block. PASTE:**

```
Core thesis: cuisine similarity is spatially structured, but not reducible to distance.
```

> **➤ Click `+` → add a Separator block** (this gives a clean visual break before Section 2).

---

# SECTION 2 — Opening: similar food, different geographies

> **➤ Click `+` → Heading block (H2). PASTE:**

```
Opening: similar food, different geographies
```

> **➤ Click `+` → Text block. PASTE:**

```
A cuisine-similarity model can tell us that Thai and Vietnamese cuisines share strong ingredient relationships, that Chinese and Korean cuisines remain similar after a distance adjustment, and that Filipino cuisine participates in links crossing island and maritime space. These statements are incomplete until they are mapped.

Thai–Vietnamese reads as a compact mainland Southeast Asian relationship. Chinese–Korean sits inside an East Asian regional setting. Filipino-related links extend through island and maritime geography where straight-line distance alone is a weak description of spatial connection. The meaning of cuisine similarity changes when we ask where it happens.

Most discussions of food similarity begin with culture, history, taste, or technique. Those are essential, but they do not answer a spatial question: if two cuisines are similar, is the similarity expected because they are near each other, or surprising because it remains strong after distance is modeled?

This atlas treats cuisines as ingredient profiles, models similarity against distance, and studies the residuals — pairs more similar than distance alone predicts. Mapped, those residuals become candidate culinary corridors.

The opening examples come from East/Southeast Asia because that region becomes the strongest focused case later. But the project does not start there. It starts with a global prototype and narrows to where spatial evidence is most interpretable. This is a global GIS method with a selected focused case, not an Asia-only cuisine study.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The question is not "which cuisines are similar?" It is "where is cuisine similarity spatially expected, and where is it surprising?"
```

> **➤ Click `+` → Separator.**

---

# SECTION 3 — Research question

> **➤ Click `+` → Heading (H2). PASTE:**

```
Research question
```

> **➤ Click `+` → Text block. PASTE:**

```
When does cuisine similarity follow geographic distance, and when does it follow corridors, bridges, regions, or boundaries instead?

Five subquestions structure the project.

First, can cuisines be represented as ingredient profiles systematic enough for comparison? The project answers this by turning cuisine-labeled recipes into cuisine-by-ingredient vectors.

Second, which cuisines are similar in ingredient space? This is the non-spatial baseline.

Third, does cuisine similarity decline with geographic distance? If so, raw similarity is not enough — we need to know how much is already explained by proximity.

Fourth, which cuisine pairs are more similar than distance predicts? These positive residuals become candidate culinary corridors.

Fifth, which focused regional cases, secondary diagnostic comparisons, and place-level bridge roles become most interpretable once residuals are mapped?

Together, these questions turn food similarity into a GIS problem. The unit of analysis is not the ingredient list — it is the relationship between ingredient similarity, geographic expectation, mapped residuals, and regional context.
```

> **➤ Click `+` → Quote block. PASTE:**

```
GIS changes the unit of insight from "similar cuisines" to "spatially unexpected culinary relationships."
```

> **➤ Click `+` → Separator.**

---

# SECTION 4 — Why food can be treated as spatial data

> **➤ Click `+` → Heading (H2). PASTE:**

```
Why food can be treated as spatial data
```

> **➤ Click `+` → Text block. PASTE:**

```
Food is local, mobile, ecological, social, and historical. Ingredients are grown in environments, moved through markets, adapted through technique, and written into recipes. That makes food a rich but complicated spatial signal.

The project does not claim a recipe corpus captures everything about a cuisine. A cuisine is not a country, and a cuisine label is not a precise polygon. "Chinese," "Mexican," "Brazilian," and "Southern U.S." are broad culinary labels, not exact spatial units. Cuisine labels are treated as approximate cultural-geographic anchors.

The spatial question emerges because similarity is uneven. Some similarities are unsurprising — neighboring cuisines often share crops, markets, climate zones, and regional histories. Others are less expected, especially when two cuisines are distant or separated by water or terrain. The goal is not to explain every similarity historically. It is to build a spatial screen that shows where similarity is expected and where it becomes interesting.

The project becomes a GIS project, not just a food-data project, when ingredient profiles are connected to geography: anchors, distances, residuals, focused cases, and bridge roles.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Scope note: cuisine labels are approximate cultural-geographic anchors, not exact countries.
```

> **➤ Click `+` → Separator.**

---

# SECTION 5 — How the culinary atlas works

> **➤ Click `+` → Heading (H2). PASTE:**

```
How the culinary atlas works
```

> **➤ Click `+` → Text block. PASTE:**

```
The atlas is built in four stages.

Stage 1: Build cuisine profiles. Cuisine-labeled recipes are normalized so closely related ingredient names can be compared, then grouped into a cuisine-by-ingredient matrix.

Stage 2: Measure culinary similarity. Each cuisine becomes an ingredient-frequency vector. Pairwise similarity is computed using cosine similarity, with robustness checks. This produces a matrix of cuisine resemblance — but cannot yet say whether resemblance is geographically expected.

Stage 3: Add geography. Each cuisine label is assigned an approximate geographic anchor. Pairwise geographic distance is calculated. Distance becomes a baseline expectation.

Stage 4: Calculate residual culinary corridors. Cuisine similarity is modeled against geographic distance. The residual is the difference between observed and predicted similarity:

Residual = observed cuisine similarity − predicted similarity from geographic distance.

A positive residual means a pair is more similar than distance alone predicts. Those positive residuals become candidate culinary corridors.

The atlas uses these residuals three ways. The global discovery screen identifies candidate corridors across the prototype. Focused cases examine where residuals are most interpretable. Residual bridge scores aggregate pairwise residuals into mapped place-level roles.

The maps are not decorative. The GIS workflow produces the central object of interpretation: spatial residuals.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Residuals are the hinge of the project: they turn ingredient resemblance into a spatial question.
```

> **➤ Click `+` → Separator.**

---

# SECTION 6 — Global discovery: from corpus to candidate corridors
**This section now hosts the hero figure.**

> **➤ Click `+` → Heading (H2). PASTE:**

```
Global discovery: from corpus to candidate corridors
```

> **➤ Click `+` → Text block. PASTE:**

```
The first map is a global discovery screen showing candidate residual culinary corridors — cuisine pairs whose ingredient similarity exceeds the distance-only model. This is the project's broadest analytical layer: the place where the atlas asks, across all retained cuisine labels, where food resemblance appears spatially unexpected.

The global view matters because it prevents the project from becoming a preselected regional story. East/Southeast Asia is not chosen first and justified afterward. It emerges as the strongest focused case after the global screen reveals which residual patterns are most spatially coherent.

Reading the figure honestly. The map is shaped by what the corpus contains. The retained cuisine anchors cluster in East and Southeast Asia, parts of Europe, North America, and a handful of Latin American and Caribbean labels. Large regions — most of Africa, most of South Asia, the Middle East, Oceania — are absent or thin. This is not a finding about world food geography. It is a property of the cuisine-labeled recipe corpus, and a reason the project narrows from a global screen to focused interpretation rather than claiming global coverage.

Within that constraint, two patterns emerge: compact regional residuals where distance alone underexplains similarity, and longer-distance residuals — including Atlantic- and Pacific-linked links — that are visually intriguing but harder to interpret.

The global screen identifies candidates. The sections that follow evaluate which candidates support stronger claims.
```

> **➤ Click `+` → Image block. Upload `v4_01_hero_world_corridors.png`.**
> **➤ Image caption — paste in the caption field below the image:**

```
Candidate residual culinary corridors across the prototype corpus, drawn as great-circle links on a Robinson-projection world map. Blue links mark the East/Southeast Asia focused case (line width proportional to residual strength); orange links mark long-distance residual outliers from the global model. Filled black dots are labeled cuisine anchors; small open circles are additional corpus anchors with less certain identity. The on-figure corpus-coverage note states the constraint directly: the map's coverage reflects the cuisine-labeled recipe corpus, not world food geography.
```

> **➤ Image alt text — open the image's "Alt text" field (gear/edit icon on the image block):**

```
Robinson-projection world map with a beige land and light-blue ocean basemap, country borders, and a subtle 30-degree graticule. Blue great-circle lines connect East and Southeast Asian cuisine anchors (Chinese, Japanese, Korean, Thai, Vietnamese, Filipino) at varying widths reflecting residual strength. Orange great-circle lines connect long-distance pairs labeled by the distance-residual scatter as above-line outliers, including British–Russian, Irish–Russian, French–Russian, Italian–Russian, and British–Southern US. Cuisine anchors in Europe, North America, the Caribbean, and South America are also marked and labeled. A boxed corpus-coverage note in the lower right names the regions absent from the corpus.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Global discovery does not prove a mechanism. It identifies where spatially unexpected resemblance, within the corpus's actual coverage, deserves closer analysis.
```

> **➤ Click `+` → Separator.**

---

# SECTION 7 — Finding 1: distance matters, but incompletely

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 1: distance matters, but incompletely
```

> **➤ Click `+` → Text block. PASTE:**

```
A raw cuisine-similarity matrix cannot tell us whether shared ingredients are surprising. For that, the project needs a geographic baseline.

The distance model asks whether cuisine similarity changes as geographic distance increases. If nearby cuisines are often more similar, distance explains part of the pattern. If some distant pairs remain highly similar, or some nearby pairs fall short of expectation, those gaps become analytically important.

The model is intentionally simple: cuisine similarity as a function of log geographic distance. This is not a final causal model of cuisine formation. It is a transparent baseline so the project can ask which similarities exceed spatial expectation.

For each pair, the model produces a predicted similarity. The observed similarity is compared to that prediction. Positive residuals identify pairs more similar than distance predicts; negative residuals, the opposite. The figure makes this gap visible.

The finding is modest but central: geography matters, but geography does not explain everything. The distance baseline produces an R² of about 0.36, leaving substantial structured variation — and that variation is where the project's analytical interest lives.
```

> **➤ Click `+` → Image block. Upload `v4_02_method_residual_baseline.png`.**
> **➤ Caption:**

```
The residual method compares observed ingredient similarity with similarity predicted from geographic distance. Points above the line are pairs more similar than the distance baseline predicts; the gap is the residual the project maps as a candidate culinary corridor.
```

> **➤ Alt text:**

```
Scatter plot of cosine similarity of filtered ingredient profiles versus log geographic distance between cuisine anchors. A regression line of similarity = 1.273 − 0.116 × log(distance) is shown with R² = 0.355. Pairs above the line, including Thai–Vietnamese, are highlighted as positive residuals.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The model does not explain cuisine history. It creates a spatial expectation against which cuisine similarity can be compared.
```

> **➤ Click `+` → Separator.**

---

# SECTION 8 — Finding 2: residuals reveal candidate culinary corridors

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 2: residuals reveal candidate culinary corridors
```

> **➤ Click `+` → Text block. PASTE:**

```
The central result is not that some cuisines are similar. It is that some cuisines are more similar than a distance baseline predicts, and that those residuals create the project's candidate culinary corridors.

A corridor in this atlas is not a route drawn from historical evidence. It is a mapped residual relationship. The term is used because the relationships are spatial and interpretable only when geography is added. The project does not treat them as proven pathways.

The residual map does two things. First, it filters the cuisine-similarity matrix through geography — a pair must exceed distance-based expectation to become interesting. Second, it turns numerical residuals into a map. Once mapped, the same residual reads differently depending on its spatial situation: a mainland adjacency, an island-maritime bridge, a regional proximity pattern, or a long-distance diagnostic link.

The global screen shows that residual similarity is not confined to one part of the world. It includes compact regional links and longer-distance diagnostic links. Different residuals support different inferential weights — which is why the project moves from a global screen to focused case selection.
```

> **➤ Click `+` → Quote block. PASTE:**

```
A residual corridor is a candidate spatial relationship, not a proven historical route.
```

> **➤ Click `+` → Separator.**

---

# SECTION 9 — From global screen to focused case: East/Southeast Asia

> **➤ Click `+` → Heading (H2). PASTE:**

```
From global screen to focused case: why East/Southeast Asia carries the strongest inference
```

> **➤ Click `+` → Text block. PASTE:**

```
The strongest focused case is East/Southeast Asia. This is not because the project is only about Asia. It is because the global residual screen needs to be narrowed to where spatial evidence is strongest.

A good focused case needs four qualities: enough retained cuisine labels to compare; positive residual links that survive filtering; a coherent geography rather than a scattered set of unrelated labels; and a map that helps interpret the residuals rather than merely displaying them.

East/Southeast Asia meets these requirements better than the other candidates. The retained cuisines include Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino. The strongest residual links include both mainland and maritime/island situations: Thai–Vietnamese as a compact mainland link, Chinese–Korean as a regional East Asian link, and Filipino-related links crossing archipelagic geography.

The focused-case map does not claim the model explains the history of these cuisines. It shows why the region is analytically useful: the residual links can be read in relation to mainland adjacency, regional proximity, archipelagic geography, and maritime space. Those spatial contexts make the focused case more interpretable than a global network of lines.

This section is the main inference section. The global screen identifies candidates; East/Southeast Asia demonstrates how residual cuisine similarity becomes a readable spatial pattern.
```

> **➤ Click `+` → Image block. Upload `v4_03_primary_case_regional_map.png`.**
> **➤ Caption:**

```
East/Southeast Asia regional map showing the strongest focused-case residual cuisine links over real geography — country fills, coastlines, rivers, and the South China Sea / Sea of Japan. Link color encodes spatial type: dark blue for mainland adjacency, teal for regional proximity, magenta for island/maritime. Line width is proportional to residual strength; the strongest residual values are labeled inline. The side panel ranks the top five focused-case residual links with their residual values.
```

> **➤ Alt text:**

```
Regional map of East and Southeast Asia rendered in PlateCarree projection from 93°E to 145°E and 4°N to 50°N, with beige land, light-blue ocean, faint country borders, rivers, and a lat/long graticule. Six cuisine anchors are marked as black dots: Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino. Colored great-circle links connect them: a thick dark-blue Thai–Vietnamese link labeled r=0.36 (mainland adjacency); teal Chinese–Korean labeled r=0.31 and Korean–Japanese labeled r=0.20 (regional proximity); magenta Filipino–Thai labeled r=0.22 and Filipino–Vietnamese labeled r=0.21 (island/maritime). A right-side panel titled "Reading the map" provides the link-type legend and a numbered top-5 residual link table.
```

> **➤ Click `+` → Quote block. PASTE:**

```
East/Southeast Asia is not the whole project. It is the focused case where the global residual method produces the most defensible spatial interpretation.
```

> **➤ Click `+` → Separator.**

---

# SECTION 10 — Terrain, coastlines, islands, maritime space

> **➤ Click `+` → Heading (H2). PASTE:**

```
Terrain, coastlines, islands, and maritime space make the corridor legible
```

> **➤ Click `+` → Text block. PASTE:**

```
The East/Southeast Asia focused case becomes more legible when residual links are placed over relief, coastlines, islands, and maritime space. This is the purpose of the Run 5 topographic corridor map.

The map adds no new causal model. It does not estimate least-cost paths, reconstruct trade routes, or prove terrain caused cuisine similarity. It provides spatial context for the residual links already identified by the cuisine-similarity and distance model.

That context matters because residual links occupy different kinds of geography. Thai–Vietnamese is a compact mainland link. Chinese–Korean is a regional East Asian link. Filipino-related links cross the South China Sea and archipelagic geography. A flat matrix makes these all look like rows and columns. A relief-and-coastline map makes their spatial differences visible.

The map also helps the StoryMap communicate visually. The viewer can see mainland Southeast Asia, the Korean peninsula, the Japanese archipelago, the Philippines, coastlines, and shallow seas in one frame. Corridor links become part of a landscape rather than abstract pairwise edges.

The strongest East/Southeast Asia residuals sit within legible regional, coastal, island, and maritime contexts. The relief map strengthens the spatial reading; it does not prove a mechanism.
```

> **➤ Click `+` → Image block. Upload `v4_04_topographic_corridor_map.png`. This is the largest figure — use full-width display if available.**
> **➤ Caption:**

```
The Run 5 relief map places the strongest East/Southeast Asia residual links over topographic, coastal, island, and maritime context. Line width reflects residual strength; line color indicates same-subregion, island/maritime, or cross-subregion link types. The map makes the corridor visually legible but does not claim that terrain or maritime routes caused the observed cuisine similarities.
```

> **➤ Alt text:**

```
Shaded relief and coastline map of East and Southeast Asia. Cuisine anchors for Chinese, Korean, Japanese, Thai, Vietnamese, and Filipino are connected by colored corridor lines. Annotations call out the Tibetan Plateau / Himalayan barrier, peninsula and island exchange context, the South China Sea maritime context, and mainland Southeast Asia adjacency context. A side panel lists top residual/access links with numerical scores.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The relief map provides spatial context, not causal proof.
```

> **➤ Click `+` → Separator.**

---

# SECTION 11 — Bridge scores: most top bridges are not Asian
**This is the strengthened section. Do not skip the second paragraph — it is the project's strongest regional-balance finding.**

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 5: residual bridge scores identify spatial bridge roles — and most top bridges are not Asian
```

> **➤ Click `+` → Text block. PASTE:**

```
Pairwise residuals are useful, but they can become a list of links. The bridge index asks a different question: which cuisine anchors repeatedly participate in positive residual relationships?

Instead of treating each pair separately, the bridge-index analysis aggregates residual links into place-level spatial roles. It combines positive residual degree, participation in top residual links, mean residual strength, long-distance residual score, and average residual behavior. The result is a map of bridge roles in the residual culinary network.

The result is regionally balanced — and is one of the project's strongest non-Asia findings. Of the top ten bridge-index cuisines, only one is Asian. The ranked list runs Filipino, Russian, Southern U.S., Jamaican, French, Spanish, British, Irish, Italian, Brazilian. That is a Caribbean–Atlantic–European–North-Atlantic pattern with one Pacific-archipelagic node. The Asia-rich texture of the focused case does not carry over into the bridge structure of the corpus, and that contrast is itself analytically important.

A bridge score is a spatial-network position, not a causal identity. It does not mean a cuisine historically caused or transmitted other cuisines. It means that, after distance is modeled, that cuisine anchor participates in multiple unexpectedly strong residual links.

This is also where the project most clearly requires GIS. Ingredient vectors alone can identify similar cuisines. They cannot tell us which mapped cuisines repeatedly exceed distance-based expectation, nor can they translate those residuals into place-level bridge roles. The bridge index depends on ingredient similarity, geographic distance, mapped anchors, residual modeling, and network aggregation working together.
```

> **➤ Click `+` → Image block. Upload `v4_05_bridge_index_map_and_chart.png`. Use full-width display.**
> **➤ Caption:**

```
Two-panel residual bridge index. Left: Robinson world map showing all corpus anchors with circle size proportional to residual bridge score and color encoding the regional balance — blue for the single Asian top-10 anchor (Filipino), warm orange for the nine non-Asian top-10 anchors, grey for other corpus anchors, white for anchors of less certain identity. Right: horizontal bar chart of the top ten bridge scores. The Filipino bar is annotated "← only Asian in top 10" to make the regional contrast unmissable. Together the panels show that ingredient resemblance alone cannot produce this insight — only mapped residuals after distance is modeled can identify place-level bridge roles, and in this corpus those roles are overwhelmingly non-Asian.
```

> **➤ Alt text:**

```
Side-by-side panels. Left panel is a Robinson-projection world map with beige land and light-blue ocean. A large blue circle marks Filipino in the western Pacific; large orange circles mark Russian in central Asia, Southern US in the U.S. southeast, Jamaican in the Caribbean, French, Spanish, British, Irish, and Italian in western and southern Europe, and Brazilian in central South America. Smaller grey dots mark other corpus anchors. Right panel is a horizontal bar chart titled "Top 10 bridge cuisines" showing residual bridge scores from 0.87 (Filipino, blue) to 0.31 (Brazilian), with all bars except Filipino in orange and an italic blue annotation "← only Asian in top 10" beside the Filipino bar.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Ingredient data identifies resemblance. GIS identifies residual bridge roles — and in this corpus, those roles are mostly non-Asian.
```

> **➤ Click `+` → Separator.**

---

# SECTION 12 — Cuisine-pair vignettes
**Tip:** if you want a more visual presentation, you can replace the four sub-headings below with a **Sidecar** block (left-side scrolling text, right-side rotating media). For a first build, plain headings + text are simpler and faster.

> **➤ Click `+` → Heading (H2). PASTE:**

```
Cuisine-pair vignettes
```

> **➤ Click `+` → Text block. PASTE:**

```
Maps and indices show structure; individual pairs make the pattern concrete. These vignettes are not historical explanations. They are examples of how the residual method creates different spatial readings.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Thai–Vietnamese: a mainland adjacency case
```

> **➤ Click `+` → Text block. PASTE:**

```
The cleanest mainland example. The relationship appears as a strong positive residual — observed ingredient similarity higher than distance alone predicts. Spatially, the pair is compact and regional, sitting within mainland Southeast Asia. The relief map makes this visible: the link appears within a coherent mainland setting rather than across scattered global space.

Safe claim: Thai–Vietnamese is a strong mainland adjacency example of residual cuisine similarity. Unsafe claim: the model proves a specific historical diffusion route.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Chinese–Korean: a regional proximity case
```

> **➤ Click `+` → Text block. PASTE:**

```
A second focused example. The pair sits inside an East Asian regional setting and remains strong after the distance baseline. A similarity matrix can say two cuisines resemble one another. A residual map says the resemblance is stronger than expected after distance is considered, and places that resemblance inside a regional geography.

Safe claim: a strong residual association inside a coherent East Asian setting. The mechanism is not claimed.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Filipino: an island and maritime bridge case
```

> **➤ Click `+` → Text block. PASTE:**

```
Filipino-related links complicate a simple land-distance story — they sit in archipelagic and maritime context rather than a compact mainland setting. The bridge index reinforces this: Filipino is the highest-scoring bridge cuisine in the corpus.

Safe claim: Filipino occupies a bridge role in the residual network and its links are more interpretable when mapped in island/maritime context. Unsafe claim: the model proves maritime exchange caused the similarities.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Iberian / Atlantic-Pacific: the mandatory non-Asia diagnostic
```

> **➤ Click `+` → Text block. PASTE:**

```
Longer-distance residual patterns appear among Iberian, Atlantic, and Pacific-linked cuisine labels — Spanish, Brazilian, Mexican, Filipino, Cajun/Creole, Jamaican, Southern U.S. The boundary/permeability check shows the Iberian/Atlantic interregional grouping has the highest mean residual of any spatial grouping in the prototype (around 0.14, n=11), exceeding the same-subregion baseline.

Distances are larger, cuisine labels broader, and the risk of recipe-platform bias higher. The value of this case is not proof — it is showing that the residual method surfaces long-distance corridor hypotheses worth future investigation.

Safe claim: hypothesis-generating. Unsafe claim: a proven Atlantic or colonial food pathway.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The vignettes turn residual pairs into spatial situations: mainland adjacency, regional proximity, island/maritime bridge context, and non-Asia diagnostic comparison.
```

> **➤ Click `+` → Separator.**

---

# SECTION 13 — Mandatory non-Asia diagnostic case and sensitivity

> **➤ Click `+` → Heading (H2). PASTE:**

```
Mandatory non-Asia diagnostic case and sensitivity
```

> **➤ Click `+` → Text block. PASTE:**

```
The StoryMap would be weaker if it only presented the East/Southeast Asia case. The global screen and the bridge-index figure both show that the residual method produces patterns beyond one region. The Iberian/Atlantic-Pacific diagnostic case makes that visible at the residual-pair level.

This case includes longer-distance and cross-region residual patterns within an Iberian/Atlantic-Pacific family of cuisine labels. These patterns are visually compelling and raise questions about long-distance culinary resemblance. They are also harder to interpret than the East/Southeast Asia focused case.

The reason is methodological. Long-distance residuals are more exposed to confounding from recipe-platform bias, broad cuisine labels, English-language recipe conventions, and shared generic ingredients. A recipe dataset may represent "Spanish," "Brazilian," or "Mexican" cuisine through a platform-specific lens, and may overrepresent pantry ingredients or popular recipe categories. The project therefore keeps this case diagnostic.

That does not make it unimportant. It shows that the residual method surfaces non-Asian hypotheses, that the global model is not a pretext for an Asian regional study, and that scope discipline matters: some residuals are strong enough to motivate focused interpretation, others are best used as future-research signals.

The boundary/permeability figure compares residual behavior across spatial groupings — same-subregion, same-region cross-subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other cross-region categories. The Iberian/Atlantic interregional grouping has the highest mean residual in the prototype, supporting the diagnostic case while showing why broader non-Asia generalizations require additional covariates.

The conclusion is balanced: the project is global in method, focused in inference, and diagnostic in its treatment of non-Asia long-distance cases.
```

> **➤ Click `+` → Image block. Upload `v4_06_secondary_residuals_by_grouping.png`.**
> **➤ Caption:**

```
Mean residual cuisine similarity by spatial grouping. The headline Iberian/Atlantic interregional grouping (saturated orange, +0.139, n=11) is the highest in the prototype and exceeds even the same-subregion baseline (lighter orange, +0.115, n=11). All other groupings — same-region cross-subregion (n=32), East/SE Asia cross-subregion (n=9), and other cross-region (n=127) — sit slightly below the distance-only expectation. The on-figure callout flags the headline as the project's mandatory non-Asia diagnostic case. The figure supports the idea that residual cuisine similarity has spatial structure beyond Asia, while showing why broader non-Asia cases should remain diagnostic rather than causal.
```

> **➤ Alt text:**

```
Horizontal bar chart titled "Where does residual cuisine similarity concentrate? Mean residual by spatial grouping." Five bars from top to bottom: Iberian/Atlantic interregional at +0.139 (n=11) in saturated orange, Same subregion at +0.115 (n=11) in lighter orange, Same region cross-subregion at -0.011 (n=32) in muted blue-grey, East/SE Asia cross-subregion at -0.014 (n=9) in muted blue-grey, Other cross-region at -0.020 (n=127) in muted blue-grey. A vertical zero line is labeled "distance-only expectation." A boxed callout to the right of the headline bar reads "Highest mean residual in the prototype. This is the project's mandatory non-Asia diagnostic case." A footer note states that positive values indicate similarity exceeding distance-only expectation and that the figure should be used as diagnostic evidence, not causal proof.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The non-Asia diagnostic case keeps the project global without overstating what the current evidence can prove.
```

> **➤ Click `+` → Separator.**

---

# SECTION 14 — Why Europe and Atlantic-linked material remain diagnostic, not primary

> **➤ Click `+` → Heading (H2). PASTE:**

```
Why Europe and Atlantic-linked material remain diagnostic, not primary
```

> **➤ Click `+` → Text block. PASTE:**

```
Europe and Atlantic-linked cuisines appear in the global screen, the bridge index, and the Iberian/Atlantic-Pacific diagnostic. They show the method surfaces long-distance residual patterns outside East/Southeast Asia. They are not treated as a second primary focused case.

This is a methodological choice, not an omission. A focused case needs more than interesting residuals. It needs a coherent regional geography, enough retained labels, stable interpretation after sensitivity checks, and a visual structure that helps the map carry the argument. East/Southeast Asia meets these requirements most clearly in the current prototype.

Europe/Atlantic-linked material is more exposed to interpretive risks. Some cuisine labels are broad. Some long-distance similarities may reflect platform-specific recipe vocabulary or shared generic ingredients. Without additional covariates for migration, trade, colonial history, language, or ingredient flows, the prototype should not elevate those links to the same inferential level as the primary case.

This does not mean the Europe/Atlantic material is weak. The bridge-index result — where most top bridges are European, North-Atlantic, or Caribbean — is a substantive finding that deserves its own future study with covariates. In the current submission, it functions as a diagnostic comparison and a boundary on the project's claims.

The hierarchy stays honest: East/Southeast Asia is the strongest focused inference case; Iberian/Atlantic-Pacific is the required non-Asia diagnostic; Europe-linked residuals are promising but not fully analyzed as a focused regional model.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Europe/Atlantic-linked residuals are included as diagnostic signals, not as a fully modeled second primary case.
```

> **➤ Click `+` → Separator.**

---

# SECTION 15 — What this proves, and what it does not prove

> **➤ Click `+` → Heading (H2). PASTE:**

```
What this proves, and what it does not prove
```

> **➤ Click `+` → Text block. PASTE:**

```
The project makes a spatial argument, not a causal historical argument.

Strong claims. Cuisine similarity is spatially structured. The distance model shows similarity is related to geographic distance but not fully explained by it (R² ≈ 0.36). Positive residuals identify candidate culinary corridors. East/Southeast Asia is the strongest focused case. The bridge index produces a spatial insight ingredient clustering alone cannot produce; nine of its top ten cuisines are non-Asian. The Run 5 relief map makes the focused corridor more visually legible.

Cautious claims. Selected residual patterns are consistent with regional adjacency, corridor plausibility, island/maritime context, or possible exchange histories. Iberian/Atlantic-Pacific residuals are useful diagnostic signals for future non-Asia work.

Forbidden claims. That migration, trade, colonialism, empire, maritime routes, or terrain caused the observed similarities. That the recipe corpus represents all world cuisines. That cuisine labels are exact nation-states. That the relief map is a least-cost or causal terrain model. That Europe has been fully analyzed as a focused regional case.

These limits are not weaknesses — they are what make the project defensible. The contribution is methodological and cartographic: GIS transforms a recipe corpus into a map of spatial expectations, residuals, focused cases, diagnostic comparisons, and bridge roles.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Strong claim: spatial structure. Cautious claim: corridor hypotheses. Forbidden claim: causal proof.
```

> **➤ Click `+` → Separator.**

---

# SECTION 16 — Sources, methods, and reproducibility

> **➤ Click `+` → Heading (H2). PASTE:**

```
Sources, methods, and reproducibility
```

> **➤ Click `+` → Text block. PASTE:**

```
The project uses a cuisine-labeled recipe corpus as the food-data foundation. Recipes become cuisine-by-ingredient profiles through ingredient normalization and generic-ingredient filtering. The analysis calculates cuisine similarity, maps cuisine labels to approximate geographic anchors, computes pairwise distance, models similarity against distance, and maps residuals.

The final maps draw on the project's processed cuisine-similarity outputs, distance/residual model outputs, focused East/Southeast Asia results, residual bridge-index outputs, secondary/diagnostic sensitivity summaries, and Run 5 topographic visualization. The Run 5 relief map uses documented topographic and coastal context as a visual layer, not a causal model.

The workflow was developed in Python for data processing and figure generation, with ArcGIS StoryMaps as the final presentation format. The accompanying PDF report contains the full methodology, figures, limitations, and source notes.

Limitations central to interpretation: the recipe corpus is not globally representative; cuisine labels are broad and cannot be treated as precise countries; ingredient normalization requires judgment; generic pantry ingredients can inflate similarity; cuisine-to-place mapping is approximate; residuals identify spatially unexpected resemblance, not causality; topographic context improves visual interpretation but does not prove terrain or maritime pathways caused the patterns.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The PDF report is the technical companion; the StoryMap is the map-led submission narrative.
```

> **➤ Click `+` → Separator.**

---

# SECTION 17 — Conclusion: what GIS changes

> **➤ Click `+` → Heading (H2). PASTE:**

```
Conclusion: what GIS changes
```

> **➤ Click `+` → Text block. PASTE:**

```
Culinary Corridors began with a simple question: which cuisines are similar? GIS changes that question.

The project does not stop at ingredient resemblance. It asks whether resemblance follows geographic distance, where it exceeds distance-based expectation, which residuals become readable as focused corridors, and which cuisine anchors become bridge nodes in a mapped residual network.

The global discovery screen shows candidate residual corridors across the prototype, scoped by what the corpus actually contains. The East/Southeast Asia case shows where those residuals become most spatially interpretable. The Run 5 relief map makes that focused corridor visually legible through terrain, coastlines, islands, and maritime space. The residual bridge index turns pairwise links into mapped roles — and those roles are mostly non-Asian, anchoring the project's regional balance. The Iberian/Atlantic-Pacific diagnostic case keeps the project global without claiming what the current evidence cannot support.

The contribution is a method for making food similarity geographically explicit. Cuisine similarity is not only a cultural pattern. It is also a geographic pattern — and GIS reveals where that pattern follows distance, where it breaks distance, and where it forms corridors and bridge roles invisible from recipes alone.
```

> **➤ Click `+` → Quote block. PASTE:**

```
GIS changes the question from "which cuisines are similar?" to "where does similarity exceed geographic expectation?"
```

> **➤ Click `+` → Separator.**

---

# SECTION 18 — Technical report and backup materials

> **➤ Click `+` → Heading (H2). PASTE:**

```
Technical report and backup materials
```

> **➤ Click `+` → Text block. PASTE:**

```
This StoryMap is the primary Fisher-facing narrative. A complete PDF report serves as the technical companion, containing the full investigation history, data pipeline, figure sequence, methodology, limitations, and submission notes.

Use the PDF if the form requires a file upload, if a reviewer asks for technical detail, or if the StoryMap link cannot be accessed. If the form allows both, submit the StoryMap link first and include the PDF as a supporting document.
```

> **➤ (Optional) Click `+` → Button block. Set the button text to "Download technical report (PDF)" and link it to your hosted PDF URL once available.**

> **➤ Click `+` → Quote block. PASTE:**

```
Recommended submission route: StoryMap link first, PDF backup second.
```

---

# Final pre-submission QA (do this BEFORE you publish)

Open your draft and walk through these checks. The order matters.

**1. Regional balance test.** Read only the headings, image captions, and quote callouts in order. By the end, you should have heard "global", "global", "global", "focused case (East/Southeast Asia)", "focused case", "non-Asian bridge majority", "non-Asia diagnostic", "Europe diagnostic, not primary." If the headings and captions alone leave the impression of an Asia-only project, something is wrong.

**2. Hero figure framing test.** Re-read Section 6 caption. It must clearly say the map's coverage reflects the corpus, not world food geography. If a reviewer could mistake the empty regions for findings, rewrite.

**3. Section 11 strengthening test.** The second paragraph of Section 11 must explicitly list the top-ten bridge cuisines and state that nine of ten are non-Asian. If that paragraph was trimmed during pasting, restore it — this is the project's strongest non-Asia evidence.

**4. Claim hierarchy test.** Search the document (Cmd/Ctrl-F) for the words "caused", "proved", "proves", "route", "pathway", "trade", "migration", "colonial". Every appearance must either be inside a "what this does NOT prove" framing, or inside Section 14 explaining why those claims are deferred. No accidental causal language.

**5. Image display test.** View the draft on desktop. Each figure should display at full readable width. Then click "Preview" and switch to mobile preview (or open the preview link on your phone). Captions should remain readable; figures should not be clipped.

**6. Figure alt text test.** For each of the six images, click the image, click the gear/edit icon, and confirm an alt-text value is set (the alt text I provided in this file). Empty alt text fails accessibility.

**7. Link test.** If you've added a PDF download button (Section 18), click it from the preview to confirm it opens the right file in a new tab.

**8. Incognito / logged-out test.** Once you publish, open the public StoryMap link in a private/incognito browser window. If it requires sign-in, your sharing settings are wrong. The Fisher reviewer must be able to open it without a Harvard account. Set sharing to "Everyone (public)" in the share menu.

**9. Submission form test.** Confirm the Fisher submission form accepts a StoryMap URL. If it requires a PDF upload, attach the PDF report and put the StoryMap URL in the description or cover-letter field.

**10. Save proof of submission.** Take a screenshot of the submitted form and save the email confirmation.

---

# Quick reference: section-to-figure-to-callout map

| § | Section | Figure | One-line role |
|---|---|---|---|
| 1 | Cover | none (text-only) | Thesis |
| 2 | Opening | none | Why mapping changes the question |
| 3 | Research question | none | Five subquestions |
| 4 | Why food = spatial | none | Scope and label discipline |
| 5 | How the atlas works | none | The four-stage method |
| 6 | Global discovery | **Hero** (`v4_01_hero_world_corridors`) | Discovery screen, honest about coverage |
| 7 | Finding 1: distance | `v4_02_method_residual_baseline` | The R² ≈ 0.36 baseline |
| 8 | Finding 2: residuals | none | Corridor concept, not historical route |
| 9 | Asia focused case | `v4_03_primary_case_regional_map` | Strongest inference, methodologically selected |
| 10 | Topographic corridor | `v4_04_topographic_corridor_map` | Relief context |
| 11 | Bridge scores | `v4_05_bridge_index_map_and_chart` | **9 of top 10 bridges are non-Asian** |
| 12 | Vignettes | none | Four pair-level readings, balanced |
| 13 | Non-Asia diagnostic | `v4_06_secondary_residuals_by_grouping` | Iberian/Atlantic mean residual ≈ 0.14 |
| 14 | Why not Europe primary | none | Methodological discipline |
| 15 | What this proves | none | Strong / cautious / forbidden |
| 16 | Sources & methods | none | Pipeline + limitations |
| 17 | Conclusion | none | What GIS changes |
| 18 | PDF backup | none (optional Button) | Submission route |

---

*End of build instructions. If the build looks right after the QA checklist, publish and submit.*

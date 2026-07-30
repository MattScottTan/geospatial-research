# Bridges Across Cuisines — StoryMap v6 Build Instructions
**Single-file build guide. Open this file, work top to bottom, paste as you go.**

Matthew Tan — Fisher Prize submission
Version: v6 (full rewrite in the EIP-submission voice)

---

## What changed from v5

This is a **complete script rewrite**. v5 fixed the figures and tightened the v3 script. v6 throws out the v3 script entirely and replaces it with a new one written in the same voice and structure as your EIP-winning *Cloudy with a Chance of Compute* submission, with two major framing shifts:

1. **The project is no longer described as an "atlas."** The word "atlas" is gone from the script. The framing is now an **investigation** of a single sharp question, pursued through numbered findings, ending in four cuisine cases. This avoids reading as repetitive next to the EIP submission.
2. **The bridge-cuisine asymmetry is the lead insight, not a buried sub-finding.** The 9-of-10 non-Asian bridge result and the Iberian/Atlantic interregional residual exceeding the same-subregion baseline are now Findings 2 and 3 — the analytical core. The East/Southeast Asia case is the focused-corridor demonstration (Finding 4), not the headline.

Everything else changed in service of those two shifts: the title, the opening, the methodology framing, the case-study selection (Filipino, Russian, Thai, Spanish), and the conclusion. The defensive "What this proves and what it does not prove" section is gone. Light caveats remain only where natural in prose.

The six figures from v5 are reused unchanged. Only their captions, alt text, and section assignments are rewritten.

---

## Pre-flight: figures ready

Have all six PNG files on your desktop, named exactly:

| § | Filename | Goes in |
|---|---|---|
| 1 | `v4_01_hero_world_corridors.png` | Section 2 (Introduction) |
| 2 | `v4_02_method_residual_baseline.png` | Section 4 (Finding 1) |
| 3 | `v4_06_secondary_residuals_by_grouping.png` | Section 5 (Finding 2) |
| 4 | `v4_05_bridge_index_map_and_chart.png` | Section 6 (Finding 3) |
| 5 | `v4_03_primary_case_regional_map.png` | Section 7 (Finding 4) |
| 6 | `v4_04_topographic_corridor_map.png` | Section 7 (Finding 4, second figure) |

### Account
Sign in to **storymaps.arcgis.com** with your Harvard ArcGIS Online account. Click **+ New story → Start from scratch**.

### Format conventions in this file

> **➤ ArcGIS action:** what to click in the editor
> **➤ PASTE:** the text to paste, in a code block

Use the floating **`+`** button between blocks to insert: Heading, Text, Image, Quote, Separator. Image alt text lives behind the gear/edit icon on the image block.

---

# COVER (Section 1)

> **➤ ArcGIS action:** Click the cover area. In the right-hand design panel choose the **"Minimal"** cover layout (no background image). If "Minimal" isn't available, pick the no-media option.
> **➤ Title field:**

```
Bridges Across Cuisines
```

> **➤ Subtitle field:**

```
Mapping the residual geography of global ingredient similarity
```

> **➤ Byline field:**

```
Matthew Scott Tan — Fisher Prize submission
```

> **➤ Date field (if present):** today's date in your preferred format.

---

# SECTION 2 — Introduction

> **➤ Click `+` → Text block (no heading needed at the top of this section — the cover already serves that role; we open with author bio + intro). PASTE:**

```
Matthew is a graduating senior at Harvard College concentrating in Mathematics and Statistics, with interests in artificial intelligence, machine learning, random matrix theory, and high-dimensional statistics. Those interests are what drew him to this project: a question about whether ingredient resemblance — when measured systematically across the world's documented cuisines and projected against geographic distance — produces a structure that the cultural framing of cuisine usually obscures. The answer, it turns out, is yes. The structure has a shape, and the shape is informative.
```

> **➤ Click `+` → Heading (H2). PASTE:**

```
Introduction
```

> **➤ Click `+` → Text block. PASTE:**

```
Thai and Vietnamese cuisines, separated by roughly 700 km of mainland Southeast Asia, share an ingredient profile resemblance well above the global mean. British and Russian cuisines, separated by 2,500 km and divided by language, climate, and political history, share a resemblance higher than most pairs of European neighbors. Filipino and Spanish cuisines, separated by more than 13,000 km across the Pacific and the Atlantic, share a resemblance comparable to that of regional neighbors elsewhere on the map.

These three pairs are not curiosities. They are systematic. Across the world's documented cuisines, a striking fraction of the variation in ingredient resemblance cannot be explained by geographic distance. Some pairs are far apart yet remarkably similar. Some pairs sit inside the same region yet diverge sharply. The geography that organizes cuisine is not the geography of straight-line kilometers.

Most analyses of food treat cuisine as a cultural object: tastes, traditions, identities. Most spatial analyses, when they reach into food at all, treat distance as the primary explanatory variable for resemblance. This project sits at the intersection. It measures pairwise ingredient similarity systematically, models how similarity declines with geographic distance, and then asks where that decline does not hold. The leftover — residual cuisine similarity — turns out to be where the geography of food becomes interesting.

The central question is:
```

> **➤ Click `+` → Quote block. PASTE:**

```
Once geographic distance is accounted for, where does cuisine resemblance still exceed what proximity predicts — and what does that residual structure reveal about how cuisines actually connect?
```

> **➤ Click `+` → Text block. PASTE:**

```
The map below is the project's starting point. Cuisine pairs whose ingredient similarity exceeds distance-based expectation are drawn as great-circle links between approximate cuisine anchors on a Robinson-projection world map. Some links connect adjacent regional neighbors — the kinds of resemblance distance does explain. Others span continents and oceans, connecting cuisines that proximity alone would never predict to share. The latter are where this project's analytical interest lies.
```

> **➤ Click `+` → Image block. Upload `v4_01_hero_world_corridors.png`. Display at full width.**
> **➤ Caption:**

```
Candidate residual cuisine corridors across the project corpus. Blue great-circle links mark the East/Southeast Asia focused case (line width proportional to residual strength); orange links mark long-distance residual outliers — pairs sitting well above the distance-similarity regression line. The map's geographic coverage reflects the cuisine-labeled recipe corpus, not world food geography. Residual links are candidate spatial associations, not proven exchange routes.
```

> **➤ Alt text:**

```
Robinson-projection world map with beige land and light-blue ocean basemap, country borders, and a subtle 30-degree graticule. Blue great-circle lines connect East and Southeast Asian cuisine anchors at varying widths. Orange great-circle lines connect long-distance pairs including British–Russian, Irish–Russian, French–Russian, Italian–Russian, and British–Southern US. Cuisine anchors in Europe, North America, the Caribbean, and South America are marked and labeled. A boxed corpus-coverage note in the lower right names the regions absent from the corpus.
```

> **➤ Click `+` → Text block. PASTE:**

```
The sections that follow describe how the analysis was built, what the residual structure looks like once distance is removed, and why a small set of cuisines — most of them not Asian — anchor a global network of long-distance ingredient resemblance.
```

> **➤ Click `+` → Separator.**

---

# SECTION 3 — How the analysis works

> **➤ Click `+` → Heading (H2). PASTE:**

```
How the analysis works
```

> **➤ Click `+` → Text block. PASTE:**

```
The analysis proceeds in three stages, each producing a layer that the next builds on.

Stage 1: Build comparable cuisine profiles. Cuisine-labeled recipes from a large recipe corpus are normalized so closely related ingredient names map to a single canonical ingredient — "scallion" and "green onion" become one entry. Ingredients are then aggregated into a cuisine-by-ingredient matrix in which each cuisine is represented as a frequency vector across thousands of normalized ingredients. This is the project's textual, chemical, and culinary signature for each cuisine.

Stage 2: Measure ingredient similarity and geographic distance. Pairwise cuisine similarity is computed using cosine similarity on the ingredient frequency vectors, with generic-ingredient filtering and robustness checks. Each cuisine label is assigned an approximate geographic anchor — a centroid representing the cuisine's home territory. Pairwise geodesic distances between anchors are computed using GeoPy's great-circle method.

Stage 3: Extract the residual. Cuisine similarity is regressed on log geographic distance. The fitted line gives, for each pair, a predicted similarity based on distance alone. The residual — observed similarity minus distance-predicted similarity — becomes the analytical object. Positive residuals identify pairs more similar than distance predicts. Mapped, they form a candidate network of long-distance culinary connection.

The four findings that follow draw on this residual layer in different ways: a distributional view, a spatial-grouping view, a network-position view, and a focused regional case.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Residuals are the hinge of the project. They turn ingredient resemblance into a spatial question.
```

> **➤ Click `+` → Separator.**

---

# SECTION 4 — Finding 1

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 1: Distance shapes cuisine similarity, but explains less than half of it.
```

> **➤ Click `+` → Text block. PASTE:**

```
Ingredient similarity declines with geographic distance, but the decline is shallow. The fitted relationship across all pairwise cuisine comparisons returns a slope of −0.116 per unit of log distance and an R² of 0.355. In concrete terms: doubling the distance between two cuisines reduces their predicted ingredient similarity by approximately 0.080 cosine-similarity units — meaningful, but small relative to the range of observed similarities, which spans roughly 0.05 to 0.92. Roughly 64 percent of the variation in cuisine similarity is structured but not explained by distance.

The shallowness matters analytically. If distance explained 90 percent of cuisine resemblance, a residual analysis would reveal little: the line would absorb most of the signal and leave only noise behind. At R² = 0.36, the residuals carry the majority of the spatial information. The largest positive residuals — pairs where similarity exceeds distance-based expectation by 0.2 cosine units or more — include several long-distance combinations the distance baseline would never anticipate: British–Southern U.S., British–Russian, Irish–Russian, French–Russian, Italian–Russian. These pairs sit between 2,500 and 8,000 km apart yet retain ingredient similarities that match or exceed those of regional neighbors.

The figure below shows the underlying pattern. Each point is one cuisine pair; the regression line is the distance baseline; named labels mark the strongest positive residuals discussed above.
```

> **➤ Click `+` → Image block. Upload `v4_02_method_residual_baseline.png`.**
> **➤ Caption:**

```
Distance baseline for cuisine similarity. Each point is a pairwise cuisine comparison: cosine similarity of filtered ingredient profiles plotted against log geographic distance between cuisine anchors. The fitted line — similarity = 1.273 − 0.116 × log(distance), R² = 0.355 — defines the distance-only expectation. Pairs above the line are positive residuals; the labeled points (Thai–Vietnamese, British–Russian, Irish–Russian, French–Russian, Italian–Russian, British–Southern U.S.) are the strongest positive residuals in the corpus.
```

> **➤ Alt text:**

```
Scatter plot of cosine similarity of filtered cuisine ingredient profiles versus log geographic distance between cuisine anchors. A regression line of similarity = 1.273 − 0.116 × log(distance) is shown with R² = 0.355. Points above the line, including Thai–Vietnamese at the short-distance end and British–Russian, Irish–Russian, French–Russian, Italian–Russian, and British–Southern U.S. at the long-distance end, are highlighted as positive residuals.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Two-thirds of cuisine similarity sits outside what distance alone can explain. That two-thirds is where the analysis goes next.
```

> **➤ Click `+` → Separator.**

---

# SECTION 5 — Finding 2

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 2: Residual cuisine similarity is structured by spatial grouping — and the ranking inverts the obvious intuition.
```

> **➤ Click `+` → Text block. PASTE:**

```
Finding 1 establishes that residuals exist and are sometimes very large. Finding 2 asks whether those residuals concentrate in any particular configuration of cuisine pairs.

To test this, pairs are partitioned into five spatial groupings based on the regional relationship between the two cuisine anchors: same-subregion (the tightest geographic neighbors), same-region cross-subregion (still within the same broad continental region but a different subregion), East/Southeast Asia cross-subregion (the focused regional case examined in Finding 4), Iberian/Atlantic interregional (the long-distance Iberian–Atlantic–Pacific cluster of cuisines), and other cross-region (everything else). Mean residual cuisine similarity is then computed within each grouping.

A distance-only intuition would predict a monotonic decline: same-subregion pairs at the top, intermediate groupings in the middle, distant cross-region pairs at the bottom. The data refuse to follow that order.
```

> **➤ Click `+` → Image block. Upload `v4_06_secondary_residuals_by_grouping.png`.**
> **➤ Caption:**

```
Mean residual cuisine similarity by spatial grouping. The Iberian/Atlantic interregional grouping sits at the top of the ranking (+0.139, n = 11), exceeding the same-subregion baseline (+0.115, n = 11). All other groupings sit slightly below the distance-only expectation. The headline annotation flags the project's clearest non-regional finding: long-distance Iberian–Atlantic–Pacific pairs are, on average, more similar than distance alone predicts by a wider margin than even the closest geographic neighbors.
```

> **➤ Alt text:**

```
Horizontal bar chart titled "Where does residual cuisine similarity concentrate? Mean residual by spatial grouping." Five bars from top to bottom: Iberian/Atlantic interregional at +0.139 (n=11) in saturated orange, Same subregion at +0.115 (n=11) in lighter orange, Same region cross-subregion at -0.011 (n=32), East/SE Asia cross-subregion at -0.014 (n=9), Other cross-region at -0.020 (n=127). A vertical zero line is labeled "distance-only expectation." A boxed callout to the right reads "Highest mean residual in the prototype. This is the project's mandatory non-Asia diagnostic case."
```

> **➤ Click `+` → Text block. PASTE:**

```
The Iberian/Atlantic interregional grouping has the highest mean residual in the corpus at +0.139 (n = 11). The same-subregion grouping comes second at +0.115 (n = 11). Same-region cross-subregion (n = 32), the East/Southeast Asia cross-subregion (n = 9), and other cross-region pairs (n = 127) sit slightly below the distance-only baseline at -0.011, -0.014, and -0.020 respectively. The full top-to-bottom ranking is, therefore, not the geography of adjacency. It is the geography of a specific long-distance configuration that connects Iberian, Atlantic-rim, and Pacific-archipelagic cuisine anchors.

The cuisines participating in the Iberian/Atlantic interregional grouping include Spanish, Filipino, Mexican, Cajun/Creole, Brazilian, Jamaican, and Southern U.S. The pairs involving these labels span three continents and two oceans — and yet, on average, exceed the distance-only baseline by a wider margin than the typical same-subregion pair. The magnitude of that difference is concrete: the Iberian/Atlantic mean exceeds the "other cross-region" mean by 0.159 cosine units, which is approximately twice the similarity loss that a doubling of geographic distance would predict from the Finding 1 baseline.

This is the project's first analytically distinctive finding. It is not that distance fails to predict similarity in general — it does, weakly. It is that the specific long-distance pairs connecting Iberian, Atlantic, and Pacific cuisines are systematically more similar than distance permits. Something else is structuring this configuration.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The strongest residuals in the corpus are not concentrated among regional neighbors. They are concentrated in a specific Iberian–Atlantic–Pacific configuration that distance alone would not predict.
```

> **➤ Click `+` → Separator.**

---

# SECTION 6 — Finding 3

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 3: A small set of bridge cuisines anchors the residual network — and the bridge geography is overwhelmingly non-Asian.
```

> **➤ Click `+` → Text block. PASTE:**

```
Findings 1 and 2 work at the pair level. Finding 3 aggregates from pairs to cuisines.

For each cuisine, a residual bridge score is computed by combining five components extracted from the residual matrix: positive residual degree (how many other cuisines the focal cuisine connects to with a positive residual), participation in the corpus's top-strength residual links, mean residual magnitude across the cuisine's pairs, long-distance residual score (whether the cuisine's residual partners are geographically distant or near), and overall residual behavior. Each component is normalized to a 0–1 scale and the five are combined with equal weights. The result is a single per-cuisine score capturing how actively each cuisine functions as a connector in the residual network.

The top ten bridge cuisines, ranked by score:

1. Filipino — 0.87
2. Russian — 0.84
3. Southern U.S. — 0.69
4. Jamaican — 0.68
5. French — 0.65
6. Spanish — 0.53
7. British — 0.51
8. Irish — 0.44
9. Italian — 0.32
10. Brazilian — 0.31

Of the top ten, only one — Filipino — is Asian. The remaining nine span the Atlantic basin (British and Irish Isles, French and Iberian peninsulas, Italian peninsula, Caribbean, Southern U.S., Brazilian Atlantic coast) and the Eurasian continent (Russian). Eight of the nine non-Asian bridges sit on the rim of the Atlantic basin or its connected geographies. The ninth, Russian, anchors a continental Eurasian span whose residual partners are themselves European cuisines on the western edge of that span.
```

> **➤ Click `+` → Image block. Upload `v4_05_bridge_index_map_and_chart.png`. Use full-width display.**
> **➤ Caption:**

```
Two-panel residual bridge index. Left: Robinson world map of cuisine anchors with circle size proportional to bridge score and color encoding regional balance — blue for the single Asian top-10 anchor (Filipino), warm orange for the nine non-Asian top-10 anchors. Right: ranked bar chart of the top ten bridge scores, with the Filipino bar annotated to flag that it is the only Asian entry. The figure makes the Atlantic-rim concentration of the bridge network visually unmistakable.
```

> **➤ Alt text:**

```
Side-by-side panels. Left panel is a Robinson-projection world map with beige land and light-blue ocean. A large blue circle marks Filipino in the western Pacific; large orange circles mark Russian in central Asia, Southern US in the U.S. southeast, Jamaican in the Caribbean, French, Spanish, British, Irish, and Italian in western and southern Europe, and Brazilian in central South America. Right panel is a horizontal bar chart titled "Top 10 bridge cuisines" showing residual bridge scores from 0.87 (Filipino, blue) to 0.31 (Brazilian), with all bars except Filipino in orange and an annotation reading "← only Asian in top 10" beside the Filipino bar.
```

> **➤ Click `+` → Text block. PASTE:**

```
The bridge network is also concentrated. The top three cuisines — Filipino, Russian, and Southern U.S. — account for 41 percent of the total bridge weight in the top 10. The top five — adding Jamaican and French — account for 64 percent. The residual network is not flat. It is anchored by a small, geographically specific set of cuisines that connect the rest into a coherent long-distance structure.

It is worth being precise about what a bridge score does and does not say. It is a network position. It says that, after the distance baseline is removed, the focal cuisine participates in many strong residual links with cuisines that are not its geographic neighbors. It does not assert that the focal cuisine caused those resemblances. It reports a structural fact about the corpus.

The structural fact is striking. Cuisine resemblance, viewed through residuals, organizes itself around an Atlantic-centered network with one major Pacific-archipelagic node. The regions whose residual links are most often discussed in food-culture writing — East and Southeast Asia, the Mediterranean, South Asia — do not dominate this layer of the analysis. Almost all of the top connectors are on the Atlantic rim.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Nine of the ten cuisines that most strongly bridge ingredient similarity, after distance is controlled for, are non-Asian. That asymmetry is the project's most distinctive finding.
```

> **➤ Click `+` → Separator.**

---

# SECTION 7 — Finding 4

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 4: The strongest focused residual corridor sits in East and Southeast Asia — and combines mainland, peninsular, and archipelagic structure.
```

> **➤ Click `+` → Text block. PASTE:**

```
Finding 3 identifies which cuisines connect the residual network most actively. Finding 4 asks where the residual links concentrate spatially when narrowed to a single focused regional case. Among focused cases, East and Southeast Asia produce the strongest, cleanest residual corridor in the corpus.

The strongest single residual link in the entire dataset is Thai–Vietnamese at +0.359 — a mainland adjacency case where ingredient similarity exceeds distance-based expectation by the largest margin observed in the corpus. Chinese–Korean follows at +0.306, a regional proximity case across the Yellow Sea. Filipino–Thai (+0.219) and Filipino–Vietnamese (+0.209) span the South China Sea and represent island-maritime links that distance alone would predict to be far weaker. Korean–Japanese (+0.20) closes the top five.
```

> **➤ Click `+` → Image block. Upload `v4_03_primary_case_regional_map.png`.**
> **➤ Caption:**

```
The East/Southeast Asia focused-case map shows the strongest regional residual cuisine links over real geography — country fills, coastlines, rivers, and the South China Sea / Sea of Japan. Link color encodes spatial type: dark blue for mainland adjacency, teal for regional proximity, magenta for island/maritime. Line width is proportional to residual strength; the strongest residual values are labeled inline. A side panel ranks the top five focused-case residual links.
```

> **➤ Alt text:**

```
Regional map of East and Southeast Asia rendered in PlateCarree projection from 93°E to 145°E and 4°N to 50°N, with beige land, light-blue ocean, faint country borders, rivers, and a lat/long graticule. Six cuisine anchors are marked: Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino. Colored great-circle links connect them: dark-blue Thai–Vietnamese labeled r=0.36 (mainland adjacency); teal Chinese–Korean labeled r=0.31 and Korean–Japanese labeled r=0.20 (regional proximity); magenta Filipino–Thai labeled r=0.22 and Filipino–Vietnamese labeled r=0.21 (island/maritime). A right-side panel ranks the top 5 residual links with their residual values.
```

> **➤ Click `+` → Text block. PASTE:**

```
Three structural features make the East/Southeast Asia case analytically clean. First, the top residuals span three distinct link types: mainland adjacency (Thai–Vietnamese), regional proximity (Chinese–Korean, Korean–Japanese), and island-maritime (Filipino–Thai, Filipino–Vietnamese). The corridor is not a chain of neighbors — it is a small network with multiple geometric configurations represented. Second, residual strength is high: all five top links sit above +0.20, well above the corpus-wide same-subregion mean of +0.115. Third, the underlying geography is interpretable: mainland Indochina, the East China Sea, the Korean peninsula, the Japanese archipelago, and the Philippine archipelago appear on the same map and the residuals can be read against their physical structure.

Adding topographic and maritime context makes the corridor's structure more legible without changing any of the residual values. The map below shows the same focused case overlaid on shaded relief and coastlines.
```

> **➤ Click `+` → Image block. Upload `v4_04_topographic_corridor_map.png`. Use full-width display.**
> **➤ Caption:**

```
The Run 5 relief map places the strongest East/Southeast Asia residual links over topographic, coastal, island, and maritime context. Line width reflects residual strength; line color indicates same-subregion, island/maritime, or cross-subregion link types. The map clarifies the spatial reading of the corridor — peninsulas, archipelagos, shallow seas, and mountain barriers — without claiming that any of these features causally produced the observed resemblance.
```

> **➤ Alt text:**

```
Shaded relief and coastline map of East and Southeast Asia. Cuisine anchors for Chinese, Korean, Japanese, Thai, Vietnamese, and Filipino are connected by colored corridor lines. Annotations call out the Tibetan Plateau and Himalayan barrier to the west, peninsula and island exchange context for Korea and Japan, the South China Sea maritime context for Filipino-Vietnamese-Thai links, and mainland Southeast Asia adjacency context for Thai-Vietnamese. A side panel lists top residual links with numerical scores.
```

> **➤ Click `+` → Text block. PASTE:**

```
Three features become more visible on the relief map. The Tibetan Plateau and Himalayan barrier mark the western edge of the corridor — the regions immediately west of the East/SE Asia residual network are separated from it by some of the highest terrain on Earth, which corresponds with the absence of strong residual links across that boundary. The Korean peninsula, Japanese archipelago, and Philippine archipelago form a coastal-and-island ring that the East Asian residuals trace closely; the Filipino node, in particular, makes more sense as an archipelagic bridge than as a point on a continental map. The South China Sea and Sea of Japan act as connectors rather than separators — maritime space across which residual similarity is actively maintained.

This is consistent with what Finding 3 implies more globally. Bridge cuisines tend to sit at the intersection of land and water — at archipelagic nodes (Filipino), at peninsular extensions (Iberian), at island-and-coast complexes (British, Irish, Italian), or at long continental spans with coastal access at multiple ends (Russian). The strongest residual network in the corpus does not respect simple straight-line distance. It rides the physical structure of coastlines, peninsulas, and shallow seas.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The corridor is not a chain. It is a small network where mainland, peninsula, and archipelago each contribute a distinct kind of residual link.
```

> **➤ Click `+` → Separator.**

---

# SECTION 8 — Four cuisines that explain the pattern

> **➤ Click `+` → Heading (H2). PASTE:**

```
Four cuisines that explain the pattern
```

> **➤ Click `+` → Text block. PASTE:**

```
The four findings above describe the residual geography in aggregate. The four cuisines that follow illustrate how that geography concentrates around individual cuisine anchors. Each represents one structural role in the network: an archetypal bridge, a long-distance continental bridge, a regional hub at the heart of the strongest corridor, and a long-distance Iberian–Atlantic–Pacific node.

Together, they describe the shape of the residual network from four different vantage points.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Filipino: archetypal residual bridge
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.87 (rank 1 of 10). Location: Philippine archipelago. Top residual links: Thai (+0.219), Vietnamese (+0.209), Korean (+0.12), Chinese (+0.11), plus participation in the long-distance Iberian–Atlantic–Pacific group anchored at the Spanish end.

Filipino is the only Asian cuisine in the top ten bridges and is the highest-scoring bridge in the entire corpus by a clear margin — its bridge score of 0.87 alone accounts for 15 percent of the total weight held by the top ten. The cuisine sits in the Philippine archipelago, geographically positioned between mainland Southeast Asia, East Asia, the Pacific Ocean, and — through historical exchange — the Spanish-speaking world.

The residual structure of Filipino cuisine reads as a maritime bridge. Its links to Thai and Vietnamese are island-to-mainland connections across the South China Sea. Its links to Chinese and Korean are island-to-mainland connections across the East and Yellow Seas. Its participation in the Iberian/Atlantic interregional grouping (Finding 2) extends the network across the Pacific. No other cuisine in the corpus participates in residual links across this many distinct geographic configurations, and none combines Asian and trans-Pacific roles so visibly.

The Filipino node is what makes the East/Southeast Asia case (Finding 4) and the Atlantic–Pacific finding (Finding 2) connect. It is the cuisine where the corridor structure meets the bridge structure.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Russian: long-distance Eurasian bridge
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.84 (rank 2). Location: continental Eurasia. Top residual partners: British, Irish, French, Italian, Spanish, Southern U.S. — every one of them named in the long-distance positive-residual cluster of the distance-similarity scatter (Figure in Finding 1).

Russian is the highest-scoring non-Asian bridge and the project's clearest long-distance case. Its top residual partners are all European or Atlantic-linked cuisines at distances ranging from roughly 2,500 to 8,000 km. None of these pairs would be predicted to share strong ingredient resemblance based on distance alone — they sit well above the regression line in Finding 1 — yet they consistently do.

The Russian span is geographically distinctive in two respects. First, the country's territorial extent reaches from the Baltic to the Pacific, and historical Russian and Soviet trade and migration networks connected northern and continental Europe to Central Asia and the Pacific Far East. Second, the residual partners cluster at one end of that span — the European end — rather than spreading across the full Eurasian range. Russian's bridge structure is a long-distance European connector more than a Eurasian span as such.

This is the case that most clearly demonstrates that bridge scores are not regional reach in disguise. Russian's bridges are intercontinental, and they are the only top-ten bridge structure that connects through continental Eurasia rather than through coastlines, archipelagos, or the Atlantic basin.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Thai: regional hub at the heart of the strongest corridor
```

> **➤ Click `+` → Text block. PASTE:**

```
Top residual links: Vietnamese (+0.359 — strongest single link in the corpus), Filipino (+0.219), plus secondary links to neighboring E/SE Asian cuisines. Location: mainland Southeast Asia. Bridge score: not in the top 10.

Thai is not a top-ten bridge cuisine. Its analytical role is different: it sits at the center of the strongest focused residual corridor in the corpus. The Thai–Vietnamese link is the highest-residual pairwise link in the entire project at +0.359, a mainland adjacency case where ingredient similarity exceeds distance-based expectation by the largest margin observed.

The Thai-anchored sub-network is dense rather than far-reaching. Thai connects to Vietnamese (mainland adjacency, the strongest case), Filipino (island-maritime, the strongest island-mainland case), and other neighboring cuisines in the regional mesh. These are short-distance links — exactly the kind distance-based intuition expects to find positive residuals — but the magnitudes exceed what a typical same-subregion pair shows globally (mean +0.115 across the corpus).

If Filipino represents the bridge — high cross-region reach — Thai represents the hub: high regional concentration. The project's strongest focused-case residuals are produced by the interaction of both roles. The corridor is anchored by a regional hub and connected outward through a maritime bridge.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Spanish: Iberian/Atlantic–Pacific node
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.53 (rank 6). Location: Iberian peninsula. Top residual partners: Filipino, Mexican, Brazilian, Cajun/Creole, Jamaican — the cuisine pairs that drive the Iberian/Atlantic interregional grouping (Finding 2). Russian also appears among Spanish's labeled long-distance positive-residual partners in the scatter view (Finding 1).

Spanish sits at one end of the project's most analytically distinctive cluster: the Iberian/Atlantic interregional grouping with the highest mean residual in the corpus (+0.139, n = 11). Spanish cuisine's residual links span the Atlantic and the Pacific. The distances are large — the link to Filipino covers roughly 13,000 km — and the ingredient resemblance is consistent.

Among the Iberian/Atlantic group, Spanish is the cuisine whose residual links extend farthest geographically. Its Pacific-spanning connection to Filipino, in particular, is a residual that would be invisible in a distance-only view of cuisine similarity but becomes the highest-magnitude long-distance configuration in the corpus once distance is removed. The Spanish node anchors the project's clearest evidence that long-distance residual cuisine similarity is not noise. It is a structured pattern with identifiable geographic configurations.

Together, Filipino, Russian, Thai, and Spanish span the residual geography of the corpus. Filipino is the maritime bridge. Russian is the continental bridge. Thai is the regional hub. Spanish is the long-distance Iberian/Atlantic–Pacific node. Each occupies a different role; together they describe the structure of the residual network the project set out to reveal.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Four cuisines, four roles. The residual network has a shape, and these four anchors are what give it that shape.
```

> **➤ Click `+` → Separator.**

---

# SECTION 9 — Conclusion

> **➤ Click `+` → Heading (H2). PASTE:**

```
Conclusion
```

> **➤ Click `+` → Text block. PASTE:**

```
The simplest measurement in this project — distance from one cuisine to another — explains roughly a third of the variation in pairwise ingredient similarity. The remaining two-thirds is where the project's analytical interest lives, and that two-thirds turns out to be structured rather than random.

The structure has a specific shape. It concentrates around a small number of bridge cuisines, almost all of them non-Asian. It clusters into specific spatial configurations — most strikingly an Iberian/Atlantic interregional pattern that exceeds the same-subregion baseline. It produces a strongest focused corridor in East and Southeast Asia where mainland adjacency, peninsular geography, and archipelagic structure combine. And it suggests, by its asymmetry, that the geography organizing cuisine resemblance is not the geography of straight-line distance. It is the geography of long-range exchange networks, maritime corridors, archipelagic bridges, and historical contact zones whose imprint on ingredient profiles persists long after the original conditions that produced them.

The strongest contribution of this project is to surface the structure that distance alone obscures. Cuisine, viewed through residuals, has a network shape — and the shape is informative.

For food-systems researchers, agricultural economists, and historians of exchange, the residual network is a starting point for more specific inquiry: which historical events, ecological conditions, or trade networks correspond with which residual links? For methodologists, the bridge index demonstrates that aggregating pairwise residuals to the unit (cuisine) level surfaces structural roles that pairwise analysis alone cannot. For curious general readers, the message is simpler. Cuisine resemblance is not just about who lives next door. It is about who has been connected, and the network of that connectedness has a shape that a map can show.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Cuisine, viewed through residuals, has a network shape. The shape is asymmetric, Atlantic-centered, and informative — and it is invisible in any analysis that treats distance as the only spatial variable.
```

> **➤ Click `+` → Separator.**

---

# SECTION 10 — Sources

> **➤ Click `+` → Heading (H2). PASTE:**

```
Sources
```

> **➤ Click `+` → Text block. PASTE:**

```
This project was developed in Python and ArcGIS Pro / ArcGIS Online, with figure rendering in Matplotlib and Cartopy.

Data processing. Recipe corpus normalization and the cuisine-by-ingredient matrix were built in Python using Pandas and NumPy. Cosine similarity was computed using SciPy. Geodesic distances between cuisine anchors were computed using GeoPy's great-circle distance method. Distance-residual modeling used a simple linear regression on log distance, implemented in scikit-learn.

Spatial analysis and visualization. ArcGIS Pro provided spatial joins, projection, and the regional case-study working layers. ArcGIS Online hosted the residual link layers used during analysis. Final cartographic figures — the global hero map, the East/Southeast Asia regional map, the bridge index, and the spatial-grouping bar chart — were rendered in Python using Matplotlib and Cartopy with Natural Earth basemap data at 110m and 50m resolution.

Bridge index. The residual bridge score for each cuisine combines five components computed from the residual matrix: positive residual degree, participation in the corpus's top-strength residual links, mean residual magnitude, long-distance residual score, and overall residual behavior. Each component is normalized to a 0–1 scale; the five are combined with equal weights to produce the published bridge score.

Boundary/permeability test. Cuisine pairs were partitioned into five spatial groupings based on the regional and subregional relationships between the two anchors. Mean residual within each grouping was computed and compared.

ChatGPT and Claude were used for guidance in processing data, structuring the analytical workflow, and formatting this StoryMap.
```

> **➤ Click `+` → Separator.**

---

# SECTION 11 — Data sources

> **➤ Click `+` → Heading (H2). PASTE:**

```
Data sources
```

> **➤ Click `+` → Text block. PASTE the following, then EDIT the corpus name and any specifics to match what you actually used:**

```
Recipe corpus. Cuisine-labeled recipes were drawn from [TODO: name of corpus, e.g. RecipeNLG / Yummly / Recipe1M+ / FlavorDB], a publicly available recipe dataset providing cuisine labels and ingredient lists. Generic pantry ingredients were filtered before similarity computation; ingredient name normalization mapped closely related variants to canonical forms.

Cuisine labels. The corpus contains [TODO: number] cuisine labels with sufficient recipe counts for inclusion. Cuisine labels are treated as approximate cultural-geographic anchors, not exact nation-state polygons. The retained labels concentrate in East and Southeast Asia, parts of Europe, North America, and a handful of Latin American and Caribbean cuisines, with the African continent, South Asia, the Middle East, and Oceania underrepresented.

Geographic anchors. Each cuisine label was assigned an approximate geographic anchor — a centroid representing the cuisine's home territory. Coordinates are documented in the project repository.

Topographic and coastline data. Natural Earth, version 5.1.1, 110m resolution for global maps and 50m resolution for regional maps. Includes land, ocean, country borders, coastlines, rivers, and lakes layers.

Distance computation. Geodesic distances between anchors use GeoPy's great-circle method on the WGS84 ellipsoid.
```

> **➤ Click `+` → Separator.**

---

# SECTION 12 — Bibliography

> **➤ Click `+` → Heading (H2). PASTE:**

```
Bibliography
```

> **➤ Click `+` → Text block. PASTE the following bibliography skeleton, then EDIT IT to match your actual sources. I have left placeholder slots [TODO: ...] where I do not know your specific citations. The first reference is included in full because it is the canonical foundational paper for ingredient-level cuisine similarity work and is almost certainly relevant to your project; verify it before keeping.**

```
[1] Ahn, Y.-Y., Ahnert, S. E., Bagrow, J. P., & Barabási, A.-L. (2011). Flavor network and the principles of food pairing. Scientific Reports, 1(1), 196. https://doi.org/10.1038/srep00196

[2] [TODO: Recipe corpus reference — e.g. Marin, J., et al. (2021). Recipe1M+: A Dataset for Learning Cross-Modal Embeddings for Cooking Recipes and Food Images. IEEE Transactions on Pattern Analysis and Machine Intelligence; OR the citation for whichever corpus you actually used.]

[3] [TODO: A reference for cosine similarity / vector-space methods in food / ingredient analysis. If you used a specific paper as a methodological model, cite it here.]

[4] [TODO: Reference for cuisine label aggregation / cuisine geography. If you drew anchor coordinates or cuisine geographies from a specific source, cite it here.]

[5] Esri. (2025). ArcGIS Pro Spatial Statistics Toolbox: Spatial Autocorrelation and Hot Spot Analysis. arcgis.com.

[6] Met Office, & Natural Earth. (2024). Natural Earth: Free vector and raster map data. naturalearthdata.com (v5.1.1).

[7] [TODO: GeoPy / geodesic computation reference if you cite the library directly. Otherwise omit.]

[8] [TODO: Any historical / geographic / regional source you used for cuisine context — e.g. food-history references, Atlantic exchange histories, Pacific maritime exchange references. Add as needed.]

[9] [TODO: Any additional method or domain references.]
```

> **➤ Click `+` → Separator.**

---

# Final pre-submission QA (do this BEFORE you publish)

**1. Voice consistency test.** Read the introduction and Finding 3 back-to-back. Both should sound like the EIP submission: declarative, specific, statistical, confident. If either reads as defensive or atlas-flavored, rewrite the offending paragraph.

**2. Bridge-finding placement test.** Section 6 (Finding 3) is the project's single most distinctive analytical insight. Confirm that the "9 of the top ten bridges are non-Asian" sentence is intact, that the ranked list of 10 cuisines is correct, and that the concentration ratios (41 percent for top 3, 64 percent for top 5) are stated.

**3. Atlas-word test.** Search (Cmd/Ctrl-F) for "atlas." It should appear ZERO times in the script. If it appears, rewrite that sentence.

**4. Number consistency test.** Cmd-F each of these key numbers and verify they are stated correctly: R² = 0.355, slope = -0.116, +0.139 (Iberian/Atlantic), +0.115 (same-subregion), n = 11, +0.359 (Thai-Vietnamese), +0.306 (Chinese-Korean), 0.87 (Filipino bridge), 0.84 (Russian bridge).

**5. Caveat-balance test.** The script intentionally drops the v3/v4/v5 "What this proves and what it does not prove" section. Confirm that you have NOT pasted that section back in. The conclusion's penultimate paragraph carries the discipline lightly without a dedicated section.

**6. Image alt-text test.** Click each image, click the gear/edit icon, confirm the alt-text I provided is in place. Empty alt text fails accessibility.

**7. Bibliography fill-in test.** The bibliography in Section 12 has [TODO] placeholders. Fill in your actual sources or delete the placeholders before publishing.

**8. Incognito / public-share test.** After publishing, open the public StoryMap link in a private browser window. If it requires sign-in, your sharing settings are wrong. Set sharing to "Everyone (public)" in the share menu.

**9. Submission form test.** Confirm the Fisher submission form accepts a StoryMap URL. If it requires a PDF upload, attach your PDF technical report and put the StoryMap URL in the description field.

**10. Save proof of submission.** Take a screenshot of the submitted form. Save the email confirmation.

---

# Quick reference: section-to-figure-to-finding map

| § | Section | Figure | Role in argument |
|---|---|---|---|
| 1 | Cover | none (text-only) | Title |
| 2 | Introduction | **Hero** (`v4_01_hero_world_corridors`) | Three-pair contrast + global scope |
| 3 | How the analysis works | none | Three-stage methodology |
| 4 | Finding 1 | `v4_02_method_residual_baseline` | Distance shapes but explains <half (R²=0.36) |
| 5 | Finding 2 | `v4_06_secondary_residuals_by_grouping` | **Iberian/Atlantic > same-subregion** |
| 6 | Finding 3 | `v4_05_bridge_index_map_and_chart` | **9 of 10 bridges non-Asian — the killer finding** |
| 7 | Finding 4 | `v4_03_primary_case_regional_map` + `v4_04_topographic_corridor_map` | E/SE Asia focused corridor |
| 8 | Four cuisines | none | Filipino, Russian, Thai, Spanish |
| 9 | Conclusion | none | What residuals reveal |
| 10 | Sources | none | Tools and methods |
| 11 | Data sources | none | Corpus, anchors, basemaps |
| 12 | Bibliography | none | Numbered references |

---

*End of build instructions. If the build looks right after the QA checklist, publish and submit.*

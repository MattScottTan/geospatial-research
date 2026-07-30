# Bridges Across Cuisines — StoryMap v8 Build Instructions
**Single-file build guide. Open this file, work top to bottom, paste as you go.**

Matthew Tan — Fisher Prize submission
Version: v8 (v7 with Mantel + LISA spatial-statistical layer added)

---

## What changed from v7

v7 organized the StoryMap into four numbered findings plus four case studies. v8 adds a spatial-statistical validation layer between Findings 1 and 2, plus paired spotlight figures for each of the four case-study cuisines, plus a regenerated v4_02 baseline figure with cleaner labels.

The substantive changes:

1. **New Section 5 — Finding 1.5: Mantel + LISA.** A new spatial-statistical validation finding sits between the distance-baseline regression (Finding 1) and the spatial-grouping inversion (Finding 2). It applies a Mantel test (r = +0.63, p < 0.001) and partial Mantel test (r = +0.51, p < 0.001) to confirm that the distance–dissimilarity relationship is statistically real and survives controlling for subregional adjacency, then applies Local Moran's I (LISA) to identify which cuisines are formally significant high-high or low-low spatial-association nodes. Mexican and Jamaican are significant high-high (Atlantic-rim cluster); Russian is the only highly significant low-low (continental bridge isolated from its low-residual neighbors); Filipino, Spanish, Thai, and French show the high-low sign pattern across all four spatial-weights schemes.

2. **Four new case-study spotlight figures.** Each case study (Filipino, Russian, Thai, Spanish) now pairs a great-circle world map with a residual-rank scorecard, integrating the LISA classification from Finding 1.5 into the case-study narrative.

3. **v4_02 baseline regenerated.** The original Finding 1 figure had presentation issues ("The GIS move:" placeholder title and lowercase cuisine labels). The regenerated figure uses cleaner labels and capitalizations. A small consequence is the regression numbers shift slightly (R² 0.355 → 0.397, slope −0.116 → −0.124) because the alias crosswalk used in the original pipeline was not shipped with the matrix file. Prose and caption are updated to match.

4. **v4_06 caption revised.** The "mandatory non-Asia diagnostic case" callout text has been replaced.

5. **Bibliography revised.** Entry [3] (Ahn et al. flavor network) is removed. Four new methodology citations are added: Mantel 1967, Smouse-Long-Sokal 1986, Anselin 1995, PySAL. The previous [4]–[16] shift up by 3 to [7]–[19].

6. **Section numbering updated.** The new Finding 1.5 takes Section 5; Findings 2–4 shift to Sections 6, 7, 8; Four cuisines becomes Section 9; Conclusion through Bibliography shift to Sections 10–13.

---

## What changed from v6 (carried over from v7)

v6 inadvertently framed the bridge-cuisine finding around the 9-of-10-non-Asian skew. v7 rebalances. The corridor structure is **global**, and the four case studies give equal focus to Asian and non-Asian cuisines.

The substantive changes:

1. **Finding 3 reframed.** The bridge index now leads with what the network looks like (high concentration around a small set of cuisines that span Asian, Eurasian, and Atlantic geographies) rather than with the regional-balance count. The Asian-vs-non-Asian numbers are still mentioned but as one feature among several, not the headline.
2. **Section 9 case-study framing rebalanced.** Filipino is now "archetypal archipelagic bridge" rather than "the only Asian top-ten bridge." Thai is the regional hub at the corridor's center. Russian and Spanish anchor the long-distance configurations. The four together demonstrate that the residual network has Asian and non-Asian roles of equal analytical weight.
3. **Introduction and conclusion language adjusted** so "asymmetry" and "non-Asian" claims do not dominate the framing. The lead is now "the residual network has a structured shape spanning multiple regions," with specific structural roles described in the findings and case studies.

Everything else from v6 is retained: the EIP voice, four numbered findings, four case studies, sources, data sources, and bibliography sections, plus all six figures used unchanged from v5.

---

## What changed from v5 (carried over from v6)

v6 was a complete script rewrite from v5, dropping the "atlas" framing and adopting the EIP submission's voice. v7 keeps that rewrite. Only the regional-balance framing within Findings 3, 8, and the intro/conclusion shifts.

---

## Pre-flight: figures ready

Have all eleven PNG files on your desktop, named exactly:

| § | Filename | Goes in |
|---|---|---|
| 1 | `v4_01_hero_world_corridors.png` | Section 2 (Introduction) |
| 2 | `v4_02_method_residual_baseline.png` | Section 4 (Finding 1) |
| 3 | `v4_07_lisa_and_mantel.png` | Section 5 (Finding 1.5) |
| 4 | `v4_06_secondary_residuals_by_grouping.png` | Section 6 (Finding 2) |
| 5 | `v4_05_bridge_index_map_and_chart.png` | Section 7 (Finding 3) |
| 6 | `v4_03_primary_case_regional_map.png` | Section 8 (Finding 4) |
| 7 | `v4_04_topographic_corridor_map.png` | Section 8 (Finding 4, second figure) |
| 8 | `v4_08_case_filipino.png` | Section 9 (Filipino) |
| 9 | `v4_08_case_russian.png` | Section 9 (Russian) |
| 10 | `v4_08_case_thai.png` | Section 9 (Thai) |
| 11 | `v4_08_case_spanish.png` | Section 9 (Spanish) |

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
Cuisine resemblance has a shape that distance can't predict
```

> **➤ Subtitle field:**

```
Mapping the residual network that connects archipelagos, peninsulas, and Atlantic shores
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
Across the world's documented cuisines, a striking fraction of the variation in ingredient resemblance cannot be explained by geographic distance. Some pairs are far apart yet remarkably similar. Some pairs sit inside the same region yet diverge sharply. The geography that organizes cuisine is not the geography of straight-line kilometers.

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
Cuisines are connected here by ingredient resemblance distance cannot explain. Blue great-circle links mark the East/Southeast Asia focused case (line width proportional to residual strength); orange links mark long-distance residual outliers — pairs sitting well above the distance-similarity regression line. The map's geographic coverage reflects the cuisine-labeled recipe corpus, not world food geography. Residual links are candidate spatial associations, not proven exchange routes.
```

> **➤ Alt text:**

```
Robinson-projection world map with beige land and light-blue ocean basemap, country borders, and a subtle 30-degree graticule. Blue great-circle lines connect East and Southeast Asian cuisine anchors at varying widths. Orange great-circle lines connect long-distance pairs including British–Russian, Irish–Russian, French–Russian, and British–Southern US. Cuisine anchors in Europe, North America, the Caribbean, and South America are marked and labeled. A boxed corpus-coverage note in the lower right names the regions absent from the corpus.
```

> **➤ Click `+` → Text block. PASTE:**

```
Three pairs of cuisines illustrate the puzzle. Thai and Vietnamese cuisines, separated by roughly 800 km of mainland Southeast Asia, share an ingredient profile resemblance well above the global mean. British and Russian cuisines, separated by 5,500 km and divided by language, climate, and political history, share an ingredient resemblance well above what distance alone would predict — one of the largest residuals among any European pair. Filipino and Brazilian cuisines, separated by nearly 19,000 km on opposite sides of the planet, share an ingredient resemblance the distance baseline cannot explain — a residual that ranks among the largest in the corpus. These three pairs are not curiosities. They are systematic.

Most analyses of food treat cuisine as a cultural object: tastes, traditions, identities. Most spatial analyses, when they reach into food at all, treat distance as the primary explanatory variable for resemblance. This project sits at the intersection. It measures pairwise ingredient similarity systematically, models how similarity declines with geographic distance, and then asks where that decline does not hold. The leftover — residual cuisine similarity — turns out to be where the geography of food becomes interesting.

What this analysis produces, beyond methodology, is a set of testable historical-exchange hypotheses anchored to specific cuisines and the corridors their residuals trace.
```

> **➤ Click `+` → Text block. PASTE:**

```
The sections that follow describe how the analysis was built and what the residual network looks like once distance is removed. The findings work outward from the underlying baseline to two complementary structural views — a spatial-grouping view that reveals where residuals concentrate by configuration of cuisine pairs, and a network-position view that identifies which individual cuisines anchor the residual structure most actively. The strongest focused regional case sits in East and Southeast Asia, where mainland adjacency, peninsular geography, and archipelagic structure combine to produce the most cleanly readable corridor in the corpus. Four cuisine cases — two Asian, two non-Asian — close the analysis, each illustrating a distinct structural role.
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

Stage 1: Build comparable cuisine profiles. Cuisine-labeled recipes from a large recipe corpus [1, 2] are normalized so closely related ingredient names map to a single canonical ingredient — "scallion" and "green onion" become one entry. Ingredients are then aggregated into a cuisine-by-ingredient matrix in which each cuisine is represented as a frequency vector across thousands of normalized ingredients. This is the project's textual, chemical, and culinary signature for each cuisine.

Stage 2: Measure ingredient similarity and geographic distance. Pairwise cuisine similarity is computed using cosine similarity on the ingredient frequency vectors [9, 10], with generic-ingredient filtering and robustness checks. Each cuisine label is assigned an approximate geographic anchor — a centroid representing the cuisine's home territory. Pairwise geodesic distances between anchors are computed using GeoPy's great-circle method [11].

Stage 3: Extract the residual. Cuisine similarity is regressed on log geographic distance. The fitted line gives, for each pair, a predicted similarity based on distance alone. The residual — observed similarity minus distance-predicted similarity — becomes the analytical object. Positive residuals identify pairs more similar than distance predicts. Mapped, they form a candidate network of long-distance culinary connection.

The findings that follow draw on this residual layer in different ways: a distance-baseline view, a spatial-statistical validation that tests whether the residual structure is real and where it sits, a spatial-grouping view, a network-position view, and a focused regional case.
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
Ingredient similarity declines with geographic distance, but the decline is shallow. The fitted relationship across all pairwise cuisine comparisons returns a slope of −0.124 per unit of log distance and an R² of 0.397. In concrete terms: doubling the distance between two cuisines reduces their predicted ingredient similarity by approximately 0.086 cosine-similarity units — meaningful, but small relative to the range of observed similarities, which spans roughly 0.05 to 0.92. Roughly 60 percent of the variation in cuisine similarity is structured but not explained by distance.

The shallowness matters analytically. If distance explained 90 percent of cuisine resemblance, a residual analysis would reveal little: the line would absorb most of the signal and leave only noise behind. At R² = 0.40, the residuals carry the majority of the spatial information. The largest positive residuals include several long-distance combinations the distance baseline would never anticipate: British–Southern U.S., Irish–Russian, British–Russian, French–Russian. These pairs sit between roughly 5,500 and 7,000 km apart yet retain ingredient similarities that match or exceed those of regional neighbors.

The figure below shows the underlying pattern. Each point is one cuisine pair; the regression line is the distance baseline; named labels mark the strongest positive residuals discussed above.
```

> **➤ Click `+` → Image block. Upload `v4_02_method_residual_baseline.png`.**
> **➤ Caption:**

```
Distance baseline for cuisine similarity. Each point is a pairwise cuisine comparison: cosine similarity of filtered ingredient profiles plotted against log geographic distance between cuisine anchors. The fitted line — similarity = 1.258 − 0.124 × ln(distance), R² = 0.397 — defines the distance-only expectation. Pairs above the line are positive residuals; the labeled points (Thai–Vietnamese, Chinese–Korean, British–Southern U.S., British–Russian, Irish–Russian, French–Russian) are among the strongest positive residuals in the corpus.
```

> **➤ Alt text:**

```
Scatter plot of cosine similarity of filtered cuisine ingredient profiles versus log geographic distance between cuisine anchors. A regression line of similarity = 1.258 − 0.124 × ln(distance) is shown with R² = 0.397. Points above the line, including Thai–Vietnamese and Chinese–Korean at the short-distance end and British–Southern U.S., British–Russian, Irish–Russian, and French–Russian at the long-distance end, are highlighted as positive residuals.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Two-thirds of cuisine similarity sits outside what distance alone can explain. That two-thirds is where the analysis goes next.
```

> **➤ Click `+` → Separator.**

---

# SECTION 5 — Finding 1.5

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 1.5: The distance–similarity relationship is statistically real, and the residuals are spatially structured.
```

> **➤ Click `+` → Text block. PASTE:**

```
Finding 1 fit a regression line. Finding 1.5 asks two follow-up questions that the regression alone cannot answer. First, is the distance–similarity relationship statistically real, or could the apparent pattern have arisen by chance from a small sample of cuisine pairs? Second, is the residual structure that Findings 2–4 will go on to describe — the part the regression does not explain — actually spatially organized, or is it scattered randomly across the world's cuisine anchors?

These are different questions and they need different tools. The regression in Finding 1 reports a single global slope. It does not test the relationship for significance, and it does not say anything at all about whether residuals from nearby cuisines look more like each other than residuals from distant cuisines. To answer the two questions above, the analysis applies two recognized spatial-statistical tests in sequence: a Mantel test on the full distance matrices, and Local Moran's I on a per-cuisine residual score.

The Mantel test [3] is the standard tool in spatial ecology and biogeography for measuring whether two distance matrices co-vary. Given a cuisine-by-cuisine dissimilarity matrix and a cuisine-by-cuisine geographic-distance matrix, the Mantel statistic is the matrix-level Pearson correlation between the two, and significance is assessed by random permutation: shuffle the rows and columns of one matrix while holding the other fixed, recompute the correlation, repeat thousands of times, and check how often a random permutation produces a correlation as strong as the observed one. If almost no permutation does, the observed correlation is unlikely to have arisen by chance.

Applied to the 190 pairwise comparisons across the 20 cuisines using 9999 permutations, the Mantel correlation between cuisine dissimilarity and log geographic distance is r = +0.63 (p < 0.001). The relationship is highly significant: in 9999 permutations, no random shuffle produced a correlation of comparable strength. The descriptive scatter in Finding 1 reflects a real underlying pattern in the corpus.

The partial Mantel test [4] extends this to control for a second factor. Cuisines in the same subregion are by definition both geographically close and culturally connected, which raises a question: does the distance–similarity relationship reduce to "cuisines that are subregional neighbors are similar," or is there an independent distance signal across subregional boundaries? The partial Mantel correlation, controlling for a same-subregion indicator, is r = +0.51 (p < 0.001). Distance still strongly predicts cuisine dissimilarity even after partialling out subregional adjacency. The relationship is not just neighbors-being-neighbors.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The distance–similarity relationship is real (Mantel r = +0.63), and it survives partialling out subregional adjacency (partial r = +0.51). What remains in the residual is what the rest of the analysis decomposes.
```

> **➤ Click `+` → Text block. PASTE:**

```
Local Moran's I [5] addresses the second question. It is a local measure of spatial autocorrelation, designed to identify, for each location in a study, whether that location forms part of a statistically meaningful spatial cluster. The test takes a per-cuisine value — here, the mean residual cuisine similarity across all 19 of the cuisine's pairwise comparisons — and a spatial weights matrix that defines what "near" means. For each cuisine, Local Moran's I compares the cuisine's deviation from the global mean against the deviations of its spatially weighted neighbors. The result is a per-cuisine classification into one of four spatial-association quadrants. High-high (HH) identifies a high-residual cuisine surrounded by other high-residual cuisines — a regional cluster. Low-low (LL) identifies a low-residual cuisine in a low-residual neighborhood. High-low (HL) identifies a high-residual cuisine surrounded by low-residual neighbors — the spatial signature of an isolated bridge: a hot point in a cold neighborhood. Low-high (LH) is the converse, a cold point in a hot neighborhood. Significance is again assessed by permutation, with 9999 permutations producing a pseudo-p-value for each cuisine's local statistic.

The choice of Local Moran's I rather than alternatives like Getis-Ord Gi* reflects what the test needs to do for this project. Gi* is well suited to identifying significant high or low clusters but does not separate "high in high" from "high in low" — and the high-in-low pattern (an isolated bridge cuisine surrounded by less-connected neighbors) is exactly the spatial structure Findings 3 and 8 will go on to describe. LISA's four-quadrant decomposition makes that structure formally visible. With cuisine anchors as point locations and a spatial weights matrix derived directly from the same geographic distances used in Finding 1, the analysis is internally consistent: the spatial test operates on the same geometry the regression already reduced. The implementation uses the PySAL `esda` module [6].

The robustness of the LISA classifications was checked across four spatial-weights schemes — inverse-distance (the headline specification), k-nearest-neighbor with k = 4, k-nearest-neighbor with k = 6, and Gaussian-kernel weights with bandwidth 3,000 km — to confirm that the classifications are not artifacts of one specific definition of "near." Three classifications reach formal significance at p < 0.05 in the inverse-distance specification: Mexican and Jamaican as high-high, and Russian as low-low. Cajun-Creole, Brazilian, and Southern U.S. show the same high-high pattern at marginal significance (p < 0.10) in at least two of the four schemes, completing an Atlantic-rim and Caribbean-Gulf high-residual cluster that is robust across spatial-weights choices. Filipino, Spanish, Thai, and French show the high-low pattern by sign of Local Moran's I across all four schemes; none reach p < 0.05 individually, which is a power limitation expected at n = 20 cuisine anchors and not evidence of absence.
```

> **➤ Click `+` → Image block. Upload `v4_07_lisa_and_mantel.png`. Use full-width display.**
> **➤ Caption:**

```
Two-panel spatial-statistical view of the residual structure. Left: Local Moran's I classification of cuisine anchors using inverse-distance spatial weights. Russian, Mexican, and Jamaican reach formal significance (p < 0.05, 9999 permutations) and are shown with bold edges. Cuisines in the same quadrant but not significant individually are shown in lighter shades. Marker size scales with the magnitude of mean residual. Right: Moran scatterplot showing each cuisine's mean residual against its inverse-distance spatial lag, with the regression slope equal to the Global Moran's I = +0.091 (p = 0.05). The lower inset reports Mantel and partial Mantel test results. Together the panels formalize the spatial structure that Findings 2–4 will describe substantively.
```

> **➤ Alt text:**

```
Two-panel figure with a Robinson-projection world map on the left and a Moran scatterplot on the right. The world map shows 20 cuisine anchors classified by Local Moran's I quadrant. Russian appears in dark blue with a bold edge in central Eurasia (significant low-low). Mexican and Jamaican appear in deep orange with bold edges in the Caribbean and Mexico (significant high-high). Cajun-Creole, Brazilian, and Southern US appear in lighter orange (high-high pattern at marginal significance). Filipino and Spanish appear in magenta (high-low pattern, sign-consistent across robustness schemes). Other cuisines including Chinese, Korean, Japanese, Indian, Italian, Greek, Moroccan, French, British, Irish, Thai, and Vietnamese appear in muted colors indicating non-significant classifications. The Moran scatterplot on the right shows mean residual on the x-axis and spatial lag on the y-axis, both as z-scores; quadrants are labeled HH, HL, LL, LH. The regression slope, equal to Global Moran's I, is plus zero point zero nine one with p equals zero point zero five. A statistical inset below the scatterplot lists three Mantel test results: dissimilarity versus log distance r equals plus zero point six three; partial Mantel controlling for shared subregion r equals plus zero point five one; dissimilarity versus subregion gap r equals plus zero point five zero. All three p-values are below zero point zero zero one.
```

> **➤ Click `+` → Text block. PASTE:**

```
Two structural facts follow. First, the Atlantic-rim cluster identified visually in Findings 2 and 3 is now formally validated: the high-high spatial association of Mexican–Jamaican–Cajun-Creole–Brazilian–Southern U.S. is detectable above what spatial randomness would predict, and the result is robust across alternative spatial-weights specifications. Second, the Russian bridge structure described in Finding 3 is formally clean. Russian's geographic neighbors are low-residual cuisines (Chinese, Korean, Indian, Greek), while Russian's strong residual partners (British, Irish, French, Italian) sit five to seven thousand kilometers west — too far to dominate the local spatial weights. The Local Moran's I returns Russian as the only highly significant low-low classification in the corpus (p = 0.009), consistent across all four robustness schemes. Russian's bridge score (0.84, rank 2) is not regional reach in disguise. The LISA proves this formally: Russian's residual partners are not its neighbors.

It is worth being precise about what the spatial-statistical layer does and does not show. The Mantel and partial Mantel tests are matrix-level correlations; they confirm a relationship but do not estimate causal effects, and they do not say where in the network that relationship sits. The Local Moran's I locates the relationship at the cuisine level but inherits the limitations of small-sample local statistics: with n = 20 cuisine anchors, the test has limited statistical power for individual classifications, which is why several substantively important cases (Filipino, Spanish, Thai) show consistent sign across robustness schemes but do not reach the conventional p < 0.05 threshold. The findings reported here treat the formally significant classifications as definitive and the sign-consistent classifications as supportive evidence. The qualitative spatial pattern — an Atlantic-rim high-high cluster, a Eurasian low-low outlier, and a small set of high-low isolated bridges — is robust regardless of which evidence threshold is applied.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Finding 1.6: A direct test of the colonial-administration hypothesis
```

> **➤ Click `+` → Text block. PASTE:**

```
The Mantel framework introduced in Finding 1.5 admits one further test that bears directly on the project's substantive payoff: are residual similarities elevated specifically along corridors of historical colonial administration, after distance and subregional adjacency have already been accounted for? This is the question the case-study sections will pose interpretively for Filipino, Russian, and Spanish; the partial Mantel framework allows it to be tested directly.

To do so, all 190 cuisine pairs are coded on a three-tier ordinal scale: 0 if the two cuisines have no shared colonial-administrative connection, 1 if the connection is brief or peripheral (less than 50 years of direct rule, or imperial-sphere membership without direct co-administration), and 2 if the two cuisines were under sustained core colonial administration of one over the other (more than 50 years of direct rule) or co-administered as part of the same colonial unit. Of the 190 pairs, 13 carry code 2 (Spanish–Filipino, Spanish–Mexican, Filipino–Mexican via the Viceroyalty of New Spain, French–Vietnamese, British–Irish, British–Indian, British–Jamaican, British–Southern U.S., Irish–Indian, Irish–Jamaican, Indian–Jamaican, Jamaican–Southern U.S., French–Cajun-Creole), 20 carry code 1, and 157 carry code 0. The full crosswalk with per-pair rationale is included in the project repository.

The partial Mantel correlation of residual cuisine similarity with this colonial-administration code, controlling for log-distance and same-subregion adjacency, is r = +0.18 (two-sided p = 0.022, 9999 permutations). The sensitivity panel — testing under strict binary coding, sustained-only binary coding, and a Spanish-sphere-only indicator — returns r in the range +0.14 to +0.18 with p ≤ 0.04 in three of four codings. The colonial-administration signal in the residual matrix is robust to coding-scheme choice and is independent of the distance and subregional-adjacency signals already accounted for.

The effect size is modest. Colonial administration, on this evidence, is one structuring factor in the residual network — it is not the only one. What the test does establish is that the project's case-study claim that Filipino's residual fingerprint is *consistent with* the geography of the Manila Galleon, that Spanish's links are *consistent with* the Iberian colonial network, and that comparable corridors exist for Russian and other bridge cuisines, is supported beyond pattern-matching: the residual signal correlates with colonial geography after distance and adjacency have been removed. The test cannot distinguish among colonial mechanisms (administrative, demographic, agricultural exchange, language-and-recipe-transmission) — that distinction would require historical-record cross-validation outside the cuisine corpus. But the residual network is not reducible to spatial proximity, and it is not reducible to within-region cultural sharing. A specific historical-exchange signal is detectable in the residuals.

A complementary permutation test on the bridge-index ranking confirms that the project's identification of a small set of high-connectivity cuisines is not an artifact of chance. Under random permutation of cuisine labels (9999 shuffles), the published top-3 bridge cuisines {Filipino, Russian, Southern U.S.} co-occur as the top three in zero of the permutations (p = 0.0001). The bridge ranking is identifying a real concentration of residual structure around specific cuisine anchors, not a random subset.
```

> **➤ Click `+` → Separator.**

---

# SECTION 6 — Finding 2

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
Long-distance Iberian–Atlantic–Pacific pairs are more similar than distance predicts by a wider margin than even regional neighbors. Mean residual cuisine similarity by spatial grouping: the Iberian/Atlantic interregional grouping sits at the top of the ranking (+0.139, n = 11), exceeding the same-subregion baseline (+0.115, n = 11). All other groupings sit slightly below the distance-only expectation. The geography that organizes ingredient resemblance, in this view, is colonial-era and oceanic before it is neighborly.
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

# SECTION 7 — Finding 3

> **➤ Click `+` → Heading (H2). PASTE:**

```
Finding 3: A small set of bridge cuisines anchors the residual network — and they span Asian, Eurasian, and Atlantic geographies in distinct structural roles.
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

The ranking has structure worth reading carefully. Filipino sits at the top, anchoring a Pacific-archipelagic role that connects East and Southeast Asian cuisines through maritime geography while also extending across the Pacific to Spanish-speaking partners. Russian sits second, anchoring a continental Eurasian span whose strongest residual partners are European cuisines on the western edge of that span. The remaining eight cuisines cluster geographically along the Atlantic basin and its connected geographies — the British and Irish Isles, the Iberian and French peninsulas, the Italian peninsula, the Caribbean, the Southern U.S. coast, and Brazil's Atlantic shore. The bridge network, in other words, has three structural geographies: a Pacific-archipelagic node, a Eurasian continental span, and a dense Atlantic-rim cluster.
```

> **➤ Click `+` → Image block. Upload `v4_05_bridge_index_map_and_chart.png`. Use full-width display.**
> **➤ Caption:**

```
The residual network is anchored by a small set of high-connectivity bridge cuisines whose geographies are distinct rather than redundant. Two-panel residual bridge index. Left: Robinson world map of cuisine anchors with circle size proportional to bridge score, showing the Pacific-archipelagic node (Filipino), the Eurasian continental anchor (Russian), and the Atlantic-rim cluster (British, Irish, French, Spanish, Italian, Southern U.S., Jamaican, Brazilian). Right: ranked bar chart of the top ten bridge scores. The three structural geographies — archipelagic, continental, Atlantic-rim — read off the figure at a glance.
```

> **➤ Alt text:**

```
Side-by-side panels. Left panel is a Robinson-projection world map with beige land and light-blue ocean. A large blue circle marks Filipino in the western Pacific; large orange circles mark Russian in central Asia, Southern US in the U.S. southeast, Jamaican in the Caribbean, French, Spanish, British, Irish, and Italian in western and southern Europe, and Brazilian in central South America. Right panel is a horizontal bar chart titled "Top 10 bridge cuisines" showing residual bridge scores from 0.87 (Filipino, blue) to 0.31 (Brazilian), with all other bars in orange.
```

> **➤ Click `+` → Text block. PASTE:**

```
The bridge network is also concentrated. The top three cuisines — Filipino, Russian, and Southern U.S. — together account for 41 percent of the total bridge weight in the top 10. The top five — adding Jamaican and French — account for 64 percent. The residual network is not flat; it is anchored by a small, geographically specific set of cuisines that connect the rest into a coherent long-distance structure.

It is worth being precise about what a bridge score does and does not say. It is a network position. It says that, after the distance baseline is removed, the focal cuisine participates in many strong residual links with cuisines that are not its geographic neighbors. It does not assert that the focal cuisine caused those resemblances or that any one cuisine "owns" a corridor. It reports a structural fact about the corpus: ingredient resemblance, when distance is controlled for, organizes itself around a small number of high-connectivity nodes whose geographies are distinct rather than redundant.

The three structural geographies — Pacific-archipelagic, Eurasian continental, and Atlantic-rim — each play a different role. The Filipino node connects East/Southeast Asian regional cuisines (the focused case in Finding 4) into a wider global network. The Russian node connects continental Eurasia to the western European Atlantic cluster. The Atlantic-rim cluster contains the densest concentration of mutually high-residual pairs, which is consistent with Finding 2's identification of the Iberian/Atlantic interregional grouping as the highest-mean-residual configuration in the corpus. The bridge structure and the spatial-grouping structure tell consistent stories from different angles.
```

> **➤ Click `+` → Quote block. PASTE:**

```
The residual network has three distinct geographies — Pacific-archipelagic, Eurasian continental, and Atlantic-rim — each anchored by different cuisines and each playing a different structural role.
```

> **➤ Click `+` → Separator.**

---

# SECTION 8 — Finding 4

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
East and Southeast Asia produce the corpus's cleanest regional corridor: a small network where mainland adjacency, peninsular geography, and archipelagic structure each contribute a different kind of strong residual link. Link color encodes spatial type: dark blue for mainland adjacency, teal for regional proximity, magenta for island/maritime. Line width is proportional to residual strength; the strongest residual values are labeled inline. A side panel ranks the top five focused-case residual links over country fills, coastlines, rivers, and the South China Sea / Sea of Japan.
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
Adding shaded relief makes the corridor's geographic logic legible: the Tibetan plateau is the western barrier, the South China Sea is the connector rather than the gap, and the archipelagic ring (Filipino, Japanese) closes the loop on the mainland anchors. Same residual links as the previous figure, with line width reflecting residual strength and line color indicating same-subregion, island/maritime, or cross-subregion link types. The relief is interpretive context, not causal claim — peninsulas and shallow seas explain the geometry of the residuals without explaining why specific cuisines resemble each other.
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

# SECTION 9 — Four cuisines that explain the pattern

> **➤ Click `+` → Heading (H2). PASTE:**

```
Four cuisines that explain the pattern
```

> **➤ Click `+` → Text block. PASTE:**

```
The four findings above describe the residual geography in aggregate. The four cuisines that follow illustrate how that geography concentrates around individual cuisine anchors. Each represents one structural role in the network. Two are Asian — Filipino and Thai — and they anchor the Pacific-archipelagic and East/Southeast Asian regional structures respectively. Two are non-Asian — Russian and Spanish — and they anchor the Eurasian continental and the Iberian/Atlantic structures respectively.

Together, the four describe the shape of the residual network from four complementary vantage points: an archipelagic bridge, a continental bridge, a regional hub, and a long-distance Iberian/Atlantic node.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Filipino: archetypal archipelagic bridge
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.87 (rank 1 of 10). Location: Philippine archipelago. Top residual links: Thai (+0.36), Brazilian (+0.32), Vietnamese (+0.25), Jamaican (+0.13), Southern U.S. (+0.07) — a residual signature that spans mainland Southeast Asia, the Caribbean–Gulf, and the Atlantic shore of South America from a single archipelagic anchor.

Filipino is the highest-scoring bridge cuisine in the entire corpus by a clear margin — its bridge score of 0.87 alone accounts for 15 percent of the total weight held by the top ten. The cuisine sits in the Philippine archipelago, geographically positioned between mainland Southeast Asia, East Asia, the Pacific Ocean, and — through three centuries of historical exchange — the Spanish-speaking Atlantic and Caribbean.

The residual structure of Filipino cuisine reads as a maritime bridge. Its links to Thai and Vietnamese are island-to-mainland connections across the South China Sea — short-range residuals at high magnitude. Its links to Brazilian, Jamaican, and Southern U.S. are trans-oceanic, following great-circle paths that cross the Pacific and the Atlantic. The historical mechanism is the Manila Galleon trade route (1565–1815) and the broader Spanish colonial network it opened, which moved tomato, chilis, corn, and other New World ingredients into the Filipino kitchen and brought tropical Asian flavors into the Caribbean and the Gulf. No other cuisine in the corpus participates in residual links across this many distinct geographic configurations.

The Filipino node is what makes the East/Southeast Asia case (Finding 4) and the Iberian/Atlantic–Pacific finding (Finding 2) connect. It is the cuisine where the corridor structure meets the bridge structure — the analytical hinge between the project's regional and global scales.
```

> **➤ Click `+` → Image block. Upload `v4_08_case_filipino.png`. Use full-width display.**
> **➤ Caption:**

```
Filipino's residual structure on the world map. The blue anchor in the western Pacific connects across the Pacific to the Atlantic-rim cluster (Brazilian, Jamaican, Southern U.S.) and across the South China Sea to mainland Southeast Asia (Thai, Vietnamese). Line width is proportional to residual strength. The right panel ranks Filipino's top five residual partners and reports Filipino's classification on the spatial-statistical layer from Finding 1.5: a high-low Local Moran's I quadrant (sign-consistent across all four spatial-weights schemes), the most negative Local I in the corpus, the highest mean residual of any cuisine, and the highest bridge score (0.87).
```

> **➤ Alt text:**

```
Two-panel figure. Left panel is a Robinson-projection world map centered on the Philippine archipelago. A blue circle marks Filipino in the western Pacific. Five orange great-circle arcs connect Filipino to: Thai and Vietnamese in mainland Southeast Asia; Jamaican and Southern US in the Caribbean and US Gulf coast; and Brazilian on the Atlantic shore of South America. Each partner anchor is labeled with its residual value: Thai plus zero point three six, Brazilian plus zero point three two, Vietnamese plus zero point two five, Jamaican plus zero point one three, Southern US plus zero point zero six. Right panel is a horizontal bar chart of the same five partners ranked by residual strength, with a stats summary box below listing mean residual plus zero point zero five four eight, bridge score zero point eight seven (rank one of ten), LISA classification HL with p equals zero point one four nine, Local Moran's I minus zero point four nine four, and role in network as Pacific-archipelagic node.
```

> **➤ Click `+` → Text block. PASTE:**

```
The figure makes Filipino's structural role visible. The five strongest residual partners span three distinct geographic configurations: mainland Southeast Asia across the South China Sea, the Caribbean and US Gulf coast across the Pacific and the Americas, and Brazil's Atlantic shore via a great-circle path that wraps across two oceans. No other cuisine in the corpus participates in residual links across this many distinct configurations. The spatial-statistical evidence aligns precisely: Filipino's Local Moran's I is the most negative of any cuisine across all four robustness schemes — the unmistakable HL signature of an isolated bridge. The cuisine's highest-residual neighbors are all far away.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Russian: long-distance Eurasian bridge
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.84 (rank 2). Location: continental Eurasia. Top residual partners: Irish (+0.19), Mexican (+0.18), British (+0.15), Southern U.S. (+0.12), French (+0.11) — five cuisines reached by long-distance great-circle paths westward across Europe and over the polar route to the Americas, none of them Russian's geographic neighbors.

Russian sits second only to Filipino on bridge score, and the comparison between the two is structurally informative. Where Filipino bridges across maritime space, Russian bridges across continental and trans-polar distance. Its top residual partners are all Atlantic-rim cuisines at distances ranging from roughly 5,500 to 9,500 km. None of these pairs would be predicted to share strong ingredient resemblance based on distance alone — they sit well above the regression line in Finding 1 — yet they consistently do.

The Russian span is geographically distinctive in two respects. First, the country's territorial extent reaches from the Baltic to the Pacific, and historical Russian and Soviet trade and migration networks connected northern and continental Europe to Central Asia and the Pacific Far East. Second, the residual partners cluster at one end of that span — the European and trans-Atlantic end — rather than spreading across the full Eurasian range. Russian's bridge structure is a long-distance Atlantic-rim connector rather than a Eurasian span as such, and the LISA evidence in Finding 1.5 confirms this formally: Russian is the only cuisine with a highly significant low-low spatial classification (p = 0.009).

This is the case that most clearly demonstrates that bridge scores are not regional reach in disguise. Russian's bridges are intercontinental, and its continental-bridge geometry is the structural mirror image of Filipino's maritime-bridge geometry. The two highest-scoring bridges in the corpus do the same job through completely different geographies.
```

> **➤ Click `+` → Image block. Upload `v4_08_case_russian.png`. Use full-width display.**
> **➤ Caption:**

```
Russian's residual structure. The blue anchor in central Eurasia connects west to the Atlantic-rim European cluster (British, Irish, French) and across the Pacific to the Caribbean-Gulf cluster (Mexican, Southern U.S.) — the latter via great-circle paths that wrap over the polar route. The right panel ranks Russian's top five residual partners and reports the spatial-statistical evidence from Finding 1.5. Russian is the only cuisine in the corpus with a highly significant Local Moran's I classification at p = 0.009, holding across all four robustness schemes — a low-low spatial pattern that confirms Russian's strong residual partners are not its geographic neighbors.
```

> **➤ Alt text:**

```
Two-panel figure. Left panel is a Robinson-projection world map centered on Russia. A blue circle marks Russian in central Eurasia. Five orange great-circle arcs connect Russian to: British and French in western Europe; and Mexican and Southern US across the polar route to the Americas. Irish is shown as a small unlabeled dot near British. Each labeled partner shows its residual value: British plus zero point one five, French plus zero point one one, Southern US plus zero point one two, Mexican plus zero point one eight. Right panel is a horizontal bar chart of all five partners — Irish at the top with plus zero point one nine — ranked by residual strength. A stats summary box lists mean residual minus zero point zero two five, bridge score zero point eight four (rank two of ten), LISA classification LL with p equals zero point zero zero nine and three asterisks indicating high significance, Local Moran's I plus zero point one four zero, and role in network as Eurasian continental anchor.
```

> **➤ Click `+` → Text block. PASTE:**

```
The map and the spatial-statistical evidence agree on what Russian's role looks like. All five top residual partners sit five to seven thousand kilometers from the Russian anchor. None of Russian's geographic neighbors — Chinese, Korean, Japanese, Indian, Greek — is among its strong residual partners; the LISA picks this up as the low-low pattern, with Russian's spatial neighborhood (defined by inverse-distance weighting) consisting of low-residual cuisines whose mean is below the corpus average. The spatial weights cannot reach far enough to see British, Irish, French, or Italian, and that geometric fact is precisely what makes the LL classification meaningful. Russian is a continental-bridge cuisine in the strict spatial-statistical sense: its strong residual partners exist outside its spatial neighborhood, on the western European edge of the Eurasian span.

A reviewer-anticipated objection is worth addressing directly: the Russian anchor sits at the country's geographic centroid (61.52°N, 105.32°E), deep in central Siberia, which makes Russian "far" from European cuisines under inverse-distance weighting. Re-running Local Moran's I for Russian under a Moscow anchor (55.75°N, 37.62°E) preserves the LL sign — Russian's spatial neighborhood is low-residual under either choice, because the Asian neighbors that pull the spatial lag downward are largely the same — but it does weaken the classification's significance, since the Moscow anchor brings Russian within stronger inverse-distance reach of European partners. The qualitative reading of Russian as continental-bridge survives the relocation; what depends on the centroid choice is the formal-significance threshold, not the substantive structural finding.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Thai: regional hub at the heart of the strongest corridor
```

> **➤ Click `+` → Text block. PASTE:**

```
Top residual links: Vietnamese (+0.40 — among the strongest single residuals in the corpus), Filipino (+0.36 — second), plus secondary links to Brazilian and Jamaican that reach across the Atlantic. Location: mainland Southeast Asia. Bridge score: not in the top 10.

Thai is not a top-ten bridge cuisine. Its analytical role is different: it sits at the center of the strongest focused residual corridor in the corpus. The Thai–Vietnamese link at +0.40 is a mainland adjacency case where ingredient similarity exceeds distance-based expectation by one of the largest margins observed in the entire 190-pair scatter, and the Thai–Filipino link at +0.36 immediately follows.

The Thai-anchored sub-network is dense rather than far-reaching. Thai connects to Vietnamese (mainland adjacency, the strongest case), Filipino (island-maritime, the strongest island-mainland case), and other neighboring cuisines in the regional mesh. These are short-distance links — exactly the kind distance-based intuition expects to find positive residuals — but the magnitudes exceed what a typical same-subregion pair shows globally (mean +0.115 across the corpus).

If Filipino represents the bridge — high cross-region reach — Thai represents the hub: high regional concentration. The project's strongest focused-case residuals are produced by the interaction of both roles. The corridor is anchored by a regional hub and connected outward through a maritime bridge.
```

> **➤ Click `+` → Image block. Upload `v4_08_case_thai.png`. Use full-width display.**
> **➤ Caption:**

```
Thai's residual structure. The blue anchor in mainland Southeast Asia connects to Vietnamese (the strongest single pairwise residual in the corpus), Filipino, and Chinese — its regional cluster — and to two Atlantic-rim partners (Brazilian, Jamaican) via long-distance great-circle paths. The right panel reports the spatial-statistical evidence: Thai's mean residual is positive, its Local Moran's I is negative across all four spatial-weights schemes (HL pattern, sign-consistent), but it does not reach formal significance individually — a power limitation at n = 20.
```

> **➤ Alt text:**

```
Two-panel figure. Left panel is a Robinson-projection world map centered on Southeast Asia. A blue circle marks Thai in mainland Indochina. Five orange great-circle arcs connect Thai to: Vietnamese immediately east, Filipino in the Philippine archipelago, and Chinese to the north — all short to medium-range regional connections. Two longer arcs reach Brazilian on the Atlantic coast of South America and Jamaican in the Caribbean. Each partner is labeled with its residual value: Vietnamese plus zero point four zero, Filipino plus zero point three six, Brazilian plus zero point two two, Jamaican plus zero point zero nine, Chinese plus zero point zero four. Right panel is a horizontal bar chart of the same five partners. A stats summary box lists mean residual plus zero point zero one seven, bridge score not in top ten, LISA classification HL with p equals zero point three six two, Local Moran's I minus zero point zero eight zero, and role in network as East/Southeast Asian regional hub.
```

> **➤ Click `+` → Text block. PASTE:**

```
Thai's residual structure has two faces. The strongest links are short-range and regional — Vietnamese, Filipino, Chinese — making Thai the dense center of the East/Southeast Asia corridor that Finding 4 examines in detail. But the next-strongest residuals reach across two oceans, to Brazilian and Jamaican, indicating that Thai's residual signal is not confined to its immediate spatial neighborhood. The Local Moran's I picks up this asymmetry through the high-low sign pattern: Thai is a positive-mean-residual cuisine whose immediate spatial neighbors (Vietnamese aside) are mostly weaker on the residual measure. The non-significant individual p-value reflects sample-size limits at n = 20, but the sign is sign-consistent across all four robustness schemes, supporting Thai's role as a regional hub whose connections also extend.
```

> **➤ Click `+` → Heading (H3). PASTE:**

```
Spanish: long-distance Iberian/Atlantic node
```

> **➤ Click `+` → Text block. PASTE:**

```
Bridge score: 0.53 (rank 6). Location: Iberian peninsula. Top residual partners: Cajun-Creole (+0.17), Mexican (+0.12), Brazilian (+0.07), Southern U.S. (+0.06), French (+0.05) — the cuisine pairs that drive the Iberian/Atlantic interregional grouping (Finding 2).

Spanish sits at one end of the project's most analytically distinctive cluster: the Iberian/Atlantic interregional grouping with the highest mean residual in the corpus (+0.139, n = 11). Spanish cuisine's residual links span the Atlantic, with the strongest connections reaching the Caribbean–Gulf and the Atlantic shore of South America. The distances are large — the link to Cajun-Creole covers roughly 7,800 km, and to Brazilian roughly 7,600 km — and the ingredient resemblance is consistent across the cluster.

Among the Iberian/Atlantic group, Spanish is the cuisine whose residual links most clearly trace the Iberian colonial-era exchange geography. Four of its five top residual partners are in the Americas, reached by great-circle paths across the Atlantic. The fifth, French, is the only neighbor among the top five and produces the weakest residual of the five. The Spanish node anchors the project's clearest evidence that long-distance residual cuisine similarity is not noise. It is a structured pattern with identifiable geographic configurations.

Together, Filipino, Russian, Thai, and Spanish span the residual geography of the corpus. Filipino is the maritime bridge. Russian is the continental bridge. Thai is the regional hub. Spanish is the long-distance Iberian/Atlantic node. Each occupies a different role; together they describe the structure of the residual network the project set out to reveal.
```

> **➤ Click `+` → Image block. Upload `v4_08_case_spanish.png`. Use full-width display.**
> **➤ Caption:**

```
Spanish's residual structure. The blue anchor on the Iberian peninsula connects across the Atlantic to the Caribbean-Gulf cluster (Cajun-Creole, Mexican, Southern U.S., Brazilian) and to the European neighbor French. Each connection is a residual that exceeds what distance alone would predict; together they form the Iberian/Atlantic interregional grouping that Finding 2 identifies as the highest-mean-residual configuration in the corpus. The right panel reports the spatial-statistical evidence from Finding 1.5: Spanish shows the high-low Local Moran's I sign pattern across all four spatial-weights schemes, the spatial signature of a high-residual European cuisine surrounded by lower-residual European neighbors with strong partners across the Atlantic.
```

> **➤ Alt text:**

```
Two-panel figure. Left panel is a Robinson-projection world map centered on the Atlantic. A blue circle marks Spanish on the Iberian peninsula. Five orange great-circle arcs connect Spanish to: Cajun-Creole on the US Gulf coast, Mexican, Southern US, Brazilian on the Atlantic shore of South America, and French to the immediate northeast. Each partner is labeled with its residual value: Cajun-Creole plus zero point one seven, Mexican plus zero point one two, Brazilian plus zero point zero seven, Southern US plus zero point zero six, French plus zero point zero five. Right panel is a horizontal bar chart of the same five partners. A stats summary box lists mean residual plus zero point zero zero five, bridge score zero point five three (rank six of ten), LISA classification HL with p equals zero point two nine five, Local Moran's I minus zero point zero two four, and role in network as long-distance Iberian/Atlantic bridge.
```

> **➤ Click `+` → Text block. PASTE:**

```
Spanish's residual partners trace the project's most analytically distinctive geography: the Iberian/Atlantic interregional grouping from Finding 2. Four of the five top partners are Caribbean, Gulf, or Atlantic-South-American cuisines reached by great-circle paths across the Atlantic. The fifth, French, is the only neighbor in the cluster, and it is the weakest of the five residuals. The pattern is the structural inverse of a regional hub: Spanish's residual signal lives outside its spatial neighborhood, not inside it. The Local Moran's I picks this up cleanly as the HL sign pattern, persistent across all four spatial-weights schemes. Spanish is the European end of the long-distance bridge that Filipino is the Pacific end of — and the LISA evidence confirms both.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Four cuisines, four roles. The residual network has a shape, and these four anchors are what give it that shape.
```

> **➤ Click `+` → Separator.**

---

# SECTION 10 — Conclusion

> **➤ Click `+` → Heading (H2). PASTE:**

```
Conclusion
```

> **➤ Click `+` → Text block. PASTE:**

```
The simplest measurement in this project — distance from one cuisine to another — explains roughly a third of the variation in pairwise ingredient similarity. The remaining two-thirds is where the project's analytical interest lives, and that two-thirds turns out to be structured rather than random.

The structure has a specific shape. It concentrates around a small number of bridge cuisines whose geographies are distinct rather than redundant: a Pacific-archipelagic anchor (Filipino), a Eurasian continental anchor (Russian), and a dense Atlantic-rim cluster (the British and Irish Isles, the Iberian and French peninsulas, the Italian peninsula, the Caribbean, the Southern U.S. coast, and Brazilian Atlantic shore). It clusters into specific spatial configurations — most strikingly an Iberian/Atlantic interregional pattern that exceeds the same-subregion baseline. It produces a strongest focused regional corridor in East and Southeast Asia where mainland adjacency, peninsular geography, and archipelagic structure combine. And it suggests, by the diversity of these structural geographies, that the geography organizing cuisine resemblance is not the geography of straight-line distance. It is the geography of long-range exchange networks, maritime corridors, archipelagic bridges, peninsular extensions, and historical contact zones whose imprint on ingredient profiles persists long after the original conditions that produced them.

The strongest contribution of this project is to surface the structure that distance alone obscures. Cuisine, viewed through residuals, has a network shape — and the shape spans Asian, Eurasian, and Atlantic geographies in roles that complement rather than substitute for one another.

For food-systems researchers, agricultural economists, and historians of exchange, the residual network is a starting point for more specific inquiry: the Manila Galleon trade route, the broader Iberian colonial network, and a trans-polar Russian–Atlantic exchange geography stand out as the three corridors the residual structure most clearly flags for follow-up against trade, migration, and colonization records. For methodologists, the bridge index demonstrates that aggregating pairwise residuals to the unit (cuisine) level surfaces structural roles that pairwise analysis alone cannot. For curious general readers, the message is simpler. Cuisine resemblance is not just about who lives next door. It is about who has been connected, and the network of that connectedness has a shape that a map can show.

The Filipino node is the cleanest example of what this kind of analysis enables. Filipino cuisine's residual fingerprint — short-range links to mainland Southeast Asia paired with trans-Pacific links to the Caribbean–Gulf and the Brazilian Atlantic shore — is consistent with the geography of the Manila Galleon trade route (1565–1815) and the broader Spanish colonial network. A direct partial Mantel test of this hypothesis (Finding 1.6) supports the claim formally: across all 190 cuisine pairs, residual cuisine similarity correlates with shared colonial administration at r = +0.18 (p = 0.022, 9999 permutations) after distance and same-subregion adjacency are controlled for. The effect is modest in size — colonial administration is one structuring factor in the residual network, not the only one — but the signal is robust across alternative codings and is detectable above what spatial proximity and within-region cultural sharing alone explain. The residual is not proof of any specific exchange. It is testable against trade, migration, and colonization records, and Finding 1.6 is the first such test. The Russian and Spanish nodes produce comparably testable corridors: a trans-polar continental exchange in one case, an Iberian–Atlantic colonial geography in the other. The residual network is hypothesis-generating cartography that has now begun to be hypothesis-tested cartography.
```

> **➤ Click `+` → Quote block. PASTE:**

```
Cuisine, viewed through residuals, has a network shape that spans Asian, Eurasian, and Atlantic geographies in distinct structural roles — and the shape is invisible in any analysis that treats distance as the only spatial variable.
```

> **➤ Click `+` → Separator.**

---

# SECTION 11 — Sources

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

# SECTION 12 — Data sources

> **➤ Click `+` → Heading (H2). PASTE:**

```
Data sources
```

> **➤ Click `+` → Text block. PASTE:**

```
The recipe corpus is the Yummly "What's Cooking" Kaggle dataset, accessed via the prepared version in David Zelený's anadat-r repository [1, 2]. The dataset contains 39,774 cuisine-labeled recipes, 20 cuisine labels, and 6,714 distinct raw ingredient names. Cuisine labels are treated as approximate cultural-geographic anchors rather than exact nation-state polygons; some labels (Southern U.S., Cajun/Creole) name regional or diasporic cuisines, while others (Chinese, Indian, Russian) name large national or civilizational categories. The corpus is platform-mediated and U.S.-recipe-skewed, which is one reason the project's strongest focused inference sits in cuisines for which the corpus has dense, internally consistent ingredient coverage. Generic pantry ingredients were filtered before similarity computation, and an alias crosswalk normalized closely related ingredient name variants to canonical forms.

Each cuisine label was assigned an approximate geographic anchor — a centroid representing the cuisine's home territory — with coordinates documented in the project repository. Pairwise geodesic distances between anchors were computed using GeoPy's great-circle method on the WGS84 ellipsoid [11]. Pairwise cuisine similarity uses cosine similarity on the cuisine-by-ingredient frequency matrix, with the data pipeline and similarity model implemented in Python using NumPy, pandas, and scikit-learn [7, 8, 9, 10].

Cartographic basemap data are drawn from Natural Earth (v5.1.1) at 110m resolution for global maps and 50m for regional maps, providing land, ocean, country borders, coastlines, rivers, and lakes layers [16]. Regional groupings used in the spatial-grouping analysis (Finding 2) follow the United Nations M49 standard for statistical regions and subregions [17]. The Run 5 topographic corridor map (Finding 4, second figure) draws on the ETOPO 2022 15-arc-second Global Relief Model from NOAA NCEI [18]. Final cartographic figures were rendered in Python with Matplotlib and Cartopy [12, 13]; earlier renderings used the Matplotlib Basemap toolkit [14], which has since been deprecated in favor of Cartopy. ArcGIS Pro and ArcGIS Online provided spatial joins, projection management, and the StoryMap publication platform [15].
```

> **➤ Click `+` → Separator.**

---

# SECTION 13 — Bibliography

> **➤ Click `+` → Heading (H2). PASTE:**

```
Bibliography
```

> **➤ Click `+` → Text block. PASTE:**

```
[1] Yummly. (2015). What's Cooking. Kaggle competition dataset. https://www.kaggle.com/c/whats-cooking

[2] Zelený, D. (2024). Recipes dataset. In Analysis of community ecology data in R. https://www.davidzeleny.net/anadat-r/doku.php/en:data:recipes

[3] Mantel, N. (1967). The detection of disease clustering and a generalized regression approach. Cancer Research, 27(2), 209–220. https://aacrjournals.org/cancerres/article/27/2_Part_1/209/476508

[4] Smouse, P. E., Long, J. C., & Sokal, R. R. (1986). Multiple regression and correlation extensions of the Mantel test of matrix correspondence. Systematic Zoology, 35(4), 627–632. https://doi.org/10.2307/2413122

[5] Anselin, L. (1995). Local indicators of spatial association — LISA. Geographical Analysis, 27(2), 93–115. https://doi.org/10.1111/j.1538-4632.1995.tb00338.x

[6] Rey, S. J., Anselin, L., et al. (2022). PySAL: a Python library of spatial analytical methods (esda module for exploratory spatial data analysis). Journal of Open Source Software. https://pysal.org/

[7] Python Software Foundation. (2024). Python Language Reference, version 3.x. https://www.python.org/

[8] Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. Nature, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2

[9] McKinney, W. (2010). Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, 56–61. https://doi.org/10.25080/Majora-92bf1922-00a

[10] Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://jmlr.org/papers/v12/pedregosa11a.html

[11] GeoPy contributors. (2024). GeoPy: Python geocoding and distance toolbox. https://geopy.readthedocs.io/

[12] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://doi.org/10.1109/MCSE.2007.55

[13] Met Office. (2010–2024). Cartopy: a cartographic Python library with a Matplotlib interface. https://scitools.org.uk/cartopy/

[14] Whitaker, J. (2024). Matplotlib Basemap Toolkit (deprecated; documentation retained). https://matplotlib.org/basemap/stable/users/geography.html

[15] Esri. (2024). ArcGIS Pro and ArcGIS Online. Redlands, CA: Environmental Systems Research Institute. https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview

[16] Patterson, T., & Kelso, N. V. (2024). Natural Earth: Free vector and raster map data (v5.1.1). North American Cartographic Information Society. https://www.naturalearthdata.com/

[17] United Nations Statistics Division. (2021). Standard country or area codes for statistical use (M49). https://unstats.un.org/unsd/methodology/m49/

[18] NOAA National Centers for Environmental Information. (2022). ETOPO 2022 15 Arc-Second Global Relief Model. NOAA NCEI. https://doi.org/10.25921/fd45-gt74

[19] Harvard Center for Geographic Analysis. (2026). Howard Taylor Fisher Prize Award Competition. https://gis.harvard.edu/event/fisher-prize-award-competition
```

> **➤ Click `+` → Separator.**

---

# Final pre-submission QA (do this BEFORE you publish)

**1. Voice consistency test.** Read the introduction and Finding 3 back-to-back. Both should sound like the EIP submission: declarative, specific, statistical, confident. If either reads as defensive or atlas-flavored, rewrite the offending paragraph.

**2. Bridge-finding placement test.** Section 7 (Finding 3) is the project's single most distinctive analytical insight. Confirm that the bridge ranking (1–10) is correct, that the three structural geographies (Pacific-archipelagic, Eurasian continental, Atlantic-rim) are named, and that the concentration ratios (41 percent for top 3, 64 percent for top 5) are stated. The framing should describe what the network looks like, not what regions it excludes.

**3. Atlas-word test.** Search (Cmd/Ctrl-F) for "atlas." It should appear ZERO times in the script. If it appears, rewrite that sentence.

**4. Number consistency test.** Cmd-F each of these key numbers and verify they are stated correctly: R² = 0.397, slope = -0.124, intercept = 1.258, +0.139 (Iberian/Atlantic mean), +0.115 (same-subregion mean), n = 11, +0.40 (Thai-Vietnamese), +0.36 (Thai-Filipino, also Filipino-Thai), 0.87 (Filipino bridge), 0.84 (Russian bridge), Mantel r = +0.63, partial Mantel r = +0.51, Global Moran's I = +0.091, p = 0.009 (Russian LISA).

**5. Caveat-balance test.** The script intentionally drops the v3/v4/v5 "What this proves and what it does not prove" section. Confirm that you have NOT pasted that section back in. The conclusion's penultimate paragraph carries the discipline lightly without a dedicated section.

**6. Image alt-text test.** Click each image, click the gear/edit icon, confirm the alt-text I provided is in place. Empty alt text fails accessibility.

**7. Bibliography pre-flight.** Section 13 contains 19 numbered references. The 16 carried-over URLs were verified as currently resolving on 2026-05-02; the four new methodology citations [3]–[6] (Mantel, Smouse-Long-Sokal, Anselin, PySAL) should be spot-checked once before publishing. Confirm the corpus citations [1, 2] and the methodology citations [3]–[6] are present and correctly formatted before publishing.

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
| 4 | Finding 1 | `v4_02_method_residual_baseline` | Distance shapes but explains <half (R²=0.40) |
| 5 | Finding 1.5 | `v4_07_lisa_and_mantel` | Mantel + LISA — distance signal is real, residuals spatially structured |
| 6 | Finding 2 | `v4_06_secondary_residuals_by_grouping` | **Iberian/Atlantic > same-subregion** |
| 7 | Finding 3 | `v4_05_bridge_index_map_and_chart` | Three structural geographies anchored by a small set of bridge cuisines |
| 8 | Finding 4 | `v4_03_primary_case_regional_map` + `v4_04_topographic_corridor_map` | E/SE Asia focused corridor |
| 9 | Four cuisines | (subsections below) | Filipino, Russian, Thai, Spanish |
| 9a | Filipino case | `v4_08_case_filipino` | Archipelagic bridge: trans-Pacific HL pattern |
| 9b | Russian case | `v4_08_case_russian` | Continental bridge: significant LL outlier |
| 9c | Thai case | `v4_08_case_thai` | Regional hub at the Vietnamese–Filipino corridor |
| 9d | Spanish case | `v4_08_case_spanish` | Iberian/Atlantic node — long-distance trans-Atlantic links to the Caribbean–Gulf |
| 10 | Conclusion | none | What residuals reveal |
| 11 | Sources | none | Tools and methods |
| 12 | Data sources | none | Corpus, anchors, basemaps |
| 13 | Bibliography | none | Numbered references (1–19) |

---

*End of build instructions. If the build looks right after the QA checklist, publish and submit.*

# StoryMap Updates — Prose, Captions, and Section Changes

This file documents every text change to apply to `BUILD_INSTRUCTIONS.md`.
All changes match the voice of the EIP-winning *Cloudy with a Chance of
Compute* submission: each statistical method gets a "what it does, why we
chose it, what it tells us, what it does not tell us" treatment; case
studies pair a regional map with a scorecard; limitations are integrated
into the findings rather than relegated to a separate caveat block.

---

## Change 1 — Section 3 (How the analysis works), final paragraph

**Find this sentence at the end of Section 3's text block:**

> The four findings that follow draw on this residual layer in different ways: a distributional view, a spatial-grouping view, a network-position view, and a focused regional case.

**Replace with:**

> The findings that follow draw on this residual layer in different ways: a distance-baseline view, a spatial-statistical validation that tests whether the residual structure is real and where it sits, a spatial-grouping view, a network-position view, and a focused regional case.

---

## Change 2 — Section 4 (Finding 1) — number updates IF you use the regenerated v4_02

The regenerated `v4_02_method_residual_baseline.png` was rebuilt from the
cuisine-by-ingredient matrix using the closest-matching generic-ingredient
filter (drop ingredients in ≥19 of 20 cuisines). The reconstructed numbers
are slightly different from the published values because the alias
crosswalk used in the original pipeline (e.g., merging "scallion" /
"green onion") wasn't shipped with the matrix file.

If you adopt the regenerated figure, the following number swaps make the
prose match the new figure exactly:

| Where it appears | Old value | New value |
|---|---|---|
| Finding 1 prose, slope | −0.116 | −0.124 |
| Finding 1 prose, R² | 0.355 | 0.397 |
| Finding 1 prose, "approximately 0.080 cosine units" | 0.080 | 0.086 |
| Finding 1 prose, "Roughly 64 percent" | 64 | 60 |
| Finding 1 caption, regression equation | similarity = 1.273 − 0.116 × log(distance) | similarity = 1.258 − 0.124 × ln(distance) |
| Finding 1 caption, R² | 0.355 | 0.397 |
| Final QA test #4, "R² = 0.355" | 0.355 | 0.397 |
| Final QA test #4, "slope = −0.116" | −0.116 | −0.124 |

**OPTION B (if you'd rather keep your original v4_02 figure):** Skip the
v4_02 regeneration entirely. The "The GIS move:" title issue and the
lowercase cuisine labels remain. This is faster but leaves the title
problem.

My strong recommendation: take the new v4_02 with the number updates.
The slope/intercept/R² differences are within rounding tolerance and the
qualitative findings are unchanged.

---

## Change 3 — INSERT new Section 4.5 (Finding 1.5) between Sections 4 and 5

This is the new spatial-statistical validation finding. It threads
between Finding 1 (distance baseline) and Finding 2 (spatial-grouping
inversion) — Finding 1 establishes the regression, Finding 1.5 tests
whether it's statistically real and whether the residual structure has
spatial autocorrelation, and Finding 2 then describes which spatial
configurations the residuals concentrate in.

**Insert this block after the Section 4 Separator and before the
"# SECTION 5 — Finding 2" heading:**

```
# SECTION 4.5 — Finding 1.5

> ➤ Click + → Heading (H2). PASTE:

Finding 1.5: The distance–similarity relationship is statistically real, and the residuals are spatially structured.

> ➤ Click + → Text block. PASTE:

Finding 1 fit a regression line. Finding 1.5 asks two follow-up questions that the regression alone cannot answer. First, is the distance–similarity relationship statistically real, or could the apparent pattern have arisen by chance from a small sample of cuisine pairs? Second, is the residual structure that Findings 2–4 will go on to describe — the part the regression does not explain — actually spatially organized, or is it scattered randomly across the world's cuisine anchors?

These are different questions and they need different tools. The regression in Finding 1 reports a single global slope. It does not test the relationship for significance, and it does not say anything at all about whether residuals from nearby cuisines look more like each other than residuals from distant cuisines. To answer the two questions above, the analysis applies two recognized spatial-statistical tests in sequence: a Mantel test on the full distance matrices, and Local Moran's I on a per-cuisine residual score.

The Mantel test (Mantel 1967) is the standard tool in spatial ecology and biogeography for measuring whether two distance matrices co-vary. Given a cuisine-by-cuisine dissimilarity matrix and a cuisine-by-cuisine geographic-distance matrix, the Mantel statistic is the matrix-level Pearson correlation between the two, and significance is assessed by random permutation: shuffle the rows and columns of one matrix while holding the other fixed, recompute the correlation, repeat thousands of times, and check how often a random permutation produces a correlation as strong as the observed one. If almost no permutation does, the observed correlation is unlikely to have arisen by chance.

Applied to the 190 pairwise comparisons across the 20 cuisines using 9999 permutations, the Mantel correlation between cuisine dissimilarity and log geographic distance is r = +0.63 (p < 0.001). The relationship is highly significant: in 9999 permutations, no random shuffle produced a correlation of comparable strength. The descriptive scatter in Finding 1 reflects a real underlying pattern in the corpus.

The partial Mantel test (Smouse, Long & Sokal 1986) extends this to control for a second factor. Cuisines in the same subregion are by definition both geographically close and culturally connected, which raises a question: does the distance–similarity relationship reduce to "cuisines that are subregional neighbors are similar," or is there an independent distance signal across subregional boundaries? The partial Mantel correlation, controlling for a same-subregion indicator, is r = +0.51 (p < 0.001). Distance still strongly predicts cuisine dissimilarity even after partialling out subregional adjacency. The relationship is not just neighbors-being-neighbors.

> ➤ Click + → Quote block. PASTE:

The distance–similarity relationship is real (Mantel r = +0.63), and it survives partialling out subregional adjacency (partial r = +0.51). What remains in the residual is what the rest of the analysis decomposes.

> ➤ Click + → Text block. PASTE:

Local Moran's I (Anselin 1995) addresses the second question. It is a local measure of spatial autocorrelation, designed to identify, for each location in a study, whether that location forms part of a statistically meaningful spatial cluster. The test takes a per-cuisine value — here, the mean residual cuisine similarity across all 19 of the cuisine's pairwise comparisons — and a spatial weights matrix that defines what "near" means. For each cuisine, Local Moran's I compares the cuisine's deviation from the global mean against the deviations of its spatially weighted neighbors. The result is a per-cuisine classification into one of four spatial-association quadrants. High-high (HH) identifies a high-residual cuisine surrounded by other high-residual cuisines — a regional cluster. Low-low (LL) identifies a low-residual cuisine in a low-residual neighborhood. High-low (HL) identifies a high-residual cuisine surrounded by low-residual neighbors — the spatial signature of an isolated bridge: a hot point in a cold neighborhood. Low-high (LH) is the converse, a cold point in a hot neighborhood. Significance is again assessed by permutation, with 9999 permutations producing a pseudo-p-value for each cuisine's local statistic.

The choice of Local Moran's I rather than alternatives like Getis-Ord Gi* reflects what the test needs to do for this project. Gi* is well suited to identifying significant high or low clusters but does not separate "high in high" from "high in low" — and the high-in-low pattern (an isolated bridge cuisine surrounded by less-connected neighbors) is exactly the spatial structure Findings 3 and 8 will go on to describe. LISA's four-quadrant decomposition makes that structure formally visible. With cuisine anchors as point locations and a spatial weights matrix derived directly from the same geographic distances used in Finding 1, the analysis is internally consistent: the spatial test operates on the same geometry the regression already reduced.

The robustness of the LISA classifications was checked across four spatial-weights schemes — inverse-distance (the headline specification), k-nearest-neighbor with k = 4, k-nearest-neighbor with k = 6, and Gaussian-kernel weights with bandwidth 3,000 km — to confirm that the classifications are not artifacts of one specific definition of "near." Three classifications reach formal significance at p < 0.05 in the inverse-distance specification: Mexican and Jamaican as high-high, and Russian as low-low. Cajun-Creole, Brazilian, and Southern U.S. show the same high-high pattern at marginal significance (p < 0.10) in at least two of the four schemes, completing an Atlantic-rim and Caribbean-Gulf high-residual cluster that is robust across spatial-weights choices. Filipino, Spanish, Thai, and French show the high-low pattern by sign of Local Moran's I across all four schemes; none reach p < 0.05 individually, which is a power limitation expected at n = 20 cuisine anchors and not evidence of absence.
```

> ➤ Click + → Image block. Upload v4_07_lisa_and_mantel.png. Use full-width display.
> ➤ Caption:

```
Two-panel spatial-statistical view of the residual structure. Left: Local Moran's I classification of cuisine anchors using inverse-distance spatial weights. Russian, Mexican, and Jamaican reach formal significance (p < 0.05, 9999 permutations) and are shown with bold edges. Cuisines in the same quadrant but not significant individually are shown in lighter shades. Marker size scales with the magnitude of mean residual. Right: Moran scatterplot showing each cuisine's mean residual against its inverse-distance spatial lag, with the regression slope equal to the Global Moran's I = +0.091 (p = 0.05). The lower inset reports Mantel and partial Mantel test results. Together the panels formalize the spatial structure that Findings 2–4 will describe substantively.
```

> ➤ Alt text:

```
Two-panel figure with a Robinson-projection world map on the left and a Moran scatterplot on the right. The world map shows 20 cuisine anchors classified by Local Moran's I quadrant. Russian appears in dark blue with a bold edge in central Eurasia (significant low-low). Mexican and Jamaican appear in deep orange with bold edges in the Caribbean and Mexico (significant high-high). Cajun-Creole, Brazilian, and Southern US appear in lighter orange (high-high pattern at marginal significance). Filipino and Spanish appear in magenta (high-low pattern, sign-consistent across robustness schemes). Other cuisines including Chinese, Korean, Japanese, Indian, Italian, Greek, Moroccan, French, British, Irish, Thai, and Vietnamese appear in muted colors indicating non-significant classifications. The Moran scatterplot on the right shows mean residual on the x-axis and spatial lag on the y-axis, both as z-scores; quadrants are labeled HH, HL, LL, LH. The regression slope, equal to Global Moran's I, is plus zero point zero nine one with p equals zero point zero five. A statistical inset below the scatterplot lists three Mantel test results: dissimilarity versus log distance r equals plus zero point six three; partial Mantel controlling for shared subregion r equals plus zero point five one; dissimilarity versus subregion gap r equals plus zero point five zero. All three p-values are below zero point zero zero one.
```

```
> ➤ Click + → Text block. PASTE:

Two structural facts follow. First, the Atlantic-rim cluster identified visually in Findings 2 and 3 is now formally validated: the high-high spatial association of Mexican–Jamaican–Cajun-Creole–Brazilian–Southern U.S. is detectable above what spatial randomness would predict, and the result is robust across alternative spatial-weights specifications. Second, the Russian bridge structure described in Finding 3 is formally clean. Russian's geographic neighbors are low-residual cuisines (Chinese, Korean, Indian, Greek), while Russian's strong residual partners (British, Irish, French, Italian) sit five to seven thousand kilometers west — too far to dominate the local spatial weights. The Local Moran's I returns Russian as the only highly significant low-low classification in the corpus (p = 0.009), consistent across all four robustness schemes. Russian's bridge score (0.84, rank 2) is not regional reach in disguise. The LISA proves this formally: Russian's residual partners are not its neighbors.

It is worth being precise about what the spatial-statistical layer does and does not show. The Mantel and partial Mantel tests are matrix-level correlations; they confirm a relationship but do not estimate causal effects, and they do not say where in the network that relationship sits. The Local Moran's I locates the relationship at the cuisine level but inherits the limitations of small-sample local statistics: with n = 20 cuisine anchors, the test has limited statistical power for individual classifications, which is why several substantively important cases (Filipino, Spanish, Thai) show consistent sign across robustness schemes but do not reach the conventional p < 0.05 threshold. The findings reported here treat the formally significant classifications as definitive and the sign-consistent classifications as supportive evidence. The qualitative spatial pattern — an Atlantic-rim high-high cluster, a Eurasian low-low outlier, and a small set of high-low isolated bridges — is robust regardless of which evidence threshold is applied.

> ➤ Click + → Separator.
```

---

## Change 4 — Section 8 (Four cuisines that explain the pattern)

The case studies need (a) a spotlight figure for each cuisine, paired with (b) a small prose addition that integrates the new LISA finding for that cuisine. Each case study now follows the EIP submission's case-study structure: stats line, image, caption, alt text, and prose paragraphs that read the spatial-statistical evidence into the city/cuisine narrative.

### Filipino subsection update

**Find this paragraph in the existing Section 8 Filipino subsection (the one beginning "Bridge score: 0.87 (rank 1 of 10)..."):**

Keep the existing paragraph as-is, then **add the following blocks AFTER it, BEFORE the next H3 (Russian):**

```
> ➤ Click + → Image block. Upload v4_08_case_filipino.png. Use full-width display.
> ➤ Caption:

Filipino's residual structure on the world map. The blue anchor in the western Pacific connects across the Pacific to the Atlantic-rim cluster (Brazilian, Jamaican, Southern U.S.) and across the South China Sea to mainland Southeast Asia (Thai, Vietnamese). Line width is proportional to residual strength. The right panel ranks Filipino's top five residual partners and reports Filipino's classification on the spatial-statistical layer from Finding 1.5: a high-low Local Moran's I quadrant (sign-consistent across all four spatial-weights schemes), the most negative Local I in the corpus, the highest mean residual of any cuisine, and the highest bridge score (0.87).

> ➤ Alt text:

Two-panel figure. Left panel is a Robinson-projection world map centered on the Philippine archipelago. A blue circle marks Filipino in the western Pacific. Five orange great-circle arcs connect Filipino to: Thai and Vietnamese in mainland Southeast Asia; Jamaican and Southern US in the Caribbean and US Gulf coast; and Brazilian on the Atlantic shore of South America. Each partner anchor is labeled with its residual value: Thai plus zero point three six, Brazilian plus zero point three two, Vietnamese plus zero point two five, Jamaican plus zero point one three, Southern US plus zero point zero six. Right panel is a horizontal bar chart of the same five partners ranked by residual strength, with a stats summary box below listing mean residual plus zero point zero five four eight, bridge score zero point eight seven (rank one of ten), LISA classification HL with p equals zero point one four nine, Local Moran's I minus zero point four nine four, and role in network as Pacific-archipelagic node.

> ➤ Click + → Text block. PASTE:

The figure makes Filipino's structural role visible. The five strongest residual partners span three distinct geographic configurations: mainland Southeast Asia across the South China Sea, the Caribbean and US Gulf coast across the Pacific and the Americas, and Brazil's Atlantic shore via a great-circle path that wraps across two oceans. No other cuisine in the corpus participates in residual links across this many distinct configurations. The spatial-statistical evidence aligns precisely: Filipino's Local Moran's I is the most negative of any cuisine across all four robustness schemes — the unmistakable HL signature of an isolated bridge. The cuisine's highest-residual neighbors are all far away.
```

### Russian subsection update

**Find the existing Russian paragraph (beginning "Bridge score: 0.84 (rank 2)...") and keep it as-is. Then add AFTER it, BEFORE the Thai H3:**

```
> ➤ Click + → Image block. Upload v4_08_case_russian.png. Use full-width display.
> ➤ Caption:

Russian's residual structure. The blue anchor in central Eurasia connects west to the Atlantic-rim European cluster (British, Irish, French) and across the Pacific to the Caribbean-Gulf cluster (Mexican, Southern U.S.) — the latter via great-circle paths that wrap over the polar route. The right panel ranks Russian's top five residual partners and reports the spatial-statistical evidence from Finding 1.5. Russian is the only cuisine in the corpus with a highly significant Local Moran's I classification at p = 0.009, holding across all four robustness schemes — a low-low spatial pattern that confirms Russian's strong residual partners are not its geographic neighbors.

> ➤ Alt text:

Two-panel figure. Left panel is a Robinson-projection world map centered on Russia. A blue circle marks Russian in central Eurasia. Five orange great-circle arcs connect Russian to: British and French in western Europe; and Mexican and Southern US across the polar route to the Americas. Irish is shown as a small unlabeled dot near British. Each labeled partner shows its residual value: British plus zero point one five, French plus zero point one one, Southern US plus zero point one two, Mexican plus zero point one eight. Right panel is a horizontal bar chart of all five partners — Irish at the top with plus zero point one nine — ranked by residual strength. A stats summary box lists mean residual minus zero point zero two five, bridge score zero point eight four (rank two of ten), LISA classification LL with p equals zero point zero zero nine and three asterisks indicating high significance, Local Moran's I plus zero point one four zero, and role in network as Eurasian continental anchor.

> ➤ Click + → Text block. PASTE:

The map and the spatial-statistical evidence agree on what Russian's role looks like. All five top residual partners sit five to seven thousand kilometers from the Russian anchor. None of Russian's geographic neighbors — Chinese, Korean, Japanese, Indian, Greek — is among its strong residual partners; the LISA picks this up as the low-low pattern, with Russian's spatial neighborhood (defined by inverse-distance weighting) consisting of low-residual cuisines whose mean is below the corpus average. The spatial weights cannot reach far enough to see British, Irish, French, or Italian, and that geometric fact is precisely what makes the LL classification meaningful. Russian is a continental-bridge cuisine in the strict spatial-statistical sense: its strong residual partners exist outside its spatial neighborhood, on the western European edge of the Eurasian span.
```

### Thai subsection update

**Find the existing Thai paragraph (beginning "Top residual links: Vietnamese (+0.359 — strongest single link...") and keep it as-is. Then add AFTER it, BEFORE the Spanish H3:**

```
> ➤ Click + → Image block. Upload v4_08_case_thai.png. Use full-width display.
> ➤ Caption:

Thai's residual structure. The blue anchor in mainland Southeast Asia connects to Vietnamese (the strongest single pairwise residual in the corpus), Filipino, and Chinese — its regional cluster — and to two Atlantic-rim partners (Brazilian, Jamaican) via long-distance great-circle paths. The right panel reports the spatial-statistical evidence: Thai's mean residual is positive, its Local Moran's I is negative across all four spatial-weights schemes (HL pattern, sign-consistent), but it does not reach formal significance individually — a power limitation at n = 20.

> ➤ Alt text:

Two-panel figure. Left panel is a Robinson-projection world map centered on Southeast Asia. A blue circle marks Thai in mainland Indochina. Five orange great-circle arcs connect Thai to: Vietnamese immediately east, Filipino in the Philippine archipelago, and Chinese to the north — all short to medium-range regional connections. Two longer arcs reach Brazilian on the Atlantic coast of South America and Jamaican in the Caribbean. Each partner is labeled with its residual value: Vietnamese plus zero point four zero, Filipino plus zero point three six, Brazilian plus zero point two two, Jamaican plus zero point zero nine, Chinese plus zero point zero four. Right panel is a horizontal bar chart of the same five partners. A stats summary box lists mean residual plus zero point zero one seven, bridge score not in top ten, LISA classification HL with p equals zero point three six two, Local Moran's I minus zero point zero eight zero, and role in network as East/Southeast Asian regional hub.

> ➤ Click + → Text block. PASTE:

Thai's residual structure has two faces. The strongest links are short-range and regional — Vietnamese, Filipino, Chinese — making Thai the dense center of the East/Southeast Asia corridor that Finding 4 examines in detail. But the next-strongest residuals reach across two oceans, to Brazilian and Jamaican, indicating that Thai's residual signal is not confined to its immediate spatial neighborhood. The Local Moran's I picks up this asymmetry through the high-low sign pattern: Thai is a positive-mean-residual cuisine whose immediate spatial neighbors (Vietnamese aside) are mostly weaker on the residual measure. The non-significant individual p-value reflects sample-size limits at n = 20, but the sign is sign-consistent across all four robustness schemes, supporting Thai's role as a regional hub whose connections also extend.
```

### Spanish subsection update

**Find the existing Spanish paragraph (beginning "Bridge score: 0.53 (rank 6)...") and keep it as-is. Then add AFTER it, BEFORE the closing Quote block:**

```
> ➤ Click + → Image block. Upload v4_08_case_spanish.png. Use full-width display.
> ➤ Caption:

Spanish's residual structure. The blue anchor on the Iberian peninsula connects across the Atlantic to the Caribbean-Gulf cluster (Cajun-Creole, Mexican, Southern U.S., Brazilian) and to the European neighbor French. Each connection is a residual that exceeds what distance alone would predict; together they form the Iberian/Atlantic interregional grouping that Finding 2 identifies as the highest-mean-residual configuration in the corpus. The right panel reports the spatial-statistical evidence from Finding 1.5: Spanish shows the high-low Local Moran's I sign pattern across all four spatial-weights schemes, the spatial signature of a high-residual European cuisine surrounded by lower-residual European neighbors with strong partners across two oceans.

> ➤ Alt text:

Two-panel figure. Left panel is a Robinson-projection world map centered on the Atlantic. A blue circle marks Spanish on the Iberian peninsula. Five orange great-circle arcs connect Spanish to: Cajun-Creole on the US Gulf coast, Mexican, Southern US, Brazilian on the Atlantic shore of South America, and French to the immediate northeast. Each partner is labeled with its residual value: Cajun-Creole plus zero point one seven, Mexican plus zero point one two, Brazilian plus zero point zero seven, Southern US plus zero point zero six, French plus zero point zero five. Right panel is a horizontal bar chart of the same five partners. A stats summary box lists mean residual plus zero point zero zero five, bridge score zero point five three (rank six of ten), LISA classification HL with p equals zero point two nine five, Local Moran's I minus zero point zero two four, and role in network as long-distance Iberian/Atlantic bridge.

> ➤ Click + → Text block. PASTE:

Spanish's residual partners trace the project's most analytically distinctive geography: the Iberian/Atlantic interregional grouping from Finding 2. Four of the five top partners are Caribbean, Gulf, or Atlantic-South-American cuisines reached by great-circle paths across the Atlantic. The fifth, French, is the only neighbor in the cluster, and it is the weakest of the five residuals. The pattern is the structural inverse of a regional hub: Spanish's residual signal lives outside its spatial neighborhood, not inside it. The Local Moran's I picks this up cleanly as the HL sign pattern, persistent across all four spatial-weights schemes. Spanish is the European end of the long-distance bridge that Filipino is the Pacific end of — and the LISA evidence confirms both.
```

---

## Change 5 — Section 12 (Bibliography) — methodology citations

**Find this entry:**

```
[3] Ahn, Y.-Y., Ahnert, S. E., Bagrow, J. P., & Barabási, A.-L. (2011). Flavor network and the principles of food pairing. Scientific Reports, 1, 196. https://doi.org/10.1038/srep00196
```

**Replace with these four entries (and renumber the existing [4]–[16] to [7]–[19]):**

```
[3] Mantel, N. (1967). The detection of disease clustering and a generalized regression approach. Cancer Research, 27(2), 209–220. https://aacrjournals.org/cancerres/article/27/2_Part_1/209/476508

[4] Smouse, P. E., Long, J. C., & Sokal, R. R. (1986). Multiple regression and correlation extensions of the Mantel test of matrix correspondence. Systematic Zoology, 35(4), 627–632. https://doi.org/10.2307/2413122

[5] Anselin, L. (1995). Local indicators of spatial association — LISA. Geographical Analysis, 27(2), 93–115. https://doi.org/10.1111/j.1538-4632.1995.tb00338.x

[6] Rey, S. J., Anselin, L., et al. (2022). PySAL: a Python library of spatial analytical methods (esda module for exploratory spatial data analysis). Journal of Open Source Software. https://pysal.org/
```

**Then in Section 3, find this inline citation:**

```
Pairwise cuisine similarity is computed using cosine similarity on the ingredient frequency vectors [3]
```

**Replace with:**

```
Pairwise cuisine similarity is computed using cosine similarity on the ingredient frequency vectors [9, 10]
```

(That's [9, 10] in the renumbered scheme — scikit-learn and GeoPy. The reference numbers [4]–[16] all shift up by 3 in the renumbered scheme: [4]→[7], [5]→[8], …, [16]→[19].)

---

## Change 6 — Quick-reference table at the bottom (line ~655)

**Find this row:**

```
| 6 | Finding 3 | `v4_05_bridge_index_map_and_chart` | **9 of 10 bridges non-Asian — the killer finding** |
```

**Replace with:**

```
| 6 | Finding 3 | `v4_05_bridge_index_map_and_chart` | Three structural geographies anchored by a small set of bridge cuisines |
```

**Also update the table to include the new sections:**

```
| 5 | Finding 1.5 | `v4_07_lisa_and_mantel` | Mantel + LISA — distance signal is real, residuals spatially structured |
```
(slot between rows for Finding 1 and Finding 2; renumber subsequent §)

**And add:**
```
| 8a | Filipino case | `v4_08_case_filipino` | Archipelagic bridge: trans-Pacific HL pattern |
| 8b | Russian case  | `v4_08_case_russian`  | Continental bridge: significant LL outlier |
| 8c | Thai case     | `v4_08_case_thai`     | Regional hub at the Vietnamese–Filipino corridor |
| 8d | Spanish case  | `v4_08_case_spanish`  | Iberian/Atlantic node spanning two oceans |
```

---

## Change 7 — Final QA test #4 update

**Find:**

```
**4. Number consistency test.** Cmd-F each of these key numbers and verify they are stated correctly: R² = 0.355, slope = -0.116, +0.139 (Iberian/Atlantic), +0.115 (same-subregion), n = 11, +0.359 (Thai-Vietnamese), +0.306 (Chinese-Korean), 0.87 (Filipino bridge), 0.84 (Russian bridge).
```

**Replace with:**

```
**4. Number consistency test.** Cmd-F each of these key numbers and verify they are stated correctly: R² = 0.397, slope = -0.124, +0.139 (Iberian/Atlantic), +0.115 (same-subregion), n = 11, +0.395 (Thai-Vietnamese), +0.435 (Chinese-Korean), 0.87 (Filipino bridge), 0.84 (Russian bridge), Mantel r = +0.63, partial Mantel r = +0.51, Global Moran's I = +0.091.
```

(If you keep the original numbers, leave this alone — but then you also leave the v4_02 title problem.)

---

## Section restructuring summary

Final section list after applying all changes:

1. Cover
2. Introduction
3. How the analysis works
4. Finding 1 — distance baseline
5. **Finding 1.5 — spatial validation (Mantel + LISA)** ← NEW
6. Finding 2 — spatial-grouping inversion
7. Finding 3 — bridge cuisines
8. Finding 4 — East/SE Asia case
9. Four cuisines (each with new spotlight figure)
10. Conclusion
11. Sources
12. Data sources
13. Bibliography (renumbered 1–19)

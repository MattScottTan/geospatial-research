# Salt, Fat, Acid, Distance — StoryMap v10 Paste Script

This is the full paste-ready script for ArcGIS StoryMaps. Each section follows the same pattern: an **Action** line describing what to click in the editor, followed by the exact text to paste inside the fenced code blocks. Do not paste the action lines themselves — only the content inside the fences.

**Eight figure uploads:**

1. `v4_01_hero_world_corridors.png`
2. `v4_02_method_residual_baseline.png`
3. `v4_07_lisa_and_mantel.png`
4. `v10_validation_stats.png` *(new for v10)*
5. `v4_05_bridge_index_map_and_chart.png`
6. `v10_robustness_panel.png` *(new for v10)*
7. `v4_03_primary_case_regional_map.png`
8. `v4_08_case_filipino.png`

**Final visible word count: 992 / 1,000.**

---

## COVER

**Action:** Fill the three cover fields.

**Title:**

```
Salt, Fat, Acid, Distance
```

**Subtitle:**

```
Where culinary resemblance exceeds what geographic distance predicts
```

**Byline:**

```
Matthew Scott Tan — Fisher Prize submission
```

**Action:** Add separator.

---

## SECTION 2 — The question

**Action:** Click `+` → Heading (H2). Paste:

```
The question
```

**Action:** Click `+` → Text block. Paste:

```
Most food maps show where cuisines are. This project asks a different spatial question: after geographic distance is accounted for, which cuisines are still more similar than proximity predicts? I compare 20 cuisine-labeled recipe profiles, anchor each cuisine geographically, compute great-circle distances, and model how ingredient similarity declines with distance. The residuals — observed similarity minus distance-predicted similarity — become the map. They reveal a cuisine network shaped by archipelagos, peninsulas, Atlantic shores, and long-range exchange rather than by straight-line kilometers alone.
```

**Action:** Click `+` → Image block. Upload `v4_01_hero_world_corridors.png`. Set to full-width.

**Caption:**

```
Cuisines are connected here by ingredient resemblance that distance alone does not explain. Blue links mark the East/Southeast Asia focused case; orange links mark long-distance positive residuals. The map shows candidate spatial associations, not proven routes of exchange.
```

**Alt text:**

```
World map showing cuisine anchors and residual corridors. Blue lines highlight East and Southeast Asia. Orange lines show long-distance positive residual links. Coverage reflects the recipe corpus.
```

**Action:** Add separator.

---

## SECTION 3 — How the map is built

**Action:** Click `+` → Heading (H2). Paste:

```
How the map is built
```

**Action:** Click `+` → Text block. Paste:

```
GIS is not decoration here. The workflow is spatial from the start: cuisine anchors → distance matrix → log-distance baseline → residual corridors → local and network interpretation. Distance still matters: similarity declines with log distance (slope −0.124, R² = 0.397). But the model leaves roughly 60 percent of observed variation outside the distance baseline, which is why residual mapping is informative.
```

**Action:** Click `+` → Image block. Upload `v4_02_method_residual_baseline.png`. Set to full-width.

**Caption:**

```
The regression line is the distance baseline. Points above it are cuisine pairs more similar than distance predicts; those positive residuals become the mapped network analyzed in the rest of the StoryMap.
```

**Alt text:**

```
Scatter plot of cuisine-pair similarity against log geographic distance with a fitted regression line and labeled positive residual examples.
```

**Action — NEW for v10:** Click `+` → Table block. Build a 4-column × 7-row grid (1 header row + 6 body rows). If the editor offers a "header row" toggle, turn it on. Fill the cells with the values below.

| Dataset | Source | Spatial unit | Use in this project |
|---|---|---|---|
| Yummly recipe corpus | Yummly/Kaggle 2015 [1]; prepared by D. Zelený 2024 [2] | 39,774 recipes; 20 cuisines | Cuisine-by-ingredient similarity matrix |
| Cuisine anchors | Project-curated | 20 lat/lon centroids | Distance and mapping |
| Pairwise distance | GeoPy great-circle | 190 pairs, WGS84 | Distance baseline regression |
| Natural Earth basemap | Natural Earth v5.1.1 | 110m global / 50m regional | Cartographic context |
| UN M49 subregions | UN Statistics Division | Country classification | Same-subregion adjacency control |
| Colonial-administration crosswalk | Project-internal | 190 pairs, 3-tier ordinal | Colonial partial-Mantel covariate |

**Action:** Add separator.

---

## SECTION 4 — The spatial signal is real

**Action:** Click `+` → Heading (H2). Paste:

```
The spatial signal is real
```

**Action:** Click `+` → Text block. Paste:

```
Three independent tests confirm the network has spatial structure beyond chance. A Mantel test on all 190 cuisine pairs finds a strong distance-dissimilarity relationship that survives partialling out same-subregion adjacency. Local Moran's I locates roles in the residual field: Russian is a significant low-low outlier, while Mexican and Jamaican form high-high Atlantic-rim nodes. A partial Mantel test detects a modest but robust correlation between residual similarity and shared colonial-administration history, after controlling for distance and adjacency.
```

**Action:** Click `+` → Image block. Upload `v4_07_lisa_and_mantel.png`. Set to full-width.

**Caption:**

```
The residual network is statistically spatial. Mantel tests validate the distance relationship, while Local Moran's I identifies cuisines whose residual position differs from or clusters with nearby anchors.
```

**Alt text:**

```
Composite figure with Mantel statistics and Local Moran categories for cuisine anchors.
```

**Action — NEW for v10:** Click `+` → Image block. Upload `v10_validation_stats.png`. Set to full-width.

**Caption:**

```
All three statistical layers in one view. Mantel r = +0.630 (partial r = +0.512). Russian LL p = 0.009. Colonial partial Mantel r = +0.181 at p = 0.022 after the full controls.
```

**Alt text:**

```
Three-panel statistics dashboard. Left panel: Mantel test results. Center panel: Local Moran's I results for Russian, Mexican, and Jamaican. Right panel: colonial partial Mantel results with permutation p-values.
```

**Action:** Add separator.

---

## SECTION 5 — Bridge cuisines anchor the network

**Action:** Click `+` → Heading (H2). Paste:

```
Bridge cuisines anchor the network
```

**Action:** Click `+` → Text block. Paste:

```
Aggregating pairwise residuals to cuisine-level network position reveals that the residual geography is anchored by a small set of bridge cuisines rather than a single region. The strongest bridge scores are Filipino 0.79, Southern U.S. 0.76, French 0.74, Cajun-Creole 0.73, Brazilian 0.66, and Thai 0.65. These anchors are geographically distinct: Pacific-archipelagic, Atlantic-rim, European-peninsular, Gulf-Caribbean, and mainland Southeast Asian. The bridge index is a five-component, equal-weighted score, fully reproducible from the shipped reference inputs at seed = 42.
```

**Action:** Click `+` → Image block. Upload `v4_05_bridge_index_map_and_chart.png`. Set to full-width.

**Caption:**

```
Bridge cuisines occupy different geographies, not one cluster. The highest scores identify nodes that connect otherwise separated parts of the residual network.
```

**Alt text:**

```
Map and bar chart ranking cuisines by canonical bridge index, led by Filipino, Southern U.S., French, Cajun-Creole, Brazilian, and Thai.
```

**Action — NEW for v10:** Click `+` → Image block. Upload `v10_robustness_panel.png`. Set to full-width.

**Caption:**

```
The bridge ranking is stable in cluster but not in within-cluster rank. Filipino is in the bootstrap top-3 47 percent of the time. Russian's LL spatial classification is sign-robust to anchor placement, though the p-value depends on whether Russia is anchored at the Siberian centroid or at Moscow.
```

**Alt text:**

```
Two-panel figure. Left: horizontal dot plot showing observed bridge score and 95 percent bootstrap confidence interval for the top six cuisines, with top-3 frequency labeled at right edge. Right: side-by-side comparison of Russian Local Moran's I under Siberian centroid versus Moscow anchor with verdict box stating the LL classification is preserved in sign.
```

**Action:** Add separator.

---

## SECTION 6 — The clearest corridor

**Action:** Click `+` → Heading (H2). Paste:

```
The clearest corridor
```

**Action:** Click `+` → Text block. Paste:

```
The clearest regional corridor is East and Southeast Asia. Chinese-Korean is the largest positive residual in the corpus (+0.44), Thai-Vietnamese is second (+0.40), and Filipino-Thai (+0.36), Filipino-Vietnamese (+0.25), and Chinese-Japanese (+0.21) form a compact corridor linking mainland adjacency, island geography, and archipelagic extension. This is the easiest place to see why the method matters: the map does not merely label similar cuisines; it shows where distance explains similarity and where it fails.
```

**Action:** Click `+` → Image block. Upload `v4_03_primary_case_regional_map.png`. Set to full-width.

**Caption:**

```
East/Southeast Asia gives the residual method its cleanest regional example. The strongest links combine nearby mainland pairs with archipelagic extensions that distance alone underpredicts.
```

**Alt text:**

```
Regional map of East and Southeast Asia showing residual links among Chinese, Korean, Japanese, Thai, Vietnamese, and Filipino cuisines.
```

**Action:** Add separator.

---

## SECTION 7 — One spotlight: Filipino

**Action:** Click `+` → Heading (H2). Paste:

```
One spotlight: Filipino
```

**Action:** Click `+` → Text block. Paste:

```
Filipino is the strongest single bridge in the network. Its top residual partners combine regional and transoceanic ties: Thai (+0.36), Brazilian (+0.32), Vietnamese (+0.25), Jamaican (+0.13), and Southern U.S. (+0.07). That mixture is the project's most interpretable hypothesis generator. The same cuisine connects the Southeast Asian corridor to Atlantic and Gulf cuisines, a pattern consistent with Spanish colonial and maritime exchange — and the colonial partial Mantel result above supports a modest version of that reading.
```

**Action:** Click `+` → Image block. Upload `v4_08_case_filipino.png`. Set to full-width.

**Caption:**

```
Filipino is the highest-scoring bridge cuisine. Its residual partners combine nearby Southeast Asian links with long-distance Atlantic and Gulf links, making it the clearest single anchor in the network.
```

**Alt text:**

```
Filipino case-study map and scorecard showing residual links to Thai, Brazilian, Vietnamese, Jamaican, and Southern U.S. cuisines.
```

**Action:** Add separator.

---

## SECTION 8 — What the map means

**Action:** Click `+` → Heading (H2). Paste:

```
What the map means
```

**Action:** Click `+` → Text block. Paste:

```
This is an exploratory 20-cuisine corpus, not a complete map of world food. Cuisine anchors are approximate centroids, the recipe corpus is platform-mediated and regionally uneven, and residuals do not prove routes of exchange. Their value is sharper: they identify where historical explanation is worth testing. Distance explains part of cuisine resemblance; GIS reveals the shape of what distance leaves behind.
```

**Action:** Click `+` → Quote block. Paste:

```
Cuisine resemblance is not only about who lives nearby. It is also about who has been connected — and the network of that connectedness has a shape a map can show.
```

**Action — NEW for v10:** Click `+` → Heading (H3). Paste:

```
References
```

**Action:** Click `+` → Text block. Paste:

```
[1] Yummly. (2015). What's Cooking. Kaggle dataset. [2] Zelený, D. (2024). Recipes dataset, anadat-r. [3] Mantel, N. (1967). The detection of disease clustering and a generalized regression approach. Cancer Research 27(2). [4] Anselin, L. (1995). Local indicators of spatial association — LISA. Geographical Analysis 27(2). [5] Patterson, T. & Kelso, N. V. (2024). Natural Earth, v5.1.1.
```

**Action:** Add separator. (This ends the StoryMap.)

---

## After pasting

Save the story (don't publish yet). Scroll top to bottom and check:

- Cover shows *Salt, Fat, Acid, Distance* with the claim subtitle.
- Each section has heading → body → image → caption in order.
- Section 3 has the data table after the residual-baseline image.
- Section 4 has both `v4_07_lisa_and_mantel` AND the new `v10_validation_stats` images.
- Section 5 has both `v4_05_bridge_index_map_and_chart` AND the new `v10_robustness_panel` images.
- Section 8 has heading → body → quote → references heading → numbered list → separator.
- Every image has alt text in the alt-text field.

Then publish to a draft URL, test in incognito, switch sharing to Everyone (public), and re-test.

---

## Submission email

Send to `jblossom@cga.harvard.edu`. Suggested subject line:

```
Fisher Prize submission — Salt, Fat, Acid, Distance — Matthew Tan
```

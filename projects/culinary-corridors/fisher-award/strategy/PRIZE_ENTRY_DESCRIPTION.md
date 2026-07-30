# Fisher Prize Entry Form — Project Description Drafts

Voice matched to the EIP-winning *Cloudy with a Chance of Compute* submission: declarative, statistical, specific. Each method gets a "what it does / why we chose it / what it tells us / what it does not tell us" treatment when there's room. Limitations are integrated inline rather than relegated to a separate caveat block. No "atlas" wording (per QA test #3 in the build doc).

All numbers below are from the v8 (regenerated-pipeline) data — they match the final BUILD_INSTRUCTIONS.md. Pick whichever variant fits the form field you're given. Each is independently submittable; they are not cumulative.

---

## Variant A — One-line summary (~30 words)

> *Bridges Across Cuisines* maps the residual network of culinary similarity that geographic distance does not explain — a 20-cuisine, 190-pair corpus regressed on log-distance and validated with Mantel and LISA spatial statistics.

---

## Variant B — Short abstract (~140 words)

> Thai and Vietnamese cuisines, separated by 800 km, share an ingredient profile resemblance well above the global mean. Filipino and Brazilian, separated by 19,000 km, share a resemblance the distance baseline cannot explain. *Bridges Across Cuisines* asks where culinary similarity exceeds what geography alone explains, and what the residuals reveal about long-distance exchange.
>
> The project regresses cosine ingredient similarity on log geographic distance across all 190 cuisine pairs, treats the residuals as a network, and tests its spatial structure with Mantel (r = +0.63, p < 0.001), partial Mantel (r = +0.51, p < 0.001), and Local Moran's I across four spatial-weights schemes. Three structural roles emerge: an Atlantic-rim high-residual cluster (Mexican and Jamaican as significant high-high LISA nodes; Cajun-Creole, Brazilian, Southern U.S. at marginal significance), a Eurasian continental bridge (Russian — the only highly-significant low-low LISA classification at p = 0.009), and a Pacific-archipelagic bridge (Filipino — most negative Local Moran's I in the corpus across all four robustness schemes).

---

## Variant C — Medium description (~330 words; the most likely form-field length)

> Modern food-and-place writing describes what people eat where. *Bridges Across Cuisines* asks a different question: which cuisines resemble each other more than geography would predict, and what does the structure of those residual connections look like on a map?
>
> The project takes a 20-cuisine, 1,434-ingredient corpus from the Yummly recipe collection and David Zelený's anadat-r repository, builds pairwise cosine similarity between cuisines, computes geodesic distances between cuisine anchors using GeoPy's great-circle method, and regresses similarity on log distance across all 190 pairs. The fitted line explains less than half of the variation (R² = 0.397, slope = −0.124). The remaining sixty percent of the variation — the residuals — becomes the analytical object. Positive residuals identify cuisines more similar than distance predicts. Mapped, they form a network of long-distance culinary connection.
>
> Three spatial-statistical methods test whether the residual network has structure beyond what spatial randomness would produce. A Mantel test (r = +0.63, p < 0.001 over 9,999 permutations) confirms that distance and dissimilarity co-vary at the matrix level. A partial Mantel (r = +0.51) shows the relationship survives partialling out subregional adjacency — the signal is not just neighbors-being-neighbors. Local Moran's I, implemented in PySAL's esda module across four spatial-weights schemes (inverse-distance, k-NN with k = 4 and k = 6, Gaussian-kernel), locates the residual structure spatially. Mexican and Jamaican appear as significant high-high spatial-association nodes in an Atlantic-rim cluster. Russian appears as the only highly-significant low-low node — a continental bridge whose strongest residual partners (Irish, British, French, Mexican, Southern U.S.) sit five to nine thousand kilometers from the Russian anchor, far outside its spatial neighborhood. Filipino shows the spatial signature of an isolated bridge: a high-residual cuisine surrounded by low-residual neighbors, with the most negative Local Moran's I in the corpus.
>
> The contribution is making the geometry of long-distance culinary similarity visible, statistically testable, and place-anchored. Bridge cuisines do their work through completely different geographies — Pacific-archipelagic, Eurasian-continental, Atlantic-rim — and the spatial-statistical layer formalizes which structural role each anchor plays.

---

## Variant D — Long description (~620 words; for narrative-style fields)

> Modern food-and-place writing describes what people eat where. *Bridges Across Cuisines* asks a different question: which cuisines resemble each other more than geography would predict, and what does the structure of those residual connections look like on a map?
>
> **The starting move.** Twenty cuisine labels from the Yummly recipe corpus, each represented as a frequency vector across 1,434 normalized ingredients, are compared pairwise using cosine similarity. Each cuisine is anchored at an approximate cultural-geographic centroid; pairwise geodesic distances between anchors are computed using GeoPy's great-circle method on the WGS84 ellipsoid. Cuisine similarity is then regressed on log distance across all 190 pairs. The fitted relationship returns a slope of −0.124 per unit of log distance and an R² of 0.397 — meaningful but small. Roughly sixty percent of the variation in cuisine similarity is structured but not explained by distance. That sixty percent, the residual, is where the project's analytical interest lives.
>
> **The spatial-statistical validation.** A Mantel test (r = +0.63, p < 0.001 over 9,999 permutations) confirms that distance and dissimilarity co-vary at the matrix level. A partial Mantel test (r = +0.51, p < 0.001) shows that the relationship survives partialling out subregional adjacency — distance is not just neighbors-being-neighbors. Local Moran's I, implemented in PySAL's esda module, is then applied to a per-cuisine mean-residual score using four spatial-weights schemes (inverse-distance, k-nearest-neighbor with k = 4 and k = 6, Gaussian-kernel with bandwidth 3,000 km) to confirm classifications are not artifacts of one specific definition of "near." Three classifications reach formal significance at p < 0.05: Mexican (HH, p = 0.047), Jamaican (HH, p = 0.040), and Russian (LL, p = 0.009 — the only highly-significant classification in the corpus). Cajun-Creole, Brazilian, and Southern U.S. show the same high-high pattern at marginal significance, completing an Atlantic-rim and Caribbean-Gulf cluster that is robust across spatial-weights choices. Filipino, Spanish, Thai, and French show the high-low sign pattern across all four schemes; none reach individual significance, which is a power limitation expected at n = 20 and not evidence of absence.
>
> **What the structure looks like.** Three structural roles emerge from the LISA layer. An Atlantic-rim high-residual cluster spans Mexican, Jamaican, Cajun-Creole, Brazilian, and Southern U.S. — formally validated as a high-high spatial association above what randomness would produce. A Eurasian continental bridge sits at Russian, whose strongest residual partners (Irish at +0.19, Mexican at +0.18, British at +0.15, Southern U.S. at +0.12, French at +0.11) all sit five to nine thousand kilometers away and are not Russian's geographic neighbors — the LISA picks this up cleanly as the LL signature. And a Pacific-archipelagic bridge anchors at Filipino, whose Local Moran's I is the most negative of any cuisine across all four robustness schemes (the unmistakable HL signature of an isolated bridge), and whose top residual partners — Thai, Brazilian, Vietnamese, Jamaican, Southern U.S. — span mainland Southeast Asia, the Caribbean–Gulf, and the Atlantic shore of South America from a single archipelagic anchor.
>
> **What the project contributes.** The work makes the geometry of long-distance culinary similarity visible, statistically testable, and place-anchored. Bridge cuisines do their work through completely different geographies, and the spatial-statistical layer formalizes which structural role each anchor plays. The accompanying StoryMap renders this argument across a hero corridor map, a distance-baseline scatter, the Mantel-and-LISA two-panel figure, a residual-by-grouping bar chart, a bridge-index map, an East/Southeast Asian regional case, and four cuisine spotlight figures (Filipino, Russian, Thai, Spanish) — each pairing a regional residual map with a per-cuisine LISA scorecard. An interactive Leaflet companion lets readers trace any cuisine's residual network anchor by anchor, with the full per-cuisine statistical profile in the popup.

---

## Notes for filling in the form

- The Fisher Prize submission form's "project description" field length depends on the year. If unsure, paste **Variant C** — it's the most likely fit for a single-paragraph or short-abstract slot.
- If the form has separate fields for *abstract* and *technical description*, use **Variant B** for the abstract and **Variant D** for the technical description.
- If the form is just "summary + URL" with a tight character limit, use **Variant A** + the StoryMap URL.
- The form will probably also ask for a project title. Use: **Bridges Across Cuisines: Mapping Residual Culinary Similarity Through Geographic Distance and Spatial-Statistical Validation**. Shorten to **Bridges Across Cuisines: A Spatial-Statistical View of Long-Distance Culinary Similarity** if the title field is short.
- Keywords field, if asked: *cuisine geography, spatial autocorrelation, LISA, Mantel test, residual analysis, food network, GIS methodology, cosine similarity, ingredient analysis, Atlantic rim, Pacific Rim, archipelagic bridges*.

---

## What this submission is asking the prize judges to recognize

The Fisher Prize judges weight GIS methodology contribution heavily. The strongest signal in this submission for that criterion is the **Mantel + LISA spatial-statistical layer** added in Section 5 (Finding 1.5). It's not just a description of residuals; it's a formal test of whether the residual structure is spatially organized, with permutation-based p-values and four-scheme robustness checks. That layer is what lifts the project from "descriptive cartography of cuisine" to "applied spatial statistics with cartographic communication" — which is the bar the GIS-use score is graded against. The case-study spotlight figures in Section 9 then demonstrate that the spatial-statistical evidence localizes cleanly to specific cuisine anchors with structurally distinct geographic roles.

If the form has a separate "what is the GIS contribution?" or "methodology novelty" field, lean into the Mantel-LISA-PySAL stack and the four-scheme robustness pattern. The contribution there is not in inventing new spatial statistics but in applying a well-validated suite of them to a domain (cuisine geography) where they have not been deployed before, with proper attention to small-sample power limits and robustness.

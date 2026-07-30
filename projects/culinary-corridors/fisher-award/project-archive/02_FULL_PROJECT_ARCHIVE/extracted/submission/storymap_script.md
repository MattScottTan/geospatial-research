# StoryMap Script — Culinary Corridors

Created: 2026-04-29

## Title

# Culinary Corridors
## Mapping Food Similarity, Spatial Residuals, and Regional Exchange

**Project description:** This project treats cuisine as spatial evidence. By comparing ingredient-profile similarity with geographic distance, it maps where food follows geography, where it breaks geography, and which places become bridges in the residual culinary landscape.

**Recommended hero text:** Food travels through distance, but not only distance. It moves through regional adjacency, migration, trade, colonial histories, maritime routes, and shared ingredient ecologies. This project uses GIS to ask where those spatial patterns become visible.

---

## 1. The question

Cuisines are often described as cultural, historical, or sensory systems. They are also spatial systems. Ingredients move through regions, ports, borders, ecologies, and households. The question for this project is:

> **When two cuisines are similar, is that similarity mostly explained by geographic distance, or do residual similarities reveal spatial corridors, regional bridges, and boundary patterns that distance alone cannot explain?**

The goal is not to prove that a specific historical event caused a cuisine pair to become similar. The goal is to build a geospatial discovery method: measure similarity, compare it to distance, map what remains, and then interpret the strongest patterns cautiously.

---

## 2. Food as spatial data

The project represents each cuisine as an ingredient profile. A cuisine is not treated as a perfect nation-state unit; it is a labeled collection of recipes from a platform-mediated recipe corpus. That limitation matters, so the project uses mapping confidence notes and focuses interpretation on cases where the spatial logic is clearest.

The workflow is:

1. clean recipe ingredient lists;
2. normalize common ingredient names;
3. build cuisine-by-ingredient matrices;
4. calculate pairwise cuisine similarity;
5. compare similarity against geographic distance;
6. map positive residuals as candidate culinary corridors;
7. focus interpretation on scoped geospatial cases.

The spatial baseline is essential. A non-spatial clustering project can say which cuisines look similar. This project asks which similarities are **unexpected given geography**.

---

## 3. Global discovery: where distance is not enough

**Place Figure 1 here:** `figures/final/final_global_discovery_figure.png`

**Caption:** Global discovery: filtered residual culinary corridors. Lines connect cuisine pairs whose observed ingredient-profile similarity is higher than a distance-only model predicts after generic-ingredient filtering. This is a discovery screen, not causal proof.

The global map is the first pass. It includes the full 20-cuisine prototype and uses filtered residuals to identify candidate corridors. Some results are plausible; others are exposed to platform bias, broad cuisine labels, or generic ingredient effects. That is why the global layer is used to discover patterns rather than carry the final explanation.

The important result is not any single line. The important result is that cuisine similarity leaves spatial residuals: pairs and places that remain interesting after a distance baseline is imposed.

---

## 4. Distance as a baseline, not the answer

**Place Figure 2 here:** `figures/final/final_distance_or_residual_model_figure.png`

**Caption:** Distance baseline and residual logic. Cuisine similarity partly declines with geographic distance, but distance does not explain the whole pattern. Residuals identify cuisine pairs whose similarity is higher or lower than the distance-only model predicts.

The Run 2 v2 filtered model estimated a negative relationship between log-distance and cosine similarity. This supports a modest claim: geography matters. The model also left substantial residual structure, which supports the project’s central GIS move: map the unexplained geography.

A positive residual does not mean that a particular historical mechanism has been proven. It means that a pair is more similar than the baseline expects, making it a candidate for focused spatial interpretation.

---

## 5. Primary focused case: East/Southeast Asia

**Place Figure 3 here:** `figures/final/final_east_southeast_asia_case_figure.png`

**Caption:** Primary focused case: East/Southeast Asia. Lines show residual links among Chinese, Japanese, Korean, Thai, Vietnamese, and Filipino cuisines where available. This is the strongest scoped interpretation because the cuisines form a coherent regional and cross-subregional case.

The East/Southeast Asia case is the strongest final inference case. It includes six target cuisines and enough pairwise comparisons to examine regional residual structure without leaning on the noisier global map.

The strongest positive residual links in the filtered case include:

- Thai–Vietnamese;
- Chinese–Korean;
- Filipino–Thai;
- Filipino–Vietnamese;
- Chinese–Filipino.

These results support a defensible claim: within this subset, cuisine similarity is spatially organized around regional adjacency and cross-subregional links. They do **not** prove a specific migration, trade, or diffusion route. They show where such questions become spatially visible.

---

## 6. From corridors to bridge roles

**Place Figure 4 here:** `figures/final/final_geospatial_bridge_or_boundary_figure.png`

**Caption:** Residual bridge scores. Point size represents each cuisine’s long-distance positive residual bridge score. This figure translates pairwise residual similarities into mapped place-level roles, making it the strongest geospatial-only visual in the project.

A residual corridor map shows lines between unexpectedly similar cuisine pairs. A bridge-score map asks a different GIS question:

> Which places repeatedly participate in positive residual corridors, especially long-distance ones?

This converts pairwise food similarity into a mapped spatial role. In Run 2 v2, Filipino cuisine emerged as especially important because it appears in both the East/Southeast Asia primary case and the Iberian/Atlantic-Pacific secondary case. Other high bridge-score cuisines require more caution because some may reflect platform bias or generic ingredient vocabulary.

The bridge-score approach is the project’s clearest Fisher contribution. It shows that the insight depends on geography, not ingredients alone.

---

## 7. Secondary case: Iberian/Atlantic-Pacific corridor hypothesis

**Place Figure 5 here:** `figures/final/final_secondary_or_sensitivity_figure.png`

**Caption:** Secondary/diagnostic case: Iberian/Atlantic-Pacific corridor. Lines show residual links among Spanish, Brazilian, Mexican, Filipino, Cajun/Creole, Jamaican, and Southern U.S. cuisines. This case illustrates long-distance corridor logic, but it should be interpreted cautiously.

The secondary case is visually compelling because it highlights long-distance residual connections. It is also where the project must be most careful. Some links are consistent with maritime, colonial, diasporic, or trade corridor hypotheses, but the prototype does not directly model those mechanisms. The recipe corpus may also amplify shared pantry ingredients, English-language recipe conventions, and platform-specific representations of cuisine.

For that reason, the Iberian/Atlantic-Pacific figure is best used as a hypothesis generator and contrast case, not as the central proof.

---

## 8. Boundary and permeability patterns

**Optional appendix/expanded figure:** `figures/final/final_boundary_permeability_appendix_figure.png`

The boundary/permeability summary groups cuisine pairs by spatial relationship: same subregion, same region but different subregion, East/Southeast Asia cross-subregion, Iberian/Atlantic interregional, and other cross-region pairs. This is exploratory, but it points to a more advanced GIS question:

> Which boundaries interrupt food similarity, and which corridors allow similarity to cross distance?

The current prototype uses grouping proxies rather than true historical routes or least-cost paths. Future work could improve this with port networks, trade flows, migration matrices, or historical route data.

---

## 9. What the project does not claim

This project makes three safeguards explicit:

1. The recipe corpus is not a representative census of world cooking.
2. Cuisine labels are not exact nation-state units.
3. Residual similarities do not prove migration, trade, colonialism, or maritime exchange.

The global map discovers candidate corridors. The focused case maps support cautious spatial interpretation. The bridge-score map shows a geospatial structure that ingredient analysis alone would miss.

---

## 10. Conclusion

Culinary Corridors uses GIS to make food similarity spatially interpretable. It shows that cuisine similarity partly follows distance, but that some of the most interesting patterns emerge where distance is incomplete: residual corridors, bridge cuisines, regional links, and boundary patterns.

The project’s central Fisher contribution is methodological as much as substantive. It demonstrates that food can be analyzed as spatial evidence: not just mapped after the fact, but modeled through geography to reveal patterns that would otherwise remain hidden.

---

## Post-audit revision note

This script was reviewed against `outputs/run3_claim_audit_checklist.md`. Language implying causal proof, global representativeness, or exact cuisine-to-nation equivalence has been removed or qualified. Mechanism language is framed as hypothesis or association unless directly computed.

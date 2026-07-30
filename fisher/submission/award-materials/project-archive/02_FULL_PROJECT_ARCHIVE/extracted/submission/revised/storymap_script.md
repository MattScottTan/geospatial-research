# Revised StoryMap Script - Culinary Corridors

Created: 2026-04-29

# Culinary Corridors
## Mapping Where Food Similarity Breaks Distance

**Project description:** This project uses GIS to ask when cuisine similarity follows geographic distance, when it exceeds distance-based expectation, and which places become bridge nodes in the residual geography of food.

---

## 1. Food similarity has geography

Cuisines are often described through ingredients, flavors, techniques, and histories. They are also spatial systems. Ingredients move through regions, ports, borders, ecologies, trade routes, households, and diasporas.

The central question is:

> **When two cuisines are similar, is that similarity mostly explained by geographic distance, or do residual similarities reveal spatial corridors, bridge regions, and boundary patterns that distance alone cannot explain?**

**Place Figure 1:** `figures/final_revised/run4_hero_spatial_argument_figure.png`

**Figure takeaway:** The strongest visual claim is not that global cuisine has one simple pattern. It is that food similarity can be compared to geography, and the residuals become candidate culinary corridors.

---

## 2. The GIS operation

A non-spatial food study can cluster cuisines by ingredient overlap. This project asks a different question: **which similarities are unexpected given geography?**

The workflow is:

1. represent each cuisine as a filtered ingredient profile;
2. calculate pairwise cuisine similarity;
3. assign each cuisine a geographic anchor with mapping-confidence notes;
4. fit a distance baseline;
5. compute residual similarity as observed similarity minus predicted similarity;
6. map positive residuals as candidate culinary corridors;
7. aggregate residual links into place-level bridge roles.

**Place Figure 2:** `figures/final_revised/run4_method_or_model_figure.png`

**Figure takeaway:** Points above the baseline are not merely similar cuisines. They are cuisines whose similarity is stronger than geographic distance would predict.

---

## 3. Why the global map is a discovery screen

The global model uses all retained cuisines to identify possible residual corridors. It is deliberately treated as a **screen**, not as a causal model. The recipe corpus is platform-mediated, cuisine labels are coarse, and straight-line distance is only a baseline for spatial expectation.

That discipline makes the analysis stronger. The global map helps locate candidate patterns, but the strongest claims come from focused cases and geospatial role metrics.

---

## 4. Primary inference case: East/Southeast Asia

The East/Southeast Asia subset is the strongest focused case because the retained cuisines form a coherent regional/cross-subregional geography and because several positive residual links remain after generic-ingredient filtering.

**Place Figure 3:** `figures/final_revised/run4_primary_case_figure.png`

**Figure takeaway:** The focused map shows where residual cuisine similarity is spatially organized within and across East/Southeast Asian subregions. It does not prove a single historical mechanism; it shows a spatial association that is stronger than a global descriptive map.

---

## 5. Geospatial-only insight: bridge roles

The bridge-score analysis translates pairwise residual links into mapped place-level roles. A high bridge index means that a cuisine participates in many positive residual links, including long-distance links, after geography has been modeled.

**Place Figure 4:** `figures/final_revised/run4_geospatial_insight_figure.png`

**Figure takeaway:** This is the clearest Fisher-style result. Ingredient clustering alone can identify similar cuisines, but only a spatial residual model can identify which cuisines act as residual bridge nodes in geographic space.

---

## 6. Boundary and limitation check

The boundary/permeability summary asks whether residual similarity differs across spatial groupings. It helps distinguish focused inference from global speculation.

**Place Figure 5:** `figures/final_revised/run4_secondary_or_limitations_figure.png`

**Figure takeaway:** Some spatial groupings show higher average residual similarity than others. This supports the idea that culinary residuals have spatial structure, while also showing why mechanism claims should remain cautious.

---

## 7. What this project shows

This project shows that cuisine similarity is spatially structured but not reducible to distance. The key contribution is methodological: GIS turns food similarity into a residual geography of corridors, bridges, and boundaries.

## 8. What this project does not claim

The project does not claim that the recipe corpus represents all global cuisine. It does not claim that migration, trade, colonialism, or maritime exchange caused any specific residual link. It treats those mechanisms as hypotheses for future testing with explicit historical, migration, or trade data.

## 9. Fisher contribution

**Culinary Corridors** aligns with the Fisher Prize because the map/model output is evidence. GIS is not decorative. It produces the core result: where food similarity follows distance, where it breaks distance, and which places become bridges in the residual geography of cuisine.


---

## Run 4 audit status
This revised version passed the Run 4 claim audit: global results are discovery, focused cases are non-causal inference, and mechanism language remains hypothesis-generating.

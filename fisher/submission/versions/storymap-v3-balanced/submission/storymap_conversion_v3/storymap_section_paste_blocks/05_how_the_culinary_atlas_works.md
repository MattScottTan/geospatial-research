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

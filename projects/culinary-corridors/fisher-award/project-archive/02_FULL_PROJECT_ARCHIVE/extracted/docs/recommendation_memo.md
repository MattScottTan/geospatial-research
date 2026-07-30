# Recommendation Memo

## Recommendation

Proceed with **Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry** as the primary Fisher project.

Fallback project: **Cuisine Similarity and Migration/Trade Residuals**, a narrower version that excludes flavor chemistry and fermentation from the main analysis.

## Why this primary project is strongest

The combined Culinary Corridors version best matches Fisher Prize patterns because it makes GIS do the explanatory work. The core output is not a map of cuisines; it is a spatial model that asks whether cuisine similarity can be explained by distance, and then maps the residuals that remain. Those residuals become candidate culinary corridors: places whose foods are more similar than geography alone predicts.

This framing aligns with observed Fisher winners because it is interdisciplinary, data-rich, visually strong, and inferential. Past winners repeatedly used spatial analysis to reveal hidden patterns of conflict, risk, access, conservation, climate impact, or historical change. Culinary Corridors would use similar logic for food: ingredient networks and residual maps reveal hidden spatial relationships among migration, trade, agriculture, culture, and chemistry.

## Evidence basis

- Public Fisher criteria include innovation/creativity, use of GIS, data, analysis, and presentation.
- Past winners favor projects where spatial analysis is necessary: storm-surge risk, Maoist insurgency, green-space access, war-damaged cities, flood detection, settlement destruction, wildfire jurisdiction risk, and spatial-chemical archaeology.
- Cuisine similarity has a literature base: Chinese regional-cuisine work found geography more important than climate; ingredient-network work treats cuisines as network fingerprints; food/drink similarity has been used in migration-prediction research.
- Data feasibility is good: official UN/FAO/CEPII/Natural Earth sources can anchor the spatial model, while RecipeDB/FlavorDB provide food-specific data if access is confirmed.
- The smoke test confirmed the code path for ingredient parsing, similarity scoring, and network/geospatial visualization.

## Primary project

**Title:** Culinary Corridors: A Geospatial Analysis of World Cuisine Through Ingredients, Migration, Trade, and Flavor Chemistry

**Central question:** How does cuisine similarity vary across space, and when do migration, trade, agricultural environment, and flavor chemistry explain culinary resemblance better than geographic proximity?

**Core method:**
1. Build cuisine/region ingredient vectors.
2. Compute cuisine similarity.
3. Model similarity against geographic distance.
4. Add migration, trade, climate/agriculture, language, and colonial/history covariates.
5. Map residual culinary corridors.
6. Add a flavor-chemistry panel where ingredient matching permits.
7. Include fermentation as a cautious science sidebar if data supports it.

## Fallback project

**Title:** Culinary Corridors: Cuisine Similarity, Migration, and Trade

**Central question:** Which cuisine pairs are more similar than geography predicts, and do migration or trade explain those links?

This fallback is still Fisher-competitive because it keeps the strongest GIS components: similarity matrices, dyadic spatial modeling, residual maps, and flow/corridor visualization. It drops flavor chemistry and fermentation if data matching becomes too slow.

## Why not make flavor chemistry the whole project

Flavor chemistry is distinctive and Pia-aligned, but ingredient-to-compound matching may be messy. Compound presence also does not equal perceived flavor. It is best as a second analytical layer that deepens the primary project after the spatial core works.

## Why not make fermentation the whole project

Fermentation is scientifically exciting, but data feasibility is weaker. Existing sourdough work is large and credible but reports little evidence for strong biogeographic patterns, which is a fascinating sidebar rather than a straightforward Fisher spatial-analysis thesis. Broader food microbiome datasets may work, but only after Run 2 verifies sample geography and metadata.

## Pia usefulness

Pia is most useful if asked to validate concrete scientific assumptions:
- ingredient taxonomy and normalization;
- flavor-chemistry interpretation;
- whether chemical similarity can be treated as sensory evidence;
- fermentation sidebar framing;
- examples of cooking processes that alter flavor geography.

## Final recommendation

Run 2 should build the cuisine-similarity + residual-corridor prototype first. If the first maps are visually strong, add flavor chemistry as a distinctive science panel. Fermentation should remain a scoped sidebar unless clean geocoded microbiome data is found quickly.

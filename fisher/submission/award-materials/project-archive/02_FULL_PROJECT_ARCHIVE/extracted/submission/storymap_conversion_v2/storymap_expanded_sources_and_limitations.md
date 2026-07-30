# Expanded Sources and Limitations

# 14. What this proves, and what it does not prove

## PASTE TEXT

# What this proves, and what it does not prove

The project makes a spatial argument, not a causal historical argument.

It can strongly claim that cuisine similarity is spatially structured. The distance model shows that similarity is related to geographic distance, but not fully explained by it. Positive residuals identify candidate culinary corridors. East/Southeast Asia is the strongest focused case. Residual bridge scores produce a spatial insight that ingredient clustering alone cannot produce. The Run 5 relief map makes the focused corridor more visually legible.

It can cautiously say that selected residual patterns are consistent with regional adjacency, corridor plausibility, island/maritime context, or possible exchange histories. These are interpretations to investigate, not mechanisms proven by the model.

It cannot claim that migration caused the observed similarities. It cannot claim that trade, colonialism, empire, maritime routes, or terrain caused the observed similarities. It cannot claim that the recipe corpus represents all world cuisines. It cannot treat cuisine labels as exact nation-states. It cannot treat the relief map as a least-cost path model or causal topographic analysis.

Those limits are not weaknesses. They are what make the project defensible. A weaker project would overread the residuals as historical truth. This project treats them as spatial evidence: model-defined relationships that become meaningful when mapped, scoped, and interpreted carefully.

The final contribution is therefore methodological and cartographic. GIS transforms a recipe corpus into a map of spatial expectations, residuals, corridors, focused cases, and bridge roles. The project shows how food can be analyzed as a spatial signal without pretending that the signal is complete or causal on its own.

## PASTE CALLOUT

> Strong claim: residuals reveal spatial structure. Cautious claim: some residuals are consistent with exchange contexts. Forbidden claim: the model proves the cause.

## EDITOR NOTE

Recommended ArcGIS block: Text block with strong/cautious/forbidden claim callout.


---

# 15. Sources, methods, and reproducibility

## PASTE TEXT

# Sources, methods, and reproducibility

This StoryMap summarizes a larger technical workflow documented in the PDF backup and internal project artifacts.

The recipe and ingredient pipeline uses a staged cuisine-labeled recipe corpus derived from the What’s Cooking / Kaggle-Yummly data family and prepared recipe source notes. Ingredients were normalized with an alias crosswalk, and generic pantry terms were removed or downweighted in sensitivity checks. The recipe corpus is treated as a platform-mediated proxy, not as a representative census of world cuisine.

The geography pipeline uses cuisine-to-place anchor points, pairwise geographic distances, UN M49-style regional groupings where relevant, and public map/relief sources for visualization. Natural Earth-style boundary and base-map data support the cartographic context. The Run 5 topographic corridor figure uses relief/coastal context from a local Basemap ETOPO-style relief image. It is a relief-context visualization, not a new elevation model or least-cost routing analysis.

The analysis pipeline was implemented with Python for data preparation, similarity computation, residual modeling, and figure generation. The StoryMap is designed for ArcGIS StoryMaps as the final presentation format. The PDF report remains the technical backup, with more detail on data sources, methods, limitations, and final figure sequence.

Key source families include Harvard Center for Geographic Analysis Fisher Prize pages, What’s Cooking / Kaggle-Yummly recipe data notes, Natural Earth public-domain map data, UN M49 statistical region definitions, Basemap/ETOPO relief context, and the project’s Run 2 through Run 6 internal artifacts.

ChatGPT was used for guidance, drafting, organization, and formatting of the project materials. The analytical results, figures, and claim hierarchy are documented in the project artifacts and should be checked through the final PDF and StoryMap QA materials before submission.

For the final StoryMap, the sources section should be visible but not overwhelming. The most important message is that every major visual has a traceable input family and that the limitations are not hidden. If a reviewer wants the full file-level record, the technical PDF and reproducibility manifests provide that backup.

## PASTE CALLOUT

> The PDF backup contains the technical report; the StoryMap presents the map-led argument.

The reproducibility standard for the StoryMap is practical rather than archival. A reviewer should be able to trace each major visual to its input family and method: recipe corpus to ingredient matrix, ingredient matrix to similarity, similarity and coordinates to residuals, residuals to focused maps, and residuals plus mapped positions to bridge roles. The PDF backup preserves the fuller file-level audit.

## EDITOR NOTE

Recommended ArcGIS block: Sources/methods text near the end. Include source hyperlinks if possible in ArcGIS.

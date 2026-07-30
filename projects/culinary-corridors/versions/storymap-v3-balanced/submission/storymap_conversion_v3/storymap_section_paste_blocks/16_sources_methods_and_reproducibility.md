# 16. Sources, methods, and reproducibility

## PASTE TEXT

# Sources, methods, and reproducibility

This project uses a cuisine-labeled recipe corpus as the food-data foundation. Recipes are transformed into cuisine-by-ingredient profiles through ingredient normalization and generic-ingredient filtering. The analysis then calculates cuisine similarity, maps cuisine labels to approximate geographic anchors, computes pairwise distance, models similarity against distance, and maps residuals.

The final maps and figures draw on the project’s processed cuisine-similarity outputs, distance/residual model outputs, focused East/Southeast Asia results, residual bridge-index outputs, secondary/diagnostic sensitivity summaries, and Run 5 topographic/relief visualization work. The Run 5 relief map uses documented topographic/coastal context as a visual layer, but it is treated as spatial context rather than a causal model.

The workflow was developed through Python-based data processing and figure generation, with ArcGIS StoryMaps used as the final presentation format. The PDF report remains the technical backup and includes the fuller methodology, figures, limitations, and source notes.

Several limitations are central to the interpretation. The recipe corpus is not globally representative. Cuisine labels are broad and cannot be treated as precise countries. Ingredient normalization requires judgment. Generic pantry ingredients can inflate similarity, which is why filtering and sensitivity checks matter. Cuisine-to-place mapping is approximate. Residuals identify spatially unexpected resemblance, not causality. Topographic context improves visual interpretation but does not prove terrain or maritime pathways caused the patterns.

The StoryMap is designed to be readable on its own, while the PDF report provides the deeper technical version. Together, they present the project as a map-led Fisher submission with transparent limitations.

## EDITOR NOTE

Recommended ArcGIS block: Sources/methods panel near the end. Link to PDF backup if possible.

## PASTE CALLOUT

> The PDF report is the technical companion; the StoryMap is the map-led submission narrative.

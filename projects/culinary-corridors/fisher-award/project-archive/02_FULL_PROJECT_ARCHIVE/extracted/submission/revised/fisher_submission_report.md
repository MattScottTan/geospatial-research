# Revised Fisher Submission Report - Culinary Corridors

Created: 2026-04-29

## Title
**Culinary Corridors: Mapping Where Food Similarity Breaks Distance**

## Abstract
This project uses GIS to treat cuisine as spatial evidence. I represent cuisines as ingredient profiles, calculate pairwise similarity, compare those similarities to geographic distance, and map the residuals: cuisine pairs and places whose similarity exceeds distance-based expectation. The global model functions as a discovery screen, while East/Southeast Asia provides the primary focused inference case. A residual bridge-index analysis then translates pairwise links into mapped place-level roles. The result is not a causal history of migration or trade; it is a geospatial method for finding candidate culinary corridors and bridge regions that would be difficult to detect from ingredient data alone.

## Problem and question
Food is global, but food similarity is not evenly distributed across the globe. Cuisines can become similar through proximity, ecology, exchange, diaspora, trade, empire, and shared techniques. The GIS question is: **when does food similarity follow distance, and when does it break distance?**

## Data
The prototype uses a staged recipe/ingredient corpus, cleaned cuisine labels, normalized ingredient names, a generic-ingredient filtering policy, cuisine-to-geography crosswalks, pairwise distances, and residual outputs from the Run 2 v2 analysis. The data are documented with source and limitation notes. The corpus is a proxy, not a globally representative census of cuisine.

## Method
The method has four steps:

1. Build filtered cuisine-by-ingredient profiles.
2. Compute pairwise cuisine similarity using cosine similarity and robustness metrics.
3. Fit a distance baseline using geographic anchors and pairwise distance.
4. Compute residual similarity: observed similarity minus distance-predicted similarity.

Positive residuals become candidate culinary corridors. A bridge-index analysis aggregates residual links into mapped cuisine-level spatial roles.

## Results
The global discovery screen shows that cuisine similarity is partly geographic but leaves meaningful residuals. The East/Southeast Asia focused case provides the most defensible interpretation because the cuisine labels form a coherent regional geography. The bridge-index analysis identifies cuisines that act as residual bridge nodes after distance is modeled.

## Fisher alignment
The project fits the Fisher Prize because the GIS workflow produces the insight. Without coordinates, distance, residual geography, and mapped bridge roles, the project would be reduced to non-spatial recipe clustering. The map/model output is the evidence.

## Limitations
The project does not prove causal mechanisms. Positive residual links are consistent with possible exchange histories, but explicit migration, trade, colonial, or maritime covariates would be needed for stronger causal claims. Cuisine labels are approximate, and recipe-platform bias remains a central limitation.

## Conclusion
**Culinary Corridors** demonstrates that food similarity can be transformed into a spatial-inference problem. GIS reveals where cuisine follows distance, where it breaks distance, and which places become bridge nodes in the residual geography of food.


---

## Run 4 audit status
This revised version passed the Run 4 claim audit: global results are discovery, focused cases are non-causal inference, and mechanism language remains hypothesis-generating.

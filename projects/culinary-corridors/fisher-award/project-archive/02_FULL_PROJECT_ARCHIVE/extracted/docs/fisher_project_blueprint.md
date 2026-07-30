# Fisher Project Blueprint

## Working title options

1. **Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry**
2. **Food as Spatial Evidence: Ingredient Networks and the Geography of Human Movement**
3. **Beyond Distance: A Geospatial Model of Cuisine Similarity and Cultural Exchange**
4. **The Flavor of Movement: Cuisine Similarity as a Signal of Migration and Trade**

Recommended title: **Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry**.

## Central research question

How does cuisine similarity vary across space, and when do migration, trade, agricultural environment, and flavor chemistry explain culinary resemblance better than geographic proximity?

## Thesis / hypothesis

World cuisines are shaped by geography, but not only by geography. If cuisines are represented as ingredient networks, then geographic distance should produce a baseline pattern of declining similarity. The most interesting cases are positive residuals: places whose cuisines are more similar than distance or climate would predict. These residual “culinary corridors” may reflect migration, trade, colonial/language ties, agricultural exchange, diaspora, and shared flavor or fermentation practices.

## Why this fits the Fisher Prize

This is not a “map of food.” The project uses GIS to produce the main insight. The analytical core is a spatial model: construct cuisine similarity, compare it with distance and spatial covariates, then map unexplained residual connections. This mirrors past Fisher-winning patterns: interdisciplinary topic, clear spatial necessity, heterogeneous data integration, methodologically explicit GIS, and visually strong cartographic output.

## Recommended scope

Start global at the country/geo-cultural-region level, then narrow if recipe coverage or cuisine labels are too noisy.

Run 2 should use the broadest clean scope feasible. If global coverage fails, narrow to one of these corridors:

1. Mediterranean–Middle East–South Asia ingredient/flavor corridors.
2. Indian Ocean trade foodways: East Africa, Arabia, South Asia, Southeast Asia.
3. Atlantic diaspora foodways: West Africa, Caribbean, United States, Latin America.
4. East/Southeast Asia fermentation and soy/fish/rice foodways.

## Data stack

### Core data

- Recipe/ingredient corpus: RecipeDB if access and license are confirmed; fallback to documented open recipe/API samples for prototype.
- Migration: UN DESA International Migrant Stock 2024.
- Trade: UN Comtrade food/spice/agriculture HS product flows.
- Agriculture/food supply: FAOSTAT crop/livestock/food balance data.
- Distance/cultural covariates: CEPII GeoDist.
- Base maps: Natural Earth Admin 0.

### Scientific extension

- Flavor chemistry: FlavorDB, FlavorDB2, FooDB, FSBI-DB, PubChem.
- Fermentation/microbiome sidebar: eLife sourdough microbiome, FoodMicroDB, cFMD, Fermented Foods Microbial Genomes Database.

### Optional environment controls

- WorldClim for climate similarity.
- EarthStat/SPAM/CROPGRIDS for crop availability.
- GAEZ/MIRCA if crop suitability or irrigated/rainfed seasonality matters.

## Methods

### 1. Cuisine representation

Create cuisine/region ingredient vectors using normalized ingredients. Start with binary and frequency vectors; later add TF-IDF and ingredient-pair networks.

### 2. Similarity matrix

Compute pairwise cuisine similarity with cosine, Jaccard, and Pearson metrics. Check robustness by excluding universal ingredients and comparing spice-only, staple-only, and category-level vectors.

### 3. Spatial baseline

Use CEPII distance to estimate how cuisine similarity decays with geographic distance. This baseline produces predicted similarity for each pair.

### 4. Residual corridors

Compute observed-minus-predicted similarity. Map high positive residuals as culinary corridors.

### 5. Explanatory overlays

Add migration, trade, language, colonial, agriculture, and climate variables to test which residuals are explained by human movement or environmental/agricultural similarity.

### 6. Flavor chemistry layer

Map ingredients to FlavorDB/FooDB compounds. Compare ingredient similarity with flavor-molecule similarity. Identify pairs that are ingredient-different but chemically similar, or ingredient-similar but chemically divergent.

### 7. Fermentation sidebar

Use sourdough and food-microbiome evidence to complicate the geographic story. Ask whether fermented foods cluster by geography, substrate, or technique. Treat this as cautious interpretation unless data is strong.

## Expected visuals

1. Global cuisine similarity cluster map.
2. Distance-decay plot: cuisine similarity vs geographic distance.
3. Residual culinary corridor map.
4. Migration/trade explanatory overlay map.
5. Ingredient-network example panels for 2–3 cuisines.
6. Ingredient similarity vs flavor-chemistry similarity scatter plot.
7. Fermentation sidebar figure, if data allows.

## Preliminary smoke-test result

A toy TheMealDB-derived smoke test was created. It loaded a four-row sample, normalized ingredients, computed cosine similarities, wrote edge/matrix outputs, and generated `figures/pilot_map_or_chart.png`. This proves the basic workflow, not the substantive claim.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Recipe data license/access unclear | Use RecipeDB only after access confirmation; keep official covariate layers as core; label recipe risk. |
| Cuisine labels are national but foodways are regional/diasporic | Use geo-cultural labels and confidence flags; avoid treating borders as cuisine borders. |
| Ingredient normalization becomes subjective | Build alias crosswalk; record match confidence; ask Pia to review taxonomy. |
| Flavor chemistry overclaims sensory similarity | Report match rates and uncertainty; use chemistry as secondary layer; ask Pia to validate language. |
| Fermentation data lacks geocodes | Keep fermentation as sidebar; do not make it the core unless Run 2 confirms metadata. |
| Too many data layers | Build Run 2 in stages: recipe similarity → distance model → residual map → migration/trade overlays → flavor layer. |

## Pia role

Pia can add high-value scientific credibility by reviewing:
- ingredient categories and which ingredients should be grouped or separated;
- how cooking and fermentation alter chemical flavor profiles;
- whether FlavorDB/FooDB-based similarity is scientifically defensible;
- which fermentation examples would best support a sidebar;
- how to frame the project so it is food science, not only digital humanities.

## Run 2 prototype plan

Run 2 should produce a working prototype:
1. confirm/download a recipe corpus;
2. build ingredient crosswalk;
3. compute cuisine similarity;
4. join to country/cuisine geography;
5. add CEPII distances;
6. create distance-decay plot;
7. create first residual corridor map;
8. test one migration or trade overlay;
9. write a short prototype interpretation.

## Run 3 final submission plan

Run 3 should polish the Fisher package:
1. finalize maps and figures;
2. write award-facing narrative;
3. add methodology appendix or notebook link;
4. prepare an ArcGIS StoryMap or web-map-heavy report;
5. include limitations, citations, and data-source transparency;
6. produce final submission assets.

## Final format recommendation

Use an **ArcGIS StoryMap or web-map-heavy submission** if Run 2 maps are strong. Keep a static PDF/poster and technical appendix as backup. The StoryMap format best matches the project’s corridor-map narrative and the Fisher emphasis on visual GIS communication.

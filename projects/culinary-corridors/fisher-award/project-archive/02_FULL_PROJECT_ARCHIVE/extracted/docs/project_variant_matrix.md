# Project Variant Matrix

User preference from WORK.md: compare variants after data review; likely final format should be recommended by worker, with ArcGIS StoryMap/web-map-heavy submission probably promising; rigor target is high network/spatial modeling with robustness checks, possibly heavier if data supports it; maximize data while grading reliability.

## Summary ranking

| Rank | Variant | Weighted Fisher score | Recommended role |
|---|---|---:|---|
| 1 | Combined Culinary Corridors: cuisine similarity + migration/trade/climate + flavor chemistry sidebar | 4.55 / 5 | Primary project |
| 2 | Cuisine similarity and migration/trade residuals | 4.35 / 5 | Fallback / simplified primary |
| 3 | Geography of flavor chemistry | 3.75 / 5 | Scientific layer, possible secondary visual |
| 4 | Fermentation/microbial geography | 3.05 / 5 | Sidebar/case study only unless Run 2 finds strong geocoded food-microbiome data |

## Variant A — Cuisine similarity as migration/trade/cultural-exchange evidence

- **Research question:** Where does cuisine similarity follow geographic distance, and where do migration, trade, colonial/language links, or crop/climate explain unexpected similarity?
- **Possible thesis:** Cuisines exhibit distance decay, but positive residuals identify culinary corridors produced by human movement and exchange rather than by nearby geography alone.
- **Data needs:** Recipe/ingredient vectors; country/region coordinates; CEPII distance/language/colonial variables; UN DESA migrant-stock dyads; UN Comtrade food-product dyads; FAOSTAT agriculture/food balance data; climate/crop layers.
- **Methods:** Ingredient normalization; cosine/Jaccard/Pearson similarity; hierarchical clustering or Leiden/Louvain networks; gravity-style dyadic regression; residual corridor mapping; robustness checks by ingredient category and source reliability.
- **Expected visuals:** Global cuisine clusters; distance-decay plot; residual corridor map; migration/trade overlay; ranked “unexpectedly similar” country/region pairs.
- **Pia role:** Validate ingredient taxonomy, interpret whether ingredient similarity is scientifically meaningful, identify where cuisine similarity should be interpreted as technique/flavor instead of raw ingredient overlap.
- **Risks:** Recipe datasets may be scraped or culturally biased; cuisine labels may not align cleanly with countries; recipe websites overrepresent English-language/globalized dishes.
- **Mitigation:** Treat recipe data as one input; keep official data layers as core; limit claims to “observed in dataset”; run sensitivity checks by data source and region.
- **Preliminary score:** 4.35 / 5.

## Variant B — Geography of flavor chemistry

- **Research question:** Do cuisines that use different ingredients converge chemically in flavor-molecule space, and does chemical similarity have a different geography from ingredient similarity?
- **Possible thesis:** Some cuisines are ingredient-distant but chemically proximate, revealing convergent flavor strategies that are not visible in ingredient lists alone.
- **Data needs:** Recipe/ingredient data; FlavorDB/FlavorDB2/FooDB/FSBI-DB ingredient-compound mappings; ingredient synonym crosswalk; country/region/cuisine labels.
- **Methods:** Ingredient-to-compound matching; flavor vectors; cosine similarity in chemical space; comparison between ingredient-similarity matrix and chemical-similarity matrix; uncertainty labeling for unmatched ingredients.
- **Expected visuals:** Ingredient-vs-flavor similarity scatter; map of chemical-similarity clusters; examples of ingredient-different/flavor-similar cuisine pairs.
- **Pia role:** High-value. She can validate whether flavor compounds should be interpreted as sensory similarity, how to handle fermentation volatiles, and where chemistry overstates actual flavor perception.
- **Risks:** Ingredient-compound databases are incomplete; flavor presence does not equal concentration or perception; ingredient matching is messy.
- **Mitigation:** Use as secondary scientific layer; report match rates; avoid strong sensory claims; ask Pia to review chemical interpretation.
- **Preliminary score:** 3.75 / 5.

## Variant C — Fermentation / microbial geography

- **Research question:** Do fermented-food microbes follow geography, substrate, technique, or household/practice more strongly?
- **Possible thesis:** Fermentation may challenge geographic determinism: sourdough evidence suggests microbial interactions and practice can matter more than biogeography, while broader food metagenome datasets may reveal substrate-based clusters.
- **Data needs:** Sourdough starter microbiome data; food microbiome atlases such as cFMD/FoodMicroDB/MiFoDB; sample geocodes; food substrate labels; fermentation technique labels.
- **Methods:** Beta-diversity or taxonomy similarity; spatial autocorrelation; substrate-stratified clustering; comparison of geographic distance vs microbial similarity.
- **Expected visuals:** Sample map by fermented-food type; microbial similarity by substrate vs distance; case-study map of sourdough samples.
- **Pia role:** Very high scientifically: fermentation mechanisms, microbial community interpretation, technique/substrate taxonomy, limitations of microbial data.
- **Risks:** Geocoded data may be sparse or imbalanced; microbial taxonomy requires domain expertise; data may be too complex for a first Fisher prototype.
- **Mitigation:** Use as a sidebar or case study; cite sourdough literature that found little biogeographic signal; do not make it the main project unless Run 2 verifies a clean geocoded sample table.
- **Preliminary score:** 3.05 / 5.

## Variant D — Combined Culinary Corridors

- **Research question:** How does cuisine similarity vary across space, and when do migration, trade, agricultural environment, and flavor chemistry explain culinary resemblance better than geographic proximity?
- **Possible thesis:** Food encodes both place and movement: ingredient networks show geography, residual corridor maps reveal migration/trade/cultural exchange, and flavor chemistry explains cases where different ingredients converge into similar sensory strategies.
- **Data needs:** RecipeDB/other ingredient source; TheMealDB/Open Food Facts as accessible pilot data; FlavorDB/FooDB; UN DESA migrant stock; UN Comtrade; FAOSTAT; CEPII; Natural Earth; WorldClim/EarthStat/SPAM as optional agriculture/environment layers.
- **Methods:** Cuisine vectors; ingredient-pair networks; cuisine-similarity matrix; dyadic spatial model; residual corridors; flavor chemistry comparison; robustness by source and region.
- **Expected visuals:** Map 1: cuisine clusters. Map 2: residual culinary corridors. Chart: similarity vs distance. Map/Network: migration/trade links explaining top residuals. Chemistry panel: ingredient similarity vs flavor similarity. Sidebar: fermentation as a challenge to simple biogeography.
- **Pia role:** Ideal. Prepare consultation packet asking her to validate ingredient grouping, chemical interpretation, fermentation sidebar, and whether the proposed narrative is scientifically accurate.
- **Risks:** Scope creep; too many data layers; recipe data uncertainty.
- **Mitigation:** Make cuisine similarity + residual corridors the primary Run 2 deliverable; flavor chemistry as second-order analysis; fermentation only as a cautious case study.
- **Preliminary score:** 4.55 / 5.

## Decision

Proceed with **Variant D: Combined Culinary Corridors**, but keep the Run 2 prototype focused on **Variant A’s core**: cuisine similarity, distance decay, and residual corridor mapping. Add flavor chemistry only after ingredient matching is stable. Keep fermentation as a scientific sidebar or discussion section unless a clean, geocoded microbiome dataset is quickly confirmed.

# Data Sources and Limitations

Created: 2026-04-29

## Dataset sources and source notes

### Recipe corpus

The prototype uses a prepared What’s Cooking / Yummly-derived recipe corpus staged in Run 2. It contains recipe-level cuisine labels and ingredient lists. Run 2 source notes and source manifest:

- `data/run2_dataset_selection_memo.md`
- `data/run2_data_access_log.md`
- `data/raw/recipe_source_manifest.md`
- Public instructional/source page used in Run 2: https://pages.github.rpi.edu/kuruzj/website_introml_rpi/notebooks/08-intro-nlp/04-what-cooking-python.html

**Limitation:** the corpus should be described as platform-mediated recipe data, not as representative global culinary data.

### Geography and boundaries

Coordinate and region/subregion grouping are documented in:

- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`

Relevant external references:

- UN M49 regional/subregional classification: https://unstats.un.org/unsd/methodology/m49/
- Natural Earth public-domain cartographic data: https://www.naturalearthdata.com/

### Fisher Prize context

Fisher Prize context is documented in:

- `docs/award_and_winner_brief.md`

Relevant public sources:

- Harvard CGA Awards page: https://gis.harvard.edu/awards
- Harvard CGA Fisher Prize competition page: https://gis.harvard.edu/event/fisher-prize-award-competition
- Harvard Student GIS Awards page: https://gis.harvard.edu/news/harvard-student-gis-awards

## Data-quality limitations

### 1. Recipe-platform bias

The recipe corpus likely reflects English-language recipe-platform conventions, recipe contributors, and platform categories. Similarity patterns may therefore reflect how recipes are submitted or labeled online as well as culinary structure.

### 2. Cuisine labels are broad

Labels such as `chinese`, `indian`, and `mexican` compress large internal regional diversity. Labels such as `southern_us` and `cajun_creole` are regional/diasporic categories rather than countries.

### 3. Cuisine-to-place mapping is approximate

Coordinates are proxy centroids or representative locations, not definitive origins of cuisine traditions. Archipelagic, diasporic, or transregional cuisines are especially difficult to map precisely.

### 4. Ingredient normalization is rule-based

Ingredient names were normalized through a reproducible aliasing process, but ambiguous terms remain. For example, variants of chiles, onions, dairy ingredients, and spice blends may not represent identical culinary functions.

### 5. Generic ingredients distort similarity

Common ingredients such as salt, water, sugar, flour, butter, oil, and pepper can make distant cuisines appear artificially similar. Run 2 v2 therefore introduced a generic-ingredient filtering policy, but filtering choices remain interpretive.

### 6. Residuals are not mechanisms

Positive residuals indicate that observed cuisine similarity is higher than a distance-only model predicts. They do not prove migration, trade, colonial history, maritime exchange, or diffusion.

## Claims the project can make

- Cuisine similarity is spatially structured in the prototype dataset.
- Geographic distance explains some, but not all, of that similarity.
- Focused cases are more interpretable than the full global map.
- Residual bridge scores show a geospatial pattern that ingredient clustering alone cannot produce.

## Claims the project cannot make

- The model explains world cuisine.
- The recipe corpus represents all cooking practices.
- The detected corridors prove historical causation.
- Cuisine labels are equivalent to nation-states.
- Flavor chemistry or fermentation explains the final results.

## Recommended disclosure sentence

This project uses platform-mediated recipe data as a prototype corpus. Its maps identify spatial patterns and candidate culinary corridors, but they should be interpreted as exploratory evidence rather than representative or causal proof.

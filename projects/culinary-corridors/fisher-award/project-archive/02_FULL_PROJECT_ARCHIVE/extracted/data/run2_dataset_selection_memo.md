# Run 2 Dataset Selection Memo

Created: 2026-04-28

## Selected primary recipe/ingredient dataset

**Primary source:** Zelený / Analysis of Community Ecology Data in R prepared version of the Kaggle/Yummly **What’s Cooking** dataset.

**Local files staged:**

- `data/raw/recipes_long.txt`
- `data/raw/recipes_cuisines.txt`
- `data/raw/recipes_cuisines_count.txt`

**Source URLs:**

- `https://www.davidzeleny.net/anadat-r/doku.php/en:data:recipes?rev=1683202162`
- `https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_long.txt`
- `https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines.txt`
- `https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines_count.txt`

**Coverage:** 39,774 recipes, 20 cuisine labels, and 6,714 raw ingredient names in the source documentation. The long-format staged file contains 428,249 recipe-ingredient rows.

**Cuisine-label quality:** Good for prototype. The labels are explicit and exactly match the Run 2 need for a 20-cuisine global prototype. They are not perfect geographies: `southern_us` and `cajun_creole` are regional/diasporic labels, while labels such as `chinese`, `indian`, and `russian` are large national/civilizational categories.

**Ingredient quality:** Good for prototype. Ingredients are already separated into individual strings, but they include spelling variants, generic ingredients, branded products, pluralization differences, and preparation descriptors. This requires an alias crosswalk and sensitivity notes.

**Access method:** Direct public raw text files from GitHub, staged in `data/raw/`.

**License / terms risk:** Medium-high. The prepared data are public, but the original dataset is described as Kaggle data compiled from Yummly, with unknown original author in the Zelený documentation. Use as prototype data, not as final core, unless Run 3 confirms permissible use or substitutes a cleaner source.

**Reliability grade:** B- for prototype. It is large, structured, and well suited to the method, but not official and potentially biased toward an American recipe platform.

**Why selected:** It is the only reviewed source that simultaneously provides (1) cuisine labels, (2) ingredient lists, (3) enough coverage for at least 20 cuisines, and (4) direct public access without an API key.

## Selected fallback source

**Fallback source:** TheMealDB API.

**Source URLs:**

- `https://www.themealdb.com/`
- `https://www.themealdb.com/api.php`
- Example API endpoints: `list.php?a=list`, `filter.php?a=Canadian`, and `lookup.php?i=52772`

**Coverage:** The public site describes an open, crowd-sourced recipe database and the API page lists methods for meal search, lookup by ID, list all areas, filter by area, and ingredient lookup. The public home page showed 598 total meals and 877 ingredients at the time of access.

**Strength:** Cleaner access terms for educational API prototyping, explicit area fields, direct meal details.

**Weakness:** Much smaller than the What’s Cooking corpus and uneven by country/area; global cuisine similarity would be less stable.

**Reliability grade:** B for access openness; C+ for analysis coverage.

## Alternatives rejected or deferred

1. **Kaggle What’s Cooking raw competition download**
   - Rejected for Run 2 primary because Kaggle access/competition terms and login can become a blocker.
   - Good underlying dataset, but the GitHub-prepared long table is faster for prototype execution.

2. **RecipeDB**
   - Deferred. It is conceptually strong for world cuisines and has literature support, but access and data format require more confirmation than Run 2 allows.

3. **RecipeNLG**
   - Rejected for Run 2 primary because it is large and rich for recipe text generation but does not provide the clean cuisine/region labels needed for this geospatial prototype.

4. **Open Food Facts**
   - Deferred/rejected for primary because it is product-label data, not recipe/cuisine data. It may be useful for a later food-supply or ingredient-origin layer.

## Decision

Proceed with the What’s Cooking/Yummly-derived long table for the real-data prototype, while explicitly flagging license/platform-bias risk. Use TheMealDB as the fallback if source integrity or redistribution concerns require a cleaner but smaller public API-based prototype.

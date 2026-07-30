# Run 2 v2 Data Quality and Bias Audit

Created: 2026-04-29

## Corpus scale

- Recipes retained: **39,774**
- Cuisines retained: **20**
- Recipe--ingredient rows: **428,249**
- Raw ingredient strings: **6,714**
- Normalized ingredient labels: **5,936**
- Original cuisine--ingredient matrix shape: **20 cuisines × 1434 ingredients**

## Recipes per cuisine

| cuisine      |   recipe_count |
|:-------------|---------------:|
| italian      |           7838 |
| mexican      |           6438 |
| southern_us  |           4320 |
| indian       |           3003 |
| chinese      |           2673 |
| french       |           2646 |
| cajun_creole |           1546 |
| thai         |           1539 |
| japanese     |           1423 |
| greek        |           1175 |
| spanish      |            989 |
| korean       |            830 |
| vietnamese   |            825 |
| moroccan     |            821 |
| british      |            804 |
| filipino     |            755 |
| irish        |            667 |
| jamaican     |            526 |
| russian      |            489 |
| brazilian    |            467 |

## Ingredient counts by cuisine

| cuisine      |   unique_normalized_ingredients |
|:-------------|--------------------------------:|
| italian      |                            2524 |
| mexican      |                            2306 |
| southern_us  |                            2120 |
| french       |                            1817 |
| chinese      |                            1517 |
| indian       |                            1385 |
| cajun_creole |                            1328 |
| japanese     |                            1216 |
| thai         |                            1146 |
| spanish      |                            1064 |
| greek        |                            1000 |
| british      |                             991 |
| vietnamese   |                             931 |
| irish        |                             848 |
| moroccan     |                             803 |
| filipino     |                             803 |
| korean       |                             756 |
| russian      |                             724 |
| jamaican     |                             716 |
| brazilian    |                             713 |

## Cuisine-to-geography mapping confidence

| mapping_confidence   |   count |
|:---------------------|--------:|
| high                 |      14 |
| medium               |       3 |
| medium-low           |       3 |

## Major bias risks

1. **Recipe-platform bias.** The source is a prepared public version of a Kaggle/Yummly-derived corpus. It is strong for prototyping, but it likely reflects English-language recipe-platform conventions rather than a representative census of world cooking.
2. **Cuisine-label limits.** Labels such as `chinese`, `indian`, and `southern_us` are broad and internally diverse. Labels such as `cajun_creole` and `southern_us` are regional/diasporic and cannot be treated as nation-states.
3. **Ingredient normalization risk.** Normalization is rule-based and inherited from Run 2. It keeps the workflow reproducible, but ambiguous ingredients and spelling variants remain.
4. **Generic ingredient effects.** High-frequency staples such as salt, water, pepper, sugar, flour, butter, eggs, onions, and garlic can make distant cuisines appear similar. Run 2 v2 therefore applies an explicit generic-ingredient sensitivity model.
5. **Centroid geography risk.** Country or regional centroid coordinates simplify large or archipelagic cuisines. They are sufficient for prototype-level distance and corridor mapping, but Run 3 should improve them where possible.

## Data-quality implication for scope

The global model should remain a discovery layer. Stronger final claims should come from focused cases, especially East/Southeast Asia, where the available cuisine labels form a coherent geographic subset and have enough recipes/pairs for a modest spatial-inference claim.

## Most common normalized ingredients before v2 filtering

| normalized_ingredient   |   recipe_occurrences |   cuisine_prevalence |
|:------------------------|---------------------:|---------------------:|
| salt                    |                22843 |                   20 |
| garlic                  |                16607 |                   20 |
| black pepper            |                12952 |                   20 |
| onion                   |                11834 |                   20 |
| sugar                   |                 8516 |                   20 |
| oil                     |                 8066 |                   20 |
| olive oil               |                 7982 |                   20 |
| water                   |                 7776 |                   20 |
| butter                  |                 7640 |                   20 |
| egg                     |                 6332 |                   20 |
| green onion             |                 5811 |                   20 |
| all-purpose flour       |                 4786 |                   20 |
| soy sauce               |                 4350 |                   20 |
| cilantro                |                 4120 |                   20 |
| ginger                  |                 4078 |                   20 |
| cumin                   |                 3675 |                   20 |
| parsley                 |                 3567 |                   20 |
| tomato                  |                 3215 |                   20 |
| carrot                  |                 3110 |                   20 |
| lemon juice             |                 3066 |                   20 |
| chicken breast          |                 3039 |                   20 |
| milk                    |                 3023 |                   20 |
| parmesan cheese         |                 2789 |                   19 |
| extra-virgin olive oil  |                 2747 |                   20 |
| oregano                 |                 2518 |                   17 |
| tomatoe                 |                 2452 |                   19 |
| lime juice              |                 2427 |                   19 |
| brown sugar             |                 2228 |                   20 |
| chile powder            |                 2174 |                   19 |
| chicken broth           |                 2084 |                   20 |

# Cuisine Matrix Summary

Input: `data/processed/cuisine_ingredient_long.csv`
Output: `data/processed/cuisine_ingredient_matrix.csv`

Retained cuisines: 20
Retained ingredients: 1434
Matrix values: cuisine-level recipe prevalence for each normalized ingredient.
Universal ingredients removed: yes (`salt`, `water`, generic `sugar`, generic `oil`, generic `pepper`).
Rare ingredients removed: ingredients appearing in fewer than 20 recipes globally.
Sparsity: 0.490

## Recipes per cuisine

| cuisine      |   recipe_id |
|:-------------|------------:|
| brazilian    |         467 |
| british      |         804 |
| cajun_creole |        1546 |
| chinese      |        2673 |
| filipino     |         755 |
| french       |        2646 |
| greek        |        1175 |
| indian       |        3003 |
| irish        |         667 |
| italian      |        7838 |
| jamaican     |         526 |
| japanese     |        1423 |
| korean       |         830 |
| mexican      |        6438 |
| moroccan     |         821 |
| russian      |         489 |
| southern_us  |        4320 |
| spanish      |         989 |
| thai         |        1539 |
| vietnamese   |         825 |

## Top retained ingredients by recipe count

| normalized_ingredient   |   recipe_count |
|:------------------------|---------------:|
| garlic                  |          16607 |
| onion                   |          11834 |
| olive oil               |           7982 |
| butter                  |           7640 |
| egg                     |           6332 |
| green onion             |           5811 |
| all-purpose flour       |           4786 |
| soy sauce               |           4350 |
| cilantro                |           4120 |
| ginger                  |           4078 |
| cumin                   |           3675 |
| parsley                 |           3567 |
| tomato                  |           3215 |
| carrot                  |           3110 |
| lemon juice             |           3066 |
| chicken breast          |           3039 |
| milk                    |           3023 |
| parmesan cheese         |           2789 |
| extra-virgin olive oil  |           2747 |
| oregano                 |           2518 |
| tomatoe                 |           2452 |
| lime juice              |           2427 |
| brown sugar             |           2228 |
| chile powder            |           2174 |
| chicken broth           |           2084 |

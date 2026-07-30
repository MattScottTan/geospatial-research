# Similarity Summary

Input: `data/processed/cuisine_ingredient_matrix.csv`
Cosine output: `data/processed/cuisine_similarity_cosine.csv`
Jaccard output: `data/processed/cuisine_similarity_jaccard.csv`

Cosine similarity uses cuisine-level ingredient-prevalence vectors.
Jaccard similarity uses binary ingredient presence after a 0.5% within-cuisine prevalence threshold.

## Top cosine-similar cuisine pairs

| cuisine_a   | cuisine_b   |   cosine |   jaccard |
|:------------|:------------|---------:|----------:|
| british     | southern_us | 0.918618 |  0.419643 |
| thai        | vietnamese  | 0.916013 |  0.544892 |
| british     | irish       | 0.914041 |  0.468439 |
| irish       | southern_us | 0.895099 |  0.435331 |
| chinese     | korean      | 0.882952 |  0.421725 |
| irish       | russian     | 0.852925 |  0.44127  |
| british     | russian     | 0.849866 |  0.45122  |
| italian     | spanish     | 0.841726 |  0.394805 |
| chinese     | japanese    | 0.824796 |  0.419453 |
| british     | french      | 0.821962 |  0.431548 |
| russian     | southern_us | 0.820853 |  0.377465 |
| french      | southern_us | 0.814417 |  0.391549 |
| japanese    | korean      | 0.812014 |  0.394737 |
| french      | irish       | 0.811095 |  0.443396 |
| brazilian   | spanish     | 0.804487 |  0.362398 |

## Top Jaccard-similar cuisine pairs

| cuisine_a    | cuisine_b   |   cosine |   jaccard |
|:-------------|:------------|---------:|----------:|
| thai         | vietnamese  | 0.916013 |  0.544892 |
| cajun_creole | southern_us | 0.627664 |  0.482866 |
| british      | irish       | 0.914041 |  0.468439 |
| french       | spanish     | 0.719881 |  0.452055 |
| british      | russian     | 0.849866 |  0.45122  |
| french       | irish       | 0.811095 |  0.443396 |
| irish        | russian     | 0.852925 |  0.44127  |
| chinese      | thai        | 0.676768 |  0.441261 |
| irish        | southern_us | 0.895099 |  0.435331 |
| french       | russian     | 0.798146 |  0.43314  |
| british      | french      | 0.821962 |  0.431548 |
| french       | italian     | 0.768205 |  0.426554 |
| greek        | italian     | 0.79076  |  0.424332 |
| chinese      | korean      | 0.882952 |  0.421725 |
| british      | southern_us | 0.918618 |  0.419643 |

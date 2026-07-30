# Flavor Chemistry Feasibility Decision

Created: 2026-04-28

## Decision

**Recommendation for Run 3: include flavor chemistry as a secondary, conditional layer; do not make it the core model until a bulk match test succeeds.**

The Run 2 spatial core works without flavor chemistry. Flavor chemistry would strengthen the project's food-science identity and create a clear role for Prof. Pia Sorensen, but it should not delay the residual-corridor analysis. The correct Run 3 threshold is:

- **Include as a full section** if at least 35% of the top 300 normalized ingredients, weighted by recipe prevalence, can be matched to FlavorDB/FooDB-style ingredient entries, or if at least 60% of the top 75 high-prevalence ingredients can be matched.
- **Use as a sidebar/case study** if match rate is lower but interpretable examples exist, such as garlic/ginger/soy sauce clusters or spice-family corridors.
- **Drop from final analysis** if ingredient names cannot be matched without excessive manual judgment.

## Candidate sources

| Source | URL | Status | License / usage risk | Notes |
|---|---|---|---|---|
| FlavorDB | `https://cosylab.iiitd.edu.in/flavordb/` | Metadata verified, not downloaded | CC BY-NC-SA 3.0 listed on site; bulk access needs confirmation | Strong fit because it links ingredients to flavor molecules and categories |
| FooDB | `https://foodb.ca/` | Metadata verified, not downloaded | CC BY-NC 4.0 shown; commercial redistribution permission caveats | Strong backup for food-constituent metadata |
| Manual top-ingredient matching | n/a | Not performed in Run 2 | Depends on source terms | Useful if limited to top 50–100 ingredients with Pia review |

## Why this is feasible but not yet proven

Run 2 normalized 6,714 raw ingredient strings into 5,936 normalized ingredient labels. The cuisine matrix retained 1,434 non-universal ingredients. Many high-frequency labels are natural foods or common ingredients that should have good chemistry matches, but several are compound/prepared labels or culinary descriptions rather than chemical-source ingredients.

## Top high-prevalence ingredients needing match review

| normalized_ingredient   |   recipe_id |
|:------------------------|------------:|
| salt                    |       22843 |
| garlic                  |       16607 |
| black pepper            |       12952 |
| onion                   |       11834 |
| sugar                   |        8516 |
| oil                     |        8066 |
| olive oil               |        7982 |
| water                   |        7776 |
| butter                  |        7640 |
| egg                     |        6332 |
| green onion             |        5811 |
| all-purpose flour       |        4786 |
| soy sauce               |        4350 |
| cilantro                |        4120 |
| ginger                  |        4078 |
| cumin                   |        3675 |
| parsley                 |        3567 |
| tomato                  |        3215 |
| carrot                  |        3110 |
| lemon juice             |        3066 |
| chicken breast          |        3039 |
| milk                    |        3023 |
| parmesan cheese         |        2789 |
| extra-virgin olive oil  |        2747 |
| oregano                 |        2518 |

## Scientific interpretation risks

1. **Ingredient names are not sensory outcomes.** A recipe containing garlic does not mean the final dish has the same sensory profile across cuisines.
2. **Preparation changes chemistry.** Fermentation, roasting, frying, boiling, and drying can change volatile compounds.
3. **Compound databases are not cuisine databases.** FlavorDB/FooDB entries are ingredient-level; the project must aggregate cautiously.
4. **Ingredient granularity matters.** `soy sauce`, `green onion`, `chile powder`, and `tomatoe/tomato` require normalization and domain review.
5. **Similarity may be dominated by generic staples.** Universal/common ingredients must remain downweighted or sensitivity-tested.

## How to use Pia

Ask Pia to review:

- Whether the top 50–100 normalized ingredients are scientifically sensible units.
- Which ingredients should be merged, separated, or treated as preparation-dependent.
- Whether flavor-molecule overlap is a defensible proxy for sensory similarity.
- Which chemical families or ingredient groups might create meaningful culinary corridors.
- Whether fermentation should appear only as an interpretive sidebar or as a small, data-backed case study.

## Run 3 implementation path

1. Acquire or export FlavorDB/FooDB ingredient lists and compound mappings.
2. Create `data/crosswalks/ingredient_flavor_source_crosswalk.csv`.
3. Match top ingredients first, using exact, alias, and manually reviewed matches.
4. Compute weighted flavor-compound vectors by cuisine.
5. Compare ingredient-similarity residuals with flavor-similarity residuals.
6. Keep all unmatched or ambiguous ingredients in a transparent audit file.

## Bottom line

Flavor chemistry is worth including if Run 3 can validate the match rate quickly. The final Fisher project should remain grounded in GIS: flavor chemistry should explain or complicate residual culinary corridors, not replace the spatial analysis.


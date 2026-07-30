# Feasibility Smoke Test Log

Date run: 2026-04-28

## Task

Run a minimal code/data feasibility check for the Fisher food-geography project without building a full production pipeline.

## Runtime context

- Script: `scripts/00_feasibility_smoke_test.py`
- Working directory: `/mnt/data`
- Inputs use relative paths.
- No API keys, tokens, or credentials were used.
- Local Python/container internet access failed with DNS resolution errors, so the test used a small manually transcribed sample from accessible browser/API snippets rather than live downloading.

## Inputs

- `data/samples/cuisine_ingredient_sample.csv`
- Source notes in sample file:
  - TheMealDB Arrabiata endpoint: `https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata`
  - TheMealDB Shakshuka endpoint: `https://www.themealdb.com/api/json/v1/1/search.php?s=Shakshuka`
  - TheMealDB Sushi search snippet from browser search results
- License/usage note: TheMealDB presents itself as a free, crowd-sourced recipe API. This source is used here only as a toy smoke test, not as a final core dataset.
- Date accessed: 2026-04-28.

## Command run

```bash
cd /mnt/data && python scripts/00_feasibility_smoke_test.py
```

## Outputs created

- `outputs/pilot_cuisine_ingredient_matrix.csv`
- `outputs/pilot_similarity_edges.csv`
- `outputs/pilot_smoke_test_summary.json`
- `figures/pilot_map_or_chart.png`

## What the script did

1. Loaded four recipe/cuisine rows.
2. Normalized basic ingredient aliases such as chopped/cherry tomatoes to `tomato`, red chilli/chilli flakes/cayenne to `chilli`, eggs to `egg`, and Parmigiano/Feta to `cheese`.
3. Built a recipe/cuisine-by-ingredient count matrix.
4. Computed pairwise cosine similarity between cuisine ingredient vectors.
5. Wrote an edge list with similarity scores and approximate coordinate distances.
6. Created a schematic coordinate/network figure showing similarity links.

## Smoke-test results

- Recipes loaded: 4
- Unique normalized ingredients: 20
- Highest similarity pair: Italian (Italy) and Egyptian (Egypt), cosine similarity 0.5893.
- The output demonstrates that the proposed Run 2 workflow is executable: ingredient parsing → vectorization → similarity matrix → edge list → geospatial/network visualization.

## What this supports

The smoke test supports the feasibility of a Run 2 prototype focused on cuisine similarity and residual corridor mapping. It does **not** prove any substantive culinary claim because the sample is deliberately tiny and source-limited.

## Required improvements for Run 2

- Replace toy sample with a documented corpus such as RecipeDB or a vetted open recipe dataset.
- Download Natural Earth and use actual base-map geometry instead of schematic longitude/latitude axes.
- Use CEPII GeoDist for actual pairwise distance, not coordinate-degree approximation.
- Add migration/trade/agriculture covariates from UN DESA, UN Comtrade, and FAOSTAT.
- Add sample-size thresholds and robust ingredient normalization.

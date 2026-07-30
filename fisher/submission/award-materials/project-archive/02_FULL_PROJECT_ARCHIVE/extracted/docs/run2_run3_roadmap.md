# Run 2 and Run 3 Roadmap

## Run 2: Working Prototype

Goal: produce a defensible prototype with real data, first maps, and preliminary interpretation.

### Proposed Run 2 tasks

1. Confirm RecipeDB or alternative recipe corpus access and license.
2. Download or create a vetted recipe/ingredient table.
3. Build `data/crosswalks/ingredient_alias_crosswalk.csv`.
4. Build `data/crosswalks/country_code_crosswalk.csv`.
5. Download Natural Earth Admin 0 country boundaries.
6. Download CEPII GeoDist dyadic distance/culture variables.
7. Build cuisine ingredient vectors for at least 20 cuisines/regions or a defensible narrower corridor.
8. Compute cosine/Jaccard/Pearson cuisine similarity matrices.
9. Create a first cuisine similarity cluster map or dendrogram.
10. Fit distance-only baseline model and create distance-decay plot.
11. Compute residuals and create first culinary-corridor map.
12. Download one migration or trade covariate and test overlay/explanatory model.
13. Draft a 1–2 page prototype interpretation with limitations.
14. Decide whether flavor chemistry is feasible for Run 3.
15. Update project scope: global, regional, or corridor-based.

### Run 2 handoff criteria

- At least one real recipe/ingredient source is parsed.
- At least 20 cuisines/regions or a well-justified corridor subset is represented.
- At least one real map and one model/plot exist.
- Primary/fallback scope is finalized.
- Remaining data blockers are explicit.

## Run 3: Polished Fisher Submission Package

Goal: turn the prototype into a polished Fisher-facing deliverable.

### Proposed Run 3 tasks

1. Finalize data cleaning and crosswalks.
2. Add migration, trade, agriculture, and language/colonial covariates.
3. Run final spatial/residual model with robustness checks.
4. Add flavor chemistry layer if ingredient matching passes quality threshold.
5. Add fermentation sidebar if Pia feedback and data support it.
6. Produce final maps: cuisine clusters, distance decay, residual corridors, explanatory overlays.
7. Write final narrative text for StoryMap/PDF.
8. Create methods appendix with data-source reliability table.
9. Prepare concise Fisher abstract and title.
10. Build ArcGIS StoryMap or web-map-heavy deliverable.
11. Create static PDF/poster backup.
12. Review with Pia and revise scientific claims.
13. Review against Fisher rubric and revise visuals.
14. Finalize citations and data/source transparency.
15. Package code/notebook appendix without secrets or large unnecessary data.

### Run 3 handoff criteria

- Final deliverable is submission-ready.
- All major maps/figures have captions and data-source notes.
- Scientific claims have been reviewed or caveated.
- Methodology is reproducible enough for evaluation.
- StoryMap/PDF clearly demonstrates that GIS produced the core insight.

## Current project decision for Run 2

Use the **Cuisine Similarity + Residual Culinary Corridors** core first. Add flavor chemistry only after ingredient matching is stable. Keep fermentation as a sidebar unless high-quality geocoded microbiome data is confirmed.

# 0. Snapshot
- Job Type: Mixed — Code/Data Prototype + Research/Synthesis + Writing/Exposition.
- Run: Fisher Award food/geospatial project, Run 2 working prototype.
- Primary Deliverables: real-data cuisine-similarity prototype; cleaned cuisine–ingredient table; cuisine similarity matrix; distance baseline; residual culinary-corridor map; one migration/trade/cultural/climate overlay test; flavor-chemistry feasibility decision; short prototype interpretation; updated Run 3 handoff.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as food-science mentor; Harvard Center for Geographic Analysis / Fisher Prize evaluators; future Run 3 worker producing polished Fisher submission.
- Prior Inputs: Run 1 artifacts in `docs/`, `data/`, `figures/`, `outputs/`, and `scripts/`, especially `docs/fisher_project_blueprint.md`, `docs/recommendation_memo.md`, `docs/run2_run3_roadmap.md`, and `data/data_source_register.csv`.
- Constraints: useful output needed quickly; use real data where possible; maximize usable data but grade reliability; prototype only, not final production code; no polished StoryMap in this run; no full final Fisher essay in this run; no direct contact with Pia; no secrets/API keys committed; source links and access dates required for all external datasets; fermentation remains secondary unless unusually strong geocoded data is discovered.

# 1. Goal
Build a working prototype for **Culinary Corridors: Mapping Food Similarity, Migration, Trade, and Flavor Chemistry**. This run should move from Run 1’s blueprint to real-data evidence: select and parse a recipe/ingredient corpus, construct cuisine/region ingredient representations, compute cuisine similarity, compare similarity against geographic distance, identify residual “culinary corridor” pairs, create the first real Fisher-style maps/figures, test one explanatory overlay such as migration or trade, and decide whether flavor chemistry is feasible for Run 3. The output should make clear whether the final Fisher submission should remain global, narrow to a corridor/region, or fall back to the simpler cuisine-similarity + migration/trade version.

- Definition of Done:
  - A primary recipe/ingredient dataset and one fallback are selected in `data/run2_dataset_selection_memo.md`, with access, license/terms, coverage, reliability, and risk documented.
  - A real cleaned cuisine–ingredient long table exists at `data/processed/cuisine_ingredient_long.csv`, representing at least 20 cuisines/regions, or a narrower corridor subset justified in `docs/scope_decision_memo.md`.
  - Ingredient normalization is documented in `data/crosswalks/ingredient_alias_crosswalk.csv`, including confidence or rule notes for ambiguous mappings.
  - Cuisine/region geographic mapping is documented in `data/crosswalks/cuisine_geo_crosswalk.csv`, with ISO/country/region codes, coordinates, and confidence notes.
  - A cuisine–ingredient matrix exists at `data/processed/cuisine_ingredient_matrix.csv`.
  - At least two cuisine similarity matrices are produced in `data/processed/`, including cosine similarity and one robustness metric such as Jaccard or Pearson.
  - A dyadic cuisine-pair table exists at `data/processed/cuisine_pair_model_table.csv`, containing cuisine pair identifiers, observed similarity, geographic distance, and any available covariates.
  - A distance-only baseline model is run and summarized in `outputs/distance_baseline_model_summary.md`.
  - Residual culinary-corridor pairs are computed and saved at `data/processed/residual_culinary_corridors.csv`.
  - At least three real figures are created: `figures/run2_cuisine_similarity_heatmap.png`, `figures/run2_distance_decay_plot.png`, and `figures/run2_residual_corridor_map.png`.
  - One explanatory overlay is tested using migration, trade, language/colonial link, climate/agriculture, or similar data, with results saved in `outputs/overlay_test_summary.md` and at least one supporting figure or table.
  - A flavor-chemistry feasibility decision exists at `docs/flavor_chemistry_feasibility_decision.md`, including match-rate expectations, source risks, and whether to include FlavorDB/FooDB-style work in Run 3.
  - A short prototype interpretation exists at `docs/run2_prototype_interpretation.md`, explaining the real preliminary findings, limitations, and Fisher relevance.
  - `docs/run3_handoff_plan.md` states whether Run 3 should proceed as global, regional/corridor-based, or fallback-only, with concrete next tasks.
  - `WORK.md` Results and Learnings are updated after each worker iteration.
- Non-goals:
  - Do not write the final Fisher submission essay/report.
  - Do not create a polished ArcGIS StoryMap or final design asset.
  - Do not build a production-grade pipeline beyond what is needed for a reproducible prototype.
  - Do not make fermentation central unless the worker discovers strong, geocoded, analyzable microbiome/fermentation data and records why it should replace the current plan.
  - Do not overclaim causality from migration/trade/culture overlays; treat them as explanatory associations unless the model design justifies stronger language.
  - Do not silently use scraped, undocumented, or license-unclear recipe data as if it were reliable; flag risk explicitly.

# 2. Acceptance Checks
- Data checks:
  - Every external dataset used must have provider, URL, date accessed, license/terms or usage risk, local path, and reliability grade recorded in `data/run2_data_access_log.md`.
  - Recipe/ingredient data must include cuisine/region labels and ingredient lists; if labels are missing or too noisy, the dataset cannot be the primary source.
  - Prototype scope must include at least 20 cuisines/regions unless a narrower corridor/region is justified by data quality and Fisher value.
  - Cuisine labels must not be treated as automatically equivalent to modern nation-state borders; confidence notes are required in `data/crosswalks/cuisine_geo_crosswalk.csv`.
  - Ingredient aliasing must preserve raw ingredient names in at least one column before normalization.
  - Large data downloads should be avoided unless necessary; sample or subset first, then scale only if needed.
- Code checks:
  - All scripts must run from the project root using relative paths.
  - Scripts must write outputs only under `data/processed/`, `outputs/`, or `figures/` unless task-specific paths say otherwise.
  - No API tokens, credentials, or personal secrets may appear in code, logs, notebooks, or data files.
  - Each script must fail clearly with an actionable error if an expected input file is missing.
  - A single reproducibility note at `outputs/run2_reproducibility_log.md` must list commands run, environment assumptions, and outputs produced.
  - Code must remain prototype-scoped: clarity and reproducibility matter more than architecture, packaging, or CI.
- Analysis checks:
  - Similarity results must include at least cosine similarity and one robustness metric.
  - The distance baseline must use actual geographic coordinates or an accepted dyadic distance dataset; it cannot use arbitrary hand-coded distances.
  - Residual corridor ranking must be computed from observed-minus-predicted similarity or an explicitly documented equivalent.
  - At least one model/plot must test whether similarity decays with distance.
  - Overlay analysis must be labeled exploratory unless the model includes appropriate controls and robustness checks.
  - Universal ingredients such as water, salt, sugar, oil, or generic spices must be handled explicitly by removal, downweighting, category flags, or sensitivity notes.
- GIS/visualization checks:
  - `figures/run2_residual_corridor_map.png` must use real coordinates and show top positive residual links or a justified geographic subset.
  - Every figure must have a caption in `figures/run2_figure_captions.md` explaining data, method, interpretation, and limitation.
  - Visuals should be Fisher-facing enough to judge promise, but not polished final assets.
- Research/writing checks:
  - `docs/run2_prototype_interpretation.md` must distinguish observed preliminary patterns from hypotheses for Run 3.
  - `docs/flavor_chemistry_feasibility_decision.md` must explain why flavor chemistry is included, delayed, or dropped.
  - `docs/run3_handoff_plan.md` must contain a clear go/no-go decision for global scope, narrower corridor scope, and flavor chemistry inclusion.
  - All factual claims about datasets, licenses, or prior literature must include source links or citations.

# 3. Plan
- Start by reading Run 1 outputs and creating a concise Run 2 setup note so the worker inherits the current recommendation rather than rediscovering it.
- Select and access-test the primary recipe/ingredient corpus first; if blocked, immediately switch to a documented fallback instead of stalling.
- Build the minimum viable data spine: raw recipes → normalized ingredient long table → cuisine–ingredient matrix → similarity matrices.
- Build the geographic spine: cuisine/region crosswalk → coordinates/ISO codes → pairwise distance table.
- Combine food similarity and distance into a dyadic model table; run the distance-only baseline and compute residuals.
- Produce three core visuals before adding complexity: similarity heatmap/cluster view, distance-decay plot, and residual corridor map.
- Add exactly one explanatory overlay for Run 2, prioritizing the easiest high-value source: migration or trade; defer additional covariates to Run 3.
- Make a conservative flavor-chemistry feasibility decision using source availability and ingredient-match plausibility; do not force chemistry into the prototype if the spatial core is not stable.
- Dependencies / ordering logic: dataset selection precedes cleaning; cleaning precedes similarity; cuisine–geo crosswalk precedes distance; distance model precedes residual map; residual map precedes interpretation; interpretation precedes Run 3 handoff.
- Risk & mitigation:
  - If recipe corpus access is blocked, add a BLOCKED note and use the best documented fallback source for the prototype.
  - If global cuisine labels are noisy, narrow to a corridor/region and document why this increases validity.
  - If ingredient normalization becomes too subjective, keep raw names, use conservative aliasing, and flag uncertain mappings for Pia review.
  - If distance has weak explanatory power, still map residuals but frame the project around “food similarity does not reduce to geography” rather than “distance predicts food.”
  - If migration/trade overlay is unavailable or too slow, use language/colonial/region link as a lighter explanatory overlay and record migration/trade for Run 3.
  - If the residual corridor map is visually weak, create a heatmap/network figure and recommend narrowed scope for Run 3.

# 4. Tasks
- [ ] [S01] Create `outputs/run2_setup_note.md` — Inputs needed: `docs/fisher_project_blueprint.md`, `docs/recommendation_memo.md`, `docs/run2_run3_roadmap.md`, `data/data_source_register.csv`. Done when: the file summarizes Run 1 recommendations, Run 2 objective, expected outputs, and any missing prior artifacts.
- [ ] [D01] Create `data/run2_dataset_selection_memo.md` — Inputs needed: `data/data_source_register.csv` and public dataset pages/repositories. Done when: one primary recipe/ingredient dataset and one fallback are selected, with coverage, cuisine-label quality, ingredient quality, access method, license/terms risk, reliability grade, and reason for rejection of at least two alternatives.
- [ ] [D02] Create `data/run2_data_access_log.md` — Inputs needed: chosen primary/fallback recipe source plus base GIS/distance/overlay sources. Done when: every external source used or attempted has provider, URL, date accessed, access status, license/usage note, local path if downloaded, and next action or blocker.
- [ ] [D03] Create `data/raw/recipe_source_manifest.md` — Inputs needed: selected recipe/ingredient source. Done when: the file records raw data filenames/paths, source URLs, schema notes, sample size, cuisine-label fields, ingredient fields, and whether the raw source can be redistributed or only referenced.
- [ ] [C01] Create `scripts/01_acquire_or_stage_recipe_data.py` — Inputs needed: selected recipe/ingredient source from `data/run2_dataset_selection_memo.md`. Done when: the script stages a small-to-medium usable recipe sample under `data/raw/` or exits with a clear instruction for manual download, and records staged paths in `data/raw/recipe_source_manifest.md`.
- [ ] [D04] Create `data/crosswalks/ingredient_alias_crosswalk.csv` — Inputs needed: raw ingredient names from staged recipe data. Done when: the file contains raw ingredient, normalized ingredient, rule/source, confidence, and notes columns for all high-frequency ingredients and known ambiguous aliases.
- [ ] [C02] Create `scripts/02_clean_recipe_ingredients.py` — Inputs needed: `data/raw/` recipe sample and `data/crosswalks/ingredient_alias_crosswalk.csv`. Done when: the script writes `data/processed/cuisine_ingredient_long.csv` with raw ingredient, normalized ingredient, cuisine/region label, recipe identifier, and frequency/count fields.
- [ ] [D05] Create `docs/scope_decision_memo.md` — Inputs needed: `data/processed/cuisine_ingredient_long.csv`. Done when: the file states whether Run 2 proceeds globally, regionally, or by corridor; reports number of cuisines/regions and recipes retained; justifies any scope below 20 cuisines/regions.
- [ ] [D06] Create `data/crosswalks/cuisine_geo_crosswalk.csv` — Inputs needed: retained cuisine/region labels from `docs/scope_decision_memo.md`; public country/region identifiers and coordinates. Done when: each retained cuisine/region has cuisine label, mapped country/region, ISO code if applicable, latitude, longitude, mapping confidence, and caveat notes.
- [ ] [C03] Create `scripts/03_build_cuisine_matrix.py` — Inputs needed: `data/processed/cuisine_ingredient_long.csv`. Done when: the script writes `data/processed/cuisine_ingredient_matrix.csv` and a short summary to `outputs/cuisine_matrix_summary.md` with shape, sparsity, top ingredients, and retained cuisines.
- [ ] [C04] Create `scripts/04_compute_similarity.py` — Inputs needed: `data/processed/cuisine_ingredient_matrix.csv`. Done when: the script writes `data/processed/cuisine_similarity_cosine.csv`, `data/processed/cuisine_similarity_jaccard.csv` or `data/processed/cuisine_similarity_pearson.csv`, and `outputs/similarity_summary.md`.
- [ ] [V01] Create `figures/run2_cuisine_similarity_heatmap.png` — Inputs needed: similarity matrices from C04. Done when: a real-data heatmap, dendrogram, or clustered similarity chart is saved and visually readable.
- [ ] [D07] Create `data/external/geography_source_manifest.md` — Inputs needed: base map/distance sources such as Natural Earth and/or CEPII GeoDist. Done when: the file records selected geography source(s), URL(s), local paths or access instructions, variables used, date accessed, and license/usage notes.
- [ ] [C05] Create `scripts/05_build_distance_pairs.py` — Inputs needed: `data/crosswalks/cuisine_geo_crosswalk.csv`; geography/distance source from D07. Done when: the script writes `data/processed/cuisine_distance_pairs.csv` with cuisine pair IDs, coordinates/ISO codes, distance variable, and source notes.
- [ ] [C06] Create `scripts/06_build_pair_model_table.py` — Inputs needed: `data/processed/cuisine_distance_pairs.csv` and similarity matrices from C04. Done when: the script writes `data/processed/cuisine_pair_model_table.csv` containing each pair’s observed similarity, distance, log-distance, and retained metadata.
- [ ] [C07] Create `scripts/07_fit_distance_baseline.py` — Inputs needed: `data/processed/cuisine_pair_model_table.csv`. Done when: the script fits a distance-only baseline, writes predictions/residuals to `data/processed/residual_culinary_corridors.csv`, and writes `outputs/distance_baseline_model_summary.md`.
- [ ] [V02] Create `figures/run2_distance_decay_plot.png` — Inputs needed: outputs from C07. Done when: the plot shows cuisine similarity against geographic distance/log-distance with fitted trend or binned summary.
- [ ] [V03] Create `figures/run2_residual_corridor_map.png` — Inputs needed: `data/processed/residual_culinary_corridors.csv`; `data/crosswalks/cuisine_geo_crosswalk.csv`. Done when: a real-coordinate map or geographic network plot shows top positive residual culinary corridors, with labels or legend sufficient for interpretation.
- [ ] [D08] Create `data/overlay_source_selection_memo.md` — Inputs needed: `data/data_source_register.csv`, `data/processed/residual_culinary_corridors.csv`, and public migration/trade/culture/climate data options. Done when: one overlay source is selected for Run 2, at least two alternatives are rejected or deferred, and rationale is based on access, joinability, explanatory value, and time.
- [ ] [C08] Create `scripts/08_test_overlay_covariate.py` — Inputs needed: selected overlay source from D08 and `data/processed/cuisine_pair_model_table.csv` or `data/processed/residual_culinary_corridors.csv`. Done when: the script joins or compares one explanatory covariate to cuisine similarity/residuals and writes output data to `data/processed/overlay_test_results.csv`.
- [ ] [R01] Create `outputs/overlay_test_summary.md` — Inputs needed: `data/processed/overlay_test_results.csv`. Done when: the file reports what overlay was tested, join success rate, preliminary association or descriptive pattern, limitations, and whether the covariate should be expanded in Run 3.
- [ ] [V04] Create `figures/run2_overlay_test_figure.png` — Inputs needed: `data/processed/overlay_test_results.csv`. Done when: one table-like chart, scatterplot, map, or network visual summarizes the overlay test.
- [ ] [R02] Create `docs/flavor_chemistry_feasibility_decision.md` — Inputs needed: `data/processed/cuisine_ingredient_long.csv`, candidate FlavorDB/FooDB-style source pages or files, and Run 1 flavor-method notes if available. Done when: the file estimates ingredient match feasibility, source access/licensing, scientific interpretation risks, Pia questions, and a clear include/defer/drop recommendation for Run 3.
- [ ] [V05] Create `figures/run2_figure_captions.md` — Inputs needed: V01, V02, V03, and V04 if available. Done when: each figure has a caption explaining data, method, what it shows, what it does not prove, and how it should improve in Run 3.
- [ ] [C09] Create `outputs/run2_reproducibility_log.md` — Inputs needed: all scripts run in Run 2. Done when: the file lists commands run from project root, runtime assumptions, package needs, input/output paths, and any failed commands or manual steps.
- [ ] [R03] Create `docs/run2_prototype_interpretation.md` — Inputs needed: model summaries, residual corridors, figures, captions, overlay summary, and scope decision. Done when: the file gives a 1–2 page interpretation of preliminary findings, Fisher relevance, limitations, and what cannot yet be claimed.
- [ ] [R04] Create `docs/run3_handoff_plan.md` — Inputs needed: `docs/run2_prototype_interpretation.md`, `docs/flavor_chemistry_feasibility_decision.md`, and `outputs/overlay_test_summary.md`. Done when: the file states global vs regional/corridor go/no-go, primary vs fallback project decision, flavor chemistry decision, remaining blockers, and 8–15 concrete Run 3 tasks.
- [ ] [Q01] Update `WORK.md` Results section with final Run 2 artifact checklist — Inputs needed: all completed artifacts. Done when: Results lists every created artifact path, verification status, key model/figure outputs, and any BLOCKED items with exact missing input.
- [ ] [Q02] Update `WORK.md` Learnings section with Run 2 pitfalls and recommendations — Inputs needed: all completed artifacts and errors encountered. Done when: Learnings records data-quality issues, source limitations, modeling pitfalls, mapping lessons, promising findings, and recommendations for Run 3.

# 5. Worker Driver Prompt
You are the worker for Run 2 of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition. Do not drift into final submission writing, polished StoryMap creation, broad literature review, or production engineering.

After each iteration, update `WORK.md` immediately: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, commands, outputs, and verification status; record Learnings with pitfalls, source issues, modeling decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing input/access/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If recipe data access fails, switch to the documented fallback source and continue building the prototype unless all viable recipe sources are blocked.

Use the acceptance checks for a Mixed code/data/research/writing job. Every dataset must have source, access, license/usage risk, and reliability notes. Scripts must use relative paths, avoid secrets, and write outputs to documented locations. All analysis claims must be conservative and preliminary. The main target is a working real-data prototype: cuisine–ingredient table, similarity matrices, distance baseline, residual corridor map, one overlay test, flavor-chemistry feasibility decision, and Run 3 handoff.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, list every artifact produced, whether the primary project remains viable, whether scope should be global or narrowed, whether flavor chemistry should be included in Run 3, and what exact inputs are needed next.

# 6. Learnings

# 7. Results

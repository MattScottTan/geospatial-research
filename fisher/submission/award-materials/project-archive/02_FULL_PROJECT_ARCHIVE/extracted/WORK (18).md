# 0. Snapshot
- Job Type: Mixed — Code/Data Prototype Amendment + Geospatial Analysis + Research/Synthesis + Writing/Exposition.
- Run: Fisher Award food/geospatial project, Run 2 Version 2 amendment run.
- Primary Deliverables: amended Run 2 prototype with defensible scope; scope-lock memo; data-quality and bias audit; filtered/sensitivity cuisine-similarity model; focused East/Southeast Asia primary case; focused Iberian/Atlantic secondary case if data supports it; additional geospatial-only analysis; revised figures; revised prototype interpretation; updated Run 3 handoff.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as food-science mentor; Harvard Center for Geographic Analysis / Fisher Prize evaluators; future Run 3 worker producing the polished Fisher submission.
- Prior Inputs: completed Run 1 and Run 2 artifacts, especially `docs/run2_prototype_interpretation.md`, `outputs/distance_baseline_model_summary.md`, `data/processed/cuisine_pair_model_table.csv`, `data/processed/residual_culinary_corridors.csv`, `data/processed/cuisine_ingredient_long.csv`, `data/processed/cuisine_ingredient_matrix.csv`, `data/crosswalks/cuisine_geo_crosswalk.csv`, `data/crosswalks/ingredient_alias_crosswalk.csv`, `figures/run2_residual_corridor_map.png`, and `docs/run3_handoff_plan.md`.
- Constraints: preserve prior Run 2 work unless superseded; do not widen scope; use real existing data where possible; conclusions must be strong but modest; global results are a discovery layer, not causal proof; no polished StoryMap; no final Fisher essay; no direct contact with Pia; no secrets/API keys; all new external sources must have source/access/license notes; any additional geospatial analysis must be feasible within a prototype run.

# 1. Goal
Amend the completed Run 2 prototype so that the Fisher project has a defensible scope and stronger geospatial identity. Run 2 Version 2 should convert the broad global result into a scoped spatial-inference prototype: use the global 20-cuisine model as a discovery screen, then focus the strongest interpretation on a primary East/Southeast Asia corridor case and, if supported, a secondary Iberian/Atlantic corridor case. The worker should add geospatial analyses whose insights cannot be obtained from non-spatial food data alone, such as path/connectivity-aware distance proxies, residual bridge scores, boundary/permeability checks, or spatial clustering/outlier summaries. The run must preserve conservative claims: identify candidate culinary corridors and spatial structure, but do not claim causal proof of migration, trade, or colonial exchange.

- Definition of Done:
  - Existing Run 2 artifacts are audited in `data/run2v2_existing_artifact_audit.csv`, with each required input marked found, missing, stale, or superseded.
  - A scope-lock decision exists at `docs/run2v2_scope_lock_decision_memo.md`, explicitly defining: global discovery layer, primary East/Southeast Asia case, secondary Iberian/Atlantic case if feasible, and excluded/diagnostic cases.
  - A data-quality and bias audit exists at `data/run2v2_data_quality_audit.md`, covering recipe-platform bias, cuisine-label limitations, sample sizes, ingredient normalization risk, generic ingredient effects, and cuisine-to-geography mapping confidence.
  - A case-subset crosswalk exists at `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`, assigning each retained cuisine to global screen, primary case, secondary case, bias-diagnostic case, or excluded case, with notes.
  - A generic-ingredient handling policy exists at `data/crosswalks/run2v2_generic_ingredient_policy.csv`, listing ingredients to remove, downweight, retain, or flag, with reasons.
  - A filtered/sensitivity cuisine matrix exists at `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`, produced from documented rules rather than silent ad hoc deletion.
  - Similarity, distance baseline, and residual outputs are recomputed for the filtered sensitivity model and saved under `data/processed/run2v2_*`.
  - The worker compares original Run 2 and Run 2 v2 results in `outputs/run2v2_global_sensitivity_summary.md`, including whether top residual corridors are stable after generic-ingredient filtering.
  - Focused case results exist at `data/processed/run2v2_focus_case_results.csv`, with at least the East/Southeast Asia case analyzed if the required cuisines exist in the dataset.
  - At least one additional geospatial-only analysis is completed and documented: path/connectivity-aware distance proxy, residual bridge score map, boundary/permeability check, or spatial cluster/outlier summary. If none can be completed, `docs/run2v2_geospatial_method_feasibility.md` must precisely explain the blocker and define the Run 3 data needed.
  - At least three revised or new figures exist under `figures/`, including one focused-case figure and one figure from the additional geospatial-only analysis.
  - Figure captions exist at `figures/run2v2_figure_captions.md`, explaining data, method, interpretation, limitations, and whether each figure is global discovery or focused inference.
  - A revised interpretation exists at `docs/run2v2_amended_prototype_interpretation.md`, clearly separating strong conclusions, cautious hypotheses, and claims that should not be made.
  - `docs/run3_handoff_plan.md` is updated with a concrete final scope recommendation, including whether to proceed with global screen + focused cases, what to do with flavor chemistry, and what Pia should validate.
  - `outputs/run2v2_reproducibility_log.md` records commands, scripts, package assumptions, inputs, outputs, and failures.
  - `WORK.md` Results and Learnings are updated after every worker iteration and at completion.
- Non-goals:
  - Do not write the final Fisher submission essay/report.
  - Do not create a polished ArcGIS StoryMap or final visual design package.
  - Do not redo all of Run 2 from scratch unless an audit shows core artifacts are invalid or missing.
  - Do not add many new covariates. Prioritize scope correction, sensitivity, and geospatial reasoning.
  - Do not make global causal claims about migration, trade, empire, or colonialism.
  - Do not make fermentation central.
  - Do not make flavor chemistry central unless existing evidence already supports it; treat it as Run 3 optional unless matching is demonstrably feasible.
  - Do not silently use or expand license-risk recipe data without documenting usage risk.

# 2. Acceptance Checks
- Data checks:
  - All prior Run 2 inputs used must be listed in `data/run2v2_existing_artifact_audit.csv`.
  - If any required prior artifact is missing, the related task must be marked BLOCKED or redirected to a documented fallback using existing data.
  - The global screen must retain the original broad model where possible, but final inference must be based on scoped cases.
  - The East/Southeast Asia primary case should include at least 5 of these cuisines if available: Chinese, Japanese, Korean, Thai, Vietnamese, Filipino. If fewer than 5 are available, the worker must mark the primary case as weak and recommend a different scoped case.
  - The Iberian/Atlantic secondary case should include at least 4 of these cuisines if available: Spanish, Brazilian, Mexican, Filipino, Cajun/Creole, Jamaican, Southern US. If fewer than 4 are available, it must remain optional or diagnostic.
  - Cuisine labels must not be treated as exact nation-state units; `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv` must include mapping-confidence notes.
  - Generic ingredient treatment must be explicit and reproducible.
  - Raw ingredient information from Run 2 must remain available; no task may overwrite raw or original processed data without creating a Run 2 v2-specific output path.
- Code checks:
  - All new scripts must run from the project root using relative paths.
  - New scripts must write outputs only under `data/processed/`, `outputs/`, or `figures/`, unless the task explicitly names another path.
  - No API tokens, credentials, or secrets may appear in code, data, logs, or markdown.
  - Each script must fail clearly with an actionable message if an expected input file is missing.
  - Scripts must be prototype-clear rather than production-engineered; avoid packaging, CI, or broad refactors.
  - `outputs/run2v2_reproducibility_log.md` must include every command used to create Run 2 v2 outputs.
- Analysis checks:
  - The global model must be described as a discovery screen, not proof.
  - Focused-case analysis must report sample sizes, cuisines retained, pair counts, and whether the conclusions are robust to generic-ingredient filtering.
  - Similarity comparisons must include cosine similarity and at least one robustness metric inherited or recomputed from Run 2, such as Jaccard or Pearson.
  - The residual ranking must be based on observed-minus-predicted similarity or a documented equivalent.
  - At least one sensitivity check must test the effect of removing or downweighting generic/pantry ingredients.
  - At least one geospatial-only analysis must use coordinates, adjacency, routes, distance, boundaries, or spatial grouping in a way that could not be obtained from ingredient vectors alone.
  - All migration/trade/colonial/language interpretations must be framed as hypotheses or associations unless supported by explicit covariate modeling.
- GIS/visualization checks:
  - New maps must use real coordinates from `data/crosswalks/cuisine_geo_crosswalk.csv` or a documented updated crosswalk.
  - A focused-case figure must show spatial relationships for East/Southeast Asia or explain why the case is blocked.
  - A geospatial-only figure must visualize one of: path/connectivity proxy, residual bridge scores, boundary/permeability, or spatial cluster/outlier results.
  - Figures must be legible enough for evaluation, but not polished final assets.
  - Every Run 2 v2 figure must have a caption in `figures/run2v2_figure_captions.md`.
- Research/writing checks:
  - `docs/run2v2_scope_lock_decision_memo.md` must state what the project can strongly conclude, cautiously suggest, and should not claim.
  - `docs/run2v2_amended_prototype_interpretation.md` must use conservative language and explicitly distinguish global screening from focused inference.
  - `docs/run3_handoff_plan.md` must include a final recommended scope and concrete Run 3 tasks.
  - Any new factual claim about external datasets, GIS methods, or historical mechanisms must include a source link or citation note.

# 3. Plan
- Audit existing Run 2 outputs first; do not redo work until the worker knows what is valid, missing, or needs amendment.
- Lock the scope before modeling: global screen, East/Southeast Asia primary case, Iberian/Atlantic secondary case if feasible, and bias-diagnostic cases.
- Identify and document generic/pantry ingredients, then recompute a filtered/sensitivity model to see whether residual corridors survive.
- Build focused-case results from the existing cleaned cuisine–ingredient and geography outputs rather than starting from raw recipe acquisition.
- Add one or two geospatial-only analyses that deepen the Fisher fit without exploding scope: path/connectivity-aware proxy, residual bridge score, or boundary/permeability analysis.
- Generate revised figures and captions that clearly mark which visuals are exploratory/global and which support narrower conclusions.
- Rewrite the Run 2 interpretation and Run 3 handoff so the final project can make strong, defensible claims.
- Dependencies / ordering logic: audit precedes scope lock; scope lock precedes case crosswalk; ingredient policy precedes filtered matrix; filtered matrix precedes recomputed residuals; recomputed residuals precede focused cases; focused cases and geospatial-only analysis precede interpretation; interpretation precedes Run 3 handoff.
- Risk & mitigation:
  - If prior artifacts are missing, mark exact blockers and use existing available data rather than rebuilding everything.
  - If East/Southeast Asia lacks enough cuisines or pair variation, select the next strongest scoped case and record why.
  - If Iberian/Atlantic results are unstable after filtering, keep it as a cautionary or diagnostic case.
  - If path-aware distance is too hard for this run, implement a simpler documented spatial-connectivity proxy and reserve least-cost/network routing for Run 3.
  - If generic-ingredient filtering removes most apparent corridors, frame that as an important data-quality finding and recommend narrower/finer recipe data for Run 3.
  - If residual maps remain visually noisy, prioritize focused maps and residual bridge-score summaries over global spaghetti-line maps.

# 4. Tasks
- [ ] [S01] Create `outputs/run2v2_setup_note.md` — Inputs needed: completed Run 2 `WORK.md`, `docs/run2_prototype_interpretation.md`, `outputs/distance_baseline_model_summary.md`, and `docs/run3_handoff_plan.md`. Done when: the file summarizes why Run 2 v2 exists, what must be amended, what prior results should be preserved, and what outputs this run must not attempt.
- [ ] [D01] Create `data/run2v2_existing_artifact_audit.csv` — Inputs needed: prior Run 2 artifact paths named in this WORK.md. Done when: each required prior artifact is listed with path, exists/missing status, role in Run 2 v2, whether it can be reused, and any blocker.
- [ ] [R01] Create `docs/run2v2_scope_lock_decision_memo.md` — Inputs needed: `data/run2v2_existing_artifact_audit.csv`, `docs/run2_prototype_interpretation.md`, and prior residual results. Done when: the file defines global discovery layer, East/Southeast Asia primary case, Iberian/Atlantic secondary case if feasible, diagnostic/excluded cases, and permitted/forbidden final claims.
- [ ] [D02] Create `data/run2v2_data_quality_audit.md` — Inputs needed: `data/processed/cuisine_ingredient_long.csv`, `data/processed/cuisine_ingredient_matrix.csv`, `data/crosswalks/cuisine_geo_crosswalk.csv`, and Run 2 source manifests. Done when: the file reports recipe counts by cuisine, ingredient counts, mapped geography confidence, likely platform bias, generic ingredient risk, and any data-quality reason to narrow scope.
- [ ] [D03] Create `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv` — Inputs needed: retained cuisine labels from `data/processed/cuisine_ingredient_long.csv` and `docs/run2v2_scope_lock_decision_memo.md`. Done when: every cuisine is assigned to global screen, East/Southeast Asia primary, Iberian/Atlantic secondary, bias-diagnostic, or excluded/unused, with mapping confidence and notes.
- [ ] [D04] Create `data/crosswalks/run2v2_generic_ingredient_policy.csv` — Inputs needed: ingredient frequencies from `data/processed/cuisine_ingredient_long.csv` and existing `data/crosswalks/ingredient_alias_crosswalk.csv`. Done when: high-frequency and likely generic ingredients are labeled remove, downweight, retain, or flag, with rule reason and confidence.
- [ ] [C01] Create `scripts/10_run2v2_filter_ingredient_matrix.py` — Inputs needed: `data/processed/cuisine_ingredient_long.csv` and `data/crosswalks/run2v2_generic_ingredient_policy.csv`. Done when: the script exists, uses relative paths, and is designed to write `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv` plus a summary file when run.
- [ ] [C02] Run `scripts/10_run2v2_filter_ingredient_matrix.py` to create `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv` — Inputs needed: script from C01 and required input files. Done when: the filtered matrix exists and preserves cuisines as rows and normalized ingredients as columns.
- [ ] [R02] Create `outputs/run2v2_filtering_summary.md` — Inputs needed: output from C02 and `data/crosswalks/run2v2_generic_ingredient_policy.csv`. Done when: the file reports ingredients removed/downweighted/retained, matrix shape before/after, cuisines retained, and expected interpretation impact.
- [ ] [C03] Create `scripts/11_run2v2_recompute_similarity_residuals.py` — Inputs needed: `data/processed/run2v2_cuisine_ingredient_matrix_filtered.csv`, `data/crosswalks/cuisine_geo_crosswalk.csv`, and prior distance-pair or pair-model data. Done when: the script exists, uses relative paths, and is designed to recompute similarity, pair table, distance baseline, and residuals for the filtered model.
- [ ] [C04] Run `scripts/11_run2v2_recompute_similarity_residuals.py` to create `data/processed/run2v2_residual_culinary_corridors_filtered.csv` — Inputs needed: script from C03 and required input files. Done when: the filtered residual corridor file exists with observed similarity, predicted similarity, residual, distance/log-distance, and cuisine-pair identifiers.
- [ ] [R03] Create `outputs/run2v2_global_sensitivity_summary.md` — Inputs needed: original `data/processed/residual_culinary_corridors.csv` and filtered `data/processed/run2v2_residual_culinary_corridors_filtered.csv`. Done when: the file compares original vs filtered top residual corridors, reports stability/instability, and states whether the global map should remain a discovery layer only.
- [ ] [V01] Create `figures/run2v2_global_residual_corridor_map_filtered.png` — Inputs needed: `data/processed/run2v2_residual_culinary_corridors_filtered.csv` and `data/crosswalks/cuisine_geo_crosswalk.csv`. Done when: the map shows top positive filtered residual links using real coordinates and avoids unreadable global clutter.
- [ ] [C05] Create `scripts/12_run2v2_focus_case_models.py` — Inputs needed: `data/crosswalks/run2v2_cuisine_case_subset_crosswalk.csv`, filtered matrix, and filtered residuals. Done when: the script exists, uses relative paths, and is designed to output focused-case pair results for primary and secondary cases.
- [ ] [C06] Run `scripts/12_run2v2_focus_case_models.py` to create `data/processed/run2v2_focus_case_results.csv` — Inputs needed: script from C05 and required input files. Done when: the file exists with case name, cuisine pairs, similarity, distance, residual or case-specific comparison metric, and notes for East/Southeast Asia and any feasible secondary case.
- [ ] [R04] Create `outputs/run2v2_focus_case_summary.md` — Inputs needed: `data/processed/run2v2_focus_case_results.csv` and scope memo. Done when: the file reports which focused cases are strong, weak, or diagnostic; includes pair counts, key patterns, and permitted claims.
- [ ] [V02] Create `figures/run2v2_east_southeast_asia_case_map.png` — Inputs needed: `data/processed/run2v2_focus_case_results.csv` and cuisine coordinates. Done when: a focused spatial figure shows East/Southeast Asia cuisine links or, if blocked, the task remains unchecked with the exact missing cuisines/data named in Results.
- [ ] [V03] Create `figures/run2v2_iberian_atlantic_case_map.png` — Inputs needed: `data/processed/run2v2_focus_case_results.csv` and cuisine coordinates. Done when: a focused spatial figure shows the secondary Iberian/Atlantic case, or the task remains unchecked with a documented reason that the case is too weak or data-insufficient.
- [ ] [R05] Create `docs/run2v2_geospatial_method_feasibility.md` — Inputs needed: existing distance/geography files, public method/source options if used, and scope memo. Done when: the file evaluates at least three geospatial-only methods — path/connectivity-aware distance, residual bridge scores, and boundary/permeability — and selects one or two to implement in this run with reasons.
- [ ] [C07] Create `scripts/13_run2v2_path_connectivity_proxy.py` — Inputs needed: `data/processed/run2v2_residual_culinary_corridors_filtered.csv`, cuisine coordinates, and `docs/run2v2_geospatial_method_feasibility.md`. Done when: the script exists and is designed to create a path/connectivity or spatial-accessibility proxy result without requiring unavailable API keys.
- [ ] [C08] Run `scripts/13_run2v2_path_connectivity_proxy.py` to create `data/processed/run2v2_path_connectivity_results.csv` — Inputs needed: script from C07 and required input files. Done when: the file exists with cuisine pairs, residuals, distance, selected path/connectivity proxy variables, and notes on whether each proxy is substantive or exploratory.
- [ ] [R06] Create `outputs/run2v2_path_connectivity_summary.md` — Inputs needed: `data/processed/run2v2_path_connectivity_results.csv`. Done when: the file explains whether path/connectivity proxies clarify any residual corridors and what true GIS/network data would improve the analysis in Run 3.
- [ ] [C09] Create `scripts/14_run2v2_residual_bridge_scores.py` — Inputs needed: filtered residual corridor file and cuisine coordinates. Done when: the script exists and is designed to aggregate pairwise residuals into place-level bridge/outlier scores.
- [ ] [C10] Run `scripts/14_run2v2_residual_bridge_scores.py` to create `data/processed/run2v2_cuisine_residual_bridge_scores.csv` — Inputs needed: script from C09 and required input files. Done when: the file exists with each cuisine’s positive residual degree, mean positive residual, long-distance residual score, and case membership.
- [ ] [V04] Create `figures/run2v2_residual_bridge_score_map.png` — Inputs needed: `data/processed/run2v2_cuisine_residual_bridge_scores.csv` and cuisine coordinates. Done when: the map shows place-level culinary bridge/outlier scores using real coordinates.
- [ ] [C11] Create `scripts/15_run2v2_boundary_permeability_check.py` — Inputs needed: cuisine case crosswalk, cuisine coordinates, filtered residuals, and any available adjacency/subregion labels. Done when: the script exists and is designed to compute a simple boundary/permeability comparison for scoped cases or to fail clearly if adjacency labels are unavailable.
- [ ] [C12] Run `scripts/15_run2v2_boundary_permeability_check.py` to create `data/processed/run2v2_boundary_permeability_results.csv` — Inputs needed: script from C11 and required input files. Done when: the output exists with pair-level or boundary-group comparisons, or the task is marked BLOCKED with the precise missing adjacency/boundary input.
- [ ] [R07] Create `outputs/run2v2_geospatial_analysis_summary.md` — Inputs needed: path/connectivity, residual bridge score, and boundary/permeability outputs that are available. Done when: the file states which geospatial-only analysis is strongest, which is exploratory, which should be dropped, and what Fisher insight each supports.
- [ ] [V05] Create `figures/run2v2_geospatial_method_comparison.png` — Inputs needed: available geospatial-only outputs. Done when: one chart/map compares at least two spatial explanations or displays the strongest geospatial-only result clearly.
- [ ] [V06] Create `figures/run2v2_figure_captions.md` — Inputs needed: all completed Run 2 v2 figures. Done when: each figure has a caption with data, method, what it shows, what it does not prove, and how it supports either global discovery or focused inference.
- [ ] [C13] Create `outputs/run2v2_reproducibility_log.md` — Inputs needed: all Run 2 v2 scripts and command history. Done when: the file lists commands run from project root, environment assumptions, input/output paths, package needs, failed commands, and manual steps.
- [ ] [R08] Create `docs/run2v2_amended_prototype_interpretation.md` — Inputs needed: scope memo, sensitivity summary, focus-case summary, geospatial analysis summary, and figure captions. Done when: the file gives a 1–2 page conservative interpretation with strong conclusions, cautious hypotheses, invalid/forbidden claims, and Fisher relevance.
- [ ] [R09] Update `docs/run3_handoff_plan.md` — Inputs needed: `docs/run2v2_amended_prototype_interpretation.md`, `outputs/run2v2_geospatial_analysis_summary.md`, and `outputs/run2v2_focus_case_summary.md`. Done when: the file states final recommended scope, Run 3 figure set, flavor-chemistry status, Pia validation questions, remaining blockers, and 8–15 concrete Run 3 tasks.
- [ ] [Q01] Update `WORK.md` Results section with final Run 2 v2 artifact checklist — Inputs needed: all completed Run 2 v2 artifacts. Done when: Results lists every created artifact path, verification status, key findings, blocked tasks, and exact missing inputs.
- [ ] [Q02] Update `WORK.md` Learnings section with Run 2 v2 pitfalls and recommendations — Inputs needed: all completed artifacts and errors encountered. Done when: Learnings records scope decisions, data-quality pitfalls, modeling lessons, geospatial-method lessons, and recommendations for Run 3.

# 5. Worker Driver Prompt
You are the worker for **Run 2 Version 2** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition. This is an amendment run, not a full restart. Preserve existing Run 2 outputs unless a task explicitly creates a Run 2 v2 replacement under a new `run2v2_*` path.

After each iteration, update `WORK.md` immediately: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, commands, outputs, and verification status; record Learnings with pitfalls, source issues, modeling decisions, geospatial decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing input/access/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If a preferred geospatial method such as true least-cost/path-aware distance is not feasible in this run, implement a clearly documented proxy only if it is honest and useful; otherwise record the blocker and continue with residual bridge scores or focused-case maps.

Use the acceptance checks for a Mixed code/data/research/writing job. Scripts must use relative paths, avoid secrets, and write outputs to documented Run 2 v2 locations. Every dataset or external method source must have source/access/license notes where applicable. All interpretation must be conservative: global results are discovery, focused cases support stronger but still non-causal conclusions, and migration/trade/colonial explanations remain hypotheses unless explicitly modeled.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, state whether the project should proceed to Run 3 as global screen + focused cases, which focused case is strongest, which geospatial-only analysis is strongest, which figures should be used in the final Fisher submission, and what exact inputs Pia or the user should provide next.

# 6. Learnings

# 7. Results

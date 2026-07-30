# 0. Snapshot
- Job Type: Mixed — Research/Synthesis + Code/Data Feasibility + Writing/Exposition.
- Primary Deliverables: first-run Fisher project blueprint; dataset inventory and feasibility evidence pack; preliminary figure(s) where feasible; Pia Sorensen consultation packet; next-run roadmap for prototype and final submission package.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as scientific mentor; Harvard Center for Geographic Analysis / Fisher Prize evaluators; future worker runs that will build the prototype and final submission.
- Constraints: useful output needed within 24 hours; first run must be research-first; maximize data coverage while grading reliability; do not build a full production code pipeline yet; do not over-focus on fermentation unless data quality supports it; current likely best final format is ArcGIS StoryMap or web-map-heavy submission, but worker must recommend the best format after evidence review; no direct contact with Pia unless separately authorized; all claims and data-source evaluations must be cited or source-linked.

# 1. Goal
Create a Fisher Prize-ready project blueprint for a food/geospatial analysis project that can later be converted into a working prototype and polished submission. The first run should determine which version of the project is strongest after reviewing past Fisher winners, available datasets, and methodological feasibility. The project should use food as a spatial signal, with candidate directions including cuisine similarity, migration/trade/cultural exchange, flavor chemistry, and fermentation/microbial diffusion. The blueprint must explain how to use Prof. Pia Sorensen effectively as a food-science mentor and identify the richest feasible data stack for a high-rigor geospatial project.

- Definition of Done:
  - Official Fisher Prize requirements and past-winner patterns are verified from public sources and summarized in `docs/award_and_winner_brief.md`.
  - At least three candidate project variants are compared and scored: cuisine similarity/migration-trade, flavor chemistry, fermentation/microbes, and any combined version that emerges from data review.
  - A data-source register contains at least 25 candidate sources across recipe/ingredient data, food chemistry, fermentation/microbiome, migration, trade, climate/agriculture, cultural/history, and base GIS layers.
  - Each data source is labeled by access status, spatial granularity, temporal coverage, license/usage risk, reliability, relevance, and whether it is core reliable data or experimental/secondary data.
  - At least 8 high-priority data sources are access-tested through a documented smoke check, metadata review, sample download, or explicit blocker note.
  - A preliminary analysis plan exists for similarity matrices, clustering/network analysis, spatial distance, migration/trade/climate comparison, residual corridor mapping, and robustness checks.
  - At least one preliminary map, chart, or network figure is created from accessible public data, or a precise blocker is recorded explaining why even a minimal figure could not be produced within the run.
  - A recommended primary project and one fallback project are selected with evidence-based reasoning.
  - A Pia consultation packet is created with a concise project summary, targeted questions, candidate datasets/methods needing scientific validation, and a draft email the user can send.
  - A next-run roadmap exists for Run 2 working prototype and Run 3 Fisher submission package.
  - `WORK.md` is updated with Results and Learnings after each completed task.
- Non-goals:
  - Do not write the final Fisher submission essay/report in this run.
  - Do not build a full production codebase or complete reproducible pipeline in this run.
  - Do not make fermentation the main project unless the dataset review shows unusually strong, geocoded, analyzable data.
  - Do not contact Prof. Pia Sorensen directly; prepare materials for the user to send.
  - Do not rely on scraped, undocumented, or license-unclear recipe data as a core source unless the risk is explicitly flagged.
  - Do not create polished final StoryMap/ArcGIS deliverables in this run.

# 2. Acceptance Checks
- Research checks:
  - `docs/award_and_winner_brief.md` must cite official Harvard/CGA sources where available and must distinguish confirmed facts from inferred patterns.
  - Past-winner analysis must include at least 10 winner/project examples, each tagged by domain, GIS method, data type, and why it appears Fisher-competitive.
  - `data/data_source_register.csv` or `data/data_source_register.md` must include at least 25 candidate sources and must not treat all sources as equally reliable.
  - Novelty claims must be conservative: use phrases such as “not found in reviewed sources” unless a literature search directly supports a stronger claim.
  - The final recommendation must explain why the chosen project is not merely “a map of food,” but a spatial analysis where GIS produces the insight.
- Code/data feasibility checks:
  - Any code created in this run must be limited to smoke tests, sample parsing, or one preliminary figure; it must not become a full pipeline.
  - Any script/notebook must run from the project root using relative paths and must record input/output paths.
  - No API key, token, or credential may be committed into files.
  - Large datasets should not be fully downloaded unless necessary; prefer metadata checks, small samples, public mirrors, or documented download instructions.
  - Every downloaded or sampled dataset must have a source URL, license/usage note, date accessed, and local path recorded.
- Writing/exposition checks:
  - `docs/fisher_project_blueprint.md` must contain: title options, central research question, thesis/hypothesis, why it fits Fisher, datasets, methods, expected visuals, risks, mitigation, timeline, and final format recommendation.
  - The recommended project must include a clear role for Pia: what scientific assumptions she can validate, what food-science framing she can improve, and what consultation questions should be asked.
  - The writing must be precise and award-facing, not speculative brainstorming only.
  - The final blueprint should be understandable to both GIS evaluators and a food-science mentor.
- Format checks:
  - The run must produce Markdown/CSV/PNG or notebook/script artifacts only; no PDF, LaTeX, StoryMap, or polished design asset is required in this run.
  - All output paths listed in Results must exist or be explicitly marked BLOCKED with the missing input.

# 3. Plan
- Verify the official Fisher Prize purpose, judging logic, and past-winner patterns so the project is optimized for the award rather than merely interesting as food science.
- Build a broad but graded data inventory that maximizes possible data: recipe/ingredient datasets, FlavorDB/FooDB-style chemistry data, fermentation/microbiome datasets, UN/FAO/Comtrade migration/trade/agriculture data, climate layers, colonial/language links, and base geospatial boundaries.
- Compare project variants after data review rather than assuming the first framing is strongest: cuisine similarity, flavor chemistry, fermentation/microbes, and combined “culinary corridors” models.
- Run only minimal feasibility checks: sample downloads, schema inspection, one smoke-test script/notebook, and at least one preliminary figure if accessible data allows.
- Produce an award-facing blueprint that defines the primary project, fallback, data stack, method sequence, expected visuals, and next two worker runs.
- Prepare a Pia consultation packet that turns the project into specific, answerable scientific questions rather than a vague request for mentorship.
- Dependencies / ordering logic: first verify Fisher criteria and winner patterns; then inventory and grade sources; then compare variants; then perform smoke checks; then recommend the primary project; then write the blueprint and Pia packet.
- Risk & mitigation: if recipe datasets are messy or license-unclear, shift core analysis toward official migration/trade/agriculture data plus open ingredient sources; if fermentation data is sparse, keep it as a sidebar/case study; if global scope is too noisy, recommend a narrower corridor or region; if no preliminary figure can be generated, record the blocker and provide a precise Run 2 data acquisition task; if StoryMap is not yet feasible, recommend a map-heavy report as interim format.

# 4. Tasks
- [ ] [R01] Create `docs/award_and_winner_brief.md` — Inputs needed: public Fisher Prize / Harvard CGA / Harvard Gazette / award-profile sources. Done when: the file summarizes official award purpose, eligibility/criteria if available, current submission expectations if available, at least 10 past winner/project examples, observed winning patterns, and source links/access dates for each factual claim.
- [ ] [R02] Create `docs/fisher_success_rubric.md` — Inputs needed: `docs/award_and_winner_brief.md`. Done when: the file defines 6–10 scoring criteria for this project, including spatial necessity, GIS sophistication, data credibility, visual clarity, interdisciplinarity, originality, feasibility, and Fisher fit.
- [ ] [R03] Create `docs/project_variant_matrix.md` — Inputs needed: user answers in this WORK.md; `docs/fisher_success_rubric.md`. Done when: the file compares at least four variants: cuisine similarity/migration-trade, flavor chemistry, fermentation/microbes, and combined culinary corridors; each variant has research question, possible thesis, data needs, methods, visuals, Pia role, risks, and preliminary score.
- [ ] [R04] Create `docs/literature_seed_list.md` — Inputs needed: public academic/search sources. Done when: the file lists at least 12 relevant papers/articles/resources on cuisine similarity, ingredient networks, flavor pairing/flavor chemistry, food and migration, fermentation microbiomes, or GIS food studies, with one-sentence relevance notes and source links.
- [ ] [D01] Create `data/data_source_register.csv` — Inputs needed: public data portals/repositories. Done when: the file contains at least 25 candidate datasets with columns for category, dataset name, provider, URL, license/terms, spatial granularity, temporal coverage, file/API format, access difficulty, reliability grade, Fisher relevance score, and risk notes.
- [ ] [D02] Create `data/core_vs_experimental_sources.md` — Inputs needed: `data/data_source_register.csv`. Done when: the file separates sources into core reliable data, useful secondary data, experimental/high-risk data, and rejected/avoid data, with reasons for each classification.
- [ ] [D03] Create `data/high_priority_access_log.md` — Inputs needed: top candidates from `data/data_source_register.csv`. Done when: at least 8 high-priority sources have documented access status: sampled/downloaded, metadata verified, API available, paywalled, license-risk, missing, or BLOCKED, with date checked and next action.
- [ ] [D04] Create `data/geo_base_layer_plan.md` — Inputs needed: public GIS boundary/source options such as Natural Earth, GADM, GeoNames, World Bank/UN country codes, or equivalent. Done when: the file specifies which base layers and geographic identifiers should be used to join country/region-level food data to maps, and flags expected name-matching problems.
- [ ] [D05] Create `data/variable_crosswalk_plan.md` — Inputs needed: candidate food, migration, trade, climate, agriculture, and culture datasets. Done when: the file proposes a common key strategy for country/region names, ISO codes, dates, cuisine labels, ingredient labels, and source-specific naming conflicts.
- [ ] [M01] Create `docs/methods_similarity_plan.md` — Inputs needed: `docs/project_variant_matrix.md`; candidate recipe/ingredient sources. Done when: the file specifies how to construct cuisine vectors, ingredient-pair networks, similarity metrics such as cosine/Jaccard/Pearson, clustering, and validation checks.
- [ ] [M02] Create `docs/methods_spatial_model_plan.md` — Inputs needed: `data/core_vs_experimental_sources.md`; `data/geo_base_layer_plan.md`. Done when: the file specifies how to compare cuisine similarity with geographic distance, migration, trade, climate/agriculture, colonial/language links, and how to create residual corridor maps.
- [ ] [M03] Create `docs/methods_flavor_chemistry_plan.md` — Inputs needed: candidate flavor chemistry datasets. Done when: the file explains how to map ingredients to flavor compounds, construct flavor vectors, compare ingredient similarity to chemical similarity, and record ingredient-matching uncertainty.
- [ ] [M04] Create `docs/methods_fermentation_plan.md` — Inputs needed: candidate fermentation/microbiome datasets. Done when: the file states whether fermentation can be core, secondary, or dropped; identifies possible fermented-food/microbiome variables; and defines a conservative use case if data is limited.
- [ ] [C01] Create `scripts/00_feasibility_smoke_test.py` or `notebooks/00_feasibility_smoke_test.ipynb` — Inputs needed: at least one accessible dataset from `data/high_priority_access_log.md`; base geo layer if creating a map. Done when: the script/notebook loads a small sample, performs one simple join/summary/similarity calculation, and writes output to `outputs/` without hard-coded absolute paths or secrets.
- [ ] [C02] Create `outputs/feasibility_smoke_test_log.md` — Inputs needed: output from `scripts/00_feasibility_smoke_test.py` or `notebooks/00_feasibility_smoke_test.ipynb`. Done when: the file records what ran, input files/URLs, output files, errors, runtime notes, and whether the smoke test supports Run 2 prototype work.
- [ ] [V01] Create `figures/pilot_map_or_chart.png` — Inputs needed: successful smoke-test output from C01. Done when: at least one preliminary map, chart, or network-style visualization exists and is sufficient to show whether a real pattern may be present; if C01 is BLOCKED, this task must remain BLOCKED and the blocker must name the missing data/input.
- [ ] [V02] Create `figures/pilot_figure_caption.md` — Inputs needed: `figures/pilot_map_or_chart.png`; source notes from `outputs/feasibility_smoke_test_log.md`. Done when: the file explains what the preliminary figure shows, what it does not prove, what data produced it, and how it would improve in Run 2.
- [ ] [R05] Create `docs/recommendation_memo.md` — Inputs needed: `docs/project_variant_matrix.md`; `data/core_vs_experimental_sources.md`; `outputs/feasibility_smoke_test_log.md`; `figures/pilot_figure_caption.md` if available. Done when: the file recommends one primary project and one fallback, with explicit reasoning based on Fisher fit, data availability, methodological rigor, visual payoff, and Pia usefulness.
- [ ] [W01] Create `docs/fisher_project_blueprint.md` — Inputs needed: all prior research/data/method artifacts. Done when: the file contains polished sections for title options, central research question, thesis/hypotheses, Fisher fit, data stack, methods, expected visuals, scope recommendation, risks/mitigations, Run 2 prototype plan, and Run 3 final submission plan.
- [ ] [W02] Create `docs/pia_consultation_packet.md` — Inputs needed: `docs/fisher_project_blueprint.md`; `docs/methods_flavor_chemistry_plan.md`; `docs/methods_fermentation_plan.md`. Done when: the file includes a one-page project summary, 8–12 targeted questions for Pia, what feedback is needed from her, which scientific assumptions she should validate, and a concise draft email the user can send.
- [ ] [W03] Create `docs/final_format_recommendation.md` — Inputs needed: `docs/award_and_winner_brief.md`; `docs/recommendation_memo.md`; `docs/fisher_project_blueprint.md`. Done when: the file recommends the best Fisher-facing format for the final project, explicitly comparing ArcGIS StoryMap/web-map-heavy submission, static report/poster, LaTeX technical report, and notebook appendix.
- [ ] [P01] Create `docs/run2_run3_roadmap.md` — Inputs needed: `docs/fisher_project_blueprint.md`; `docs/recommendation_memo.md`. Done when: the file defines Run 2 as working prototype and Run 3 as polished Fisher submission package, with 8–15 proposed tasks for each future run and clear handoff criteria.
- [ ] [Q01] Update `WORK.md` Results section with final artifact checklist — Inputs needed: all completed artifacts. Done when: Results lists every created artifact path, whether it passed acceptance checks, and any BLOCKED items with required next input.
- [ ] [Q02] Update `WORK.md` Learnings section with project-specific pitfalls/patterns — Inputs needed: all completed artifacts and errors encountered. Done when: Learnings records data-quality pitfalls, promising sources, rejected sources, Fisher-framing insights, and recommendations for the next worker.

# 5. Worker Driver Prompt
You are the worker for this Fisher Prize planning job. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is needed to satisfy that task’s “Done when” condition. Do not expand into a full code pipeline, final Fisher submission, polished StoryMap, or deep fermentation project unless the task explicitly requires it.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when there is concrete evidence; add a short Results entry with created/changed paths and verification status; add a Learnings entry for pitfalls, patterns, data-source issues, or methodological decisions; add new tasks only if they are atomic, verifiable, and necessary for the Definition of Done. If blocked, do not guess silently: leave the task unchecked, add a BLOCKED Results entry naming the missing input, and proceed to the next highest-priority unblocked task.

Use the acceptance checks for a Mixed research/data/writing job. All factual claims must have source links or citations. All datasets must be graded for reliability and license/access risk. Any code must be limited to smoke testing or one preliminary figure, must use relative paths, and must avoid secrets. The final output of this run is a Fisher-ready blueprint plus feasibility evidence, not a completed prototype or final submission.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, list every artifact produced, the recommended primary project, the fallback project, and the precise inputs needed for Run 2.

# 6. Learnings

# 7. Results

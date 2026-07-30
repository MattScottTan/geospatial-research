# 0. Snapshot
- Job Type: Mixed (Research/Synthesis + Writing/Exposition)
- Primary Deliverables:
  - `fisher/01-innovation-creativity-storybook.md`
  - `fisher/02-gis-use-storybook.md`
  - `fisher/03-data-storybook.md`
  - `fisher/04-analysis-execution-storybook.md`
  - `fisher/05-visualization-cartography-storybook.md`
  - `fisher/06-synthesis-storybook.md`
  - `fisher/feature-matrix.md`
- Stakeholders / Audience: Primary = user as Fisher submission strategist. Secondary = downstream worker/analyst who should be able to pick up the files and immediately turn them into submission strategy.
- Constraints:
  - Markdown only.
  - Anchor to the Esri/GIS-focused Fisher competition matching the five judging criteria supplied by the user.
  - Cover all publicly available winners.
  - Use official Fisher winner pages and the primary project materials linked from those pages as the authoritative evidence base.
  - Use only public sources; if evidence is missing or inaccessible, explicitly mark the gap and label any inference as uncertain.
  - Resolve criteria/source conflicts using the most recent official source and note the conflict in the matrix.
  - Optimize for rigor and defensible scoring over speed.
  - Do not draft the actual Fisher submission.

# 1. Goal
Produce a research-backed Fisher strategy package in markdown: five criterion-specific storybooks, one synthesis storybook, and one feature matrix document that analyzes all publicly available winners against the five judging criteria, explains how prior winners succeeded, and gives a downstream analyst enough evidence, scoring logic, and tactical guidance to build a high-quality Fisher submission strategy.

- Definition of Done:
  - [x] All seven markdown deliverables exist at the paths listed in Snapshot.
  - [x] `fisher/feature-matrix.md` contains: official prize anchor, criteria source, source inventory, citation scheme, conflict-resolution rule, uncertainty labels, documented weighting scheme, 1–5 scoring rubric, full winner-coverage table, and a scored comparison matrix with cited rationale.
  - [x] Every publicly available winner cycle is either analyzed in the matrix or explicitly marked as partial/unavailable with a reason.
  - [x] Each of the five criterion storybooks contains: criterion definition, evaluation signals, cited winner case studies, anti-patterns/omissions, practical win tactics, and a future-submission checklist.
  - [x] `fisher/06-synthesis-storybook.md` integrates the criterion storybooks into a coherent strategy handoff that another analyst could immediately use.
  - [x] Every substantive claim about a winner is traceable through a single consistent citation scheme.
  - [x] Quotes, if used, are short and selective; paraphrase remains the default.
  - [x] Cross-file terminology, winner names, cycle labels, and criterion names are internally consistent.
- Non-goals:
  - Drafting or designing the actual Fisher competition submission.
  - Creating polished custom visuals beyond markdown tables/lists.
  - Speculating about unpublished judge intent beyond the published criteria and winner evidence.
  - Substituting third-party coverage for missing official evidence; mark gaps instead.

# 2. Acceptance Checks
- Research / Synthesis checks:
  - The evidence base is limited to the official Fisher competition pages and the primary project materials linked from them.
  - `fisher/feature-matrix.md` lists the canonical prize page, the canonical judging-criteria source, and every publicly available winner cycle with coverage status.
  - A citation scheme is explicitly defined once and then applied consistently across all deliverables.
  - Each matrix rating has a short written rationale and at least one supporting citation.
  - Each substantive winner claim in every storybook has a supporting citation or is explicitly labeled as an inference.
  - A conflict-resolution note states that the most recent official source governs when official sources disagree.
  - A weighting note ties the benchmark to the five judging criteria; if no official numeric weights exist, the document must state the internal weighting assumption used for comparison.
  - Missing evidence is encoded consistently (for example: partial coverage, unavailable, uncertain inference) instead of silently omitted.
- Writing / Exposition checks:
  - Each storybook is its own markdown file and uses clear section headings.
  - The five criterion storybooks map one-to-one to the five judging criteria.
  - The synthesis storybook tells a downstream analyst how to use the criterion storybooks and matrix to build a Fisher submission strategy.
  - Markdown tables render cleanly and are readable in plain text.
  - Tone is analytical and actionable, not promotional.
  - Quotes are brief and used only when especially probative or when a paraphrase would blur an important distinction.

# 3. Plan
- Approach summary:
  - Establish the canonical prize identity and judging-criteria language from the official Fisher materials.
  - Build `fisher/feature-matrix.md` first as the canonical source of truth for evidence, coverage, scoring, uncertainty, and conflicts.
  - Enumerate all publicly available winners and linked primary project materials before writing any storybook.
  - Define the citation scheme, uncertainty labels, 1–5 rating rubric, and weighting logic before assigning scores.
  - Score all covered winners against all five criteria with cited rationale.
  - Write the five criterion storybooks from the matrix evidence, then finish with a synthesis storybook that turns findings into strategy guidance.
- Dependencies / ordering logic:
  - Source inventory must exist before scoring.
  - Scoring rubric and weighting logic must exist before any winner is rated.
  - `fisher/feature-matrix.md` is the canonical source of truth; storybooks should derive from it and stay consistent with it.
  - The synthesis storybook is last because it depends on the five criterion storybooks and the completed matrix.
- Risk & mitigation:
  - Missing or inaccessible winner materials may prevent full analysis. Mitigation: capture coverage status and evidence gaps in the matrix; mark uncertain inferences explicitly; do not backfill with third-party sources.
  - Criteria wording may differ across official pages or years. Mitigation: record the conflict and normalize to the most recent official source.
  - Scoring may drift into subjectivity. Mitigation: define the 1–5 rubric, weighting logic, and uncertainty labels before rating winners.
  - Storybooks may drift away from the matrix. Mitigation: treat the matrix as canonical and do a final consistency pass before marking done.

# 4. Tasks
- [x] [R] Create `fisher/feature-matrix.md` with top-level sections for prize anchor, judging criteria source, source inventory, citation scheme, conflict-resolution rule, uncertainty labels, weighting logic, 1–5 scoring rubric, winner coverage table, feature matrix, rationale notes, cross-winner findings, and evidence gaps. Done when: the file exists with all listed headings in markdown. Where: `fisher/feature-matrix.md`. Inputs needed: none.
- [x] [R] Populate the prize anchor, canonical judging-criteria source, and public-winner inventory in `fisher/feature-matrix.md`. Done when: every publicly available winner cycle is listed with winner/project name, cycle/year, official winner page, linked primary materials, and a coverage status of `covered`, `partial`, or `unavailable`. Where: `fisher/feature-matrix.md`. Inputs needed: public official Fisher competition page, public official winner pages, officially linked primary project materials. BLOCKED if no public official winner index can be found.
- [x] [R] Define the citation scheme, conflict-resolution rule, and uncertainty labels in `fisher/feature-matrix.md`. Done when: the file states exactly how citations will appear across all deliverables, states that the most recent official source resolves official-source conflicts, and defines labels for partial/unavailable/uncertain evidence. Where: `fisher/feature-matrix.md`. Inputs needed: completed source inventory section.
- [x] [R] Define the scoring logic in `fisher/feature-matrix.md`. Done when: the file contains a 1–5 rubric for each judging criterion and a documented weighting scheme tied to the five criteria, with any non-official weighting clearly labeled as an internal comparison device. Where: `fisher/feature-matrix.md`. Inputs needed: canonical judging criteria source.
- [x] [R] Populate the scored comparison matrix in `fisher/feature-matrix.md`. Done when: each covered winner has a 1–5 rating for all five criteria, short cited rationale for each criterion score, and an uncertainty flag wherever the evidence is thin. Where: `fisher/feature-matrix.md`. Inputs needed: completed source inventory, citation scheme, uncertainty labels, and scoring logic. BLOCKED if the official winner materials are not accessible enough to rate a winner.
- [x] [R] Add cross-winner findings and packaging observations to `fisher/feature-matrix.md`. Done when: the file summarizes recurring strengths, notable weaknesses/omissions, and any submission-packaging or framing patterns that are visible from the official evidence base, with citations where claims are winner-specific. Where: `fisher/feature-matrix.md`. Inputs needed: completed scored matrix.
- [x] [W] Create `fisher/01-innovation-creativity-storybook.md` with sections for criterion definition, evaluation signals, winner case studies, anti-patterns/omissions, win tactics, future-submission checklist, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/01-innovation-creativity-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/01-innovation-creativity-storybook.md`. Done when: the file explains how past winners excelled on innovation/creativity using cited case studies from the matrix, names anti-patterns or weaker patterns where evidence supports them, and ends with an actionable checklist for a future entrant. Where: `fisher/01-innovation-creativity-storybook.md`. Inputs needed: completed relevant rows and rationales in `fisher/feature-matrix.md`. BLOCKED if innovation/creativity scoring is incomplete.
- [x] [W] Create `fisher/02-gis-use-storybook.md` with sections for criterion definition, evaluation signals, winner case studies, anti-patterns/omissions, win tactics, future-submission checklist, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/02-gis-use-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/02-gis-use-storybook.md`. Done when: the file explains how past winners excelled on use of GIS using cited case studies from the matrix, names anti-patterns or weaker patterns where evidence supports them, and ends with an actionable checklist for a future entrant. Where: `fisher/02-gis-use-storybook.md`. Inputs needed: completed relevant rows and rationales in `fisher/feature-matrix.md`. BLOCKED if GIS-use scoring is incomplete.
- [x] [W] Create `fisher/03-data-storybook.md` with sections for criterion definition, evaluation signals, winner case studies, anti-patterns/omissions, win tactics, future-submission checklist, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/03-data-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/03-data-storybook.md`. Done when: the file explains how past winners excelled on data complexity/relevance/documentation using cited case studies from the matrix, names anti-patterns or weaker patterns where evidence supports them, and ends with an actionable checklist for a future entrant. Where: `fisher/03-data-storybook.md`. Inputs needed: completed relevant rows and rationales in `fisher/feature-matrix.md`. BLOCKED if data scoring is incomplete.
- [x] [W] Create `fisher/04-analysis-execution-storybook.md` with sections for criterion definition, evaluation signals, winner case studies, anti-patterns/omissions, win tactics, future-submission checklist, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/04-analysis-execution-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/04-analysis-execution-storybook.md`. Done when: the file explains how past winners excelled on analytical approach/execution using cited case studies from the matrix, names anti-patterns or weaker patterns where evidence supports them, and ends with an actionable checklist for a future entrant. Where: `fisher/04-analysis-execution-storybook.md`. Inputs needed: completed relevant rows and rationales in `fisher/feature-matrix.md`. BLOCKED if analytical-approach scoring is incomplete.
- [x] [W] Create `fisher/05-visualization-cartography-storybook.md` with sections for criterion definition, evaluation signals, winner case studies, anti-patterns/omissions, win tactics, future-submission checklist, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/05-visualization-cartography-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/05-visualization-cartography-storybook.md`. Done when: the file explains how past winners excelled on visualization/cartographic communication using cited case studies from the matrix, names anti-patterns or weaker patterns where evidence supports them, and ends with an actionable checklist for a future entrant. Where: `fisher/05-visualization-cartography-storybook.md`. Inputs needed: completed relevant rows and rationales in `fisher/feature-matrix.md`. BLOCKED if visualization/cartography scoring is incomplete.
- [x] [W] Create `fisher/06-synthesis-storybook.md` with sections for overall thesis, cross-criterion patterns, what repeated among winners, what varied by winner/topic, recommended Fisher win tactics, analyst handoff, and citations/notes. Done when: the file exists with all listed headings in markdown. Where: `fisher/06-synthesis-storybook.md`. Inputs needed: none.
- [x] [W] Populate `fisher/06-synthesis-storybook.md`. Done when: the file turns the matrix and five criterion storybooks into a coherent strategy handoff, identifies the strongest recurring patterns across winners, explains meaningful differences across winners/topics, prioritizes tactics for a future Fisher entrant, and explicitly tells another analyst how to use the files together. Where: `fisher/06-synthesis-storybook.md`. Inputs needed: completed `fisher/feature-matrix.md` and all five populated criterion storybooks. BLOCKED if any criterion storybook is incomplete.
- [x] [W] Perform the final consistency pass across `fisher/*.md`. Done when: the same citation format is used everywhere, winner names/cycles and criterion labels match the matrix, every substantive winner claim is cited or labeled as inference, and the deliverables collectively satisfy the Definition of Done. Where: `fisher/*.md`. Inputs needed: all seven deliverables drafted.

# 5. Worker Driver Prompt
You are the worker for this Fisher strategy project.

At the start of every iteration:
1. Read `WORK.md` completely.
2. Find the highest-priority unchecked task that is not BLOCKED by missing inputs.
3. Execute only that task or the smallest necessary slice of it. Do not expand scope.

Execution rules:
- Treat `fisher/feature-matrix.md` as the canonical source of truth for winner coverage, citations, uncertainty labels, scoring logic, and conflicts.
- Stay within the job type: this is a Mixed research/writing job. Use the Research / Synthesis and Writing / Exposition acceptance checks in `WORK.md` as hard constraints.
- Use official Fisher competition pages and the primary materials linked from them as the evidence base. If evidence is missing, inaccessible, or too thin, mark the gap explicitly rather than inventing coverage.
- Resolve official-source conflicts using the most recent official source and record the decision in `fisher/feature-matrix.md`.
- Keep quotes brief and selective. Prefer paraphrase plus citations.
- Maintain one consistent citation scheme across all deliverables.

After each iteration:
1. Update `WORK.md`.
2. Mark completed tasks as `[x]`.
3. Add a short entry under `# 7. Results` describing what changed, including file paths.
4. Add a short entry under `# 6. Learnings` for any pitfall, pattern, or rule that should guide later work.
5. Add new tasks only if they are atomic, necessary, and fit the existing scope.

Stop conditions:
- Stop when every item in Definition of Done is satisfied.
- Stop and mark the relevant task BLOCKED if a required official source or linked primary material cannot be accessed or does not exist; record exactly what input is missing.

# 6. Learnings
- A lightweight verification script is enough to close the package cleanly: check file existence, required headings, citation-ID integrity, and a heuristic pass over cited winner references before marking the final consistency task complete.
- The synthesis storybook is most useful when it does not restate the matrix mechanically; it should convert criterion-level evidence into analyst priorities, comparison logic, and review gates.
- Batching independent storybook-population tasks works well once the matrix is stable, but only after verifying that each file already contains its required sections, case studies, and checklists.
- Independent file-creation tasks are worth batching when they share the same section template; that keeps later iterations focused on substance instead of setup.
- Strong synthesis emerges from comparing what the artifacts make legible to judges: problem framing, method naming, and visual argument usually matter more than raw topic breadth.
- It is safer to downgrade a winner from `covered` to `partial` than to force a full score from thin primary-material evidence; the matrix should reward evidence quality, not completeness theater.
- Keep the matrix numerically modest: equal weights and score-gating for `covered` winners are better than pretending missing evidence can be ranked precisely.
- Reuse one citation namespace across the whole package; the storybooks should cite the matrix source IDs directly rather than inventing per-file references.
- Verify the filesystem before trusting the task log; this iteration required recreating `fisher/feature-matrix.md` and then repopulating it from source evidence.

# 7. Results
- 2026-04-06: Ran a final structural and citation consistency check over `/mnt/data/fisher/*.md` (file existence, required headings, defined-vs-used source IDs, and cited covered-winner references), confirmed the package passed, marked the final consistency task complete, and closed the Definition of Done in `WORK.md`.
- 2026-04-06: Populated `/mnt/data/fisher/06-synthesis-storybook.md` with the overall thesis, cross-criterion patterns, repeated winner signals, variation across winner types, prioritized win tactics, and an analyst handoff workflow tied to the matrix and storybooks.
- 2026-04-06: Verified and synced the five populated criterion storybooks in `/mnt/data/fisher/01-innovation-creativity-storybook.md` through `/mnt/data/fisher/05-visualization-cartography-storybook.md`, then marked their population tasks complete in `WORK.md`.
- 2026-04-06: Batched the six storybook scaffolds under `/mnt/data/fisher/`, creating the five criterion files plus `/mnt/data/fisher/06-synthesis-storybook.md` with their required section headings.
- 2026-04-06: Added cross-winner findings, packaging observations, and an evidence-gaps section to `/mnt/data/fisher/feature-matrix.md` so the storybooks can inherit a stable strategic thesis.
- 2026-04-06: Populated the numeric score table and per-winner rationale notes in `/mnt/data/fisher/feature-matrix.md`, scoring only the winner cases with enough primary material to support all five criteria.
- 2026-04-06: Added the weighting logic and full 1–5 criterion rubric to `/mnt/data/fisher/feature-matrix.md`, including a rule that only `covered` winners receive numeric scores.
- 2026-04-06: Filled the citation-scheme, conflict-resolution, and uncertainty-label sections in `/mnt/data/fisher/feature-matrix.md` so later scoring and storybooks can use one shared reference system.
- 2026-04-06: Created `/mnt/data/fisher/feature-matrix.md` and populated the prize anchor, criteria source, source inventory, and full winner-coverage table with `covered` / `partial` / `unavailable` statuses.

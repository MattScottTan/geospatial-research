# 0. Snapshot
- Job Type: Mixed — GIS/Cartographic Visualization + Light Code/Data + Writing/Exposition + Submission Packaging.
- Run: Fisher Award **Run 5 — Topographic Corridor Visualization Enhancement** for the Culinary Corridors project.
- Primary Deliverables: a visually striking East/Southeast Asia corridor/topographic figure set; a documented topographic or shaded-relief data manifest; a terrain/barrier/corridor interpretation memo; revised StoryMap/report insertion text; final figure-use decision; updated must-do submission checklist.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as food-science mentor; Harvard Center for Geographic Analysis / Fisher Prize reviewers; any panel/committee reviewing the Fisher submission package.
- Prior Inputs:
  - Existing final submission package and committee report from Run 4 v2, especially `submission/final_committee/final_committee_report.md`, `report/final_committee/culinary_corridors_committee_report.pdf`, `submission/revised/storymap_script.md`, and `submission/final_committee/final_submission_readiness_checklist.md`.
  - Existing figures and data from Runs 2 v2, 4, and 4 v2, especially `figures/final_revised/run4_primary_case_figure.png`, `figures/final_revised/run4_geospatial_insight_figure.png`, `figures/final_revised/run4v2_topographic_corridor_map.png`, `data/processed/run2v2_focus_case_results.csv`, `data/processed/run4v2_east_se_asia_accessibility_metrics.csv`, `data/crosswalks/cuisine_geo_crosswalk.csv`, and `outputs/run4v2_topographic_corridor_summary.md`.
- Constraints:
  - This is not a new research run; it is a targeted visual/geospatial enhancement run.
  - Do not widen the project beyond the settled submission scope: global discovery screen + East/Southeast Asia primary case + Iberian/Atlantic-Pacific secondary/diagnostic case.
  - The Run 5 enhancement should focus on the East/Southeast Asia corridor because this is the strongest focused inference case.
  - Any topographic or terrain map must use a documented real geodata source, such as Natural Earth shaded relief/raster relief, ETOPO, SRTM, GEBCO, or another public elevation/relief source. If no real elevation/relief data can be accessed, the task must produce a clearly labeled schematic and must not call it a topographic map.
  - Do not claim that terrain, maritime corridors, migration, trade, or historical exchange caused cuisine similarity unless explicitly modeled and qualified. Use “context,” “corridor plausibility,” “consistent with,” and “spatial interpretation,” not causal proof.
  - Do not overwrite prior Run 2/Run 2 v2/Run 3/Run 4/Run 4 v2 artifacts; save all new files under `run5_*`, `figures/final_revised/run5_*`, `outputs/run5_*`, `data/processed/run5_*`, `docs/run5_*`, or `submission/final_committee/run5_*`.
  - No API keys, tokens, credentials, or private map-service dependencies.
  - Keep final additions submission-friendly: one or two strong new figures, not a cluttered gallery.

# 1. Goal
Create a focused topographic/corridor visualization enhancement that makes the East/Southeast Asia culinary corridor more visually striking and more clearly geospatial for the Fisher Award submission. Run 5 should add a map-led visual layer that shows how the strongest cuisine-residual links sit within coastlines, island geography, mountain/terrain context, and plausible corridor/accessibility structure. The run should produce at least one committee-ready topographic or shaded-relief corridor map, a concise interpretation memo, and revised insertion text for the StoryMap/report so the final submission better communicates why geography matters.

## Definition of Done
- [ ] `outputs/run5_setup_note.md` exists and explains why Run 5 exists, what it adds beyond Run 4 v2, and what it must not attempt.
- [ ] `outputs/run5_input_artifact_audit.csv` exists and confirms availability of all prior figures/data needed for the East/Southeast Asia enhancement.
- [ ] `docs/run5_topographic_visual_strategy.md` exists and selects the final map concept: topographic relief corridor map, coastal/maritime corridor inset, terrain/barrier callout, or a justified combination.
- [ ] `data/run5_topographic_geodata_manifest.md` exists and documents the geodata source(s), provider, URL or local source, access date, license/usage note, spatial extent, resolution/scale, and whether the data are true elevation/relief or schematic context.
- [ ] If real topographic/relief data are accessible, a processing script exists at `scripts/19_run5_topographic_corridor_visuals.py`; if not, a blocker exists at `docs/run5_topographic_data_blocker.md` with an explicit fallback.
- [ ] At least one new committee-ready figure exists under `figures/final_revised/`:
  - Required: `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`.
  - Optional if feasible: `figures/final_revised/run5_corridor_callout_or_inset.png`.
- [ ] `figures/final_revised/run5_figure_captions.md` exists and gives data, method, what each figure shows, what it does not prove, and where it should appear in the StoryMap/report.
- [ ] `outputs/run5_topographic_corridor_interpretation.md` exists and states whether the new map strengthens, replaces, or only supplements the Run 4 v2 topographic/corridor figure.
- [ ] `submission/final_committee/run5_storymap_insert.md` exists and contains ready-to-paste StoryMap text for the new figure.
- [ ] `submission/final_committee/run5_report_insert.md` exists and contains ready-to-paste report text and a figure caption/cross-reference for the comprehensive committee report.
- [ ] `submission/final_committee/run5_must_do_list.md` exists and updates the practical must-do submission list to include the Run 5 figure integration, final QA, and claim-safety checks.
- [ ] `outputs/run5_claim_and_visual_audit.md` exists and verifies that the new map is visually useful, properly caveated, not overclaimed, and aligned with the Fisher spatial-necessity argument.
- [ ] `outputs/run5_reproducibility_and_manifest.md` exists and records commands, geodata inputs, figure inputs, output paths, manual steps, and reproducibility caveats.
- [ ] `WORK.md` Results and Learnings are updated after every worker iteration and at completion.

## Non-goals
- Do not redo the full cuisine-similarity pipeline.
- Do not redo Run 4 winner-alignment or Run 4 v2 committee-report generation unless a direct insertion is required.
- Do not add a global topographic analysis.
- Do not add many new maps. One strong map is better than several weak maps.
- Do not claim topography or maritime routes caused observed residuals.
- Do not introduce new large datasets unless they directly serve the East/Southeast Asia corridor/topographic figure.
- Do not create or host an ArcGIS StoryMap unless separately authorized and credentials/access are available.
- Do not overwrite existing committee reports or StoryMap scripts; create insert files or revised copies only if the task explicitly requires them.

# 2. Acceptance Checks

## GIS / Topographic Checks
- The primary new figure must make the corridor visually more striking than the prior Run 4 v2 map.
- The figure must use real coordinates from the existing cuisine crosswalk and real coastline/relief/elevation context if accessible.
- If the figure uses true relief/elevation data, the manifest must identify the source and distinguish shaded relief, elevation raster, bathymetry, coastline, administrative boundaries, and any schematic overlays.
- If the figure is only schematic because topographic data are blocked, it must be labeled as a schematic spatial-context map, not a topographic map.
- The figure must focus on East/Southeast Asia and should not include unnecessary global clutter.
- The corridor lines must be derived from existing residual/focused-case outputs or Run 4 v2 accessibility metrics, not hand-drawn without data provenance.
- The map must include enough labels/legend/caption information to explain residual links, topographic/coastal context, and limitations.

## Analysis / Interpretation Checks
- The new map must support one narrow spatial interpretation, such as:
  - high-residual cuisine pairs sit within coherent regional/coastal/island corridor contexts;
  - maritime/coastal geography helps contextualize Filipino links;
  - mainland adjacency helps contextualize Thai–Vietnamese and Chinese–Korean links;
  - terrain/coastal context makes the focused case more spatially interpretable than a pure matrix.
- The interpretation must not infer causality from topography alone.
- Any statements about mountains, coasts, islands, maritime access, or terrain barriers must be framed as spatial context unless supported by explicit model variables.
- The worker must state whether the Run 5 map should be a main figure, supporting figure, or appendix figure.

## Visualization / Submission Checks
- The new figure must be legible at committee-report scale and StoryMap scale.
- The new figure should have a title, compact legend, clear line weights, and readable labels.
- The figure should visually foreground the corridor/residual argument, not just show a pretty basemap.
- The new figure must not duplicate the role of the existing residual bridge-index figure; it should add corridor/topographic context.
- If two figures are created, one must be selected as the primary submission figure and the other must be labeled as optional/appendix.

## Writing / Packaging Checks
- `submission/final_committee/run5_storymap_insert.md` must be concise and ready to paste into the existing StoryMap after the East/Southeast Asia case section or as a supporting map section.
- `submission/final_committee/run5_report_insert.md` must be usable in the committee report without rewriting the whole document.
- `submission/final_committee/run5_must_do_list.md` must clearly state the exact manual tasks the user must do next to integrate the figure into the final StoryMap/report.
- All claims in the insert text must match the claim audit.

## Code / Reproducibility Checks
- Any new script must run from the project root using relative paths.
- Scripts must write only to Run 5-specific output paths.
- No API keys or private credentials may appear in code, data, logs, markdown, or figure metadata.
- If external geodata are downloaded, the command/source and date accessed must be logged.
- If internet access is unavailable, use existing local data or create a documented blocker/fallback.

# 3. Plan
- Audit the existing Run 4 v2 topographic/corridor figure and the East/Southeast Asia focused-case data so the worker knows what must be improved rather than duplicated.
- Select one visual concept that makes the corridor more striking: shaded-relief corridor map, coastal/maritime inset, terrain/barrier callout, or combined relief + residual overlay.
- Attempt to use a real public relief/topographic source at a manageable regional scale. Prefer lightweight sources such as Natural Earth shaded relief/raster relief or an already-available public elevation raster; do not spend the run building a heavy GIS pipeline.
- Create a focused East/Southeast Asia figure that overlays residual cuisine links on topographic/coastal context.
- Write figure captions and interpretation that make the spatial mechanism clear but non-causal.
- Create StoryMap/report insertion text so the new figure can be integrated without rewriting the whole submission.
- Update the must-do list so the user knows exactly how to use the new figure in the final Fisher submission.
- Run a final claim/visual audit and reproducibility manifest.

## Dependencies / Ordering Logic
1. Setup note and artifact audit precede figure strategy.
2. Figure strategy precedes geodata sourcing.
3. Geodata manifest precedes any topographic figure claim.
4. Script/data processing precedes figure creation.
5. Figure creation precedes caption, interpretation, and insertion text.
6. Claim/visual audit precedes final must-do list.
7. Reproducibility manifest and WORK.md updates come last.

## Risk & Mitigation
- Risk: Real topographic data are unavailable in the execution environment. Mitigation: use Natural Earth or existing public-domain relief if locally accessible; otherwise create a clearly labeled schematic and a blocker describing exact needed data.
- Risk: The new map becomes decorative rather than analytical. Mitigation: require corridor lines from residual/focused-case data and a caption that explains the spatial argument.
- Risk: The map visually overstates terrain as causal. Mitigation: include explicit caption language that terrain/coastal context is interpretive context, not causal proof.
- Risk: The figure is cluttered. Mitigation: limit to top 4–6 East/Southeast Asia residual links and use callouts/insets rather than plotting every pair.
- Risk: StoryMap/report integration creates inconsistencies. Mitigation: create insertion text rather than rewriting the whole submission, and run a claim/visual audit.

# 4. Tasks
- [ ] [S01] Create `outputs/run5_setup_note.md` — Inputs needed: Run 4 v2 summary artifacts, existing committee report, existing StoryMap script, and this `WORK.md`. Done when: the file states Run 5’s purpose, target figure type, what prior work is preserved, and non-goals.
- [ ] [A01] Create `outputs/run5_input_artifact_audit.csv` — Inputs needed: `data/processed/run2v2_focus_case_results.csv`, `data/processed/run4v2_east_se_asia_accessibility_metrics.csv`, `data/crosswalks/cuisine_geo_crosswalk.csv`, `figures/final_revised/run4v2_topographic_corridor_map.png`, `submission/revised/storymap_script.md`, and `submission/final_committee/final_committee_report.md`. Done when: each required input is listed with exists/missing status, role, reuse/revise/exclude decision, and blocker note if missing.
- [ ] [V01] Create `docs/run5_topographic_visual_strategy.md` — Inputs needed: `outputs/run5_input_artifact_audit.csv`, existing Run 4 v2 topographic map, East/Southeast Asia case data, and final submission needs. Done when: the file selects one primary visual concept and one fallback, identifies target figure role, planned data layers, top residual pairs to show, and why the figure improves the corridor argument.
- [ ] [D01] Create `data/run5_topographic_geodata_manifest.md` — Inputs needed: selected geodata source(s), local geodata if available, or public source pages if accessed. Done when: the manifest lists provider, URL/local path, date accessed, license/usage note, spatial extent, resolution/scale, variables/layers used, and whether the map is true topographic/relief or schematic.
- [ ] [C01] Create `scripts/19_run5_topographic_corridor_visuals.py` or `docs/run5_topographic_data_blocker.md` — Inputs needed: figure strategy, geodata manifest, focused-case data, and cuisine coordinate crosswalk. Done when: either a relative-path script exists to create the Run 5 figure(s), or a blocker document states exactly why implementation is infeasible and what data/tool is needed.
- [ ] [C02] Run `scripts/19_run5_topographic_corridor_visuals.py` to create `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png` — Inputs needed: script from C01 and required data. Done when: the figure exists, uses Run 5-specific output path, and visibly overlays East/Southeast Asia residual/corridor links on topographic/coastal context; if blocked, leave unchecked and record exact blocker.
- [ ] [C03] Optionally create `figures/final_revised/run5_corridor_callout_or_inset.png` — Inputs needed: script from C01 and successful primary figure data. Done when: an optional inset/callout exists that clarifies one corridor, or the task is explicitly marked skipped in Results because the primary figure is sufficient.
- [ ] [V02] Create `figures/final_revised/run5_figure_captions.md` — Inputs needed: completed Run 5 figure(s), geodata manifest, and corridor metrics. Done when: each figure has a caption with data source, method, visual reading guide, interpretation, limitation, and recommended placement.
- [ ] [R01] Create `outputs/run5_topographic_corridor_interpretation.md` — Inputs needed: Run 5 figure(s), Run 4 v2 corridor summary, and focused-case results. Done when: the file states what the new map adds, what it does not prove, whether it should replace/supplement the Run 4 v2 topographic map, and which final claim it supports.
- [ ] [W01] Create `submission/final_committee/run5_storymap_insert.md` — Inputs needed: Run 5 figure captions and interpretation memo. Done when: the file contains ready-to-paste StoryMap section text with heading, short body text, figure placement note, caption, and claim-safety language.
- [ ] [W02] Create `submission/final_committee/run5_report_insert.md` — Inputs needed: Run 5 figure captions and interpretation memo. Done when: the file contains report-ready prose and caption/cross-reference text for inserting the new figure into the committee report.
- [ ] [F01] Create `submission/final_committee/run5_must_do_list.md` — Inputs needed: StoryMap insert, report insert, final readiness checklist, and Run 5 figure decision. Done when: the file lists exact manual steps to integrate the Run 5 figure into the StoryMap, PDF/report, captions, source notes, and final QA.
- [ ] [Q01] Create `outputs/run5_claim_and_visual_audit.md` — Inputs needed: Run 5 figure(s), captions, StoryMap insert, report insert, and visual strategy. Done when: the audit verifies visual clarity, topographic-data honesty, non-causal language, source documentation, and Fisher spatial-necessity alignment.
- [ ] [F02] Create `outputs/run5_reproducibility_and_manifest.md` — Inputs needed: all Run 5 scripts, figures, manifests, inserts, and command history. Done when: the file lists input artifacts, geodata sources, commands/manual steps, output paths, package assumptions, and reproducibility caveats.
- [ ] [Q02] Update `WORK.md` Results section with final Run 5 artifact checklist — Inputs needed: all completed Run 5 artifacts. Done when: Results lists every created artifact path, verification status, key figure decision, blocked/skipped tasks, and exact missing inputs if any.
- [ ] [Q03] Update `WORK.md` Learnings section with Run 5 lessons and final recommendations — Inputs needed: all completed artifacts and any errors encountered. Done when: Learnings records topographic-data lessons, figure-design lessons, claim-discipline lessons, and final recommendations for the submission.

# 5. Worker Driver Prompt
You are the worker for **Run 5 — Topographic Corridor Visualization Enhancement** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is a focused visual/geospatial enhancement run, not a new research run. Preserve all existing Run 2, Run 2 v2, Run 3, Run 4, and Run 4 v2 artifacts unless a task explicitly creates a Run 5-specific file. The main objective is to create a stronger East/Southeast Asia topographic/corridor visualization that makes the corridor visually striking and strengthens the Fisher spatial-necessity argument.

Use real topographic/relief/coastline data if accessible and document it. If real topographic data cannot be obtained, create a precisely labeled schematic only if it is still useful, and do not call it a topographic map. Do not overclaim: terrain, coastlines, islands, and maritime corridors may provide spatial context, but they do not prove causal mechanisms unless explicitly modeled.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, commands/manual steps, outputs, and verification status; record Learnings with geodata issues, figure design decisions, claim decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing input/access/tool/data, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If the optional inset/callout is unnecessary, mark it skipped in Results rather than expanding scope.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, state whether the Run 5 map should replace, supplement, or remain appendix-only relative to the Run 4 v2 topographic/corridor map, and list the exact manual steps needed to integrate it into the StoryMap/report.

# 6. Learnings

# 7. Results

# 0. Snapshot
- Job Type: Mixed — Research/Synthesis + GIS/Data Improvement + Writing/Exposition + Visualization/Submission Packaging.
- Run: Fisher Award **Run 4 — Winner-Alignment Improvement Pass** for the Culinary Corridors project.
- Primary Deliverables: playbook intake memo; current submission vs past-winner alignment audit; weighted Fisher scorecard; prioritized upgrade plan; improved spatial thesis and scope memo; at least one strengthened geospatial analysis or a precise blocker; revised final figure set; revised StoryMap/report/abstract/pitch; poster/StoryMap compliance materials; updated LaTeX/PDF report if feasible; final before/after improvement memo.
- Stakeholders / Audience: Matthew Tan; Prof. Pia Sorensen as food-science mentor; Harvard Center for Geographic Analysis / Fisher Prize reviewers; any advisor or reviewer asked to evaluate competitiveness.
- Prior Inputs:
  - Strategy packet zip: `fisher_award_strategy_packet.zip`, especially `outputs/fisher_award_playbook.md`, `outputs/feature_matrix.md`, `outputs/scoring_rubric.md`, `outputs/production_timeline.md`, and `outputs/topic_scoring_template.md`.
  - Existing Culinary Corridors submission artifacts from Runs 1–3, especially `submission/storymap_script.md`, `submission/fisher_submission_report.md`, `submission/abstract_and_pitch.md`, `submission/technical_appendix.md`, `submission/data_sources_and_limitations.md`, `figures/final/*`, `docs/run3_final_scope_and_claims.md`, `docs/run3_fisher_positioning_memo.md`, `outputs/run3_claim_audit_checklist.md`, and `report/culinary_corridors_full_report.pdf` / `.tex` if present.
- Constraints:
  - This run improves alignment with past Fisher winners and the Fisher scoring playbook; it must not restart the entire data project.
  - Preserve the settled scope unless the playbook audit shows a clear competitiveness reason to narrow it further: **global discovery screen + East/Southeast Asia primary case + Iberian/Atlantic-Pacific secondary/diagnostic case**.
  - Global results remain exploratory/discovery; focused cases carry the strongest inference.
  - Do not claim causality for migration, trade, colonialism, or maritime exchange unless explicitly modeled and qualified.
  - Do not centralize fermentation or flavor chemistry unless a concise competitiveness memo shows the gain outweighs the added risk.
  - Do not overwrite Run 2/Run 2 v2/Run 3 artifacts; save revised outputs under `run4_*`, `submission/revised/`, `figures/final_revised/`, or `report/revised/` paths.
  - No secrets/API keys. If ArcGIS StoryMap hosting is unavailable, produce StoryMap-ready copy and asset instructions only.
  - Use the strategy packet’s competition rules as the baseline: Fisher criteria are innovation/creativity, use of GIS, data complexity/relevance/documentation, analytical approach/execution, and visualization/cartographic communication. Preserve poster constraints if using poster materials: 42” × 36”, PDF, and no more than 350 words of descriptive text excluding legends/labels/title/citations/captions.

# 1. Goal
Improve the existing **Culinary Corridors** Fisher submission so it more closely matches the patterns and tactical standards identified in the Fisher Award strategy packet and past-winner playbooks. The worker should audit the current package against the playbook, identify gaps relative to previous winners, prioritize the highest-value upgrades, strengthen the project’s spatial necessity and cartographic argument, revise the submission narrative and figures accordingly, and produce a clear before/after assessment of competitiveness. The end state should be a submission package that reads less like a general food-data project and more like a Fisher-winning GIS project: spatially necessary, analytically executed, data-documented, visually compelling, and disciplined in its claims.

## Definition of Done
- [ ] `outputs/run4_playbook_intake_memo.md` exists and summarizes the relevant strategy-packet rules, past-winner patterns, scoring rubric, production constraints, and implications for Culinary Corridors.
- [ ] `outputs/run4_current_submission_audit.csv` exists and inventories all current Run 3/report artifacts with reuse/revise/exclude status.
- [ ] `docs/run4_past_winner_alignment_matrix.md` exists and compares Culinary Corridors to the major past-winner archetypes and tactics from the strategy packet.
- [ ] `outputs/run4_fisher_scorecard_before.md` exists and scores the current project against the strategy-packet rubric, including compliance gate, spatial necessity gate, weighted five-criterion score, and evidence for each score.
- [ ] `docs/run4_priority_upgrade_plan.md` exists and lists 5–10 upgrade moves ranked by expected Fisher score gain, deadline cost, risk, and required artifacts.
- [ ] `docs/run4_revised_spatial_thesis_and_scope.md` exists and states the upgraded one-sentence spatial thesis, final scope, strong claims, cautious hypotheses, forbidden claims, and why the project requires GIS.
- [ ] At least one concrete geospatial-competitiveness upgrade is completed and documented, such as a clearer residual-bridge analysis, boundary/permeability analysis, path/connectivity proxy, spatial outlier/hotspot summary, or improved focused corridor map. If no additional GIS computation is feasible, `docs/run4_geospatial_upgrade_blocker.md` must precisely explain why and define the exact data/method needed.
- [ ] `figures/final_revised/` contains a revised figure set aligned with the playbook: at minimum a hero spatial argument figure, one methods/result figure, one East/Southeast Asia focused case figure, one geospatial-only insight figure, and one limitations/sensitivity figure or appendix figure.
- [ ] `figures/final_revised/run4_revised_figure_captions.md` exists and gives each figure’s data, method, result, limitation, and role in the Fisher argument.
- [ ] `submission/revised/storymap_script.md` exists and is revised to follow the winning playbook: map-led, concise, visually structured, and explicitly tied to Fisher criteria.
- [ ] `submission/revised/fisher_submission_report.md` exists and incorporates the revised thesis, figure set, claims, limitations, and playbook alignment.
- [ ] `submission/revised/abstract_and_pitch.md` exists with a 150–250 word abstract, a 60–90 second pitch, and a 2–3 sentence description optimized for the Fisher judging criteria.
- [ ] `submission/revised/poster_text_350_word_draft.md` exists and provides a <=350-word poster-style narrative option even if StoryMap remains the recommended format.
- [ ] `outputs/run4_claim_and_compliance_audit.md` exists and checks revised materials against overclaiming risks, source documentation, poster/StoryMap constraints, and the Fisher scoring rubric.
- [ ] `outputs/run4_fisher_scorecard_after.md` exists and compares before/after scores with explicit evidence for any claimed improvement.
- [ ] If feasible, revised LaTeX/PDF report artifacts exist under `report/revised/`, including `culinary_corridors_winner_aligned_report.tex`, `culinary_corridors_winner_aligned_report.pdf`, and a source bundle zip. If PDF compilation is unavailable, a precise blocker is recorded.
- [ ] `submission/revised/final_handoff_checklist.md` exists and lists final deliverables, recommended submission route, unresolved blockers, and exact next manual steps.
- [ ] `outputs/run4_reproducibility_and_manifest.md` exists and records all reused inputs, revised outputs, commands/manual steps, figure sources, and caveats.
- [ ] `WORK.md` Results and Learnings are updated after every worker iteration and at completion.

## Non-goals
- Do not redo the full recipe/ingredient ingestion pipeline unless an audit proves the existing outputs are invalid.
- Do not expand into a new topic or add unrelated datasets merely to look complex.
- Do not create a hosted ArcGIS StoryMap unless credentials/access are explicitly available.
- Do not contact Prof. Pia Sorensen directly; prepare or revise materials for the user to send.
- Do not represent the recipe corpus as globally representative.
- Do not hide the recipe-platform bias, cuisine-label caveats, or ingredient-normalization uncertainty.
- Do not let the playbook force superficial imitation of past winners; use winner patterns to strengthen the current project’s own spatial argument.
- Do not create polished design assets at the expense of analytical clarity, data provenance, and claim discipline.

# 2. Acceptance Checks

## Research / Playbook Checks
- The strategy packet must be inspected before recommendations are made; do not rely only on memory of prior winners.
- `outputs/run4_playbook_intake_memo.md` must explicitly extract the five official Fisher criteria, compliance gates, spatial necessity gate, and repeatable past-winner patterns.
- The past-winner alignment matrix must distinguish between direct emulation opportunities and patterns that are inappropriate for Culinary Corridors.
- Any recommendation to change scope, method, or visuals must point to either a Fisher criterion, spatial necessity gate, or repeated winner pattern from the strategy packet.
- Novelty claims must remain conservative; use “candidate,” “suggests,” “consistent with,” and “hypothesis-generating” where causal or representativeness proof is unavailable.

## Data / GIS Checks
- All new analysis must use existing Run 2 v2 / Run 3 data where possible; any new external source must have provider, URL, access date, license/usage note, and reason for inclusion.
- Any geospatial upgrade must use coordinates, distances, regions, boundaries, routes, adjacency, or spatial grouping in a way that cannot be replicated from ingredient vectors alone.
- If implementing new code, scripts must run from project root, use relative paths, avoid secrets, and write outputs only to `data/processed/run4_*`, `outputs/run4_*`, or `figures/final_revised/` unless otherwise specified.
- Original figures and data must not be overwritten.
- Any new model or metric must include a short interpretation note and a limitation note.

## Writing / Exposition Checks
- Revised text must be Fisher-facing and visually guided: question → spatial method → evidence → focused case → limitation → contribution.
- Revised materials must foreground GIS as the engine of the result, not as decorative mapping.
- The global screen, East/Southeast Asia case, and secondary/diagnostic case must be clearly distinguished.
- The report and StoryMap script must use the same thesis, claim hierarchy, and terminology.
- Claims must match the claim audit and must not exceed the evidence.

## Visualization / Cartography Checks
- Final revised figures must be legible enough for judging and must have captions that explain what the map/chart proves and what it does not prove.
- The hero figure must communicate the spatial argument quickly: cuisine similarity is partly geographic, but key insights appear in residual corridors/bridges/boundaries.
- Figures must avoid unnecessary global clutter; use focused maps for inference.
- The final figure set must include at least one “spatial necessity” visual where the insight requires geography.

## Operations / Submission Checks
- If poster text is produced, descriptive text must be <=350 words and stored separately from captions/legends/labels.
- StoryMap route must include section order, figure placement, captions, and asset list even if not hosted.
- Final handoff checklist must include registration, submission deadline, email/submission route, file/URL QA, and source/citation checks.
- All listed final outputs must exist or be marked BLOCKED with exact missing input.

# 3. Plan
- Extract the tactical lessons from the uploaded strategy packet and convert them into a project-specific audit rubric for Culinary Corridors.
- Score the current Run 3/report package honestly before editing; identify the weakest Fisher criteria and the highest-value upgrades.
- Strengthen the project around past-winner patterns: spatial necessity, nontrivial GIS execution, transparent data provenance, a clear analytical workflow, and map-led communication.
- Revise the thesis and scope so the final story is not “world food similarity,” but a spatial-inference project about residual culinary corridors and focused regional evidence.
- Implement or refine one geospatial-only upgrade if feasible within the existing data; if not feasible, document the blocker and ensure the narrative/figures still emphasize existing residual bridge/boundary outputs.
- Rebuild the figure hierarchy around a hero map and a small set of supporting visuals rather than a broad figure dump.
- Revise StoryMap/report/abstract/poster-text materials after the upgraded claims and figures are set.
- Run a claim/compliance audit and create a before/after scorecard to show how the package became more winner-aligned.

## Dependencies / Ordering Logic
1. Strategy-packet intake precedes all scoring and edits.
2. Current artifact audit precedes figure/narrative revision.
3. Before-scorecard precedes upgrade plan.
4. Upgrade plan precedes any new geospatial work or figure revision.
5. Revised spatial thesis precedes revised StoryMap/report writing.
6. Revised figures precede final captions and narrative integration.
7. Claim/compliance audit precedes final revisions and after-scorecard.
8. Handoff checklist and reproducibility manifest come last.

## Risk & Mitigation
- Risk: The current project still appears too much like non-spatial recipe analysis. Mitigation: require a spatial necessity memo, hero map, and one geospatial-only figure.
- Risk: Past-winner comparison tempts overclaiming or superficial imitation. Mitigation: require a matrix that distinguishes emulate vs. avoid patterns.
- Risk: Data-license/platform bias weakens credibility. Mitigation: make source limitations visible and treat global results as discovery only.
- Risk: New GIS analysis is too heavy for the timeline. Mitigation: prioritize refinement of existing residual bridge/boundary outputs; document blockers for heavier path/network analysis.
- Risk: Figure set becomes visually cluttered. Mitigation: use a figure-selection memo and demote weak figures to appendix or exclude them.
- Risk: Poster/StoryMap compliance is overlooked. Mitigation: produce separate compliance checklist and <=350-word poster text draft.

# 4. Tasks
- [ ] [S01] Create `outputs/run4_playbook_intake_memo.md` — Inputs needed: `fisher_award_strategy_packet.zip` and extracted packet files. Done when: the memo summarizes the official Fisher criteria, compliance constraints, spatial necessity gate, weighted scoring logic, past-winner archetypes, and the top implications for improving Culinary Corridors.
- [ ] [S02] Create `outputs/run4_current_submission_audit.csv` — Inputs needed: existing Run 3/report artifacts under `submission/`, `figures/final/`, `docs/`, `outputs/`, and `report/`. Done when: each relevant artifact is listed with path, exists/missing status, role, reuse/revise/exclude decision, and notes.
- [ ] [A01] Create `docs/run4_past_winner_alignment_matrix.md` — Inputs needed: strategy packet `outputs/feature_matrix.md`, `outputs/fisher_award_playbook.md`, and current project materials. Done when: the matrix compares Culinary Corridors to major past-winner patterns/archetypes, identifying emulate moves, avoid moves, and project-specific gaps.
- [ ] [A02] Create `outputs/run4_fisher_scorecard_before.md` — Inputs needed: strategy packet `outputs/scoring_rubric.md`, current StoryMap/report/figures, and current claim audit. Done when: the current project is scored against compliance gate, spatial necessity gate, and the five weighted Fisher criteria with evidence and weaknesses.
- [ ] [A03] Create `docs/run4_priority_upgrade_plan.md` — Inputs needed: `outputs/run4_fisher_scorecard_before.md` and `docs/run4_past_winner_alignment_matrix.md`. Done when: 5–10 upgrade moves are ranked by expected Fisher score gain, implementation cost, risk, affected criterion, and required artifact.
- [ ] [A04] Create `docs/run4_revised_spatial_thesis_and_scope.md` — Inputs needed: `docs/run4_priority_upgrade_plan.md`, current scope/claims memo, and Run 2 v2 interpretation. Done when: the file states revised title options, one-sentence spatial thesis, final scope, strong conclusions, cautious hypotheses, forbidden claims, and spatial necessity argument.
- [ ] [D01] Create `data/run4_data_and_source_risk_review.md` — Inputs needed: `submission/data_sources_and_limitations.md`, `data/run2v2_data_quality_audit.md`, `data/run2_data_access_log.md`, and strategy-packet data criteria. Done when: the file identifies source/documentation weaknesses that would hurt Fisher scoring and gives exact fixes or disclosures.
- [ ] [G01] Create `docs/run4_geospatial_upgrade_selection.md` — Inputs needed: `docs/run4_priority_upgrade_plan.md`, Run 2 v2 geospatial outputs, and available data. Done when: the worker selects one primary geospatial upgrade and one fallback from residual bridge score refinement, boundary/permeability, path/connectivity proxy, spatial outlier/hotspot summary, focused corridor map refinement, or other justified GIS method.
- [ ] [G02] Create `scripts/17_run4_geospatial_upgrade.py` or `docs/run4_geospatial_upgrade_blocker.md` — Inputs needed: selected upgrade from G01 and necessary processed data. Done when: either a relative-path script exists to generate `data/processed/run4_geospatial_upgrade_results.csv`, or a blocker document precisely states why implementation is infeasible and what data/method is needed.
- [ ] [G03] Run `scripts/17_run4_geospatial_upgrade.py` to create `data/processed/run4_geospatial_upgrade_results.csv` — Inputs needed: script from G02 and processed input data. Done when: results exist with documented variables, cuisine pairs or place-level units, spatial metric(s), interpretation fields, and limitations; if blocked, leave unchecked and record exact blocker.
- [ ] [G04] Create `outputs/run4_geospatial_upgrade_summary.md` — Inputs needed: `data/processed/run4_geospatial_upgrade_results.csv` or blocker document. Done when: the file explains what the geospatial upgrade adds to Fisher competitiveness, what it shows, what it does not prove, and how it should be used in final text/figures.
- [ ] [V01] Create `docs/run4_revised_figure_strategy.md` — Inputs needed: `outputs/run4_fisher_scorecard_before.md`, final Run 3 figures, and strategy-packet visualization criteria. Done when: the file defines the revised figure hierarchy: hero figure, method/result figure, primary case figure, geospatial-only figure, secondary/sensitivity figure, appendix figures, and excluded figures.
- [ ] [V02] Create `figures/final_revised/run4_hero_spatial_argument_figure.png` — Inputs needed: selected final/global/residual/geospatial data and V01. Done when: a legible hero figure exists that communicates the core spatial argument quickly.
- [ ] [V03] Create `figures/final_revised/run4_method_or_model_figure.png` — Inputs needed: distance/residual model outputs and V01. Done when: the figure clearly explains the residual method or distance baseline.
- [ ] [V04] Create `figures/final_revised/run4_primary_case_figure.png` — Inputs needed: East/Southeast Asia focused case outputs and V01. Done when: the figure foregrounds the primary focused case and its spatial logic.
- [ ] [V05] Create `figures/final_revised/run4_geospatial_insight_figure.png` — Inputs needed: residual bridge/boundary/path/connectivity outputs or run4 upgrade results. Done when: the figure shows an insight that requires geospatial structure rather than ingredient similarity alone.
- [ ] [V06] Create `figures/final_revised/run4_secondary_or_limitations_figure.png` — Inputs needed: Iberian/Atlantic-Pacific outputs, sensitivity results, data-quality audit, or V01. Done when: a secondary/diagnostic/limitations figure exists or the task is explicitly marked excluded with reason in V01.
- [ ] [V07] Create `figures/final_revised/run4_revised_figure_captions.md` — Inputs needed: all revised figures. Done when: each figure has a caption with data, method, result, limitation, and role in Fisher argument.
- [ ] [W01] Create `submission/revised/storymap_outline.md` — Inputs needed: `docs/run4_revised_spatial_thesis_and_scope.md`, V01, and revised figure captions. Done when: the outline has section order, figure placement, intended viewer takeaway, and transitions.
- [ ] [W02] Create `submission/revised/storymap_script.md` — Inputs needed: `submission/revised/storymap_outline.md`, revised figures/captions, current StoryMap script, and playbook criteria. Done when: the revised script is complete, map-led, concise, and clearly aligned with Fisher criteria and past-winner tactics.
- [ ] [W03] Create `submission/revised/fisher_submission_report.md` — Inputs needed: revised StoryMap script, current report, revised captions, data/source risk review, and technical appendix. Done when: the report is revised around the winner-aligned thesis, figure hierarchy, methods, results, limitations, and conclusion.
- [ ] [W04] Create `submission/revised/abstract_and_pitch.md` — Inputs needed: revised thesis/scope and revised report/script. Done when: the file includes a 150–250 word abstract, a 60–90 second pitch, and a 2–3 sentence project description optimized for Fisher scoring.
- [ ] [W05] Create `submission/revised/poster_text_350_word_draft.md` — Inputs needed: revised report/script and strategy packet format rules. Done when: the file contains a poster-style narrative of <=350 descriptive words, plus a separate word-count note.
- [ ] [W06] Create `submission/revised/pia_review_packet.md` — Inputs needed: prior Pia packet, revised thesis, revised figures, and data/source risk review. Done when: the packet includes a concise email draft, one-page summary, revised figure list, and 8–12 targeted questions focused on food-science validity and claim discipline.
- [ ] [Q01] Create `outputs/run4_claim_and_compliance_audit.md` — Inputs needed: revised script, revised report, revised abstract/pitch, poster-text draft, revised scope memo, and strategy-packet scoring/compliance rules. Done when: the file checks overclaiming, source documentation, global-vs-focused inference, poster/StoryMap compliance, and Fisher rubric alignment.
- [ ] [W07] Revise `submission/revised/storymap_script.md` after Q01 — Inputs needed: `outputs/run4_claim_and_compliance_audit.md`. Done when: every flagged overclaim or clarity issue in the script is corrected or explicitly justified.
- [ ] [W08] Revise `submission/revised/fisher_submission_report.md` after Q01 — Inputs needed: `outputs/run4_claim_and_compliance_audit.md`. Done when: every flagged overclaim or clarity issue in the report is corrected or explicitly justified.
- [ ] [Q02] Create `outputs/run4_fisher_scorecard_after.md` — Inputs needed: revised final materials, Q01, and `outputs/run4_fisher_scorecard_before.md`. Done when: before/after scores are compared with evidence for improvements and remaining weak criteria.
- [ ] [R01] Create or update `report/revised/culinary_corridors_winner_aligned_report.tex` — Inputs needed: `submission/revised/fisher_submission_report.md`, revised captions, revised figures, and current LaTeX source if available. Done when: a LaTeX source file exists under `report/revised/` with the revised winner-aligned report content and figure references.
- [ ] [R02] Compile `report/revised/culinary_corridors_winner_aligned_report.pdf` — Inputs needed: LaTeX source from R01 and revised figures. Done when: the PDF compiles without fatal errors and opens successfully; if LaTeX is unavailable, mark BLOCKED with exact error.
- [ ] [R03] Create `report/revised/culinary_corridors_winner_aligned_source_bundle.zip` — Inputs needed: revised LaTeX source, bibliography/source notes if any, and figures needed to compile. Done when: the zip exists and contains all compile-relevant files.
- [ ] [F01] Create `submission/revised/final_handoff_checklist.md` — Inputs needed: all revised artifacts, Q01, Q02, and production timeline. Done when: the checklist lists recommended submission route, required files/assets, registration/submission steps, remaining blockers, review steps, and final QA items.
- [ ] [F02] Create `outputs/run4_reproducibility_and_manifest.md` — Inputs needed: all run4 outputs, scripts, data inputs, figure inputs, and report compilation logs if available. Done when: the manifest lists reused inputs, revised outputs, commands/manual steps, package assumptions, and reproducibility caveats.
- [ ] [Q03] Update `WORK.md` Results section with final Run 4 artifact checklist — Inputs needed: all completed Run 4 artifacts. Done when: Results lists every created artifact path, verification status, key improvements, blocked items, and exact missing inputs.
- [ ] [Q04] Update `WORK.md` Learnings section with Run 4 pitfalls and recommendations — Inputs needed: all completed artifacts and errors encountered. Done when: Learnings records playbook alignment lessons, figure/narrative lessons, source limitations, GIS-method lessons, and final recommendations.

# 5. Worker Driver Prompt
You are the worker for **Run 4 — Winner-Alignment Improvement Pass** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is an improvement and alignment run, not a full restart. Use the uploaded `fisher_award_strategy_packet.zip` as the playbook for what previous winners and the Fisher criteria suggest. Preserve existing Run 2, Run 2 v2, Run 3, and report outputs unless a task explicitly creates a revised copy under `submission/revised/`, `figures/final_revised/`, `report/revised/`, `outputs/run4_*`, `data/processed/run4_*`, or `docs/run4_*`. Do not widen the project into an unrelated topic.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, commands/manual steps, outputs, and verification status; record Learnings with pitfalls, source issues, figure decisions, claim decisions, geospatial-method decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing input/access/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If a desired geospatial upgrade is too heavy for the available data/time, use the best existing residual bridge/boundary/focused-case analysis and clearly document what would be required for a stronger implementation.

Use the acceptance checks for a Mixed research/data/GIS/writing/visualization job. Every factual or dataset claim needs a source link or citation note. Every revised figure needs a caption and documented input. All final language must be conservative: global results are discovery, focused cases support stronger but non-causal inference, and migration/trade/colonial/maritime interpretations remain hypotheses unless directly modeled. The playbook should improve strategic alignment, not justify overclaiming.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, state whether the revised package is more Fisher-competitive, what the before/after score changed by, which figures and submission route are recommended, which claims are safe, and what exact manual steps the user must take next.

# 6. Learnings

# 7. Results

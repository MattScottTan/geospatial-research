# 0. Snapshot
- Job Type: Mixed — Writing/Exposition + GIS/Visualization Packaging + Operations/Submission QA.
- Run: Fisher Award **Run 6 — ArcGIS StoryMap Conversion Package** for the Culinary Corridors project.
- Primary Deliverables: complete ArcGIS StoryMap copy-paste package; section-by-section script; figure upload/placement plan; captions and alt text; callout boxes; source/limitations panel text; final StoryMap QA checklist; PDF backup integration instructions; updated WORK.md results/learnings.
- Stakeholders / Audience: Matthew Tan; Harvard Center for Geographic Analysis / Fisher Prize reviewers; Prof. Pia Sorensen or other advisors reviewing the final version.
- Prior Inputs:
  - Final Run 5 report and figures, especially `report/final_complete/culinary_corridors_complete_final_report.pdf`, `submission/revised/storymap_script.md`, `submission/final_committee/final_committee_report.md`, `submission/final_committee/run5_storymap_insert.md`, `figures/final_revised/run4_hero_spatial_argument_figure.png`, `figures/final_revised/run4_method_or_model_figure.png`, `figures/final_revised/run4_primary_case_figure.png`, `figures/final_revised/run5_east_se_asia_topographic_corridor_map.png`, `figures/final_revised/run4_geospatial_insight_figure.png`, `figures/final_revised/run4_secondary_or_limitations_figure.png`, and `figures/final_revised/run5_figure_captions.md`.
  - Run 5 WORK/source specification and results, especially the instruction that the Run 5 map should be added immediately after the East/Southeast Asia focused-case section and should not replace the residual bridge-index figure.
- Constraints:
  - This run is for conversion and packaging, not further analysis.
  - Do not create new substantive claims, new geospatial models, or new figures unless a copy/formatting issue blocks StoryMap conversion.
  - Preserve claim hierarchy: global = discovery; East/Southeast Asia = primary focused inference; Iberian/Atlantic-Pacific = secondary/diagnostic; topography = spatial context; residual bridge index = strongest geospatial-only insight.
  - Use cautious language: no causal claims about migration, trade, colonialism, terrain, or maritime routes unless explicitly qualified.
  - Make the final output easy for Matthew to copy and paste into ArcGIS StoryMaps.
  - Do not host or publish the StoryMap unless the user separately provides access and explicit authorization.
  - No secrets/API keys. No external credentials.
  - All final StoryMap text should be concise, visually guided, and panel/judge-facing.

# 1. Goal
Convert the completed **Culinary Corridors** Fisher Award project into a polished, copy-paste-ready ArcGIS StoryMap package. The output should guide the user through building the StoryMap section by section, with exact headings, body text, image placement instructions, captions, alt text, callout boxes, source/limitations notes, and QA checks. The StoryMap should present the project as a map-led GIS investigation: it should move from research question to spatial method, global discovery, East/Southeast Asia focused case, topographic corridor context, residual bridge-index insight, secondary/sensitivity case, limitations, and conclusion.

## Definition of Done
- [x] `outputs/run6_setup_note.md` exists and states the purpose of Run 6, inherited scope, inputs, non-goals, and final StoryMap sequence.
- [x] `outputs/run6_input_artifact_audit.csv` exists and confirms availability/reuse status for all figures, captions, final report, source notes, and Run 5 insertion text needed for conversion.
- [x] `submission/storymap_conversion/storymap_build_order.md` exists and gives the exact ArcGIS StoryMap build order, recommended block types, figure upload order, and section transitions.
- [x] `submission/storymap_conversion/storymap_copy_paste_script.md` exists and contains complete copy-paste-ready StoryMap text, organized by section, including headings, body paragraphs, captions, callouts, and source/limitation notes.
- [x] `submission/storymap_conversion/storymap_figure_manifest.csv` exists and lists every figure to upload with filename, section placement, role, caption, alt text, source note, and whether it is required or optional.
- [x] `submission/storymap_conversion/storymap_alt_text_and_accessibility.md` exists and contains alt text and accessibility notes for each figure and map.
- [x] `submission/storymap_conversion/storymap_source_and_limitations_panel.md` exists and contains concise source/data/limitations language suitable for a StoryMap side panel or closing section.
- [x] `submission/storymap_conversion/storymap_callout_boxes.md` exists and contains short highlighted callouts for research question, method, key finding, caution, and contribution.
- [x] `submission/storymap_conversion/storymap_css_style_notes.md` exists and gives practical ArcGIS styling recommendations: section emphasis, image sizing, caption placement, typography, color restraint, and map-led pacing.
- [x] `submission/storymap_conversion/storymap_pdf_backup_instructions.md` exists and explains how to link or mention the PDF backup in the StoryMap and/or submission form.
- [x] `submission/storymap_conversion/storymap_final_qa_checklist.md` exists and gives a concrete pre-submission QA checklist for desktop/mobile, figure legibility, source links, claim discipline, and form submission.
- [x] `submission/storymap_conversion/storymap_one_page_submission_summary.md` exists and gives a compact one-page description for submission forms, emails, or advisor review.
- [x] `submission/storymap_conversion/storymap_asset_package_manifest.md` exists and lists all assets to upload or keep beside the StoryMap.
- [x] Optional if useful: `submission/storymap_conversion/storymap_section_word_counts.csv` exists and reports approximate section lengths so the StoryMap stays concise.
- [x] `outputs/run6_claim_safety_audit.md` exists and verifies that the copy-paste text preserves the approved claim hierarchy and does not overclaim global representativeness, causality, topography, or cuisine-to-place precision.
- [x] `outputs/run6_reproducibility_and_manifest.md` exists and records reused inputs, generated outputs, manual steps, and unresolved blockers.
- [x] `WORK.md` Results and Learnings are updated after every worker iteration and at completion.

## Non-goals
- Do not redo statistical analysis, geospatial analysis, or figure generation.
- Do not rewrite the entire project into a new thesis.
- Do not create a hosted ArcGIS StoryMap without explicit user authorization and access.
- Do not add unverified historical claims about trade, migration, empire, or maritime routes.
- Do not bury limitations; they must appear early enough that reviewers see the project’s claim discipline.
- Do not create a long PDF-style essay inside the StoryMap; the StoryMap must be concise and visual.
- Do not treat the recipe corpus as globally representative.
- Do not describe the Run 5 relief map as a causal topographic model; it is spatial/relief context.

# 2. Acceptance Checks

## StoryMap / Writing Checks
- The StoryMap must be copy-paste-ready: every section should include exact heading text, body text, figure instruction, caption, and any callout.
- The StoryMap must be visually guided, not report-like: figures should lead the argument.
- The final section order must be:
  1. Title / hero
  2. Research question and problem
  3. Data and caveats
  4. Spatial method / residual logic
  5. Global discovery screen
  6. East/Southeast Asia primary case
  7. Run 5 topographic corridor context
  8. Residual bridge-index / geospatial-only insight
  9. Secondary/diagnostic case and sensitivity
  10. Limitations and claim discipline
  11. Conclusion and contribution
  12. Sources / PDF backup note
- Every section must tell the reviewer what to look at and why it matters.
- The global figure must be described as discovery, not proof.
- The East/Southeast Asia case must be described as the main focused inference case.
- The Run 5 topographic corridor map must be described as relief/coastal/spatial context, not causal proof.
- The residual bridge-index figure must be framed as the strongest geospatial-only insight.

## Figure / Accessibility Checks
- Every figure in the manifest must have:
  - exact filename/path;
  - upload order;
  - recommended StoryMap section;
  - required/optional status;
  - caption;
  - alt text;
  - source/method note;
  - limitation note.
- Captions should be concise enough for StoryMap use but precise enough to prevent overclaiming.
- Alt text must be meaningful, not just “map” or “figure.”
- The primary figure sequence must include:
  1. `run4_hero_spatial_argument_figure.png`
  2. `run4_method_or_model_figure.png`
  3. `run4_primary_case_figure.png`
  4. `run5_east_se_asia_topographic_corridor_map.png`
  5. `run4_geospatial_insight_figure.png`
  6. `run4_secondary_or_limitations_figure.png`
- Optional: `run5_corridor_callout_or_inset.png` can be included as a sidecar/inset if the StoryMap layout has room.

## Claim Safety Checks
- Strong claims must be limited to spatial structure, residual corridors, focused-case evidence, and bridge-score insight.
- Cautious claims may say patterns are consistent with regional adjacency, exchange, maritime/coastal context, or corridor plausibility.
- Forbidden claims must not appear: causation by migration/trade/empire/topography; global representativeness; exact cuisine-to-nation equivalence; true least-cost path/topographic route modeling.
- The limitations section must mention recipe-platform bias, cuisine-label coarseness, mapping uncertainty, ingredient normalization uncertainty, generic ingredient effects, and non-causality.

## Operations / ArcGIS Checks
- The build-order document must be usable without additional explanation.
- The package must distinguish text the user should paste from notes/instructions.
- The user should be able to build the StoryMap by following the artifacts in sequence.
- The final QA checklist must include checking the StoryMap in private/incognito browser, desktop, and mobile if possible.
- The PDF backup instructions must tell the user where to place the PDF link and how to mention it in the submission form.

# 3. Plan
- Audit the final Run 5/Run 4/Run 3 assets and choose the exact figures for StoryMap conversion.
- Freeze the StoryMap narrative sequence and turn the committee-report logic into shorter, map-led sections.
- Create a build-order guide that tells the user which ArcGIS StoryMap block to use for each section.
- Create a full copy-paste script with headings, body text, figure notes, captions, callouts, and source/limitation notes.
- Create a figure manifest with alt text and upload/placement guidance.
- Create separate callout, source/limitations, and PDF-backup documents to make the ArcGIS build process simple.
- Run a claim-safety audit against the approved hierarchy.
- Create final QA and asset-package checklists.

## Dependencies / Ordering Logic
1. Input audit precedes figure manifest and build order.
2. Figure manifest precedes section script and alt text.
3. Build order precedes copy-paste script.
4. Copy-paste script precedes claim audit.
5. Claim audit precedes final QA checklist.
6. PDF backup and asset package instructions come last.
7. WORK.md Results/Learnings are updated at every iteration and at completion.

## Risk & Mitigation
- Risk: The StoryMap becomes too text-heavy. Mitigation: enforce short sections, callouts, and figure-led pacing.
- Risk: The figures are not immediately understandable. Mitigation: provide captions, alt text, and “what to notice” text for each figure.
- Risk: The StoryMap overclaims. Mitigation: run a claim-safety audit and explicitly separate global discovery from focused inference.
- Risk: ArcGIS block types are unavailable or user interface differs. Mitigation: provide generic alternatives for each block type.
- Risk: The PDF backup is forgotten. Mitigation: include PDF placement and submission-form instructions.
- Risk: StoryMap cannot accept a figure or PDF file directly. Mitigation: provide fallback instructions to upload image assets separately and link the PDF through a public/shareable URL.

# 4. Tasks
- [x] [S01] Create `outputs/run6_setup_note.md` — Inputs needed: Run 5 final outputs, current final PDF, final figures, and this `WORK.md`. Done when: the file states Run 6’s purpose, inherited scope, chosen StoryMap sequence, non-goals, and immediate risks.
- [x] [A01] Create `outputs/run6_input_artifact_audit.csv` — Inputs needed: all final figures, final PDF report, final committee report, revised StoryMap script, Run 5 storymap insert, Run 5 captions, and final claim audits. Done when: each artifact is listed with path, exists/missing status, role, reuse/revise/exclude decision, and blocker note if missing.
- [x] [F01] Create `submission/storymap_conversion/storymap_figure_manifest.csv` — Inputs needed: input audit and final figure files. Done when: the CSV lists each StoryMap figure with path, upload order, section, required/optional status, caption, alt text, source note, limitation note, and recommended display size.
- [x] [W01] Create `submission/storymap_conversion/storymap_build_order.md` — Inputs needed: figure manifest, final report, and final StoryMap script. Done when: the file gives exact ArcGIS StoryMap section order, recommended block type for each section, figure placement, and transition logic.
- [x] [W02] Create `submission/storymap_conversion/storymap_copy_paste_script.md` — Inputs needed: build order, figure manifest, final report, existing StoryMap script, Run 5 insert, and claim hierarchy. Done when: the file contains a complete copy-paste-ready StoryMap with section headings, exact body text, figure placement notes, captions, and callouts.
- [x] [W03] Create `submission/storymap_conversion/storymap_callout_boxes.md` — Inputs needed: copy-paste script and final claim hierarchy. Done when: the file contains concise callout boxes for research question, method, main finding, caution, geospatial contribution, and conclusion.
- [x] [W04] Create `submission/storymap_conversion/storymap_source_and_limitations_panel.md` — Inputs needed: data/source limitations from final report and final claim audit. Done when: the file contains concise source/limitations text suitable for a StoryMap source panel or final methods note.
- [x] [W05] Create `submission/storymap_conversion/storymap_alt_text_and_accessibility.md` — Inputs needed: figure manifest and final figures. Done when: each figure has meaningful alt text, plus accessibility recommendations for color, captions, image sizing, and mobile readability.
- [x] [W06] Create `submission/storymap_conversion/storymap_css_style_notes.md` — Inputs needed: build order and figure sequence. Done when: the file gives practical design guidance for ArcGIS StoryMap styling, section breaks, image sizing, text length, and visual hierarchy.
- [x] [W07] Create `submission/storymap_conversion/storymap_pdf_backup_instructions.md` — Inputs needed: final PDF path and expected submission strategy. Done when: the file explains where/how to include the PDF backup link in the StoryMap and what to do if the Fisher submission form accepts only one file or one URL.
- [x] [W08] Create `submission/storymap_conversion/storymap_one_page_submission_summary.md` — Inputs needed: final report, abstract/pitch, and copy-paste script. Done when: the file provides a one-page project description for submission forms, advisor emails, or a StoryMap introduction sidebar.
- [x] [Q01] Create `outputs/run6_claim_safety_audit.md` — Inputs needed: copy-paste script, source/limitations panel, callouts, and final claim hierarchy. Done when: the audit verifies every major claim as strong/cautious/forbidden-safe and lists any required edits.
- [x] [W09] Revise `submission/storymap_conversion/storymap_copy_paste_script.md` after claim audit — Inputs needed: `outputs/run6_claim_safety_audit.md`. Done when: all flagged overclaims or ambiguous phrases in the copy-paste script are corrected or explicitly justified.
- [x] [F02] Create `submission/storymap_conversion/storymap_asset_package_manifest.md` — Inputs needed: final figure manifest, final PDF, and all StoryMap conversion files. Done when: the manifest lists every asset/file the user should keep in the StoryMap build folder and whether it must be uploaded, linked, or only referenced.
- [x] [F03] Create `submission/storymap_conversion/storymap_final_qa_checklist.md` — Inputs needed: build order, copy-paste script, asset package manifest, and claim audit. Done when: the checklist gives concrete pre-submission QA steps for links, figures, captions, desktop/mobile, incognito/private access, source notes, PDF backup, and final submission form.
- [x] [F04] Optionally create `submission/storymap_conversion/storymap_section_word_counts.csv` — Inputs needed: copy-paste script. Done when: approximate word counts by section are listed, or the task is marked skipped if unnecessary.
- [x] [F05] Create `outputs/run6_reproducibility_and_manifest.md` — Inputs needed: all generated Run 6 files and reused inputs. Done when: the manifest records input artifacts, generated outputs, manual steps, package assumptions, and blockers.
- [x] [Q02] Update `WORK.md` Results section with final Run 6 artifact checklist — Inputs needed: all completed Run 6 artifacts. Done when: Results lists every created artifact path, verification status, skipped/blocked tasks, key decisions, and exact manual next steps.
- [x] [Q03] Update `WORK.md` Learnings section with Run 6 lessons and final recommendations — Inputs needed: all completed artifacts and any errors encountered. Done when: Learnings records StoryMap conversion lessons, figure-placement lessons, claim-safety lessons, and final recommendations for the user.

# 5. Worker Driver Prompt
You are the worker for **Run 6 — ArcGIS StoryMap Conversion Package** of the Fisher Award **Culinary Corridors** project. Your source of truth is `WORK.md`.

At the start of every iteration, read `WORK.md` completely, especially the Goal, Definition of Done, Acceptance Checks, Tasks, Learnings, and Results. Pick the single highest-priority unblocked task. Batch tasks only if they are clearly independent and use the same execution pattern. Execute tightly: do only what is required to satisfy the chosen task’s “Done when” condition.

This is a conversion and packaging run, not a new research run. Preserve all existing analysis, figures, reports, and claim hierarchy. Do not create new substantive findings. The main objective is to produce a copy-paste-ready ArcGIS StoryMap package with exact section text, figure placement notes, captions, callouts, alt text, source notes, PDF backup instructions, and QA steps.

Use the final figure sequence: hero residual-corridor figure; residual/distance method figure; East/Southeast Asia focused-case figure; Run 5 topographic corridor map; residual bridge-index figure; secondary/limitations figure. Make sure global results are presented as discovery only, East/Southeast Asia as the main focused inference case, topography as spatial context, and residual bridge scores as the strongest geospatial-only insight.

After each iteration, immediately update `WORK.md`: mark completed tasks `[x]` only when the done-condition is met; record Results with paths, outputs, and verification status; record Learnings with conversion issues, claim decisions, figure-placement decisions, or next-time advice; add new tasks only when they are atomic, verifiable, and necessary for the Definition of Done.

If blocked, do not guess silently. Leave the task unchecked, add a BLOCKED note in Results naming the exact missing file/input/decision, add a new atomic “Unblock:” task if needed, and continue to the next highest-priority unblocked task. If an optional word-count artifact is unnecessary, mark it skipped in Results rather than expanding scope.

Stop when the Definition of Done is satisfied or when all remaining tasks are BLOCKED. In the final Results update, list the exact files the user should open, the order for building the StoryMap, the final figure upload order, and the manual QA steps before submission.

# 6. Learnings

- The StoryMap should be figure-led rather than report-like; every section tells the reviewer what to notice and why it matters.
- The Run 5 topographic map is useful as spatial context, but it must not be described as a causal terrain or route model.
- The residual bridge-index figure remains the strongest geospatial-only insight because it turns pairwise residuals into mapped place-level roles.
- The global residual map should be used as a discovery screen; the East/Southeast Asia case should carry the main focused interpretation.
- ArcGIS image handling can crop cover images, so the hero map may work better as a full-width image below a simpler cover if the cover crop hides map detail.
- Local sandbox links are not public submission links; upload assets to ArcGIS, Harvard storage, or another approved/shareable location before submission.


# 7. Results

Run 6 completed on 2026-05-01.

## Created artifacts
- `outputs/run6_setup_note.md` — Run purpose, inherited scope, final sequence, non-goals, and risks.
- `outputs/run6_input_artifact_audit.csv` — input figure/report/caption audit with reuse decisions.
- `submission/storymap_conversion/storymap_figure_manifest.csv` — upload order, file paths, captions, alt text, source notes, limitation notes, and display guidance for all required/optional figures.
- `submission/storymap_conversion/storymap_build_order.md` — exact ArcGIS StoryMap build sequence with recommended block types and transitions.
- `submission/storymap_conversion/storymap_copy_paste_script.md` — complete copy-paste-ready StoryMap sections, body text, captions, figure placement notes, callouts, and final source/PDF note.
- `submission/storymap_conversion/storymap_callout_boxes.md` — reusable callouts for research question, method, key finding, caution, contribution, and conclusion.
- `submission/storymap_conversion/storymap_source_and_limitations_panel.md` — concise source/limitations panel text.
- `submission/storymap_conversion/storymap_alt_text_and_accessibility.md` — meaningful alt text and accessibility guidance for every figure.
- `submission/storymap_conversion/storymap_css_style_notes.md` — practical ArcGIS StoryMap design/style notes.
- `submission/storymap_conversion/storymap_pdf_backup_instructions.md` — how to include or submit the full PDF backup.
- `submission/storymap_conversion/storymap_one_page_submission_summary.md` — compact project summary for submission forms, emails, or advisor review.
- `outputs/run6_claim_safety_audit.md` — verifies that StoryMap language preserves claim hierarchy and avoids forbidden claims.
- `submission/storymap_conversion/storymap_asset_package_manifest.md` — all files/assets to keep in the build folder and their use.
- `submission/storymap_conversion/storymap_final_qa_checklist.md` — concrete pre-submission QA steps.
- `submission/storymap_conversion/storymap_section_word_counts.csv` — approximate section lengths for pacing.
- `outputs/run6_reproducibility_and_manifest.md` — inputs, outputs, assumptions, and manual next steps.
- `WORK.md` — updated source-of-truth log for this completed Run 6.

## Key StoryMap decisions
- Primary format: ArcGIS StoryMap.
- Backup format: final complete PDF report.
- Required figure sequence: hero residual-corridor figure; residual/distance method figure; East/Southeast Asia focused-case figure; Run 5 topographic corridor map; residual bridge-index figure; secondary/limitations figure.
- Optional figure: Run 5 corridor callout/inset if the StoryMap layout has room.
- Claim hierarchy preserved: global = discovery; East/Southeast Asia = primary focused inference; topography = spatial context; residual bridge index = strongest geospatial-only insight.

## Manual next steps
1. Open `submission/storymap_conversion/storymap_build_order.md`.
2. Upload figures using `submission/storymap_conversion/storymap_figure_manifest.csv`.
3. Paste the text from `submission/storymap_conversion/storymap_copy_paste_script.md` section by section.
4. Add alt text from `submission/storymap_conversion/storymap_alt_text_and_accessibility.md`.
5. Add a public/shareable PDF backup link using `storymap_pdf_backup_instructions.md`.
6. Complete `submission/storymap_conversion/storymap_final_qa_checklist.md` before submission.

No blockers remain. No hosted StoryMap was created because the run was explicitly limited to conversion materials and did not have ArcGIS credentials or publishing authorization.

# WORK.md — Bridges Across Cuisines: Final Competitiveness Fixes

# 0. Snapshot
- **Job Type:** Mixed (Code/Engineering + Writing/Exposition + Research/Synthesis + Operations)
- **Primary Deliverables:**
  - `tools/build_bridge_index.py` — canonical, reproducible bridge-index script (NEW)
  - `figures/v4_05_bridge_index_map_and_chart.png` — regenerated with canonical values
  - `tools/build_v4_01_hero.py` — corrected hero-figure regeneration script (NEW or revised)
  - `figures/v4_01_hero_world_corridors.png` — regenerated; no Italian–Russian orange corridor
  - `current_state/BUILD_INSTRUCTIONS_v8.md` — updated bridge values, reframed Russian case study, new Section 12 data-provenance appendix
  - `current_state/storymap_preview.pdf` — rebuilt from updated build doc
  - Updated `docs/PRIZE_ENTRY_DESCRIPTION.md`, `README.md`, `docs/ANALYSIS_EXTENSION_NOTES.md`, `docs/QA_REPORT.md` — all numerically consistent
  - Published ArcGIS StoryMap URL + sent submission email (USER actions)
- **Stakeholders / Audience:** Matthew Tan (project owner). Final reviewers: Howard T. Fisher Prize judges at Harvard CGA.
- **Constraints:**
  - **Hard deadline: Sunday May 3, 2026 at 23:59 ET.** Package was assembled ~21:30; remaining wall-clock budget is tight.
  - StoryMap **not yet published** (Path A). All edits live in build doc + figure files only — **no live ArcGIS edits during this work**. Single paste-and-publish at the end.
  - Registration confirmed (per user).
  - Do not introduce new analytical methods. Reuse Mantel / partial Mantel / LISA / bootstrap / permutation infrastructure already in the project.
  - Preserve the Scoring Pass: claim-title cover (*"Cuisine resemblance has a shape that distance can't predict"*), claim-led captions on Figures 1, 4, 5, 6, 7, the Manila-Galleon-named Conclusion payoff, and the front-loaded Introduction order.
  - Preserve EIP voice: declarative-statistical, no "atlas" word, no "proves" (hypothesis-confirming sense).
  - Reproducibility constants: seed = 42, 9999 permutations, 2000 bootstrap iterations.

# 1. Goal
Apply three pre-publication fixes that close the project's open audit trails before the StoryMap goes live: (1) replace the published bridge-index values (0.87 / 0.84 / 0.69 …) with canonical values that fall out of a fully documented, reproducible formula — accepting that Russian's #2 ranking does not survive — and propagate the new values + reframed Russian case study across every doc that cites them; (2) regenerate the hero corridor map under the corrected residual pipeline so that no negative-residual pair (Italian–Russian most importantly) is drawn as a positive-residual corridor, and fix the Moroccan longitude bug in `tools/figdata.py` along the way; (3) add a 9-column data-provenance dictionary as a Section 12 appendix to satisfy the packet's documented-data discipline. Then rebuild the PDF preview, run a number-consistency sweep, paste into ArcGIS StoryMaps, incognito-test the public URL, and email Jeff Blossom before 23:59.

## Definition of Done (verifiable)
- [ ] `tools/build_bridge_index.py` runs deterministically (seed=42) and emits `bridge_index_canonical.json` with values for all 20 cuisines.
- [ ] `figures/v4_05_bridge_index_map_and_chart.png` regenerated; bar chart values, map circle sizes, and inline labels all read from `bridge_index_canonical.json`.
- [ ] `figures/v4_01_hero_world_corridors.png` regenerated; visual inspection confirms (a) no orange corridor for Italian–Russian, (b) Moroccan anchor at correct longitude (−7.09), (c) Robinson projection + corpus-coverage note preserved, (d) overall style matches previously published version.
- [ ] `tools/figdata.py` Moroccan longitude corrected to −7.09.
- [ ] `current_state/BUILD_INSTRUCTIONS_v8.md` Section 7 (Finding 3) prose, Figure 5 caption, and Section 9 Russian case study updated; Russian's bridge claim demoted from "second-place" to "participates in the residual network"; LISA LL classification leads the Russian narrative.
- [ ] All bridge-index values cited in `BUILD_INSTRUCTIONS_v8.md`, `README.md`, `docs/PRIZE_ENTRY_DESCRIPTION.md` (all 4 variants), `docs/ANALYSIS_EXTENSION_NOTES.md`, `docs/QA_REPORT.md` match the canonical values.
- [ ] Section 12 has a new "Data dictionary" appendix block immediately after the existing narrative — 9 columns, one row per dataset cited in the bibliography (excludes pure software references), each row cross-references a bibliography entry [N].
- [ ] `current_state/storymap_preview.pdf` rebuilds cleanly (`xelatex` × 2 passes); new bridge values visible in PDF.
- [ ] Number-consistency QA sweep: every numerical claim in the build doc is verified against the regenerated working data; no stale value survives.
- [ ] **USER:** StoryMap published, public sharing on, incognito-tested from a second device, all 11 figures + appendix table render correctly on desktop and mobile.
- [ ] **USER:** Submission email sent to `jblossom@cga.harvard.edu` with StoryMap URL + Variant C description before 23:59 ET.
- [ ] **USER:** Sent timestamp + non-bounce confirmation saved.

## Non-goals
- Do not add new analytical methods. The bootstrap, permutation test, partial Mantel, LISA, anchor sensitivity are all sufficient.
- Do not redesign the StoryMap structure. Sections 1–13 stay in their current order; the data dictionary is an appendix block inside Section 12, not a new section.
- Do not undo any Scoring Pass framing (claim-title, claim-led captions, payoff paragraph, front-loaded Introduction).
- Do not expand the corpus. n = 20 stays.
- Do not address project-level issues outside the three-item fix list (e.g., do not redo the Russian anchor sensitivity, do not add new colonial-coding rationales).
- Do not edit live in ArcGIS until the full paste-and-publish step.

# 2. Acceptance Checks

## Code/Engineering checks
- `tools/build_bridge_index.py` (a) imports only project-standard libraries (NumPy, pandas), (b) reads inputs from `reference_inputs/`, (c) is deterministic with seed=42 and produces identical output across runs.
- `tools/build_fig05_bridge.py` no longer contains any hardcoded `BRIDGE_SCORES` dict; reads from `bridge_index_canonical.json`.
- `tools/build_v4_01_hero.py` runs from project root and uses `reference_inputs/residual_matrix.npy` + `reference_inputs/distance_matrix.npy` + `reference_inputs/cuisines.txt` + corrected `tools/figdata.py` for anchor coordinates.
- The hero-figure orange-corridor selection uses (distance ≥ threshold) AND (residual > 0) — Italian–Russian (residual = −0.022) is filtered out by the residual-sign condition.
- Both regenerated figures match the published visual style: Robinson projection, beige land + light-blue ocean, country borders, 30° graticule, labeled cuisine anchors, corpus-coverage note in the lower right of the hero.

## Writing/Exposition checks
- "atlas" appears 0 times in `BUILD_INSTRUCTIONS_v8.md`.
- "proves" / "demonstrates" / "shows that" do not appear in hypothesis-confirming sense; "is consistent with" / "is testable against" / "supports the claim formally" usage preserved.
- Claim-title (*Cuisine resemblance has a shape that distance can't predict*) and the five claim-led captions (Figures 1, 4, 5, 6, 7) are preserved verbatim except where Figure 5's caption needs new numerical values.
- Russian case study (Section 9): LISA LL p = 0.009 is the lead evidence; bridge-index claim either dropped or softened to "participates in the residual network alongside Filipino, Southern U.S., and French anchors."
- All bridge-index magnitudes in prose match `bridge_index_canonical.json` to 2 decimal places.
- Section 7 (Finding 3) "three structural geographies" framing (Pacific-archipelagic / Eurasian-continental / Atlantic-rim) is preserved — these are LISA-driven, not bridge-index-driven, and they survive the recompute.

## Research/Synthesis checks
- Section 12 data dictionary has all 9 columns: Dataset name / Source citation / Date accessed / Spatial resolution or unit / Temporal coverage / CRS or projection / Preprocessing performed / Why relevant / Known limitations.
- Every dataset/data-product cited in the bibliography has a row (Yummly, Zelený, Natural Earth, ETOPO 2022, UN M49, colonial crosswalk, ArcGIS Pro/Online if it provided basemap data). Pure software-tool references (NumPy, pandas, scikit-learn, GeoPy, Matplotlib, Cartopy, Basemap, PySAL, Mantel-method papers) do **not** get a row — they belong in the bibliography only.
- Each row cross-references its bibliography entry by `[N]` so a judge can trace every dataset claim to a citation.
- "Known limitations" column is honest and dataset-specific (not boilerplate); for the Yummly corpus this means platform-mediation + U.S.-recipe-skew + n=20 cuisine label coverage.

## Operations checks
- PDF preview rebuilds without errors; page count within ±2 of the previous build (currently 23 pages).
- Number-consistency QA: extend the table from `docs/QA_REPORT.md` with new bridge-index rows; every entry verified against working data; no stale numbers survive.
- **USER:** ArcGIS StoryMap publishes; sharing set to public.
- **USER:** Incognito test from a second device passes (URL loads, all 13 sections + appendix render, 11 figures display, mobile rendering acceptable).
- **USER:** Submission email sent before 23:59; timestamp saved; no bounce-back received within 30 minutes.

# 3. Plan

## Approach
- **Run three substantive tracks in parallel where possible.** [C] Code track produces canonical values + regenerated figures. [W] Writing track waits on canonical values, then propagates them. [R] Research track is independent and can run anytime. [O] Operations track runs last.
- **Code-then-Writing dependency.** W1 (substitution table) is gated on C3 (canonical top-10 verified). All other [W] tasks gate on W1. Hero regeneration (C7–C10) is independent of bridge-index work and can run in parallel.
- **Single paste-and-publish.** No intermediate ArcGIS publishes. Worker stops at `O2`; user takes over at `O3`.
- **Minimum-viable fallback for each track**, in case time runs out:
  - **Bridge-index fallback:** If C1–C6 cannot complete, fall back to a footnote in Section 7 disclosing that "the bridge-index values are versioned in `analysis_pipeline/build_case_studies.py`; an independent reimplementation (`analysis_extension/bridge_bootstrap.py`) reproduces the ranking pattern but with different absolute values" — a transparent caveat instead of a recompute.
  - **Hero figure fallback:** If C7–C10 cannot complete, ship the existing PNG with the alt-text-only fix that's already in place. Cosmetic-only loss.
  - **Data dictionary fallback:** If R1–R3 cannot complete fully, ship a compact 4-column inline table at the top of Section 12 (Dataset / Source / Resolution+CRS / Preprocessing+Limits) without the full 9-column appendix.

## Dependencies / ordering logic
- **Critical path:** C1 → C2 → C3 → W1 → (W2..W9 in parallel) → O1 → O2 → USER:O3
- **Independent of critical path (run in parallel):**
  - C7 → C8 → C9 → C10 (hero regeneration)
  - R1 → R2 → R3 (data dictionary)
- **Internal Code dependencies:** C5 depends on C2 (needs canonical JSON); C6 depends on C5; C4 depends on C3 (needs new top-3).
- **Stop-edit rule:** No edits to `BUILD_INSTRUCTIONS_v8.md` after O1 (PDF rebuild) until QA in O2 passes.

## Risk & mitigation (each row has a corresponding task)
| Risk | Mitigation | Where in tasks |
|---|---|---|
| Canonical bridge-index formula is ambiguous; recompute produces unstable values | C1 explicitly documents the 5 components + normalization in a docstring before any value is changed downstream | C1 |
| Russian's #2 ranking loss cascades into more narrative damage than expected | Russian case study leads on LISA LL evidence (independent of bridge index) — survives the recompute; W4 explicitly reframes around LISA | W4 |
| Hero figure regeneration produces visually different style | C8 reads style parameters from existing PNG metadata first; C10 visual-inspection step before integrating | C8, C10 |
| Hero regeneration fails or runs over budget | Documented fallback: ship existing PNG with alt-text-only fix | Plan §"Minimum-viable fallback" |
| Data-dictionary table renders awkwardly in ArcGIS | R2 decision step + R3 uses ArcGIS-friendly markdown table syntax | R2, R3 |
| Cross-document inconsistency on bridge values | W1 produces a single substitution table that all other [W] tasks consume; O2 number-consistency sweep at the end | W1, O2 |
| Time pressure: paste-and-publish too late for 23:59 | Stop-edit rule at O1; minimum-viable fallbacks per track; user takes over at O3 immediately when worker reports done | Plan, O1 |
| Submission email goes to wrong address or arrives without URL | O6 spec includes exact recipient, subject, body template, attached/inline URL | USER:O6 |

# 4. Tasks

Flat checkbox list. Track prefixes: **[C]** Code, **[W]** Writing, **[R]** Research, **[O]** Operations. **USER:** = manual action outside worker scope.

## [C] Code track — canonical bridge index + figure regeneration

- [ ] **C1.** Document the canonical 5-component bridge-index formula in a header docstring of a new file `tools/build_bridge_index.py`. Read `analysis_extension/bridge_bootstrap.py` and `analysis_pipeline/build_case_studies.py` first; the canonical formula is the one already implemented in `bridge_bootstrap.py`. Docstring lists each component, its computation, the equal-weighting scheme, and the 0–1 normalization step.
  - **Path:** `tools/build_bridge_index.py` (new file)
  - **Inputs:** `analysis_extension/bridge_bootstrap.py`, `analysis_pipeline/build_case_studies.py`
  - **Done when:** file exists; docstring lists all 5 components by name with formulas; no implementation yet.

- [ ] **C2.** Implement `tools/build_bridge_index.py` to compute canonical bridge index for all 20 cuisines from the residual matrix and emit `analysis_extension/bridge_index_canonical.json` with `{cuisine: score}` sorted descending. Use seed = 42; deterministic.
  - **Path:** `tools/build_bridge_index.py`, `analysis_extension/bridge_index_canonical.json`
  - **Inputs:** `reference_inputs/residual_matrix.npy`, `reference_inputs/cuisines.txt`
  - **Done when:** script runs end-to-end, emits the JSON file, ranks all 20 cuisines, identical output across reruns.

- [ ] **C3.** Verify canonical top-10 against the bootstrap point estimates in `docs/ANALYSIS_EXTENSION_NOTES.md` (Filipino ≈ 0.79, Southern U.S. ≈ 0.76, French ≈ 0.74, Cajun-Creole ≈ 0.73, Brazilian ≈ 0.66, Russian ≈ 0.38). Confirm new top-3 = {Filipino, Southern U.S., French}.
  - **Path:** verification only; results recorded in §6 Learnings
  - **Inputs:** `bridge_index_canonical.json`, `docs/ANALYSIS_EXTENSION_NOTES.md`
  - **Done when:** canonical top-3 confirmed and recorded.

- [ ] **C4.** Modify `analysis_extension/top3_permutation.py` to test the **new** canonical top-3 (Filipino, Southern U.S., French) instead of the old published top-3. Re-run; save new p-value to `analysis_extension/top3_permutation_v2.json`.
  - **Path:** `analysis_extension/top3_permutation.py` (modify constant), `analysis_extension/top3_permutation_v2.json`
  - **Inputs:** residual matrix; new top-3 from C3
  - **Done when:** new p-value computed and persisted; check sign matches published-top-3 result direction.

- [ ] **C5.** Modify `tools/build_fig05_bridge.py` to read `analysis_extension/bridge_index_canonical.json` instead of any hardcoded `BRIDGE_SCORES` dict. No other logic change.
  - **Path:** `tools/build_fig05_bridge.py`
  - **Inputs:** existing script
  - **Done when:** grep `BRIDGE_SCORES` returns no hardcoded constant in the file; script imports + reads JSON.

- [ ] **C6.** Regenerate `figures/v4_05_bridge_index_map_and_chart.png`. Visual style (color palette, projection, fonts, two-panel layout) must match the published version. Bar chart and map circle sizes both reflect new canonical values.
  - **Path:** `figures/v4_05_bridge_index_map_and_chart.png`
  - **Inputs:** modified `tools/build_fig05_bridge.py`, `bridge_index_canonical.json`
  - **Done when:** PNG regenerated; visual inspection confirms (a) Filipino remains top of bar chart, (b) Russian no longer near top, (c) "Pacific-archipelagic anchor" annotation still on Filipino, (d) Eurasian/Atlantic-rim color encoding preserved.

- [ ] **C7.** Read `tools/build_fig01_hero.py` (existing). Determine whether it can produce the hero map with corrected residual filtering or whether a clean rewrite is needed. Document decision.
  - **Path:** `tools/build_fig01_hero.py` (read), decision recorded in §6 Learnings
  - **Inputs:** existing script
  - **Done when:** decision made: revise existing OR write `tools/build_v4_01_hero.py` from scratch.

- [ ] **C8.** Implement orange-corridor selection logic: pairs with (geographic distance ≥ long-distance threshold used by the original) AND (residual > 0 under the regenerated pipeline). Blue corridors (E/SE Asia focused-case links) are unchanged. Code path: revised `tools/build_fig01_hero.py` OR new `tools/build_v4_01_hero.py` per C7.
  - **Path:** chosen script from C7
  - **Inputs:** `reference_inputs/residual_matrix.npy`, `reference_inputs/distance_matrix.npy`, `reference_inputs/cuisines.txt`
  - **Done when:** Italian–Russian (residual −0.022) is filtered out by the residual-sign condition; verify by listing the corridors the script will draw before rendering.

- [ ] **C9.** Fix the Moroccan longitude bug in `tools/figdata.py`: change Moroccan longitude from 35.21 to −7.09. Confirm no other downstream constants reference the bad value.
  - **Path:** `tools/figdata.py`
  - **Inputs:** existing file
  - **Done when:** grep confirms Moroccan longitude is −7.09 in all locations within `figdata.py`.

- [ ] **C10.** Regenerate `figures/v4_01_hero_world_corridors.png` using the corrected hero script and fixed `figdata.py`. Visual inspection: (a) Italian–Russian not drawn as orange line, (b) Moroccan anchor at correct longitude, (c) Robinson projection + beige land + light-blue ocean preserved, (d) corpus-coverage note in lower right preserved, (e) blue E/SE Asia focused-case corridors unchanged, (f) overall style matches previously published version closely enough that a reader would not notice the regeneration.
  - **Path:** `figures/v4_01_hero_world_corridors.png`
  - **Inputs:** chosen script from C7–C8, fixed `tools/figdata.py`
  - **Done when:** PNG regenerated; all six visual checks pass.

## [W] Writing track — propagate canonical values + reframe Russian

- [ ] **W1.** Build a substitution table mapping `{old_published_value → new_canonical_value}` and `{old_top_3_membership → new_top_3_membership}` from C3 output. This is the single source of truth for all [W] tasks.
  - **Path:** `WORK_substitution_table.md` (scratch, project root)
  - **Inputs:** `bridge_index_canonical.json` from C2
  - **Done when:** table covers Filipino (0.87 → new), Russian (0.84 → new), Southern U.S. (0.69 → new), and any other entry that appears in the existing top-10 or in case-study text.
  - **BLOCKED until:** C3 done.

- [ ] **W2.** Update Section 7 (Finding 3) prose in `current_state/BUILD_INSTRUCTIONS_v8.md` (lines ~378–441). Replace bridge-index magnitudes; demote Russian from "second-place bridge" to "continental-bridge LISA anchor that participates in the residual network." Recompute or soften concentration ratios (the 41% / 64% claim) under new values. Keep "three structural geographies" framing intact.
  - **Path:** `current_state/BUILD_INSTRUCTIONS_v8.md` (Section 7)
  - **Inputs:** W1 substitution table; new canonical values
  - **Done when:** every numerical claim in Section 7 matches `bridge_index_canonical.json`; Russian's bridge-rank claim demoted; three-structural-geographies framing preserved.
  - **BLOCKED until:** W1 done.

- [ ] **W3.** Update the Figure 5 caption block in `current_state/BUILD_INSTRUCTIONS_v8.md` to match new values. Preserve the claim-led opening sentence ("The residual network is anchored by a small set of high-connectivity bridge cuisines whose geographies are distinct rather than redundant.") — only the specific values cited later in the caption change.
  - **Path:** `current_state/BUILD_INSTRUCTIONS_v8.md` (Figure 5 caption)
  - **Inputs:** W1 substitution table
  - **Done when:** caption opens with claim sentence; numerical values match canonical; alt text also updated if it cites values.
  - **BLOCKED until:** W1 done.

- [ ] **W4.** Reframe the Russian case study (Section 9, Russian block). Lead with the LISA LL classification (the only highly-significant LL in the corpus, p = 0.009 published / p = 0.081 independent — keep both citations, the dual-implementation transparency is a strength). Demote any bridge-index ranking claim. Preserve: trans-polar / Eurasian-continental framing, the anchor-sensitivity paragraph (Siberian centroid vs Moscow), and the top-5 residual partner list (Irish, Mexican, British, Southern U.S., French) — those are LISA / residual-matrix facts, independent of the bridge index.
  - **Path:** `current_state/BUILD_INSTRUCTIONS_v8.md` (Section 9, Russian case study)
  - **Inputs:** existing case study, LISA results, W1 substitution table
  - **Done when:** paragraph leads with LISA LL evidence; bridge-index claim removed or softened to "participates in"; trans-polar / continental-bridge framing intact; anchor-sensitivity paragraph intact; partner list intact.
  - **BLOCKED until:** W1 done.

- [ ] **W5.** Sweep `current_state/BUILD_INSTRUCTIONS_v8.md` for any remaining bridge-index value citations (Sections 2, 5, 8, 10). Update each to canonical values. The Manila Galleon Conclusion paragraph cites Filipino specifically — that anchor survives the recompute; only any specific numeric claim needs updating.
  - **Path:** `current_state/BUILD_INSTRUCTIONS_v8.md` (full doc grep)
  - **Inputs:** W1 substitution table
  - **Done when:** grep for old published values (0.87, 0.84, 0.69, 0.68, 0.65) finds zero hits in the build doc; every replacement matches W1.
  - **BLOCKED until:** W1 done.

- [ ] **W6.** Update `docs/PRIZE_ENTRY_DESCRIPTION.md` Variants A, B, C, D. Variant B specifically cites "Filipino 0.87, Russian 0.84, Southern_US 0.69" — replace with canonical values and adjust prose around Russian's role. Variant D's longer narrative may also reference these values.
  - **Path:** `docs/PRIZE_ENTRY_DESCRIPTION.md`
  - **Inputs:** W1 substitution table
  - **Done when:** all four variants use canonical values; Russian framing demoted in any sentence that previously said "Filipino top, Russian second."
  - **BLOCKED until:** W1 done.

- [ ] **W7.** Update `README.md` headline-results table row "Top bridge cuisines (published)" with canonical values.
  - **Path:** `README.md`
  - **Inputs:** W1 substitution table
  - **Done when:** README headline table matches canonical.
  - **BLOCKED until:** W1 done.

- [ ] **W8.** Update `docs/ANALYSIS_EXTENSION_NOTES.md` to remove "the bridge-index reimplementation does not reproduce published values" caveat language (it's no longer a caveat now that the reimplementation IS the published index). Re-frame the bootstrap CIs and permutation results as direct tests of the canonical index. Update the new-top-3 permutation result from C4.
  - **Path:** `docs/ANALYSIS_EXTENSION_NOTES.md`
  - **Inputs:** W1, C4 output (`top3_permutation_v2.json`)
  - **Done when:** the "reimplementation vs published" caveat is gone; permutation result cites the new top-3.
  - **BLOCKED until:** W1, C4 done.

- [ ] **W9.** Update `docs/QA_REPORT.md` to mark the bridge-index reproducibility flag as resolved. Add a new entry to the number-consistency table covering the new canonical values.
  - **Path:** `docs/QA_REPORT.md`
  - **Inputs:** W1 substitution table
  - **Done when:** QA report acknowledges the audit-trail closure; table extended with new bridge-index rows; status notes updated.
  - **BLOCKED until:** W1 done.

## [R] Research/Synthesis track — data-provenance dictionary

- [ ] **R1.** Compile a 9-column data-dictionary entry for each non-software dataset cited in the build doc's bibliography. Columns: Dataset / Source [bib N] / Date accessed / Spatial resolution or unit / Temporal coverage / CRS or projection / Preprocessing performed / Why relevant / Known limitations. Expected rows: Yummly recipe corpus, Zelený anadat-r repository, Natural Earth (land/borders/coastlines/rivers/lakes — 110m + 50m), ETOPO 2022 15-arc-second relief, UN M49 statistical regions, the colonial-administration crosswalk (project-internal new dataset, cite `analysis_extension/colonial_crosswalk.csv`), ArcGIS Pro/Online (basemap data only). **Exclude:** NumPy, pandas, scikit-learn, GeoPy, Matplotlib, Cartopy, Basemap, PySAL, Mantel and Smouse-Long-Sokal papers, Anselin LISA paper, Python language reference, Fisher Prize page entry — these are software/method/admin references, not datasets.
  - **Path:** `WORK_data_dictionary.md` (scratch, project root)
  - **Inputs:** `current_state/BUILD_INSTRUCTIONS_v8.md` Section 12 + Bibliography, `analysis_extension/README.md`
  - **Done when:** all expected dataset rows present; each cell filled (no blanks); each row references a bibliography number.

- [ ] **R2.** Decide table location structure inside Section 12. Default: keep the existing two narrative paragraphs intact (they read well and support the EIP voice), and append a new "Data dictionary appendix" subsection at the end of Section 12 with the full 9-column table. ArcGIS-friendly markdown pipe-table syntax. Document the decision in §6 Learnings.
  - **Path:** structural decision; documented in §6
  - **Done when:** decision committed and recorded.

- [ ] **R3.** Insert the data-dictionary appendix block into `current_state/BUILD_INSTRUCTIONS_v8.md` immediately after the existing Section 12 narrative, before the Section 12 separator that leads to Section 13. Use the existing `> ➤ ArcGIS action` + `> ➤ PASTE` directive format. Add a small subheading ("Data dictionary") via a heading block.
  - **Path:** `current_state/BUILD_INSTRUCTIONS_v8.md` (Section 12, after existing narrative)
  - **Inputs:** R1 dictionary, R2 decision
  - **Done when:** new heading + paste block + table inserted; table renders as markdown pipe-table; every row has a bibliography cross-reference.
  - **BLOCKED until:** R1, R2 done.

## [O] Operations track — QA + handoff

- [ ] **O1.** Rebuild `current_state/storymap_preview.pdf` from the updated build doc. Run `xelatex storymap_preview.tex` twice for cross-references. Confirm: PDF builds without errors; new bridge-index values visible on Section 7 page; new Section 12 appendix table renders; page count within ±2 of previous (currently 23 pages).
  - **Path:** `current_state/storymap_preview.pdf`
  - **Inputs:** updated `current_state/storymap_preview.tex` (regenerate via `tools/build_latex.py` if its inputs changed), regenerated figures from C6 + C10
  - **Done when:** PDF rebuilds cleanly; visual spot-check on Sections 7 / 9 / 12 confirms updates landed.
  - **BLOCKED until:** all [W], [R], C6, C10 done.

- [ ] **O2.** Number-consistency QA sweep. Extend the table in `docs/QA_REPORT.md` with new bridge-index entries; re-verify every numerical claim in `BUILD_INSTRUCTIONS_v8.md` against the working data (Mantel r = +0.63, partial Mantel r = +0.51, colonial partial Mantel r = +0.18 / p = 0.022, LISA Mexican p = 0.047 / Jamaican p = 0.040 / Russian p = 0.009, Local I values, top residual pairs, R² = 0.397, slope = −0.124, plus all new bridge values). Flag any stale number; do not stop until all match.
  - **Path:** `docs/QA_REPORT.md` (extend table); verification log to §7 Results
  - **Inputs:** all updated docs, JSON results files
  - **Done when:** table shows ✓ for every checked claim; zero stale numbers; results logged.
  - **BLOCKED until:** O1 done.

- [ ] **O3.** **USER:** Open ArcGIS StoryMaps editor at `storymaps.arcgis.com`. Sign in with Harvard ArcGIS Online account. Click + New story → Start from scratch. Paste `current_state/BUILD_INSTRUCTIONS_v8.md` from top to bottom following every `> ➤ ArcGIS action` and `> ➤ PASTE` directive. Upload all 11 figures (now including regenerated v4_01 and v4_05). Add alt text per the build doc's Alt-text blocks.
  - **Path:** ArcGIS Online (manual)
  - **Done when:** all 13 sections + Section 12 appendix pasted; all 11 figures uploaded; all alt texts entered.

- [ ] **O4.** **USER:** Set sharing to public. Copy URL.
  - **Path:** ArcGIS Online (manual)
  - **Done when:** URL accessible without ArcGIS sign-in.

- [ ] **O5.** **USER:** Incognito / private-browser test from a second device. Verify (a) URL loads, (b) all 13 sections render, (c) all 11 figures load, (d) Section 12 appendix table renders, (e) mobile rendering acceptable on phone, (f) cover-page claim title displays correctly.
  - **Path:** manual
  - **Done when:** all six checks pass; any failure → fix in editor, re-test, repeat.

- [ ] **O6.** **USER:** Compose submission email to `jblossom@cga.harvard.edu`. Subject: *Fisher Prize Submission — Bridges Across Cuisines — Matthew Tan*. Body: Variant C from `docs/PRIZE_ENTRY_DESCRIPTION.md` (≈330 words) + StoryMap URL + brief sender details (Harvard College, graduating senior, concentration). Save a draft for screenshot before sending.
  - **Path:** email client (manual)
  - **Done when:** email composed; URL inline; sender info clear; draft saved.

- [ ] **O7.** **USER:** Send before 23:59 ET. Within 30 minutes confirm: sent timestamp, URL still public, no bounce-back, no SMTP failure. Save a screenshot of the sent email + the StoryMap URL response.
  - **Path:** email client (manual)
  - **Done when:** email confirmed sent before 23:59; non-bounce confirmed; proof-of-submission saved.

# 5. Worker Driver Prompt

```
You are executing a Mixed-track plan against WORK.md for the "Bridges Across Cuisines"
Fisher Prize submission. The deadline is tonight at 23:59 ET.

EVERY ITERATION:
1. Read WORK.md from project root. Re-read it fully — do not rely on memory between
   iterations.
2. Pick the highest-priority unblocked task. Priority order:
   (a) Critical-path tasks: C1 → C2 → C3 → W1 → (W2..W9 in parallel) → O1 → O2.
   (b) Independent tracks runnable in parallel: C7..C10 (hero), R1..R3 (data dict).
   (c) USER-prefixed tasks (O3..O7) are out of scope. Stop and report when reached.
   Within a track, do tasks in numeric order. A task is "blocked" if its
   "BLOCKED until:" line names a task that is not yet [x].
3. Execute the chosen task tightly. Touch only the files in its "Path" line.
   Do not expand scope. Do not add features.
4. Verify the "Done when:" condition before marking complete. If you cannot
   verify, do not mark [x]; instead, append a Learning note about why, and pick
   the next unblocked task.
5. Update WORK.md:
   - Mark the task [x].
   - Append a one-line entry to §7 Results stating what changed and the file path.
   - If you discovered a pitfall, pattern, or surprise, append a one-paragraph
     entry to §6 Learnings.
   - Add new tasks ONLY if they are atomic, have a Path + Done-when, and are
     necessary for Definition of Done. Use the same [C]/[W]/[R]/[O] prefix.
6. Stop when:
   - Every Definition of Done item that is NOT a USER: task is checked, OR
   - You hit a hard blocker that requires user input (record it in §6 and §7
     and stop), OR
   - You have completed all worker-track tasks (C, W, R, and O1+O2). Then
     report: "Worker track complete. USER tasks O3–O7 remain. Suggested order
     and timing in §3 Plan."

ACCEPTANCE CHECKS to enforce (job is Mixed):
- Code: deterministic with seed=42; reads from reference_inputs/; visual style
  of regenerated figures matches published versions.
- Writing: claim-title preserved; "atlas" word absent; "proves" absent in
  hypothesis-confirming sense; bridge-index values match bridge_index_canonical.json
  to 2 decimal places everywhere.
- Research: all 9 columns present in data-dictionary; bibliography
  cross-references on every row; software-only references excluded.
- Operations: PDF rebuilds cleanly; number-consistency sweep passes.

DO NOT:
- Edit live in ArcGIS StoryMaps. All edits go to BUILD_INSTRUCTIONS_v8.md and
  figure files. The user pastes once at O3.
- Add new analytical methods. Reuse existing infrastructure.
- Undo Scoring Pass framing (claim-title, claim-led captions, payoff paragraph,
  front-loaded Introduction, Manila-Galleon-named Conclusion).
- Touch Sections 1, 3, 4, 5 unless explicitly required by a task.
- Modify reference_inputs/*.npy or *.json — these are immutable analytical inputs.

FALLBACKS if time runs short (each track has one — see §3 Plan):
- Bridge-index: footnote-only disclosure instead of recompute.
- Hero figure: ship existing PNG with alt-text-only fix.
- Data dictionary: ship compact 4-column inline table without 9-column appendix.

If you must invoke a fallback, mark the original tasks [~] (partial) rather
than [x], record the fallback decision in §6 Learnings, and add a new
fallback-specific task with [x] when complete.

Begin: read WORK.md.
```

# 6. Learnings
*(initially empty — worker appends one paragraph per surprise/pitfall/pattern as work progresses)*

# 7. Results
*(initially empty — worker appends one line per completed task: what changed, file path, any URL or hash)*

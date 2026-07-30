# WORK.md — Bibliography and Data Sources Completion

# 0. Snapshot
- **Job Type:** Mixed — Writing/Exposition (inserting corpus name + cuisine count, formatting bibliography) + Research/Synthesis (selecting and verifying references)
- **Primary Deliverables:** Updated `BUILD_INSTRUCTIONS.md` (the v7 file currently in `/mnt/user-data/outputs/`), with all `[TODO: ...]` placeholders in Section 11 (Data sources) and Section 12 (Bibliography) replaced with verified, EIP-style numbered citations. Inline numbered citations added at appropriate points in Section 3 (How the analysis works) and Section 11.
- **Stakeholders / Audience:** Matthew Tan (project owner, primary reader); Harvard CGA / Fisher Prize reviewers (eventual readers of the published StoryMap)
- **Constraints:**
  - Match EIP submission's numbered citation style (`[1]`, `[2]`, …) inline and in the bibliography list
  - Use only sources Matthew actually drew on per the LaTeX final report and v3 paste block 16, **plus** standard tool/library citations for code that was actually used
  - Each reference must be verifiable (real publication/site, current URL)
  - Edit Sections 3, 11, and 12 only — do not modify Findings, case studies, conclusion, or the figure structure
  - Total bibliography target: 12–18 entries (focused project, not EIP density)
  - The script must remain pasteable into ArcGIS StoryMaps without changes to block types
- **Reference materials available:**
  - `/home/claude/fisher_full/report/final_complete/culinary_corridors_complete_final_report.tex` — final LaTeX report with the "Selected Source and Artifact Notes" section
  - `/home/claude/fisher_full/data/raw/recipe_source_manifest.md` — names the corpus (Yummly/Kaggle "What's Cooking" via Zelený anadat-r)
  - `/home/claude/fisher_full/data/run2_dataset_selection_memo.md` — 39,774 recipes, 20 cuisines, 6,714 raw ingredient names confirmed
  - `/home/claude/fisher_full/storymap_step_by_step_package/storymap_full_script_by_blocks.md` — block 15 has the prose source families list
  - `/mnt/user-data/outputs/culinary_corridors_storymap_v7_BUILD_INSTRUCTIONS.md` — current canonical script (v7) with `[TODO]` placeholders to fill

# 1. Goal

Update Sections 3, 11, and 12 of the v7 BUILD_INSTRUCTIONS.md so (a) the recipe corpus is named ("Yummly 'What's Cooking' / Kaggle, accessed via Zelený's anadat-r prepared version"), (b) the cuisine count is stated (20 cuisine labels; 39,774 recipes; 6,714 raw ingredients), and (c) Section 12 contains a complete numbered bibliography in EIP style with verified references — no `[TODO]` placeholders anywhere in the file. Inline `[N]` citations are added at the right points in Sections 3 and 11 so the bibliography is grounded in the body text.

## Definition of Done

- [ ] `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md` exists (renamed from `culinary_corridors_storymap_v7_BUILD_INSTRUCTIONS.md` or copied to that path) with all updates applied
- [ ] Section 11 paste block names the corpus exactly as: "Yummly 'What's Cooking' Kaggle dataset, accessed via the prepared version in Zelený's anadat-r repository"
- [ ] Section 11 paste block states "20 cuisine labels," "39,774 recipes," and "6,714 raw ingredient names" (or equivalent prose phrasing)
- [ ] Section 11 paste block lists the source families (Natural Earth, UN M49, Basemap/ETOPO) in prose — not bullets — matching EIP voice
- [ ] Section 12 paste block contains a numbered bibliography with 12–18 entries, no `[TODO]` markers, no fabricated authors/titles
- [ ] Each Section 12 entry has format: `[N] Author(s). (Year). Title. Source/Publisher. URL.`
- [ ] Section 3 (How the analysis works) has inline `[N]` citations at appropriate points (e.g., after first mention of GeoPy, after first mention of cosine similarity, after first mention of the recipe corpus)
- [ ] Section 11 has inline `[N]` citations at appropriate points (after each named source family)
- [ ] All inline `[N]` numbers exist as entries in Section 12; no orphan citations
- [ ] Cmd-F search for the literal string `[TODO` in the entire file returns 0 hits
- [ ] Every URL in the bibliography has been verified to load to a real, on-topic page (or replaced if dead)
- [ ] No changes to Sections 1, 2, 4, 5, 6, 7, 8, 9, 10, or to any image upload / caption / alt-text instruction
- [ ] Final file delivered via `present_files`

## Non-goals

- Do not rewrite Findings 1–4, the four cuisine case studies, the conclusion, or the introduction
- Do not change figure filenames, captions, alt text, or upload order
- Do not add citations for sources Matthew did not consult (no Crosby, Mintz, Carney, Anderson unless Matthew explicitly approves them in iteration)
- Do not change the citation style (must remain numbered `[N]` to match EIP)
- Do not modify any cover, byline, or build-instruction wrapper text
- Do not run the StoryMap build, publish, or submit

# 2. Acceptance Checks

**Writing (format):**
- [ ] Bibliography entries use consistent format: `[N] Author. (Year). Title. Source. URL.`
- [ ] Inline citations use bracketed numerals `[N]` (no `(N)`, no superscript)
- [ ] Section 11 is prose, not bullets (matches EIP)
- [ ] Section 12 is a numbered list (one entry per number)
- [ ] No `[TODO]`, `[FILL IN]`, `[verify]`, `[??]`, or any placeholder syntax remains anywhere in the file

**Research (citation accuracy):**
- [ ] Every citation is a real, currently-resolvable source (web-verified within this run)
- [ ] No invented authors, titles, or DOIs
- [ ] All tool citations match what the project actually used (Python, scikit-learn, NumPy, Pandas, SciPy, GeoPy, Matplotlib, Cartopy, Natural Earth, ArcGIS Pro, ArcGIS Online)
- [ ] All data citations match what the project actually used (Yummly/Kaggle/Zelený, Natural Earth, UN M49, ETOPO)
- [ ] Any "added for methodological context" reference (e.g., Ahn et al. 2011 Flavor Network) is clearly justified by the project's actual analytical move, not added for prestige

**Number consistency:**
- [ ] Inline `[N]` numbers in Sections 3 and 11 each correspond to an entry in Section 12
- [ ] Section 12 entries are numbered consecutively starting at `[1]` with no gaps
- [ ] Same source is cited with the same `[N]` everywhere it appears

# 3. Plan

## Approach summary
- Take the source families already documented in the LaTeX report and v3 sources block as the canonical base list
- Add citations for the Python libraries actually used in the figure-generation code (scikit-learn for regression, GeoPy for geodesic distances, Cartopy + Matplotlib for figures, NumPy/Pandas for data handling)
- Optionally add 1–2 academic methodology references (Ahn et al. 2011 Flavor Network is the obvious foundational paper for ingredient-network analysis, even if Matthew did not cite it — flag clearly for his review)
- Web-verify every URL before inclusion
- Convert URL-list style to EIP numbered format `[N] Author. (Year). Title. Source. URL.`
- Lock the numbering, then add inline `[N]` citations at natural points in Sections 3 and 11
- Final consistency pass: every inline number resolves; no `[TODO]` remains

## Dependencies / ordering logic
1. T1 (assemble candidate list) → T2 (verify URLs) → T3 (freeze numbering)
2. T3 must complete before T4, T5, T6 (any of which need fixed numbers)
3. T4, T5, T6 can run in any order once T3 is done
4. T7 (final QA) runs last
5. T8 (deliver) runs after T7

## Risk & mitigation
- **Risk:** Adding academic references Matthew did not consult could be flagged as overclaiming a literature review.
  → **Mitigation (Task T1.5):** Any reference not in the LaTeX report's existing sources gets an explicit "added for methodological context — Matthew to confirm" note in the WORK.md Results during iteration. Worker pauses for confirmation if more than 3 such additions accumulate.
- **Risk:** Citation URLs go stale or 404.
  → **Mitigation (Task T2):** Web-search every URL; if dead, find a current canonical URL or remove the entry.
- **Risk:** Inline citation numbers drift from bibliography numbering.
  → **Mitigation (Task T7):** Final QA includes explicit cross-reference check between every `[N]` in the body and Section 12 entries.
- **Risk:** Worker over-edits and rewrites prose outside the three target sections.
  → **Mitigation (driver prompt):** Driver prompt explicitly enumerates the only three sections that may be modified, and instructs the worker to use `str_replace` (not full file rewrites) wherever possible.
- **Risk:** Worker invents citations to hit a target count.
  → **Mitigation (acceptance check):** Every entry must have a verified URL. No URL = no entry.

# 4. Tasks

- [ ] **T1. Assemble candidate reference list.** Inputs: `/home/claude/fisher_full/report/final_complete/culinary_corridors_complete_final_report.tex` (the "Selected Source and Artifact Notes" section), the figure-generation Python scripts (which name actual libraries used), and `/home/claude/fisher_full/data/raw/recipe_source_manifest.md`. Done when: a draft list exists at `/tmp/references_draft.md` containing every candidate citation in the form `Author. (Year). Title. Source. URL.`, organized into three groups: (a) data sources used, (b) tooling/libraries used, (c) optional methodological context (clearly flagged). Where: `/tmp/references_draft.md`.

- [ ] **T2. Web-verify each candidate reference.** Inputs: `/tmp/references_draft.md`. Done when: each entry has been confirmed by web search to be a real source with a currently-resolvable URL; entries that cannot be verified are either replaced with a verified equivalent (if the citation type is essential — e.g., the corpus paper) or removed (if optional). Annotate each entry in the file with `[verified YYYY-MM-DD]` or `[removed: reason]`. Where: `/tmp/references_draft.md` (annotated in place).

- [ ] **T3. Freeze the numbering and produce the final bibliography list.** Inputs: verified `/tmp/references_draft.md`. Done when: the entries are numbered `[1]` through `[N]` (where N is between 12 and 18), in a logical order (corpus first, then methodology, then tooling, then basemap/regional sources, then institutional pages), and saved at `/tmp/bibliography_final.md` ready to drop into Section 12. Where: `/tmp/bibliography_final.md`.

- [ ] **T4. Copy v7 file to working file and update Section 11 (Data sources).** Inputs: current `/mnt/user-data/outputs/culinary_corridors_storymap_v7_BUILD_INSTRUCTIONS.md`, `/tmp/bibliography_final.md`. Done when: a copy named `BUILD_INSTRUCTIONS.md` exists in `/mnt/user-data/outputs/`, and within it, Section 11's paste block has the corpus name ("Yummly 'What's Cooking' Kaggle dataset, accessed via Zelený's anadat-r prepared version"), the counts (20 cuisine labels; 39,774 recipes; 6,714 raw ingredient names), the source families in prose with inline `[N]` citations matching the bibliography, and zero `[TODO]` markers. Where: `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md` (Section 11 only). Use `str_replace` against the entire current Section 11 paste block.

- [ ] **T5. Update Section 12 (Bibliography).** Inputs: `/tmp/bibliography_final.md`, `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md`. Done when: Section 12's paste block contains the full numbered bibliography from `/tmp/bibliography_final.md`, each entry on its own line, no `[TODO]` markers, no `[verify or replace]` notes, and the editorial wrapper around the paste block is updated to remove the "I have left placeholder slots…" preamble (it is no longer accurate). Where: `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md` (Section 12 only).

- [ ] **T6. Add inline `[N]` citations to Section 3 (How the analysis works).** Inputs: `/tmp/bibliography_final.md`, current Section 3 paste block. Done when: Section 3 has inline numbered citations at these points (or equivalents): after the first mention of the recipe corpus → corpus citation; after "GeoPy's great-circle method" → GeoPy citation; after "cosine similarity" → either Ahn et al. 2011 (if included) or scikit-learn / SciPy citation; after "Natural Earth" if mentioned (it isn't currently in Section 3, but Section 11 is the natural home — verify). Edits use `str_replace` and add only the numbered brackets, not new sentences. Where: `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md` (Section 3 only).

- [ ] **T7. Final QA pass.** Inputs: updated `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md`. Done when: (a) `grep -c "\[TODO" BUILD_INSTRUCTIONS.md` returns 0; (b) every inline `[N]` in Sections 3 and 11 has a matching entry in Section 12; (c) Section 12 numbering is consecutive with no gaps; (d) each entry in Section 12 has a non-empty URL; (e) the file's other sections (1, 2, 4, 5, 6, 7, 8, 9, 10) are byte-for-byte identical to the v7 version (verify with `diff` against the original v7). Where: `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md`.

- [ ] **T8. Deliver the updated file.** Inputs: completed `/mnt/user-data/outputs/BUILD_INSTRUCTIONS.md`. Done when: `present_files` has been called on the file with a brief summary message describing what changed (Sections 3, 11, 12) and what remained untouched. Where: chat output to user.

# 5. Worker Driver Prompt

```
You are the worker for a tightly scoped editing task. Read this WORK.md before every iteration. Your job is to fill in the bibliography and corpus details for an ArcGIS StoryMap submission's build-instructions document, without touching anything else.

ITERATION LOOP:
1. Open WORK.md. Find the highest-priority unchecked task in Section 4. Tasks are ordered; respect the dependencies in Section 3.
2. Confirm the task's inputs are available. If any input is missing or ambiguous, mark the task BLOCKED with a one-line reason in WORK.md Section 4 and stop.
3. Execute the task. Produce exactly one concrete artifact per task. Do not bundle multiple tasks.
4. Verify the task's "Done when" condition is satisfied.
5. Update WORK.md:
   - Mark the task [x]
   - Append a short bullet under Section 7 (Results) describing what changed (paths, line counts, key decisions made)
   - Append a short bullet under Section 6 (Learnings) IF you discovered something useful (a dead URL, a citation Matthew did not consult, a formatting subtlety)
   - Add new tasks ONLY if they are atomic AND necessary AND were not foreseeable at planning time. Each new task must have its own "Done when" condition and live location.
6. STOP when the Definition of Done in Section 1 is fully checked, OR when a task is BLOCKED and explicitly captures what input is needed.

CONSTRAINTS YOU MUST RESPECT:
- Edit ONLY Sections 3, 11, and 12 of /mnt/user-data/outputs/BUILD_INSTRUCTIONS.md. Sections 1, 2, 4, 5, 6, 7, 8, 9, 10 are off-limits.
- Use str_replace for in-place edits. Do not rewrite the whole file.
- Every reference you add must have a verified, currently-resolvable URL. No URL = no entry. If a URL is dead, find a canonical replacement or omit the entry.
- Do NOT invent authors, titles, DOIs, or institutional affiliations. If you cannot verify, do not include.
- Maintain numbered citation style [N] inline and in the bibliography list. Do not switch to author-year or any other style.
- If you find yourself adding more than 3 references that Matthew did not previously cite, PAUSE. Surface this in WORK.md Results, mark the task BLOCKED, and stop. Wait for confirmation before continuing.
- Do not run the StoryMap build, publish, or submit. Do not invoke ArcGIS or any external service. You are an editor, not a publisher.

ACCEPTANCE CHECKS (run after each iteration that touches the deliverable):
- grep -c "\[TODO" /mnt/user-data/outputs/BUILD_INSTRUCTIONS.md should be 0 by end of T5
- Every inline [N] in Section 3 and Section 11 must correspond to an entry in Section 12
- Section 12 numbering must be consecutive [1], [2], ..., [N] without gaps
- Sections 1, 2, 4, 5, 6, 7, 8, 9, 10 must be byte-for-byte identical to the v7 source

STOP CONDITIONS:
- All Section 4 tasks are checked AND Section 1 Definition of Done is fully checked → call present_files on the deliverable, write a brief summary message, stop.
- Task is BLOCKED with a clearly captured "needs input" reason → stop without calling present_files. The user will respond.
- More than 3 unforeseen reference additions accumulate → pause, surface in Results, stop.

DO NOT:
- Rewrite the script.
- Change the citation style.
- Add references the user did not consult unless explicitly flagged with a "Matthew to confirm" note in Results.
- Touch the figures or figure captions.
- Run beyond the scope of the 8 tasks listed in Section 4 unless adding genuinely atomic, verifiable subtasks.
```

# 6. Learnings

(initially empty — populated during execution)

# 7. Results

(initially empty — populated during execution)

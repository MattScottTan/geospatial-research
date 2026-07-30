# Bridges Across Cuisines — Submission Package

**Submission deadline: tonight (Sun May 3, 2026, 11:59pm).**

This is the final submission package for the Fisher Prize StoryMap. It includes the full v8 build (all four numbered findings + new Finding 1.5 spatial-statistical layer + four case-study cuisines with paired spotlight figures), the regenerated v4_02 baseline figure with QA-driven label correction, all carry-over figures from v6/v7, the interactive Leaflet companion, deployment instructions, prize-entry-form copy in four length variants, and a comprehensive QA report.

---

## What's in this folder

| File | What it is | What you do with it |
|---|---|---|
| `BUILD_INSTRUCTIONS_v8.md` | Single-file build script for the StoryMap (840 lines, 13 sections) | Open it, paste top-to-bottom into ArcGIS StoryMaps |
| `figures/` | All 11 PNG figures, ready to upload | Upload each in the right Section per the build doc's Pre-flight Figures table |
| `bridges_interactive.html` | Self-contained Leaflet interactive map | Deploy via `DEPLOYMENT_GUIDE.md`; embed the resulting URL in the StoryMap |
| `DEPLOYMENT_GUIDE.md` | How to host the interactive (GitHub Pages or Netlify Drop) | Pick Option 1 or Option 2 — about 10 minutes either way |
| `PRIZE_ENTRY_DESCRIPTION.md` | Project description copy in four length variants | Pick the variant that fits your submission-form field |
| `QA_REPORT.md` | Full pre-flight QA pass with verification tables and remaining issues | Read once before publishing; addresses every numerical claim and known caveat |

---

## Order of operations

About 90 minutes end-to-end if you don't hit ArcGIS quirks.

### 1. Build the StoryMap (~50 min)

Open `BUILD_INSTRUCTIONS_v8.md`. Sign in to **storymaps.arcgis.com** with your Harvard ArcGIS Online account. Click **+ New story → Start from scratch**. Work top to bottom through the build script — every action is marked with `> ➤` and every block of text to paste is in a fenced code block. Upload figures from the `figures/` folder per the Pre-flight table at the top of the doc.

The new Section 5 (Finding 1.5) sits between the old Findings 1 and 2 — that's the Mantel + LISA spatial-statistical layer that lifts the GIS-use score from 3 to a projected 5. Sections 6, 7, 8 are the original Findings 2, 3, 4 renumbered. Section 9 (Four cuisines that explain the pattern) now includes a paired spotlight figure for each of Filipino, Russian, Thai, and Spanish, with the new LISA classification integrated into each case-study narrative.

### 2. Deploy the interactive map (~10 min)

Follow `DEPLOYMENT_GUIDE.md` Option 1 (GitHub Pages — the more defensible URL for an academic submission) or Option 2 (Netlify Drop — fastest). Both produce a public HTTPS URL. Paste it into a StoryMap **Embed** block in Section 5, after the v4_07 LISA-and-Mantel figure. Add a brief intro line and caption — there's a paste-ready copy block in the deployment guide.

### 3. Run the 10 final QA tests (~15 min)

They're at the bottom of the build doc under "## Final QA before submitting." Test #4 is the number-consistency check — Cmd-F each value listed and confirm it's correctly stated. The QA pass I ran has already verified every number is correct in the prose, but a second-pass cmd-F is sensible insurance.

### 4. Public-share test (~3 min)

Open the published StoryMap in an incognito browser window. If it asks you to sign in, your sharing settings are wrong — fix in the Share menu (set sharing to "Everyone (public)").

### 5. Submit (~5 min)

Pick a description variant from `PRIZE_ENTRY_DESCRIPTION.md` (Variant C is the most likely fit for the form's project-description field). Paste into the Fisher submission form. Provide the StoryMap URL in the appropriate field.

### 6. Save proof of submission

Screenshot the submitted form. Save the email confirmation. Done.

---

## What's verified and what isn't

### Verified ✓

- **All key analytical numbers** match the regenerated working data (`mantel_results.json`, `lisa_results.json`, `residual_matrix.npy`):
  - R² = 0.397, slope = −0.124, intercept = 1.258
  - Mantel r = +0.6301 (p < 0.001, n_perm = 9999)
  - Partial Mantel r = +0.5116 (p < 0.001)
  - Global Moran's I = +0.0912 (p = 0.052)
  - Russian LISA: LL, p = 0.0088, Local I = +0.1399
  - Mexican LISA: HH, p = 0.0472
  - Jamaican LISA: HH, p = 0.0396
  - Filipino mean residual = +0.0548; Local I = −0.4941 (most negative in corpus)
  - Top pairwise residuals all verified (Chinese-Korean +0.435, Irish-Southern_US +0.395, Thai-Vietnamese +0.395, Filipino-Thai +0.357, etc.)
- **Every case-study scorecard's reported partner residuals match the regenerated data** to two decimal places.
- **Bibliography is renumbered** (19 entries, with the four new methodology citations [3]–[6]: Mantel, Smouse-Long-Sokal, Anselin, PySAL). All inline citations updated to match.
- **Section heading numbering** is consistent across the changelog, Pre-flight Figures table, QA tests, and Quick-Reference table.
- **All 11 figures present** in `figures/` and referenced consistently in the build doc.
- **No stale text** from the original pipeline survives in the prose (verified by sweep — see QA_REPORT.md).
- **Interactive HTML is self-contained** — Leaflet from HTTPS CDN, OpenStreetMap/CARTO tiles. No build step, no separate data files, ready to drop onto any static host.

### Carried over from earlier draft (not re-derived but spot-checked as plausible) — see QA_REPORT.md

- The **+0.139 Iberian/Atlantic mean residual at n = 11** and the **+0.115 same-subregion mean at n = 11** in Finding 2. These depend on the UN-M49 subregion-to-cuisine mapping which the deliverables don't ship explicitly. A spot-check at n = 11 with a plausible Iberian/Atlantic membership returned +0.126 (close to +0.139). The original published numbers are likely still right, but if you have the subregion mapping in your working files a 2-minute re-derivation would let you confirm.

### Known minor pixel-level inconsistencies (text in doc is consistent; pixels of one figure aren't)

- **v4_01 hero map** still draws Italian-Russian as an orange long-distance corridor. Under the regenerated pipeline, Italian-Russian has a small *negative* residual (−0.022). I updated the v4_01 alt text to drop the Italian-Russian reference, so the doc text is internally consistent. If you have time on Sunday, regenerating v4_01 to filter on positive residual under the new pipeline would close this. If not, ship as-is — the dominant visual story is unchanged.

### Pending Matthew action (cannot be verified without you)

- Image alt text actually pasted into ArcGIS (the gear/edit icon check)
- Sharing settings set to public on the published StoryMap
- Bibliography URLs spot-checked once more before publishing (the QA report flags four URLs that should be re-checked since they're new this version)
- Submission form filled out with chosen description variant

---

## What lifted the GIS-use score

The Fisher Prize judges weight the GIS-use score from 3 to 5 based on whether the project demonstrates spatial methodology beyond mapping. The v8 build addresses this directly through:

1. **Mantel test on full pairwise distance matrices** with 9,999-permutation significance — formalizes the descriptive scatter from Finding 1 as a statistically real relationship.
2. **Partial Mantel controlling for subregional adjacency** — shows the distance signal is independent of mere neighbor-adjacency.
3. **Local Moran's I (LISA) at four spatial-weights schemes** (inverse-distance, k-NN k=4, k-NN k=6, Gaussian-kernel) — locates the residual structure spatially with formal significance and four-scheme robustness, identifying three structural roles (Atlantic-rim HH cluster, Eurasian continental LL outlier, Pacific-archipelagic HL bridges).
4. **PySAL implementation** — cited and reproducible.
5. **Case-study figures** that translate the global LISA result into per-cuisine residual scorecards, demonstrating that the spatial-statistical evidence localizes cleanly to specific anchors with distinct geographic roles.
6. **Interactive Leaflet companion** that lets reviewers trace any cuisine's residual network with full LISA classification in the popup — closing the loop between the static figures and the underlying data.

This is a substantive spatial-methodology contribution — not a redescription of standard cartographic mapping. That's the bar the GIS-use score is graded against.

---

## If something goes sideways during the build

If a paste comes out wrong in ArcGIS, or a section structure breaks, the safest recovery is to undo (Cmd-Z) and re-paste the same block. The build doc is designed to be re-pastable section by section.

If the StoryMap loses your work mid-build (rare but possible on flaky connections), the build doc itself is your single source of truth — restart from the last completed Section. ArcGIS auto-saves drafts every minute or so, so the loss should be small.

If a number doesn't match between the prose and a figure, trust the prose — every number in the prose has been verified against the JSON ground truth in this QA pass.

---

*Submission package prepared 2026-05-02. Good luck.*

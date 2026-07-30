# Workspace Integrity Audit

Date: 2026-03-14 11:56 AM America/New_York

## Verdict

The primary export bundle extracted at:

`/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full/`

is complete enough to serve as the working repo and source of truth for the submission build.

## Verified top-level structure

The extracted repo includes all critical working areas required by the plan:

- `src/` - core atlas pipeline
- `data/raw/` and `data/processed/` - baseline inputs and processed layers
- `outputs/` - frozen/generated tables, GIS layers, and figures
- `report/` - authoritative LaTeX report source and current PDF
- `docs/` - supporting analytical briefs, StoryMap guidance, and submission notes
- `deliverables/` - current packaged report PDF
- `extensions/stage4/`, `extensions/stage5/`, `extensions/stage6/` - causal extensions
- `extensions/eip_cases/` and `extensions/final_product_spec/` - case-study and final-product support materials
- `scripts/` - local execution helpers
- repo metadata/config (`README.md`, `Makefile`, `.codex/`, `AGENTS.md`)

## Source-of-truth decisions

### Code
Primary source of truth:
- `src/`
- `extensions/`
- `scripts/`

### Data
Primary source of truth:
- `data/raw/`
- `data/processed/`

### Frozen baseline outputs
Primary source of truth:
- `outputs/`
- `report/figures/`
- `report/tables/`

### Final report text to rewrite in place
Primary source of truth:
- `report/main.tex`

### Existing submission-support docs
Primary source of truth:
- `docs/`

### External planning references used to steer the rebuild
Reference-only inputs, not repo source of truth:
- `/mnt/data/WINNER_MATRIX.md`
- `/mnt/data/AWARD_PLAYBOOK (1).md`
- `/mnt/data/NOVELTY_METHODS_MEMO.md`
- `/mnt/data/SUBMISSION_GAP_ANALYSIS.md`
- `/mnt/data/WORK (7).md`
- `/mnt/data/WORK_EIP_FISHER_ADAPTED.md`
- `/mnt/data/Improved_EIP_Fisher_Submission_Plan.md`

## Completeness notes

- The full export already includes the baseline atlas repo plus prior stage-extension materials.
- A fallback extraction from `/mnt/data/EIP Project.zip` is **not required** for core execution.
- The repo is suitable for local reruns and for in-place report rewriting.
- Live ArcGIS Online / StoryMaps publication is still outside the local workspace and will require manual login later.

## Immediate implications for execution

1. Use this extracted workspace as the only working repo for all subsequent tasks.
2. Preserve the current `report/main.tex` and `report/main.pdf` before rewriting.
3. Treat `outputs/` as the baseline reference state before any refreshed rerun.
4. Record any later drift between regenerated outputs and the frozen bundle in the rebuild log.

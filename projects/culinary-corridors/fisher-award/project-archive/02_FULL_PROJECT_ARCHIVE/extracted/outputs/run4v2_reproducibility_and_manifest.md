# Run 4 v2 Reproducibility and Manifest

Created: 2026-04-30

## Commands and manual steps

- Created setup/audit/design/manifest documents from existing Run 2 v2, Run 3, and Run 4 artifacts.
- Created `scripts/18_run4v2_topographic_corridor_enhancement.py` and ran it from project root with `python scripts/18_run4v2_topographic_corridor_enhancement.py`.
- Generated `data/processed/run4v2_east_se_asia_accessibility_metrics.csv` and `figures/final_revised/run4v2_topographic_corridor_map.png`.
- Generated committee-ready Markdown reports, claim audit, and figure list.
- Generated LaTeX source in `report/final_committee/` and compiled with `pdflatex -interaction=nonstopmode culinary_corridors_committee_report.tex`.
- Rendered the PDF with `/home/oai/skills/pdfs/scripts/render_pdf.py` for visual QA.

## New outputs

- `outputs/run4v2_setup_note.md` — exists
- `outputs/run4v2_input_artifact_audit.csv` — exists
- `docs/run4v2_topographic_corridor_design_memo.md` — exists
- `data/run4v2_external_geodata_manifest.md` — exists
- `scripts/18_run4v2_topographic_corridor_enhancement.py` — exists
- `data/processed/run4v2_east_se_asia_accessibility_metrics.csv` — exists
- `outputs/run4v2_topographic_corridor_summary.md` — exists
- `figures/final_revised/run4v2_topographic_corridor_map.png` — exists
- `figures/final_revised/run4v2_figure_caption.md` — exists
- `figures/final_revised/run4v2_final_figure_decision_memo.md` — exists
- `submission/final_committee/final_committee_figure_list.md` — exists
- `submission/final_committee/final_committee_report.md` — exists
- `submission/final_committee/final_committee_report_short.md` — exists
- `submission/final_committee/final_committee_claim_audit.md` — exists
- `submission/final_committee/final_submission_readiness_checklist.md` — exists
- `report/final_committee/culinary_corridors_committee_report.tex` — exists
- `report/final_committee/culinary_corridors_committee_report.pdf` — exists
- `report/final_committee/culinary_corridors_committee_source_bundle.zip` — exists

## Reused inputs

- `data/processed/run2v2_focus_case_results.csv`
- `data/processed/run2v2_residual_culinary_corridors_filtered.csv`
- `data/processed/run2v2_cuisine_residual_bridge_scores.csv`
- `data/crosswalks/cuisine_geo_crosswalk.csv`
- `figures/final_revised/run4_*.png`
- `submission/revised/fisher_submission_report.md`
- `docs/run4_revised_spatial_thesis_and_scope.md`
- `outputs/run4_claim_and_compliance_audit.md`

## Package assumptions

- Python packages used: pandas, numpy, matplotlib.
- LaTeX build used local `pdflatex`.
- No external API keys or credentials were used.
- No new external geodata were downloaded; the Run 4 v2 map uses documented proxy variables.

## Caveats

- Corridor-accessibility metrics are transparent proxies, not measured terrain or route data.
- The recipe corpus remains a proxy and should not be represented as globally exhaustive.
- StoryMap hosting remains a manual step.

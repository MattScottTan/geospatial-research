# Run 3 Claim Audit Checklist

Created: 2026-04-29

## Audit scope

Audited files:

- `docs/run3_final_scope_and_claims.md`
- `submission/storymap_script.md`
- `submission/fisher_submission_report.md`
- `submission/data_sources_and_limitations.md`
- `submission/abstract_and_pitch.md`

## Claim status table

| Claim | Status | Evidence/source | Required language |
|---|---|---|---|
| Cuisine similarity is spatially structured in the prototype dataset. | Strong / safe | Run 2 v2 filtered model, residual maps, focused case outputs | “shows” acceptable for computed prototype results. |
| Geographic distance explains some but not all cuisine similarity. | Strong / safe | `outputs/run2v2_filtered_distance_baseline_summary.md`; reported negative log-distance coefficient and R² 0.3553 | “partly explains” or “explains some” only. |
| The global map identifies candidate culinary corridors. | Strong / safe | Filtered residual output and global map | Must say “candidate” and “discovery screen.” |
| East/Southeast Asia is the strongest focused case. | Strong / safe | Scope memo and focused case outputs | Safe as project-selection conclusion. |
| East/Southeast Asian links prove a diffusion route. | Forbidden | Not directly modeled | Do not use. Use “spatial association” only. |
| Iberian/Atlantic-Pacific links reflect colonial/maritime exchange. | Cautious only | Residual map is consistent with hypothesis, but mechanism not modeled | Use “consistent with” or “hypothesis,” not “caused by.” |
| Recipe corpus represents world cuisine. | Forbidden | Platform-mediated data; data-quality audit warns against this | Must state not representative. |
| Cuisine labels equal nation-states. | Forbidden | Crosswalk confidence notes | Must state coordinates are proxies. |
| Residual bridge scores are geospatial-only insight. | Strong / safe | Bridge scores require distance, coordinates, residuals, and pair aggregation | Safe if phrased as method contribution. |
| Flavor chemistry explains residuals. | Forbidden for current package | Not operationally matched in final analysis | Treat as future work or Pia-validation question. |
| Fermentation explains residuals. | Forbidden for current package | Not central, no geocoded microbiome analysis | Exclude or future work only. |

## Overclaim scan

- `storymap_script.md`: no causal proof language found after revision note; mechanism language framed as candidate, hypothesis, or association.
- `fisher_submission_report.md`: no representativeness claim found; limitation section explicitly rejects representative and causal interpretation.
- `abstract_and_pitch.md`: safe; uses “suggests,” “prototype,” and “spatially structured.”
- `data_sources_and_limitations.md`: safe; explicitly lists forbidden claims.

## Required edits completed

- Added post-audit revision note to `submission/storymap_script.md`.
- Added post-audit revision note to `submission/fisher_submission_report.md`.
- Ensured “global discovery” is consistently distinguished from focused inference.
- Ensured migration/trade/colonial/maritime language remains hypothetical.

## Final audit result

The final narrative is claim-safe for a Fisher-facing prototype submission, provided the user does not present residual corridors as causal historical proof and discloses recipe-platform limitations.

# Run 4 Geospatial Upgrade Selection

Created: 2026-04-29

| Candidate upgrade | Feasibility with current data | Fisher value | Risk | Decision |
|---|---|---|---|---|
| Residual bridge-score refinement | High | High | Low | **Implement** |
| Boundary/permeability synthesis | High | Medium-High | Low | Use as limitations/secondary figure |
| Path/connectivity proxy | Medium | Medium | Medium | Keep as appendix/future-work note |
| Spatial outlier/hotspot summary | Medium-Low | Medium | Medium | Defer because n=20 is small |
| Focused corridor map refinement | High | High | Low | Implement visually |

## Selected primary upgrade
**Residual bridge-score refinement.** This converts pairwise residual corridors into a ranked place-level spatial role metric. It is Fisher-aligned because the output depends on coordinates, distance residuals, long-distance links, and case geography; it cannot be computed from ingredient similarity alone.

## Fallback / supporting upgrade
**Boundary/permeability synthesis**, using existing boundary-class outputs to show how residual similarity behaves across same-subregion, cross-subregion, and diagnostic corridor classes.

## Implementation
Create and run `scripts/17_run4_geospatial_upgrade.py` to generate `data/processed/run4_geospatial_upgrade_results.csv`.

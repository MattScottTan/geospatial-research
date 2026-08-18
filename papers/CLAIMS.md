# CLAIMS — numeric provenance ledger

Every number appearing in either paper must have a row here, mapping it to the script and
output field that produces it. Per **D-007** this file is maintained *while* writing, not
reconstructed afterwards. **T-010** audits the papers against this file rather than
building it.

Re-run everything with:

```
python analysis/04_disconnection_prevalence.py
python analysis/05_selection_inflation.py
```

Both are seeded (`SEED = 42`) and deterministic. Deterministic quantities must match
exactly; Monte Carlo quantities within the stated standard error.

---

## Paper 1 — component structure and Gi\*

Source: `analysis/04_disconnection_prevalence.py`
Outputs: `analysis/outputs/disconnection_prevalence.json` (summary),
`analysis/outputs/disconnection_prevalence_full.csv` (all 1,764 rows),
`papers/paper1/data/prevalence_summary.csv`, `papers/paper1/data/prevalence_by_n_k.csv`

### The case study (published atlas, 319 cities, k = 8)

| Claim | Value | Output field |
|---|---|---|
| Components in the weights graph | 2 | `reference_319_k8.n_components` |
| Units outside the largest component | 67 | `reference_319_k8.n_outside_largest` |
| Largest component size | 252 | `319 − n_outside_largest` |
| Cold spots, global standardisation | 33 | `reference_319_k8.cold_global` |
| Cold spots, within-component | 25 | `reference_319_k8.cold_within` |
| Hot spots, both | 7 | `reference_319_k8.hot_global` / `hot_within` |
| Smaller component's mean offset | −0.264 | `reference_319_k8.max_abs_offset` |
| Between-component share of variance | 0.80% | `reference_319_k8.between_var_share` |

### Per-component detail — the artifact itself

All emitted by `reference_detail()`, under `reference_detail` in the JSON.

| Claim | Value | Output field |
|---|---|---|
| Large component: n, offset from global mean | 252, +0.070 | `components[0].n`, `.offset_from_global` |
| Large component: mean Gi\* z | +0.142 | `components[0].mean_gi_z_global` |
| Large component: cold spots, global → within | 19 → 22 | `components[0].cold_global` / `.cold_within` |
| Large component: hot spots | 7 → 6 | `components[0].hot_global` / `.hot_within` |
| **Small component: n, offset** | **67, −0.264** | `components[1].n`, `.offset_from_global` |
| **Small component: mean Gi\* z** | **−0.566** | `components[1].mean_gi_z_global` |
| **Small component: cold spots, global → within** | **14 → 3** | `components[1].cold_global` / `.cold_within` |
| Small component: hot spots | 0 → 1 | `components[1].hot_global` / `.hot_within` |

The −0.566 versus +0.142 contrast **is** the finding: every unit in the smaller component
is displaced by more than half a standard deviation before any real spatial pattern is
considered.

### The null result (required by D-009)

| Claim | Value | Output field |
|---|---|---|
| Moran's I | 0.0661 | `reference_detail.morans_I` |
| p, free permutation | 0.0085 | `reference_detail.moran_p_free_permutation` |
| p, within-component permutation | 0.0080 | `reference_detail.moran_p_within_component_permutation` |
| Null SD, free vs within | see fields | `moran_null_sd_free` / `moran_null_sd_within` |

Moran's I is essentially untouched by the disconnection. Paper 1 must report this with
the same prominence as the Gi\* finding.

### Prevalence

| Claim | Value | Output field |
|---|---|---|
| Configurations swept | 1,764 | `n_configurations` |
| Overall disconnection rate | 39.4% | `overall_disconnect_rate` |
| Top-by-population sampling | 46.4% | `by_scheme.top_by_population` |
| Random sampling | 39.0% | `by_scheme.random` |
| Rate at k = 3 | 99.3% | `by_k.3` |
| Rate at k = 6 | 72.8% | `by_k.6` |
| **Rate at k = 8 (conventional)** | **49.0%** | `by_k.8` |
| Rate at k = 12 | 17.0% | `by_k.12` |
| Rate at k = 20 | 6.8% | `by_k.20` |
| Rate at k = 40 | 0.0% | `by_k.40` |

Note the by-`k` rates above are pooled over all `n`. The paper's n × k table is
`papers/paper1/data/prevalence_by_n_k.csv`; cite cells from there, not from the pooled
figures, when discussing a specific sample size.

### Consequences when disconnection occurs

| Claim | Value | Output field |
|---|---|---|
| Median units outside largest component | 173 | `when_disconnected.median_units_outside_largest` |
| Median share outside largest component | 37.0% | `when_disconnected.median_share_outside_largest` |
| Median between-component variance share | 0.85% | `when_disconnected.median_between_var_share` |
| Cold-spot count changes under the fix | 85.9% | `when_disconnected.frac_cold_count_changes` |
| Median change when it changes | −1 | `when_disconnected.median_cold_delta_when_changed` |

The median change of −1 is small; the case study's −8 is at the tail. **Paper 1 must not
generalise from the case study's magnitude.** Report the distribution, not the example.

---

## Paper 2 — selective inference for weights selection

Source: `analysis/05_selection_inflation.py`
Outputs: `analysis/outputs/selection_inflation.json`,
`papers/paper2/data/inflation_surface.csv`

Design: 5 candidate grids × 3 sample sizes × 4 rules, B = 20,000 replicates of iid
Gaussian noise on real city locations. Per-`k` critical values are set at each `k`'s own
95th percentile, so **every individual `k` has exactly 5.0% Type I error by construction**
— all inflation comes from choosing among them.

| Claim | Value | Output field |
|---|---|---|
| Replicates per configuration | 20,000 | `replicates` |
| Max Monte Carlo standard error | 0.28 pp | `max_mc_se` |
| Reference: union rule | 14.1% | `reference.union` |
| Reference: arg-max rule | 11.3% | `reference.argmax` |
| Reference: mean inter-k correlation | 0.611 | `reference.mean_corr` |
| Union / first-significant range | 8.3% – 18.7% | `by_rule.union`, `by_rule.first_sig` |
| Arg-max range | 7.8% – 13.0% | `by_rule.argmax` |
| **Majority rule range (conservative)** | **1.9% – 4.6%** | `by_rule.majority` |

### Facts the paper must state

- **Union and first-significant are the same rule.** They coincide exactly, because
  scanning upward and stopping at the first significant `k` rejects if and only if some
  `k` is significant. The paper reports **three** distinct rules, not four.
- **The majority rule is conservative, not inflated.** It under-rejects at 1.9–4.6%
  against 5% nominal. This inverts the usual advice and is the most actionable result in
  the paper. Its power cost is not measured here — say so.
- **Inflation is not monotone in grid size.** The fine grid (7 values) gives 13.3% while
  the standard grid (6 values) gives 14.3%, because correlation differs (0.714 vs 0.604).
  Effective independent looks, not grid size, is the governing quantity. Per-cell values
  are in `inflation_surface.csv`.

---

### The published atlas against its own null (Paper 2 motivation)

Emitted by `observed_vs_critical()`, under `observed_vs_critical` in the JSON. Weights are
symmetrized binary kNN — the published specification.

| k | observed I | critical value | p | significant |
|---|---|---|---|---|
| 4 | 0.0536 | 0.0546 | 0.0529 | no |
| 6 | 0.0584 | 0.0449 | 0.0192 | **yes** |
| **8** | **0.0661** | 0.0387 | **0.0046** | **yes** |
| 12 | 0.0333 | 0.0317 | 0.0439 | **yes** |
| 20 | 0.0164 | 0.0242 | 0.1080 | no |
| 40 | 0.0041 | 0.0158 | 0.2124 | no |

Fields: `observed_I`, `critical_value`, `p_value`, `significant_at_05`, `argmax_k`.

Two facts the paper should use. **Significant at 3 of 6 candidate k values** — neither
fragile nor universal, and a far more informative summary than a single p-value. And
**arg-max is k = 8**, the published choice. State plainly that k = 8 is also the field's
most common default, so this is very likely coincidence; the point is that the sensitivity
makes the choice consequential whenever anyone does look.

**Correction to an earlier figure.** A previously circulated by-k series
({0.0545, 0.0574, 0.0685, 0.0373, 0.0195, 0.0053}) was a *mean across four weights
specifications* from `analysis/01_weights_sensitivity.py`, not the published specification.
The table above supersedes it. Reassuringly, I at k = 8 is 0.0661, matching the published
0.066 exactly, and arg-max is k = 8 under both.

---

## Open provenance gaps

**None.** All numbers either paper needs are emitted by committed scripts. T-008 and T-009
are both unblocked.

Paper 1 closed by `reference_detail()`; Paper 2 closed by `observed_vs_critical()`. The
prevalence sweep is unchanged at 1,764 configurations and 39.4% after both edits.

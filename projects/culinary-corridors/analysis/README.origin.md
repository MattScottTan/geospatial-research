# Bridges Across Cuisines — Geospatial Follow-On Analysis

This folder contains the post-submission analytical extensions that were
designed to address the three highest-leverage geospatial-specific
investigations identified in the project's review:

1. **Direct test of the colonial-administration hypothesis** (replaces the
   storymap's "is consistent with" framing with a tested partial Mantel
   correlation).
2. **Russian-anchor sensitivity** (addresses the obvious reviewer objection
   that the Russian LL classification depends on the Siberian-centroid
   anchor choice).
3. **Bridge-index small-sample stability** (bootstrap CIs on bridge scores
   and a permutation test on the top-3 ranking).

All scripts are reproducible end-to-end with `python3 <script_name>.py`.
Random seed = 42 throughout. Permutations / bootstraps use 9999 / 2000
iterations respectively.

## Scripts

### `colonial_mantel.py`
Partial Mantel of residual cuisine similarity ~ colonial-administration code,
controlling for log-distance and same-subregion. Inputs: `residual_matrix.npy`,
`distance_matrix.npy`, `cuisines.txt`, `colonial_crosswalk.csv`. Output:
`colonial_mantel_results.json`.

**Headline result:** r_partial = +0.181, two-sided p = 0.022 (9999 perm). The
colonial-administration hypothesis is supported with a modest but statistically
significant partial correlation, after controlling for both distance and same-
subregion adjacency.

### `colonial_mantel_sensitivity.py`
Sensitivity panel for the partial Mantel under alternative codings: strict
binary, sustained-only binary, Spanish-sphere-only. Output:
`colonial_mantel_sensitivity.json`.

**Result:** r in [+0.14, +0.18] across all four codings; three of four
significant at p < 0.05. Result is robust to coding-scheme choice.

### `russian_anchor_sensitivity.py`
Recomputes Russian's Local Moran's I and spatial-lag values under both the
Siberian-centroid (61.52 N, 105.32 E) and Moscow (55.75 N, 37.62 E) anchors,
holding the residual matrix fixed. Output: `russian_anchor_sensitivity.json`.

**Result:** Russian's LL classification (low residual + low-residual
neighborhood) is **sign-robust** across both anchors but **not significance-
robust**: p ≈ 0.08 under Siberian centroid (this implementation), p ≈ 0.24
under Moscow anchor. The anchor choice substantially affects the inverse-
distance weights' coverage of European partners.

(Note: the published Russian LISA p-value is 0.009, computed by PySAL using a
slightly different conditional-permutation scheme. Our independent
implementation gives a more conservative p; the qualitative finding — LL sign
present, weakening under Moscow anchor — is the substantive point.)

### `bridge_bootstrap.py`
Bootstrap 95% CIs on the bridge index. Resamples the 190 cuisine pairs with
replacement, 2000 iterations. Output: `bridge_bootstrap.json`.

**Result:** CIs are wide at n = 20 (~0.3 to 0.9 per cuisine for top-tier
positions). Filipino has the highest top-3 frequency (47% of bootstraps).
The Atlantic-rim cluster (Filipino, Southern_US, French, Cajun-Creole,
Brazilian, Jamaican, British) dominates the top-tier robustly. Russian's
position depends on bridge-index implementation choice (see note below).

**Important caveat:** This bootstrap uses an independent reimplementation of
the bridge index from the descriptive specification in BUILD_INSTRUCTIONS.md
(five components, equal-weighted, 0–1 normalized). The reimplemented index
qualitatively reproduces the published ranking (Filipino top, Atlantic-rim
clustered) but not the exact published values (Filipino 0.87, Russian 0.84,
etc.). A reviewer reading this should understand that the CI numbers apply
to *this* reimplemented index, not directly to the published bridge scores.
The substantive finding — that small-sample bridge-index rankings have
non-trivial uncertainty — applies regardless.

### `top3_permutation.py`
Permutation test: under random row/column permutation of the residual matrix,
how often does the published top-3 {Filipino, Russian, Southern U.S.}
co-occur as the top-3 of the recomputed bridge index? Output:
`top3_permutation.json`.

**Result:** p = 0.0001 (zero matches in 9999 permutations). The published
top-3 co-occurrence is essentially never produced by chance.

## Inputs (all from `/home/claude/handoff/working_data/`)

- `residual_matrix.npy` — 20×20 residual cuisine similarity matrix
- `distance_matrix.npy` — 20×20 great-circle km between cuisine anchors
- `cuisines.txt` — cuisine ordering for both matrices
- `mean_resid.npy` — per-cuisine mean residual (derived from R)
- `lisa_results.json` — published LISA results
- `mantel_results.json` — published Mantel results

## Outputs (all in this folder after running scripts)

- `colonial_crosswalk.csv` — three-tier ordinal coding of all 190 cuisine pairs
- `colonial_mantel_results.json`
- `colonial_mantel_sensitivity.json`
- `russian_anchor_sensitivity.json`
- `bridge_bootstrap.json`
- `top3_permutation.json`

## Reproducibility

```
cd /home/claude/work/analysis
python3 colonial_mantel.py
python3 colonial_mantel_sensitivity.py
python3 russian_anchor_sensitivity.py
python3 bridge_bootstrap.py
python3 top3_permutation.py
```

All scripts set `seed = 42` and run independently of one another. Run order
does not matter; outputs are deterministic given inputs.

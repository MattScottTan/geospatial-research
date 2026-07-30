"""
colonial_mantel_sensitivity.py — Sensitivity panel for the colonial-administration
partial Mantel test under alternative codings.

Codings tested:
  - Primary (already in colonial_mantel.py): three-tier ordinal 0/1/2.
  - (a) Strict binary: collapse 1+2 -> 1, 0 -> 0.
  - (b) Sustained-only binary: collapse 0+1 -> 0, 2 -> 1.
  - (c) Spanish-only: 1 if the pair is in the Spanish colonial sphere
        (involves Spain or one of its colonies), 0 otherwise.

For each coding, the headline H2 partial Mantel (controlling for log-distance
and same-subregion) is recomputed with 9999 permutations, seed=42.
"""
import json
import csv
import numpy as np

# ----- Inputs -----
R = np.load('residual_matrix.npy')
D = np.load('distance_matrix.npy')
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f if l.strip()]
n = len(cuisines)
idx = {c: i for i, c in enumerate(cuisines)}

SUBREGION = {
    'thai':'se_asia_mainland', 'vietnamese':'se_asia_mainland',
    'filipino':'se_asia_island',
    'chinese':'east_asia', 'korean':'east_asia', 'japanese':'east_asia',
    'indian':'south_asia',
    'british':'n_europe', 'irish':'n_europe',
    'french':'w_europe', 'spanish':'s_europe', 'italian':'s_europe', 'greek':'s_europe',
    'russian':'e_europe',
    'moroccan':'n_africa',
    'mexican':'central_america', 'cajun_creole':'n_america_south', 'southern_us':'n_america_south',
    'jamaican':'caribbean',
    'brazilian':'s_america',
}

# Cuisines in the Spanish colonial sphere (territories administered by Spain
# at any point during the modern era, plus Spain itself).
SPANISH_SPHERE = {'spanish', 'mexican', 'filipino', 'cajun_creole', 'jamaican',
                  'brazilian',  # peripheral via Iberian Union
                  }

# ----- Build base matrices -----
G = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i != j and SUBREGION[ci] == SUBREGION[cj]:
            G[i, j] = 1.0

logD = np.zeros((n, n))
iu = np.triu_indices(n, k=1)
for i, j in zip(*iu):
    logD[i, j] = np.log(D[i, j])
    logD[j, i] = logD[i, j]

# Read crosswalk (skip comment lines)
with open('colonial_crosswalk.csv') as f:
    lines = [l for l in f if not l.lstrip().startswith('#')]
rows = list(csv.DictReader(lines))

def build_C(map_fn):
    M = np.zeros((n, n))
    for r in rows:
        a, b = r['cuisine_a'], r['cuisine_b']
        new_code = map_fn(int(r['code']), a, b)
        i, j = idx[a], idx[b]
        M[i, j] = M[j, i] = new_code
    return M

C_primary = build_C(lambda c, a, b: c)
C_binary  = build_C(lambda c, a, b: 1 if c >= 1 else 0)
C_sustained_only = build_C(lambda c, a, b: 1 if c == 2 else 0)
C_spanish_only = build_C(lambda c, a, b: 1 if (a in SPANISH_SPHERE and b in SPANISH_SPHERE and c >= 1) else 0)

# ----- Partial Mantel infrastructure (same as colonial_mantel.py) -----
def upper(M): return M[iu]

def partial_corr_four(y, x, z1, z2):
    Z = np.column_stack([np.ones_like(z1), z1, z2])
    by, *_ = np.linalg.lstsq(Z, y, rcond=None)
    bx, *_ = np.linalg.lstsq(Z, x, rcond=None)
    ry = y - Z @ by
    rx = x - Z @ bx
    return np.corrcoef(ry, rx)[0, 1]

def partial_mantel_two_controls(M_y, M_x, M_z1, M_z2, n_perm=9999, seed=42):
    rng = np.random.default_rng(seed)
    iu_local = np.triu_indices(M_y.shape[0], k=1)
    y = M_y[iu_local]; x = M_x[iu_local]
    z1 = M_z1[iu_local]; z2 = M_z2[iu_local]
    obs_r = partial_corr_four(y, x, z1, z2)
    perm_rs = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(M_y.shape[0])
        x_perm = M_x[np.ix_(order, order)][iu_local]
        perm_rs[k] = partial_corr_four(y, x_perm, z1, z2)
    p_two = (np.sum(np.abs(perm_rs) >= np.abs(obs_r)) + 1) / (n_perm + 1)
    p_one_pos = (np.sum(perm_rs >= obs_r) + 1) / (n_perm + 1)
    return obs_r, p_two, p_one_pos

results = {}
for label, M in [
    ('primary_ordinal_0_1_2', C_primary),
    ('strict_binary_any_colonial', C_binary),
    ('sustained_only_binary', C_sustained_only),
    ('spanish_sphere_only', C_spanish_only),
]:
    n_nonzero = int(np.sum(M[iu] > 0))
    obs_r, p_two, p_one_pos = partial_mantel_two_controls(R, M, logD, G, n_perm=9999, seed=42)
    results[label] = {
        'r_partial': float(obs_r),
        'p_two_sided': float(p_two),
        'p_one_sided_positive': float(p_one_pos),
        'n_nonzero_pairs': n_nonzero,
    }
    print(f'{label:36s}  r = {obs_r:+.4f}  p_two = {p_two:.4f}  '
          f'(n_nonzero = {n_nonzero})')

out = {
    'description': 'Sensitivity panel for partial Mantel residual ~ colonial-administration | log-distance + same-subregion. 9999 permutations, seed=42.',
    'controls': ['log-distance', 'same-subregion'],
    'n_pairs_total': len(iu[0]),
    'codings': results,
    'interpretation': (
        'A consistent positive r across codings supports the colonial-administration '
        'hypothesis robustly. Effect-size differences across codings indicate which '
        'aspect of the colonial signal is loading the partial correlation.'
    ),
}
with open('colonial_mantel_sensitivity.json', 'w') as f:
    json.dump(out, f, indent=2)
print()
print('Saved colonial_mantel_sensitivity.json')

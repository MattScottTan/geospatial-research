"""
colonial_mantel.py — Partial Mantel test of residual cuisine similarity ~
shared colonial administration, controlling for log-distance and same-subregion.

Inputs (must be in working directory):
  - residual_matrix.npy         : 20x20, observed similarity minus distance-predicted
  - distance_matrix.npy         : 20x20, great-circle km between cuisine anchors
  - cuisines.txt                : 20 cuisine labels in matrix order
  - colonial_crosswalk.csv      : 190 pairs with codes 0/1/2 + rationale

Output:
  - colonial_mantel_results.json : main partial-Mantel result + 3-way correlation panel

Methodology:
  - Builds a 20x20 colonial-administration matrix C from the crosswalk codes.
  - Builds a 20x20 same-subregion matrix G (consistent with step2_mantel.py).
  - Builds log-distance matrix logD.
  - Tests three hypotheses:
      H1 (main): partial Mantel of residual ~ colonial, controlling for logD.
      H2 (extended): partial Mantel of residual ~ colonial, controlling for logD AND same-subregion.
      H3 (descriptive): bivariate Mantel of residual ~ colonial.
  - Permutation: 9999 shuffles of the colonial matrix's rows/columns; null distribution
    of the partial correlation; two-sided p.

Random seed: 42 throughout (matches existing pipeline conventions).
"""
import json
import csv
import itertools
import numpy as np

# ----- Inputs -----
R = np.load('residual_matrix.npy')           # 20x20, residual = obs sim - predicted
D = np.load('distance_matrix.npy')           # 20x20, km
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f if l.strip()]
n = len(cuisines)
idx = {c: i for i, c in enumerate(cuisines)}
assert n == 20, f'Expected 20 cuisines, got {n}'

# Subregion mapping (verbatim from step2_mantel.py)
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

# ----- Build matrices -----
# Same-subregion indicator: G[i,j] = 1 if same subregion, 0 if different.
# (step2_mantel.py used the inverted convention; we use the positive-association
# version here so the partial Mantel reads "controlling for shared subregion."
# Sign of the partial correlation is unaffected by this choice.)
G = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i != j and SUBREGION[ci] == SUBREGION[cj]:
            G[i, j] = 1.0

# Colonial-administration matrix: C[i,j] = 0/1/2 from the crosswalk.
C = np.zeros((n, n))
with open('colonial_crosswalk.csv') as f:
    lines = [l for l in f if not l.lstrip().startswith('#')]
reader = csv.DictReader(lines)
n_pairs_loaded = 0
for row in reader:
    a, b = row['cuisine_a'], row['cuisine_b']
    code = int(row['code'])
    i, j = idx[a], idx[b]
    C[i, j] = code
    C[j, i] = code
    n_pairs_loaded += 1
assert n_pairs_loaded == 190, f'Expected 190 pairs, got {n_pairs_loaded}'

# Log-distance matrix (use small epsilon for diagonal which is zero)
logD = np.zeros((n, n))
iu = np.triu_indices(n, k=1)
for i, j in zip(*iu):
    logD[i, j] = np.log(D[i, j])
    logD[j, i] = logD[i, j]

# ----- Mantel infrastructure (consistent with step2_mantel.py) -----
def upper(M):
    return M[iu]

def mantel_r(x, y):
    return np.corrcoef(x, y)[0, 1]

def partial_corr_three(y, x, z):
    """Partial correlation r_yx.z."""
    ryx = np.corrcoef(y, x)[0, 1]
    ryz = np.corrcoef(y, z)[0, 1]
    rxz = np.corrcoef(x, z)[0, 1]
    denom = np.sqrt((1 - ryz**2) * (1 - rxz**2))
    return (ryx - ryz * rxz) / denom

def partial_corr_four(y, x, z1, z2):
    """
    Partial correlation r_yx.{z1,z2}: residualize y and x against {z1, z2},
    then correlate the residuals.
    """
    Z = np.column_stack([np.ones_like(z1), z1, z2])
    # OLS residuals
    by, *_ = np.linalg.lstsq(Z, y, rcond=None)
    bx, *_ = np.linalg.lstsq(Z, x, rcond=None)
    ry = y - Z @ by
    rx = x - Z @ bx
    return np.corrcoef(ry, rx)[0, 1]

def partial_mantel_test(M_y, M_x, controls, n_perm=9999, seed=42):
    """
    Partial Mantel: correlate M_y with M_x controlling for one or more matrices.
    Permute M_x's rows/columns to obtain null.

    controls: list of full-square control matrices (one or two).
    Returns (obs_r, p_two_sided, p_one_sided_pos, perm_rs).
    """
    rng = np.random.default_rng(seed)
    n = M_y.shape[0]
    iu = np.triu_indices(n, k=1)
    y = M_y[iu]; x = M_x[iu]
    if len(controls) == 1:
        z = controls[0][iu]
        obs_r = partial_corr_three(y, x, z)
    elif len(controls) == 2:
        z1 = controls[0][iu]; z2 = controls[1][iu]
        obs_r = partial_corr_four(y, x, z1, z2)
    else:
        raise ValueError("controls must be 1 or 2 matrices")
    perm_rs = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(n)
        M_x_perm = M_x[np.ix_(order, order)]
        x_perm = M_x_perm[iu]
        if len(controls) == 1:
            perm_rs[k] = partial_corr_three(y, x_perm, z)
        else:
            perm_rs[k] = partial_corr_four(y, x_perm, z1, z2)
    p_two = (np.sum(np.abs(perm_rs) >= np.abs(obs_r)) + 1) / (n_perm + 1)
    p_one_pos = (np.sum(perm_rs >= obs_r) + 1) / (n_perm + 1)
    return obs_r, p_two, p_one_pos, perm_rs

# ----- Run tests -----
y_vec = upper(R)         # residual cuisine similarity
c_vec = upper(C)         # colonial-administration code
g_vec = upper(G)         # same-subregion indicator
ld_vec = upper(logD)     # log-distance

# Bivariate Mantel: residual vs colonial
r_bi = mantel_r(y_vec, c_vec)
print(f'Bivariate Mantel residual ~ colonial: r = {r_bi:+.4f}')

# H1: partial Mantel residual ~ colonial | log-distance
print('Running H1 (partial Mantel, control: log-distance)...')
r1, p1_two, p1_one, perm1 = partial_mantel_test(R, C, [logD], n_perm=9999, seed=42)
print(f'  r_partial = {r1:+.4f}, p_two = {p1_two:.4f}, p_one_pos = {p1_one:.4f}')

# H2: partial Mantel residual ~ colonial | log-distance, same-subregion
print('Running H2 (partial Mantel, controls: log-distance, same-subregion)...')
r2, p2_two, p2_one, perm2 = partial_mantel_test(R, C, [logD, G], n_perm=9999, seed=42)
print(f'  r_partial = {r2:+.4f}, p_two = {p2_two:.4f}, p_one_pos = {p2_one:.4f}')

# Descriptive: simple correlations
def safe_corr(a, b):
    return float(np.corrcoef(a, b)[0, 1])

panel = {
    'r_residual_colonial': safe_corr(y_vec, c_vec),
    'r_residual_logD': safe_corr(y_vec, ld_vec),
    'r_residual_subregion': safe_corr(y_vec, g_vec),
    'r_colonial_logD': safe_corr(c_vec, ld_vec),
    'r_colonial_subregion': safe_corr(c_vec, g_vec),
    'r_logD_subregion': safe_corr(ld_vec, g_vec),
}

# ----- Save -----
out = {
    'description': 'Partial Mantel test of residual cuisine similarity ~ colonial-administration code',
    'inputs': {
        'residual_matrix': 'residual_matrix.npy',
        'distance_matrix': 'distance_matrix.npy',
        'cuisines': 'cuisines.txt',
        'colonial_crosswalk': 'colonial_crosswalk.csv',
    },
    'coding_scheme': {
        '0': 'no shared colonial administration',
        '1': 'brief/peripheral colonial connection (<50 yr or sphere-only)',
        '2': 'sustained core colonial administration (>50 yr direct rule or co-administration)',
    },
    'n_cuisines': n,
    'n_pairs': len(y_vec),
    'n_permutations': 9999,
    'seed': 42,
    'code_distribution': {
        '0': int(np.sum(c_vec == 0)),
        '1': int(np.sum(c_vec == 1)),
        '2': int(np.sum(c_vec == 2)),
    },
    'bivariate_mantel': {
        'description': 'Mantel correlation of residual ~ colonial (no controls)',
        'r': float(r_bi),
    },
    'partial_mantel_H1': {
        'description': 'Partial Mantel residual ~ colonial | log-distance',
        'r_partial': float(r1),
        'p_two_sided': float(p1_two),
        'p_one_sided_positive': float(p1_one),
        'controls': ['log-distance'],
    },
    'partial_mantel_H2_main': {
        'description': 'Partial Mantel residual ~ colonial | log-distance, same-subregion (HEADLINE RESULT)',
        'r_partial': float(r2),
        'p_two_sided': float(p2_two),
        'p_one_sided_positive': float(p2_one),
        'controls': ['log-distance', 'same-subregion'],
    },
    'correlation_panel': panel,
}
with open('colonial_mantel_results.json', 'w') as f:
    json.dump(out, f, indent=2)
print()
print('Saved colonial_mantel_results.json')
print()
print('==== HEADLINE ====')
print(f'Partial Mantel r (controlling for log-distance and same-subregion) = {r2:+.4f}')
print(f'Two-sided p (9999 perm) = {p2_two:.4f}')

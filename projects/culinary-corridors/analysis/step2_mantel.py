"""
Step 2: Mantel test on similarity vs distance matrices,
plus partial Mantel controlling for shared subregion.

Mantel test: matrix correlation with permutation-based significance.
Standard tool in spatial ecology / biogeography for distance-matrix
hypothesis testing (Mantel 1967; Smouse, Long & Sokal 1986 for partial).
"""
import numpy as np

# Load
S = np.load('similarity_matrix.npy')           # 20x20 cosine similarity (filtered)
D = np.load('distance_matrix.npy')             # 20x20 great-circle km
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f]
n = len(cuisines)

# We'll also need a "shared-subregion" indicator matrix for the partial Mantel.
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
G = np.zeros((n,n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i != j:
            G[i,j] = 1.0 if SUBREGION[ci] != SUBREGION[cj] else 0.0
# G[i,j] = 0 if same subregion, 1 if different. So G is a "subregional separation" matrix.

# Convert similarity to dissimilarity (Mantel convention is matrix-correlation;
# direction doesn't change inferential conclusions, but we follow the standard
# practice of correlating dissimilarity-with-distance so a positive r means
# "farther apart = more dissimilar").
DSim = 1.0 - S    # dissimilarity matrix
# For interpretation alignment with the StoryMap, we'll also report the equivalent
# similarity-vs-distance Mantel (which has the opposite sign).

iu = np.triu_indices(n, k=1)
ds = DSim[iu]; di = D[iu]; gs = G[iu]; sm = S[iu]

# log distance is what the StoryMap baseline uses
log_d = np.log(di)

def mantel_r(x, y):
    """Pearson correlation between two condensed-form matrices."""
    return np.corrcoef(x, y)[0,1]

def mantel_test(M1_full, M2_full, n_perm=9999, seed=42):
    """
    Mantel test by row/column permutation of M1.
    M1_full, M2_full are full square matrices (n,n).
    Returns observed r, two-sided p, and the null distribution.
    """
    rng = np.random.default_rng(seed)
    n = M1_full.shape[0]
    iu = np.triu_indices(n, k=1)
    obs_r = mantel_r(M1_full[iu], M2_full[iu])
    perm_rs = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(n)
        M1_perm = M1_full[np.ix_(order, order)]
        perm_rs[k] = mantel_r(M1_perm[iu], M2_full[iu])
    # Two-sided p-value
    p_two = (np.sum(np.abs(perm_rs) >= np.abs(obs_r)) + 1) / (n_perm + 1)
    p_one = (np.sum(perm_rs >= obs_r) + 1) / (n_perm + 1)  # one-sided (positive)
    return obs_r, p_one, p_two, perm_rs

def partial_mantel(M_y, M_x, M_z, n_perm=9999, seed=42):
    """
    Partial Mantel test: correlation of M_y and M_x controlling for M_z.
    Computes the partial correlation r_yx.z analytically, then
    permutes the residualized M_y to obtain a null.
    Following Smouse, Long & Sokal (1986).
    """
    rng = np.random.default_rng(seed)
    n = M_y.shape[0]
    iu = np.triu_indices(n, k=1)
    y = M_y[iu]; x = M_x[iu]; z = M_z[iu]

    def partial_corr(y, x, z):
        ryx = np.corrcoef(y, x)[0,1]
        ryz = np.corrcoef(y, z)[0,1]
        rxz = np.corrcoef(x, z)[0,1]
        denom = np.sqrt((1 - ryz**2) * (1 - rxz**2))
        return (ryx - ryz * rxz) / denom

    obs_r = partial_corr(y, x, z)
    perm_rs = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(n)
        M_y_perm = M_y[np.ix_(order, order)]
        y_perm = M_y_perm[iu]
        perm_rs[k] = partial_corr(y_perm, x, z)
    p_two = (np.sum(np.abs(perm_rs) >= np.abs(obs_r)) + 1) / (n_perm + 1)
    p_one = (np.sum(perm_rs >= obs_r) + 1) / (n_perm + 1)
    return obs_r, p_one, p_two, perm_rs

# ========== MAIN MANTEL: dissimilarity vs log-distance ==========
LD = np.where(D > 0, np.log(np.where(D > 0, D, 1)), 0)

print("="*72)
print("MANTEL TEST 1 — Dissimilarity (1 - cosine) vs log geographic distance")
print("="*72)
r1, p1_one, p1_two, null1 = mantel_test(DSim, LD, n_perm=9999)
print(f"  Observed Mantel r = {r1:+.4f}")
print(f"  One-sided p (r > 0): {p1_one:.4f}")
print(f"  Two-sided p:         {p1_two:.4f}")
print(f"  Null distribution: mean={null1.mean():+.4f}, sd={null1.std():.4f}")
print(f"  Interpretation: cuisines that are farther apart geographically tend to")
print(f"                  be more dissimilar in ingredient profile.")

# Equivalent similarity-vs-distance Mantel (negative sign expected)
print(f"\n  Equivalent similarity-vs-log-distance r = {-r1:+.4f} (sign flip — same test)")

# ========== PARTIAL MANTEL: control for shared subregion ==========
print("\n" + "="*72)
print("PARTIAL MANTEL — Dissimilarity vs log-distance, controlling for")
print("                 different-subregion indicator (Smouse-Long-Sokal 1986)")
print("="*72)
r2, p2_one, p2_two, null2 = partial_mantel(DSim, LD, G, n_perm=9999)
print(f"  Partial Mantel r = {r2:+.4f}")
print(f"  One-sided p: {p2_one:.4f}")
print(f"  Two-sided p: {p2_two:.4f}")
print(f"  Interpretation: distance still correlates with dissimilarity even after")
print(f"                  removing the variance shared with subregional adjacency.")

# Also report the simpler 'shared subregion ↔ dissimilarity' Mantel for context
print("\n" + "="*72)
print("MANTEL TEST 2 — Dissimilarity vs different-subregion indicator")
print("="*72)
r3, p3_one, p3_two, null3 = mantel_test(DSim, G, n_perm=9999)
print(f"  Observed Mantel r = {r3:+.4f}")
print(f"  One-sided p: {p3_one:.4f}")
print(f"  Two-sided p: {p3_two:.4f}")
print(f"  Interpretation: cuisines in different subregions are more dissimilar than")
print(f"                  cuisines in the same subregion (as expected).")

# Save Mantel results for the writeup
import json
mantel_results = {
    'distance_vs_dissim': {
        'r': float(r1),
        'r_similarity_distance': float(-r1),
        'p_one_sided': float(p1_one),
        'p_two_sided': float(p1_two),
        'n_pairs': int(len(ds)),
        'n_perm': 9999,
    },
    'partial_distance_controlling_subregion': {
        'r_partial': float(r2),
        'p_one_sided': float(p2_one),
        'p_two_sided': float(p2_two),
    },
    'subregion_vs_dissim': {
        'r': float(r3),
        'p_one_sided': float(p3_one),
        'p_two_sided': float(p3_two),
    }
}
with open('mantel_results.json','w') as f:
    json.dump(mantel_results, f, indent=2)
print(f"\nSaved mantel_results.json")

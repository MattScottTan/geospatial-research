"""
Step 3: Local Moran's I on per-cuisine mean residual scores.

For each cuisine, the per-cuisine residual score is the mean of its
residuals across all 19 pairs it participates in. This converts the
pairwise residual matrix to a 20-length vector — the natural input
for a local spatial autocorrelation test on cuisine anchors.

Spatial weights: inverse great-circle distance, row-standardized,
no self-weight. Anselin (1995); pysal/esda implementation.
"""
import numpy as np
import pandas as pd
import json
from libpysal.weights import W
from esda.moran import Moran, Moran_Local

# Load
S = np.load('similarity_matrix.npy')
D = np.load('distance_matrix.npy')
R = np.load('residual_matrix.npy')
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f]
n = len(cuisines)

# ========== Per-cuisine mean residual ==========
np.fill_diagonal(R, 0.0)  # safety: residual is zero on the diagonal anyway
mean_resid = R.sum(axis=1) / (n - 1)

print("Per-cuisine mean residual (descending):")
for c, r in sorted(zip(cuisines, mean_resid), key=lambda x: -x[1]):
    print(f"  {c:<14} {r:+.4f}")

# ========== Spatial weights: inverse-distance, row-standardized ==========
# Weight w_ij = 1/d_ij for i != j, then row-standardized so sum_j w_ij = 1.
W_raw = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            W_raw[i, j] = 1.0 / D[i, j]

# Row-standardize
row_sums = W_raw.sum(axis=1)
W_norm = W_raw / row_sums[:, None]

# Build pysal W object
neighbors = {i: [j for j in range(n) if j != i] for i in range(n)}
weights = {i: W_norm[i, [j for j in range(n) if j != i]].tolist() for i in range(n)}
w = W(neighbors, weights)
w.transform = 'r'  # already row-standardized but ensures pysal knows

# ========== Global Moran's I (sanity check) ==========
moran_global = Moran(mean_resid, w, permutations=9999)
print(f"\nGlobal Moran's I on mean residual (with inverse-distance weights):")
print(f"  I = {moran_global.I:+.4f}")
print(f"  E[I] = {moran_global.EI:+.4f}")
print(f"  Pseudo p-value (9999 perm) = {moran_global.p_sim:.4f}")
print(f"  z-score = {moran_global.z_sim:+.4f}")

# ========== Local Moran's I (LISA) ==========
lisa = Moran_Local(mean_resid, w, permutations=9999, seed=42)

# Quadrant classification:
# 1 = HH (high in high), 2 = LH (low in high),
# 3 = LL (low in low), 4 = HL (high in low)
QUADRANT_NAME = {1: 'HH', 2: 'LH', 3: 'LL', 4: 'HL'}

# Use significance threshold p < 0.05; non-significant → 'NS'
SIG = 0.05

results = []
for i, c in enumerate(cuisines):
    p = lisa.p_sim[i]
    q = QUADRANT_NAME[lisa.q[i]]
    label = q if p < SIG else 'NS'
    results.append({
        'cuisine': c,
        'mean_resid': float(mean_resid[i]),
        'local_I': float(lisa.Is[i]),
        'p_sim': float(p),
        'quadrant_raw': q,
        'classification': label,
    })

# Print sorted by local I
print(f"\n{'Cuisine':<14} {'mean_resid':>11} {'Local I':>9} {'p_sim':>7} {'quadrant':>9} {'classification':>15}")
print("-" * 75)
for r in sorted(results, key=lambda x: -x['local_I']):
    print(f"  {r['cuisine']:<14} {r['mean_resid']:>+11.4f} {r['local_I']:>+9.4f} "
          f"{r['p_sim']:>7.4f} {r['quadrant_raw']:>9} {r['classification']:>15}")

# Tabulate classification counts
print(f"\nClassification summary:")
from collections import Counter
counts = Counter(r['classification'] for r in results)
for k in ['HH','HL','LL','LH','NS']:
    if k in counts:
        members = [r['cuisine'] for r in results if r['classification']==k]
        print(f"  {k}: {counts[k]:>2}  ({', '.join(members)})")

# Save results
with open('lisa_results.json','w') as f:
    json.dump({
        'global_moran_I': float(moran_global.I),
        'global_moran_p': float(moran_global.p_sim),
        'global_moran_z': float(moran_global.z_sim),
        'per_cuisine': results,
    }, f, indent=2)

# Save mean_resid for plotting
np.save('mean_resid.npy', mean_resid)
print(f"\nSaved lisa_results.json and mean_resid.npy")

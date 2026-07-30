"""
Step 3b: LISA robustness — re-run with k-nearest-neighbor weights (k=4, k=6)
and Gaussian-kernel inverse distance, in addition to plain inverse-distance.
The classification (HH/LL/HL/LH/NS) should be qualitatively stable across
defensible weights choices.
"""
import numpy as np
from libpysal.weights import W
from esda.moran import Moran, Moran_Local

D = np.load('distance_matrix.npy')
mean_resid = np.load('mean_resid.npy')
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f]
n = len(cuisines)

QUAD = {1:'HH', 2:'LH', 3:'LL', 4:'HL'}

def make_w_inverse_distance(D, n):
    Wm = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Wm[i,j] = 1.0 / D[i,j]
    Wm = Wm / Wm.sum(axis=1, keepdims=True)
    neigh = {i: [j for j in range(n) if j != i] for i in range(n)}
    wts   = {i: Wm[i,[j for j in range(n) if j != i]].tolist() for i in range(n)}
    w = W(neigh, wts); w.transform='r'; return w

def make_w_knn(D, n, k):
    Wm = np.zeros((n,n))
    for i in range(n):
        order = np.argsort(D[i])
        # skip i itself (D[i,i]=0)
        nbrs = [j for j in order if j != i][:k]
        for j in nbrs:
            Wm[i,j] = 1.0 / k
    neigh = {i: [j for j in range(n) if Wm[i,j] > 0] for i in range(n)}
    wts   = {i: [Wm[i,j] for j in range(n) if Wm[i,j] > 0] for i in range(n)}
    w = W(neigh, wts); w.transform='r'; return w

def make_w_gaussian(D, n, sigma_km=3000):
    Wm = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Wm[i,j] = np.exp(-(D[i,j]**2) / (2 * sigma_km**2))
    Wm = Wm / Wm.sum(axis=1, keepdims=True)
    neigh = {i: [j for j in range(n) if j != i] for i in range(n)}
    wts   = {i: Wm[i,[j for j in range(n) if j != i]].tolist() for i in range(n)}
    w = W(neigh, wts); w.transform='r'; return w

schemes = {
    'inv_distance':       make_w_inverse_distance(D, n),
    'knn_k4':             make_w_knn(D, n, 4),
    'knn_k6':             make_w_knn(D, n, 6),
    'gaussian_3000km':    make_w_gaussian(D, n, 3000),
}

results = {}
for name, w in schemes.items():
    moran_g = Moran(mean_resid, w, permutations=9999)
    lisa = Moran_Local(mean_resid, w, permutations=9999, seed=42)
    results[name] = {
        'global_I': moran_g.I,
        'global_p': moran_g.p_sim,
        'classifications': [QUAD[lisa.q[i]] if lisa.p_sim[i] < 0.05 else 'NS'
                            for i in range(n)],
        'p_sims': lisa.p_sim.tolist(),
        'local_Is': lisa.Is.tolist(),
    }

# Print global Moran results
print(f"{'Weights scheme':<22} {'Global I':>10} {'p':>7}")
print("-"*45)
for name, r in results.items():
    print(f"{name:<22} {r['global_I']:>+10.4f} {r['global_p']:>7.4f}")

# Print classification table
print(f"\n{'Cuisine':<14}", end='')
for name in schemes:
    print(f"  {name:>14}", end='')
print()
print("-" * (14 + 16*len(schemes)))
for i, c in enumerate(cuisines):
    print(f"{c:<14}", end='')
    for name in schemes:
        cls = results[name]['classifications'][i]
        p = results[name]['p_sims'][i]
        loc_I = results[name]['local_Is'][i]
        flag = '*' if cls != 'NS' else ' '
        # Show raw quadrant + significance flag
        print(f"  {cls:>4}{flag} ({p:.2f}) ", end='')
    print()

# Save robustness table
import json
with open('lisa_robustness.json','w') as f:
    json.dump(results, f, indent=2, default=lambda x: float(x) if hasattr(x,'item') else x)
print("\nSaved lisa_robustness.json")

# Also report sign-of-Local-I robustness — even when p is not <0.05, the
# direction is often consistent across schemes
print(f"\nSign of Local I across schemes (positive = clustered with similar; negative = dissimilar):")
print(f"{'Cuisine':<14}", end='')
for name in schemes: print(f"  {name:>14}", end='')
print()
for i, c in enumerate(cuisines):
    print(f"{c:<14}", end='')
    for name in schemes:
        loc_I = results[name]['local_Is'][i]
        sign = '+' if loc_I > 0 else '-'
        print(f"  {sign:>14}", end='')
    print()

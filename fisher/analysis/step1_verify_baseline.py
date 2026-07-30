"""
Step 1: Reproduce Matthew's published distance-similarity baseline.
Target numbers from figdata.py / Finding 1:
  intercept = 1.273
  slope     = -0.116
  R^2       = 0.355
"""
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LinearRegression
from geopy.distance import great_circle

# Load matrix
df = pd.read_csv('cuisine_ingredient_matrix.csv', index_col=0)
print(f"Matrix: {df.shape[0]} cuisines x {df.shape[1]} ingredients")

# Anchors. Use figdata.py for confirmed cuisines; resolve Anchor_A=Indian, Anchor_B=Moroccan.
# Note: figdata.py Anchor_B is at (31.79, 35.21) which is the Levant, not Morocco.
# Morocco's centroid is (31.79, -7.09). Try both to see which the published baseline used.
ANCHORS = {
    'brazilian':   (-14.24, -51.93),
    'british':     ( 55.38,  -3.44),
    'cajun_creole':( 30.50, -91.20),
    'chinese':     ( 35.86, 104.20),
    'filipino':    ( 12.88, 121.77),
    'french':      ( 46.23,   2.21),
    'greek':       ( 39.07,  21.82),
    'indian':      ( 20.59,  78.96),
    'irish':       ( 53.41,  -8.24),
    'italian':     ( 41.87,  12.57),
    'jamaican':    ( 18.11, -77.30),
    'japanese':    ( 36.20, 138.25),
    'korean':      ( 35.91, 127.77),
    'mexican':     ( 23.63,-102.55),
    'moroccan':    ( 31.79,  -7.09),   # using actual Morocco centroid
    'russian':     ( 61.52, 105.32),
    'southern_us': ( 33.00, -86.00),
    'spanish':     ( 40.46,  -3.75),
    'thai':        ( 15.87, 100.99),
    'vietnamese':  ( 14.06, 108.28),
}

cuisines = df.index.tolist()
n = len(cuisines)
print(f"All cuisines have anchors: {all(c in ANCHORS for c in cuisines)}")

# Pairwise cosine similarity on the raw frequency matrix
# (cosine similarity is scale-invariant per-row, so unnormalized rows are fine)
S = cosine_similarity(df.values)
print(f"Similarity matrix shape: {S.shape}")
print(f"Similarity diagonal (should be 1.0): {S.diagonal()[:3]}")

# Pairwise great-circle distance in km
D = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i < j:
            d = great_circle(ANCHORS[ci], ANCHORS[cj]).kilometers
            D[i, j] = d
            D[j, i] = d

# Extract upper triangle (190 unique pairs for n=20)
iu = np.triu_indices(n, k=1)
sim_pairs = S[iu]
dist_pairs = D[iu]

print(f"\nNumber of pairs: {len(sim_pairs)}")
print(f"Similarity range: {sim_pairs.min():.3f} to {sim_pairs.max():.3f}")
print(f"Distance range: {dist_pairs.min():.0f} to {dist_pairs.max():.0f} km")

# Fit similarity ~ log10(distance) — try both natural log and log10
log_d = np.log(dist_pairs)
log10_d = np.log10(dist_pairs)

reg_ln = LinearRegression().fit(log_d.reshape(-1, 1), sim_pairs)
reg_log10 = LinearRegression().fit(log10_d.reshape(-1, 1), sim_pairs)

print(f"\n--- Natural log fit (ln) ---")
print(f"  intercept = {reg_ln.intercept_:.3f}")
print(f"  slope     = {reg_ln.coef_[0]:.4f}")
print(f"  R^2       = {reg_ln.score(log_d.reshape(-1,1), sim_pairs):.3f}")

print(f"\n--- log10 fit ---")
print(f"  intercept = {reg_log10.intercept_:.3f}")
print(f"  slope     = {reg_log10.coef_[0]:.4f}")
print(f"  R^2       = {reg_log10.score(log10_d.reshape(-1,1), sim_pairs):.3f}")

print(f"\nPublished target: intercept=1.273, slope=-0.116, R^2=0.355")

"""
Step 1b: Find the generic-ingredient filtering threshold that reproduces
Matthew's published baseline (R²=0.355, slope=-0.116, intercept=1.273).
"""
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LinearRegression
from geopy.distance import great_circle

df = pd.read_csv('cuisine_ingredient_matrix.csv', index_col=0)
cuisines = df.index.tolist()
n = len(cuisines)

ANCHORS = {
    'brazilian':(-14.24,-51.93), 'british':(55.38,-3.44), 'cajun_creole':(30.50,-91.20),
    'chinese':(35.86,104.20), 'filipino':(12.88,121.77), 'french':(46.23,2.21),
    'greek':(39.07,21.82), 'indian':(20.59,78.96), 'irish':(53.41,-8.24),
    'italian':(41.87,12.57), 'jamaican':(18.11,-77.30), 'japanese':(36.20,138.25),
    'korean':(35.91,127.77), 'mexican':(23.63,-102.55), 'moroccan':(31.79,-7.09),
    'russian':(61.52,105.32), 'southern_us':(33.00,-86.00), 'spanish':(40.46,-3.75),
    'thai':(15.87,100.99), 'vietnamese':(14.06,108.28),
}

# Distance matrix (precomputed — doesn't depend on filtering)
D = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i < j:
            d = great_circle(ANCHORS[ci], ANCHORS[cj]).kilometers
            D[i, j] = d; D[j, i] = d
iu = np.triu_indices(n, k=1)
log_d = np.log(D[iu])

# Compute "presence breadth" of each ingredient (how many cuisines use it)
presence = (df.values > 0).sum(axis=0)
print(f"Ingredient presence distribution:")
print(f"  In all 20 cuisines: {(presence == 20).sum()}")
print(f"  In 15-20:           {((presence >= 15) & (presence <= 20)).sum()}")
print(f"  In 10-14:           {((presence >= 10) & (presence <= 14)).sum()}")
print(f"  In 5-9:             {((presence >= 5) & (presence <= 9)).sum()}")
print(f"  In 1-4:             {((presence >= 1) & (presence <= 4)).sum()}")

# Show the most-universal ingredients (these are the "generic" ones)
top_universal = pd.Series(presence, index=df.columns).sort_values(ascending=False).head(30)
print(f"\nMost universal ingredients (count of cuisines using them):")
for ing, cnt in top_universal.items():
    print(f"  {cnt:>2}  {ing}")

# Sweep: filter ingredients that appear in >= K cuisines, refit, report R²
print(f"\n{'Filter (drop if in >= K cuisines)':<35} {'n_kept':>7} {'R²':>8} {'slope(ln)':>12} {'intercept':>11}")
print("-" * 78)
for k in [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8]:
    keep = presence < k
    M = df.values[:, keep]
    if M.shape[1] < 10:
        continue
    S = cosine_similarity(M)
    sim = S[iu]
    reg = LinearRegression().fit(log_d.reshape(-1,1), sim)
    r2 = reg.score(log_d.reshape(-1,1), sim)
    print(f"  drop >= {k:>2} cuisines (keep <{k}){'':<8} {keep.sum():>7} {r2:>8.3f} {reg.coef_[0]:>12.4f} {reg.intercept_:>11.3f}")

print(f"\nTarget: R²=0.355, slope=-0.116, intercept=1.273")

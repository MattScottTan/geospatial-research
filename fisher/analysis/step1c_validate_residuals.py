"""
Step 1c: Cross-validate that my residual matrix reproduces the published
spatial-grouping means from Finding 2:
  Iberian/Atlantic interregional: +0.139 (n=11)
  Same subregion:                 +0.115 (n=11)
  Same region cross-subregion:    -0.011 (n=32)
  E/SE Asia cross-subregion:      -0.014 (n=9)
  Other cross-region:             -0.020 (n=127)
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

# Apply generic-ingredient filter (drop those in >= 19 cuisines)
presence = (df.values > 0).sum(axis=0)
keep = presence < 19
M = df.values[:, keep]
print(f"Filtered matrix: {M.shape[1]} ingredients (from {df.shape[1]})")

# Similarity and distance matrices
S = cosine_similarity(M)
D = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i < j:
            d = great_circle(ANCHORS[ci], ANCHORS[cj]).kilometers
            D[i,j] = d; D[j,i] = d

iu = np.triu_indices(n, k=1)
sim = S[iu]; dist = D[iu]; log_d = np.log(dist)

# Fit baseline
reg = LinearRegression().fit(log_d.reshape(-1,1), sim)
r2 = reg.score(log_d.reshape(-1,1), sim)
print(f"Baseline: intercept={reg.intercept_:.3f}, slope={reg.coef_[0]:.4f}, R²={r2:.3f}")

# Compute residuals
predicted = reg.predict(log_d.reshape(-1,1))
resid = sim - predicted

# Make a residual matrix for later use
R = np.zeros_like(S)
for k, (i,j) in enumerate(zip(*iu)):
    R[i,j] = resid[k]; R[j,i] = resid[k]

# Classify each pair into Matthew's five spatial groupings
# Iberian/Atlantic interregional: pairs among {spanish, filipino, mexican, cajun_creole, brazilian, jamaican, southern_us}
IBERIAN_ATLANTIC = {'spanish','filipino','mexican','cajun_creole','brazilian','jamaican','southern_us'}

# Subregion classification (M49-style)
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
REGION = {
    'thai':'asia','vietnamese':'asia','filipino':'asia','chinese':'asia','korean':'asia',
    'japanese':'asia','indian':'asia',
    'british':'europe','irish':'europe','french':'europe','spanish':'europe',
    'italian':'europe','greek':'europe','russian':'europe',
    'moroccan':'africa',
    'mexican':'americas','cajun_creole':'americas','southern_us':'americas',
    'jamaican':'americas','brazilian':'americas',
}

def classify_pair(a, b):
    if {a, b}.issubset(IBERIAN_ATLANTIC):
        return 'iberian_atlantic_interregional'
    if SUBREGION[a] == SUBREGION[b]:
        return 'same_subregion'
    # E/SE Asia cross-subregion: pairs where both are in SE/East/South Asia but different subregions
    asian_subs = {'se_asia_mainland','se_asia_island','east_asia','south_asia'}
    if SUBREGION[a] in asian_subs and SUBREGION[b] in asian_subs:
        return 'ese_asia_cross_subregion'
    if REGION[a] == REGION[b]:
        return 'same_region_cross_subregion'
    return 'other_cross_region'

# Compute mean residual per grouping
groupings = {}
for k, (i,j) in enumerate(zip(*iu)):
    g = classify_pair(cuisines[i], cuisines[j])
    groupings.setdefault(g, []).append(resid[k])

print(f"\n{'Grouping':<35} {'n':>5} {'mean residual':>15}")
print("-" * 60)
target = {
    'iberian_atlantic_interregional': (0.139, 11),
    'same_subregion':                  (0.115, 11),
    'same_region_cross_subregion':    (-0.011, 32),
    'ese_asia_cross_subregion':       (-0.014, 9),
    'other_cross_region':             (-0.020, 127),
}
for g, vals in sorted(groupings.items(), key=lambda x: -np.mean(x[1])):
    tgt_mean, tgt_n = target.get(g, (None, None))
    print(f"{g:<35} {len(vals):>5} {np.mean(vals):>15.3f}   target: mean={tgt_mean}, n={tgt_n}")

# Top E/SE Asia residual links — should match
print(f"\n--- Top E/SE Asia residuals ---")
print("Target: Thai-Vietnamese=+0.359, Chinese-Korean=+0.306, Filipino-Thai=+0.219, Filipino-Vietnamese=+0.209, Korean-Japanese=+0.20")
ese_pairs = [('thai','vietnamese'),('chinese','korean'),('filipino','thai'),('filipino','vietnamese'),('korean','japanese'),('chinese','japanese'),('filipino','korean'),('filipino','chinese')]
for a, b in ese_pairs:
    i, j = cuisines.index(a), cuisines.index(b)
    print(f"  {a:<12}-{b:<12}  resid={R[i,j]:+.3f}  sim={S[i,j]:.3f}  dist={D[i,j]:.0f} km")

# Long-distance positive-residual outliers
print(f"\n--- Long-distance outliers (target: well above regression line) ---")
ld_pairs = [('british','southern_us'),('british','russian'),('irish','russian'),
            ('french','russian'),('italian','russian'),('spanish','russian')]
for a, b in ld_pairs:
    i, j = cuisines.index(a), cuisines.index(b)
    print(f"  {a:<12}-{b:<12}  resid={R[i,j]:+.3f}  sim={S[i,j]:.3f}  dist={D[i,j]:.0f} km")

# Save residual matrix and similarity matrix for later steps
np.save('similarity_matrix.npy', S)
np.save('distance_matrix.npy', D)
np.save('residual_matrix.npy', R)
with open('cuisines.txt','w') as f:
    f.write('\n'.join(cuisines))
print("\nSaved: similarity_matrix.npy, distance_matrix.npy, residual_matrix.npy, cuisines.txt")

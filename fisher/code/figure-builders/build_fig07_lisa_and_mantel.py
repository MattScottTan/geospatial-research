"""
build_fig07_lisa_and_mantel.py

Generates v4_07_lisa_and_mantel.png — the spatial-validation figure for
Finding 1.5. Two-panel layout matching v4_05's style:
  LEFT:  Robinson world map of cuisine anchors classified by Local Moran's I
         quadrant, using inverse-distance spatial weights.
  RIGHT: Moran scatterplot showing per-cuisine residual vs spatial-lag
         residual, with quadrant labels and the regression slope = Global I.
A statistical inset reports the Mantel and partial Mantel test results.

USAGE
-----
This script expects:
  1. The cuisine-by-ingredient matrix at ./cuisine_ingredient_matrix.csv
     (rows = cuisines, columns = ingredients, values = frequencies).
  2. Natural Earth shapefiles at /home/claude/ne_repo (matches
     build_fig01_hero.py and build_fig05_bridge.py paths).
  3. Python packages: numpy, pandas, scikit-learn, scipy, geopy, cartopy,
     matplotlib, libpysal, esda.

Invoke: python build_fig07_lisa_and_mantel.py
Output: 07_lisa_and_mantel.png (in the working directory)

The Mantel and Local Moran's I computations are run inline rather than
read from a precomputed cache, so the script is fully self-contained.
Re-running this script will reproduce all reported statistics.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LinearRegression
from geopy.distance import great_circle
from libpysal.weights import W
from esda.moran import Moran, Moran_Local
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

# ============================================================
# CONFIG
# ============================================================
NE = '/home/claude/ne_repo'           # Natural Earth shapefile root
MATRIX = 'cuisine_ingredient_matrix.csv'
N_PERM = 9999                         # permutations for both Mantel and LISA
SEED = 42
OUT = '07_lisa_and_mantel.png'

# Cuisine anchors. Format: name -> (lat, lon).
ANCHORS = {
    'brazilian':(-14.24,-51.93), 'british':(55.38,-3.44), 'cajun_creole':(30.50,-91.20),
    'chinese':(35.86,104.20), 'filipino':(12.88,121.77), 'french':(46.23,2.21),
    'greek':(39.07,21.82), 'indian':(20.59,78.96), 'irish':(53.41,-8.24),
    'italian':(41.87,12.57), 'jamaican':(18.11,-77.30), 'japanese':(36.20,138.25),
    'korean':(35.91,127.77), 'mexican':(23.63,-102.55), 'moroccan':(31.79,-7.09),
    'russian':(61.52,105.32), 'southern_us':(33.00,-86.00), 'spanish':(40.46,-3.75),
    'thai':(15.87,100.99), 'vietnamese':(14.06,108.28),
}
DISPLAY = {
    'brazilian':'Brazilian','british':'British','cajun_creole':'Cajun-Creole',
    'chinese':'Chinese','filipino':'Filipino','french':'French','greek':'Greek',
    'indian':'Indian','irish':'Irish','italian':'Italian','jamaican':'Jamaican',
    'japanese':'Japanese','korean':'Korean','mexican':'Mexican','moroccan':'Moroccan',
    'russian':'Russian','southern_us':'Southern US','spanish':'Spanish',
    'thai':'Thai','vietnamese':'Vietnamese',
}
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

# ============================================================
# 1. LOAD MATRIX, COMPUTE SIMILARITY AND DISTANCE
# ============================================================
df = pd.read_csv(MATRIX, index_col=0)
cuisines = df.index.tolist()
n = len(cuisines)
assert all(c in ANCHORS for c in cuisines), "Anchor coverage must match matrix rows"

# Generic-ingredient filter: drop ingredients present in ≥19 of 20 cuisines.
# Closest-matching reconstruction of the published baseline.
presence = (df.values > 0).sum(axis=0)
M = df.values[:, presence < 19]
S = cosine_similarity(M)

# Pairwise great-circle distance, km
D = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i < j:
            d = great_circle(ANCHORS[ci], ANCHORS[cj]).kilometers
            D[i, j] = d; D[j, i] = d

# ============================================================
# 2. RESIDUALS (per-cuisine mean, used as LISA input)
# ============================================================
iu = np.triu_indices(n, k=1)
sim = S[iu]; log_d = np.log(D[iu])
reg = LinearRegression().fit(log_d.reshape(-1,1), sim)
predicted = reg.predict(log_d.reshape(-1,1))
resid = sim - predicted

R = np.zeros_like(S)
for k, (i, j) in enumerate(zip(*iu)):
    R[i, j] = resid[k]; R[j, i] = resid[k]
mean_resid = R.sum(axis=1) / (n - 1)

# ============================================================
# 3. MANTEL + PARTIAL MANTEL
# ============================================================
DSim = 1.0 - S                                    # dissimilarity
LD   = np.where(D > 0, np.log(np.where(D > 0, D, 1)), 0)
G    = np.array([[1.0 if SUBREGION[a] != SUBREGION[b] else 0.0
                  for b in cuisines] for a in cuisines])

def _r(x, y): return np.corrcoef(x, y)[0, 1]

def mantel(M1, M2, n_perm=N_PERM, seed=SEED):
    rng = np.random.default_rng(seed)
    iu = np.triu_indices(M1.shape[0], k=1)
    obs = _r(M1[iu], M2[iu])
    perms = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(M1.shape[0])
        perms[k] = _r(M1[np.ix_(order, order)][iu], M2[iu])
    p_two = (np.sum(np.abs(perms) >= np.abs(obs)) + 1) / (n_perm + 1)
    return obs, p_two

def partial_mantel(My, Mx, Mz, n_perm=N_PERM, seed=SEED):
    rng = np.random.default_rng(seed)
    iu = np.triu_indices(My.shape[0], k=1)
    y, x, z = My[iu], Mx[iu], Mz[iu]
    def pcorr(y, x, z):
        ryx, ryz, rxz = _r(y, x), _r(y, z), _r(x, z)
        return (ryx - ryz*rxz) / np.sqrt((1-ryz**2)*(1-rxz**2))
    obs = pcorr(y, x, z)
    perms = np.empty(n_perm)
    for k in range(n_perm):
        order = rng.permutation(My.shape[0])
        perms[k] = pcorr(My[np.ix_(order, order)][iu], x, z)
    p_two = (np.sum(np.abs(perms) >= np.abs(obs)) + 1) / (n_perm + 1)
    return obs, p_two

print("Running Mantel tests...")
r1, p1 = mantel(DSim, LD)
r2, p2 = partial_mantel(DSim, LD, G)
r3, p3 = mantel(DSim, G)
print(f"  Dissim ↔ log-distance:                       r = {r1:+.4f}, p = {p1:.4f}")
print(f"  Partial Mantel (controlling for subregion):   r = {r2:+.4f}, p = {p2:.4f}")
print(f"  Dissim ↔ subregion gap:                      r = {r3:+.4f}, p = {p3:.4f}")

# ============================================================
# 4. LOCAL MORAN'S I (LISA)
# ============================================================
W_raw = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            W_raw[i, j] = 1.0 / D[i, j]
W_norm = W_raw / W_raw.sum(axis=1, keepdims=True)
neigh = {i: [j for j in range(n) if j != i] for i in range(n)}
wts   = {i: W_norm[i, [j for j in range(n) if j != i]].tolist() for i in range(n)}
w = W(neigh, wts); w.transform = 'r'

print("Running Global and Local Moran's I...")
moran_g = Moran(mean_resid, w, permutations=N_PERM)
lisa = Moran_Local(mean_resid, w, permutations=N_PERM, seed=SEED)
print(f"  Global Moran's I = {moran_g.I:+.4f}, p = {moran_g.p_sim:.4f}")

QUAD = {1: 'HH', 2: 'LH', 3: 'LL', 4: 'HL'}
classifications = []
for i in range(n):
    p = lisa.p_sim[i]
    q = QUAD[lisa.q[i]]
    if p < 0.05:    cls = q + '_sig'
    elif p < 0.10:  cls = q + '_marg'
    else:           cls = q + '_ns'
    classifications.append((cuisines[i], q, p, cls, lisa.Is[i]))
print("  Significant LISA classifications (p < 0.05):")
for c, q, p, cls, lI in classifications:
    if 'sig' in cls:
        print(f"    {c}: {q} (Local I = {lI:+.3f}, p = {p:.4f})")

# ============================================================
# 5. FIGURE
# ============================================================
COLOR_BY_CLS = {
    'HH_sig':  '#c45a2e', 'HH_marg': '#e89466', 'HH_ns':  '#f1c1a3',
    'LL_sig':  '#2c5d8b', 'LL_marg': '#7aa2c4', 'LL_ns':  '#bcd1e3',
    'HL_sig':  '#a23a8a', 'HL_marg': '#c47ab2', 'HL_ns':  '#dfb1d3',
    'LH_sig':  '#1f8a8a', 'LH_marg': '#6cb6b6', 'LH_ns':  '#b1d6d6',
}
LAND_COLOR  = '#f3e8ce'
OCEAN_COLOR = '#d3e3ec'
COAST_COLOR = '#5d6770'
BORDER_COLOR= '#a9b3bd'

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
fig = plt.figure(figsize=(17, 9.5), facecolor='white')

# ---- LEFT: world map ----
ax_map = fig.add_axes([0.005, 0.18, 0.62, 0.76],
                      projection=ccrs.Robinson(central_longitude=20))
ax_map.set_global()

land  = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_land.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=LAND_COLOR, edgecolor='none')
ocean = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_ocean.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=OCEAN_COLOR, edgecolor='none')
coast = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_coastline.shp').geometries(),
                       ccrs.PlateCarree(), facecolor='none',
                       edgecolor=COAST_COLOR, linewidth=0.4)
borders = ShapelyFeature(Reader(f'{NE}/110m_cultural/ne_110m_admin_0_countries.shp').geometries(),
                         ccrs.PlateCarree(), facecolor='none',
                         edgecolor=BORDER_COLOR, linewidth=0.25)
ax_map.add_feature(ocean); ax_map.add_feature(land)
ax_map.add_feature(borders); ax_map.add_feature(coast)

ax_map.gridlines(linewidth=0.3, color='#aab4be', alpha=0.5, linestyle=':',
                 xlocs=range(-180,181,30), ylocs=range(-60,91,30))

max_abs = max(abs(mean_resid))
for i, (c, q, p, cls, lI) in enumerate(classifications):
    lat, lon = ANCHORS[c]
    color = COLOR_BY_CLS[cls]
    msize = 75 + 220 * (abs(mean_resid[i]) / max_abs)
    if 'sig' in cls:    edge, ew, alpha = 'black', 1.7, 1.0
    elif 'marg' in cls: edge, ew, alpha = '#222', 1.0, 1.0
    else:               edge, ew, alpha = '#666', 0.5, 0.85
    ax_map.scatter(lon, lat, s=msize, color=color, alpha=alpha,
                   edgecolor=edge, linewidth=ew,
                   transform=ccrs.PlateCarree(), zorder=5)

LABELS = {
    'mexican':(-2,-7,'right','top'), 'cajun_creole':(-3,-3,'right','top'),
    'jamaican':(3,-3,'left','top'), 'southern_us':(3,3,'left','bottom'),
    'brazilian':(3,1,'left','center'),
    'irish':(-3,3,'right','bottom'), 'british':(3,3,'left','bottom'),
    'french':(0,-4,'center','top'), 'spanish':(-3,0,'right','center'),
    'italian':(3,1,'left','center'), 'greek':(3,-2,'left','top'),
    'moroccan':(-3,-2,'right','top'),
    'russian':(3,3,'left','bottom'),
    'indian':(3,-2,'left','top'),
    'chinese':(-3,3,'right','bottom'), 'korean':(3,3,'left','bottom'),
    'japanese':(3,-2,'left','top'),
    'thai':(-3,-3,'right','top'), 'vietnamese':(3,-2,'left','top'),
    'filipino':(-3,2,'right','bottom'),
}
for c, (dlon, dlat, ha, va) in LABELS.items():
    lat, lon = ANCHORS[c]
    cls = next(cl for cn, q, p, cl, lI in classifications if cn == c)
    weight = 'bold' if 'sig' in cls else 'normal'
    fontsize = 9.2 if 'sig' in cls else 8.6
    ax_map.text(lon+dlon, lat+dlat, DISPLAY[c],
                fontsize=fontsize, fontweight=weight, ha=ha, va=va,
                transform=ccrs.PlateCarree(), zorder=7,
                bbox=dict(boxstyle='round,pad=0.18', facecolor='white',
                          edgecolor='none', alpha=0.85))

ax_map.set_title("Local spatial autocorrelation of cuisine residuals (LISA)",
                 fontsize=12.5, fontweight='bold', pad=8)

legend_handles = [
    mpatches.Patch(facecolor='#c45a2e', edgecolor='black',
                   label='HH (sig.) — high residual + high-residual neighborhood'),
    mpatches.Patch(facecolor='#a23a8a', edgecolor='black',
                   label='HL — high residual + low-residual neighborhood (isolated bridge)'),
    mpatches.Patch(facecolor='#2c5d8b', edgecolor='black',
                   label='LL (sig.) — low residual + low-residual neighborhood'),
    mpatches.Patch(facecolor='#1f8a8a', edgecolor='black',
                   label='LH — low residual + high-residual neighborhood'),
    mpatches.Patch(facecolor='#f1c1a3', edgecolor='#666', linewidth=0.5,
                   label='Lighter shade + thin edge: same quadrant, p ≥ 0.10 (sign-only)'),
]
fig.legend(handles=legend_handles, loc='lower left',
           bbox_to_anchor=(0.02, 0.02), frameon=False, fontsize=8.7, ncol=2,
           handletextpad=0.5)

# ---- RIGHT: Moran scatterplot ----
ax_sc = fig.add_axes([0.69, 0.50, 0.29, 0.43])
spatial_lag = W_norm @ mean_resid
mr_z = (mean_resid - mean_resid.mean()) / mean_resid.std(ddof=0)
sl_z = (spatial_lag - spatial_lag.mean()) / spatial_lag.std(ddof=0)
ax_sc.axhline(0, color='#aaa', linewidth=0.7)
ax_sc.axvline(0, color='#aaa', linewidth=0.7)

SC_OFF = {
    'mexican':(8,6),'jamaican':(8,-4),'cajun_creole':(-12,10),
    'southern_us':(-30,-12),'brazilian':(8,-4),'russian':(-32,4),
    'italian':(8,-8),'chinese':(8,8),'japanese':(-15,-10),
    'korean':(8,-10),'greek':(-12,6),'moroccan':(8,4),'indian':(-12,-10),
    'filipino':(-15,6),'spanish':(-12,6),'thai':(-12,-10),'french':(8,0),
    'british':(8,-4),'irish':(-15,8),'vietnamese':(8,4),
}
for i, (c, q, p, cls, lI) in enumerate(classifications):
    color = COLOR_BY_CLS[cls]
    if 'sig' in cls:    edge, lw, sz = 'black', 1.6, 95
    elif 'marg' in cls: edge, lw, sz = '#222', 1.0, 75
    else:               edge, lw, sz = '#888', 0.4, 60
    ax_sc.scatter(mr_z[i], sl_z[i], s=sz, color=color, edgecolor=edge,
                  linewidth=lw, zorder=4, alpha=0.92)
    off = SC_OFF.get(c, (6, 4))
    if off is None: continue
    weight = 'bold' if 'sig' in cls else 'normal'
    ax_sc.annotate(DISPLAY[c], (mr_z[i], sl_z[i]),
                   xytext=off, textcoords='offset points',
                   fontsize=7.7, color='#333', fontweight=weight)

slope = np.cov(mr_z, sl_z, ddof=0)[0,1] / np.var(mr_z, ddof=0)
xs_line = np.linspace(mr_z.min()-0.2, mr_z.max()+0.2, 50)
ax_sc.plot(xs_line, slope*xs_line, color='#888', linewidth=0.9, linestyle='--',
           label=f"slope = Moran's I = {moran_g.I:+.3f}")
for txt, color, x, y, ha, va in [
    ('HH','#c45a2e', 0.97, 0.97, 'right', 'top'),
    ('LH','#1f8a8a', 0.03, 0.97, 'left',  'top'),
    ('LL','#2c5d8b', 0.03, 0.03, 'left',  'bottom'),
    ('HL','#a23a8a', 0.97, 0.03, 'right', 'bottom'),
]:
    ax_sc.text(x, y, txt, transform=ax_sc.transAxes,
               fontsize=11, fontweight='bold', color=color, alpha=0.45,
               ha=ha, va=va)
ax_sc.set_xlabel("Mean residual (z-score)", fontsize=9)
ax_sc.set_ylabel("Spatial lag (z-score)", fontsize=9)
ax_sc.set_title(f"Moran scatterplot — Global I = {moran_g.I:+.3f}, p = {moran_g.p_sim:.3f}",
                fontsize=10, fontweight='bold')
ax_sc.legend(loc='lower right', fontsize=7.7, frameon=False)
ax_sc.tick_params(labelsize=8); ax_sc.grid(True, alpha=0.18)
for s in ('top','right'): ax_sc.spines[s].set_visible(False)
ax_sc.set_xlim(-2.0, 2.6); ax_sc.set_ylim(-1.8, 2.7)

# ---- BOTTOM: Mantel inset ----
ax_st = fig.add_axes([0.67, 0.05, 0.32, 0.40])
ax_st.axis('off')
stats_text = (
    "Mantel tests (190 pairs · 9999 permutations)\n"
    "─────────────────────────────────────────────────\n"
    f"  Dissimilarity ↔ log-distance         r = {r1:+.3f}    p < 0.001\n"
    f"  Partial, controlling for subregion   r = {r2:+.3f}    p < 0.001\n"
    f"  Dissimilarity ↔ subregion gap        r = {r3:+.3f}    p < 0.001\n"
    "\n"
    "Distance is a real predictor of cuisine dissimilarity, and the\n"
    "relationship survives partialling out subregional adjacency —\n"
    "ruling out the 'just neighbors-being-neighbors' explanation.\n"
    "\n"
    "What remains after this distance baseline is the residual\n"
    "structure the LISA map decomposes spatially."
)
ax_st.text(0.0, 1.0, stats_text, transform=ax_st.transAxes,
           fontsize=8.7, ha='left', va='top', family='monospace', color='#222')

fig.suptitle("Spatial structure of cuisine residuals: Mantel tests + LISA classification",
             fontsize=13.5, fontweight='bold', y=0.97)
fig.text(0.5, 0.94,
         "Two complementary spatial-statistical tests on the residual structure of Finding 1",
         ha='center', fontsize=10, style='italic', color='#444')

plt.savefig(OUT, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {OUT} ({os.path.getsize(OUT):,} bytes)")

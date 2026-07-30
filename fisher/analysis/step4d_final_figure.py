"""
Step 4d: Final LISA + Mantel figure.
Approach: drop leader lines (too fragile across cartopy versions).
Use inline labels with carefully tuned offsets. For ultra-tight clusters
(European, East Asian) accept slightly smaller text.
"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
from cartopy.feature import ShapelyFeature
from libpysal.weights import W
from esda.moran import Moran, Moran_Local

S = np.load('similarity_matrix.npy')
D = np.load('distance_matrix.npy')
mean_resid = np.load('mean_resid.npy')
with open('cuisines.txt') as f:
    cuisines = [l.strip() for l in f]
with open('mantel_results.json') as f:
    mantel = json.load(f)
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
DISPLAY = {
    'brazilian':'Brazilian','british':'British','cajun_creole':'Cajun-Creole',
    'chinese':'Chinese','filipino':'Filipino','french':'French','greek':'Greek',
    'indian':'Indian','irish':'Irish','italian':'Italian','jamaican':'Jamaican',
    'japanese':'Japanese','korean':'Korean','mexican':'Mexican','moroccan':'Moroccan',
    'russian':'Russian','southern_us':'Southern US','spanish':'Spanish',
    'thai':'Thai','vietnamese':'Vietnamese',
}

# LISA
W_raw = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i != j: W_raw[i,j] = 1.0 / D[i,j]
W_norm = W_raw / W_raw.sum(axis=1, keepdims=True)
neigh = {i: [j for j in range(n) if j != i] for i in range(n)}
wts   = {i: W_norm[i,[j for j in range(n) if j != i]].tolist() for i in range(n)}
w = W(neigh, wts); w.transform='r'

moran_g = Moran(mean_resid, w, permutations=9999)
lisa = Moran_Local(mean_resid, w, permutations=9999, seed=42)

QUAD = {1:'HH', 2:'LH', 3:'LL', 4:'HL'}
classifications = []
for i in range(n):
    p = lisa.p_sim[i]
    q = QUAD[lisa.q[i]]
    if p < 0.05:    cls = q + '_sig'
    elif p < 0.10:  cls = q + '_marg'
    else:           cls = q + '_ns'
    classifications.append((cuisines[i], q, p, cls, lisa.Is[i]))

COLOR_BY_CLS = {
    'HH_sig':  '#c45a2e', 'HH_marg': '#e89466', 'HH_ns':  '#f1c1a3',
    'LL_sig':  '#2c5d8b', 'LL_marg': '#7aa2c4', 'LL_ns':  '#bcd1e3',
    'HL_sig':  '#a23a8a', 'HL_marg': '#c47ab2', 'HL_ns':  '#dfb1d3',
    'LH_sig':  '#1f8a8a', 'LH_marg': '#6cb6b6', 'LH_ns':  '#b1d6d6',
}

fig = plt.figure(figsize=(17, 9.5), facecolor='white')

ax_map = fig.add_axes([0.005, 0.18, 0.62, 0.76],
                      projection=ccrs.Robinson(central_longitude=20))
ax_map.set_global()
NE_PATH = '/usr/local/lib/python3.12/dist-packages/pyogrio/tests/fixtures/naturalearth_lowres/naturalearth_lowres.shp'
countries = ShapelyFeature(shpreader.Reader(NE_PATH).geometries(),
                           ccrs.PlateCarree(),
                           facecolor='#f3e8ce', edgecolor='#a9b3bd', linewidth=0.3)
ax_map.add_feature(countries)
ax_map.set_facecolor('#d3e3ec')
ax_map.gridlines(linewidth=0.3, color='#aab4be', alpha=0.5, linestyle=':',
                 xlocs=range(-180,181,30), ylocs=range(-60,91,30))

# Markers — smaller base size to leave more room for labels
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

# Inline label offsets — tuned per cuisine.
# Tuple format: (dx_in_degrees, dy_in_degrees, ha, va)
LABELS = {
    # Americas
    'mexican':     (-2,  -7, 'right', 'top'),
    'cajun_creole':(-3,  -3, 'right', 'top'),
    'jamaican':    ( 3,  -3, 'left',  'top'),
    'southern_us': ( 3,   3, 'left',  'bottom'),
    'brazilian':   ( 3,   1, 'left',  'center'),
    # Europe — staggered carefully
    'irish':       (-3,   3, 'right', 'bottom'),
    'british':     ( 3,   3, 'left',  'bottom'),
    'french':      ( 0,  -4, 'center','top'),     # straight down to avoid Spanish
    'spanish':     (-3,   0, 'right', 'center'),   # straight left
    'italian':     ( 3,   1, 'left',  'center'),
    'greek':       ( 3,  -2, 'left',  'top'),
    # Africa / Mid-East
    'moroccan':    (-3,  -2, 'right', 'top'),
    # Eurasia / Russia
    'russian':     ( 3,   3, 'left',  'bottom'),
    # South Asia
    'indian':      ( 3,  -2, 'left',  'top'),
    # East Asia
    'chinese':     (-3,   3, 'right', 'bottom'),
    'korean':      ( 3,   3, 'left',  'bottom'),
    'japanese':    ( 3,  -2, 'left',  'top'),
    # SE Asia
    'thai':        (-3,  -3, 'right', 'top'),
    'vietnamese':  ( 3,  -2, 'left',  'top'),
    'filipino':    (-3,   2, 'right', 'bottom'),
}

for c, (dlon, dlat, ha, va) in LABELS.items():
    lat, lon = ANCHORS[c]
    cls = next(cls for cn, q, p, cls, lI in classifications if cn == c)
    weight = 'bold' if 'sig' in cls else 'normal'
    fontsize = 9.2 if 'sig' in cls else 8.6
    ax_map.text(lon+dlon, lat+dlat, DISPLAY[c],
                fontsize=fontsize, fontweight=weight, ha=ha, va=va,
                transform=ccrs.PlateCarree(), zorder=7,
                bbox=dict(boxstyle='round,pad=0.18',
                          facecolor='white', edgecolor='none', alpha=0.85))

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

# === Right: Moran scatterplot ===
ax_sc = fig.add_axes([0.69, 0.50, 0.29, 0.43])
spatial_lag = W_norm @ mean_resid
mr_z = (mean_resid - mean_resid.mean()) / mean_resid.std(ddof=0)
sl_z = (spatial_lag - spatial_lag.mean()) / spatial_lag.std(ddof=0)

ax_sc.axhline(0, color='#aaa', linewidth=0.7)
ax_sc.axvline(0, color='#aaa', linewidth=0.7)

SC_OFF = {
    'mexican':    ( 8,  6),
    'jamaican':   ( 8, -4),
    'cajun_creole':(-12, 10),
    'southern_us':(-30,-12),
    'brazilian':  ( 8, -4),
    'russian':    (-32, 4),     # significant — keep bold; pull far left
    'italian':    (8, -8),      # right-down to clear Russian
    'chinese':    (8, 8),       # right-up to clear Russian
    'japanese':   (-15, -10),
    'korean':     ( 8, -10),
    'greek':      (-12, 6),
    'moroccan':   ( 8, 4),
    'indian':     (-12, -10),
    'filipino':   (-15, 6),
    'spanish':    (-12, 6),
    'thai':       (-12, -10),
    'french':     ( 8, 0),
    'british':    ( 8, -4),
    'irish':      (-15, 8),
    'vietnamese': ( 8, 4),
}
for i, (c, q, p, cls, lI) in enumerate(classifications):
    color = COLOR_BY_CLS[cls]
    if 'sig' in cls:    edge, lw, sz = 'black', 1.6, 95
    elif 'marg' in cls: edge, lw, sz = '#222', 1.0, 75
    else:               edge, lw, sz = '#888', 0.4, 60
    ax_sc.scatter(mr_z[i], sl_z[i], s=sz, color=color, edgecolor=edge,
                  linewidth=lw, zorder=4, alpha=0.92)
    off = SC_OFF.get(c, (6, 4))
    if off is None:
        continue   # suppressed label
    dx, dy = off
    weight = 'bold' if 'sig' in cls else 'normal'
    ax_sc.annotate(DISPLAY[c], (mr_z[i], sl_z[i]),
                   xytext=(dx, dy), textcoords='offset points',
                   fontsize=7.7, color='#333', fontweight=weight)

slope = np.cov(mr_z, sl_z, ddof=0)[0,1] / np.var(mr_z, ddof=0)
xs = np.linspace(mr_z.min()-0.2, mr_z.max()+0.2, 50)
ax_sc.plot(xs, slope*xs, color='#888', linewidth=0.9, linestyle='--',
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
ax_sc.tick_params(labelsize=8)
ax_sc.grid(True, alpha=0.18)
for s in ['top','right']: ax_sc.spines[s].set_visible(False)
ax_sc.set_xlim(-2.0, 2.6)
ax_sc.set_ylim(-1.8, 2.7)

# === Mantel inset ===
ax_st = fig.add_axes([0.67, 0.05, 0.32, 0.40])
ax_st.axis('off')
m1 = mantel['distance_vs_dissim']
m2 = mantel['partial_distance_controlling_subregion']
m3 = mantel['subregion_vs_dissim']
stats_text = (
    "Mantel tests (190 pairs · 9999 permutations)\n"
    "─────────────────────────────────────────────────\n"
    f"  Dissimilarity ↔ log-distance         r = {m1['r']:+.3f}    p < 0.001\n"
    f"  Partial, controlling for subregion   r = {m2['r_partial']:+.3f}    p < 0.001\n"
    f"  Dissimilarity ↔ subregion gap        r = {m3['r']:+.3f}    p < 0.001\n"
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

plt.savefig('v4_07_lisa_and_mantel.png', dpi=170,
            bbox_inches='tight', facecolor='white')
print("Saved v4_07_lisa_and_mantel.png")

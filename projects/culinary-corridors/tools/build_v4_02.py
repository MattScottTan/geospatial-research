"""
Build replacement for v4_02 (baseline scatter): the published figure had two
problems that hurt the GIS framing in a Fisher Prize submission:
  (1) Title said "The GIS move: convert cuisine similarity into distance residuals"
      — meta-language about GIS as a single methodological move.
  (2) Cuisine labels were lowercase and underscore-joined ("british_southern_us")
      rather than properly capitalized.
This replacement regenerates the scatter from the cuisine-by-ingredient matrix
with a neutral title and properly formatted cuisine names.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.linear_model import LinearRegression
from geopy.distance import great_circle

# ===== Reproduce the residual baseline =====
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
DISPLAY = {
    'brazilian':'Brazilian','british':'British','cajun_creole':'Cajun-Creole',
    'chinese':'Chinese','filipino':'Filipino','french':'French','greek':'Greek',
    'indian':'Indian','irish':'Irish','italian':'Italian','jamaican':'Jamaican',
    'japanese':'Japanese','korean':'Korean','mexican':'Mexican','moroccan':'Moroccan',
    'russian':'Russian','southern_us':'Southern US','spanish':'Spanish',
    'thai':'Thai','vietnamese':'Vietnamese',
}

# Generic-ingredient filter: drop ingredients present in ≥19 of 20 cuisines.
# Matches the published baseline most closely (intercept and slope within 0.02).
presence = (df.values > 0).sum(axis=0)
keep = presence < 19
M = df.values[:, keep]
S = cosine_similarity(M)

D = np.zeros((n, n))
for i, ci in enumerate(cuisines):
    for j, cj in enumerate(cuisines):
        if i < j:
            d = great_circle(ANCHORS[ci], ANCHORS[cj]).kilometers
            D[i,j] = d; D[j,i] = d

iu = np.triu_indices(n, k=1)
sim = S[iu]; dist = D[iu]; log_d = np.log(dist)
reg = LinearRegression().fit(log_d.reshape(-1,1), sim)
intercept, slope, r2 = reg.intercept_, reg.coef_[0], reg.score(log_d.reshape(-1,1), sim)
predicted = reg.predict(log_d.reshape(-1,1))
resid = sim - predicted

# Build pair-level frame for plotting
pairs = []
for k, (i, j) in enumerate(zip(*iu)):
    pairs.append({
        'a': cuisines[i], 'b': cuisines[j],
        'sim': sim[k], 'log_d': log_d[k], 'resid': resid[k],
    })
pairs = pd.DataFrame(pairs)

# Identify positive vs negative residual; label only the strongest outliers
HIGHLIGHT = {
    ('thai','vietnamese'),
    ('chinese','korean'),
    ('british','southern_us'),
    ('british','russian'),
    ('irish','russian'),
    ('french','russian'),
    ('italian','russian'),
}

# ===== Figure =====
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig = plt.figure(figsize=(13.5, 7.8), facecolor='white')
ax = fig.add_axes([0.085, 0.13, 0.85, 0.74])

POS_COLOR = '#3d8a5d'
NEG_COLOR = '#7e7da3'
LINE_COLOR = '#222'

# Plot points with positive vs negative residual
mask_pos = pairs['resid'] >= 0
ax.scatter(pairs.loc[mask_pos,'log_d'], pairs.loc[mask_pos,'sim'],
           s=58, color=POS_COLOR, edgecolor='white', linewidth=0.6,
           alpha=0.85, zorder=3, label='Above the line: similarity exceeds distance prediction')
ax.scatter(pairs.loc[~mask_pos,'log_d'], pairs.loc[~mask_pos,'sim'],
           s=58, color=NEG_COLOR, edgecolor='white', linewidth=0.6,
           alpha=0.85, zorder=3, label='Below the line: similarity falls short of distance prediction')

# Regression line
xs = np.linspace(pairs['log_d'].min()-0.1, pairs['log_d'].max()+0.1, 100)
ys = intercept + slope*xs
ax.plot(xs, ys, color=LINE_COLOR, linewidth=1.7, zorder=4,
        label=f'Distance-only baseline')

# Highlight + label outliers
LABEL_OFFSETS = {
    ('thai','vietnamese'):     (0.18, 0.025, 'left',   'bottom'),
    ('chinese','korean'):      (0.20, -0.005,'left',   'center'),
    ('british','southern_us'): (-0.12, 0.022,'right',  'bottom'),
    ('british','russian'):     ( 0.18, 0.020,'left',   'bottom'),
    ('irish','russian'):       ( 0.18,-0.020,'left',   'top'),
    ('french','russian'):      (-0.18,-0.018,'right',  'top'),
    ('italian','russian'):     ( 0.18,-0.038,'left',   'top'),
}

for _, row in pairs.iterrows():
    pair_key = (row['a'], row['b'])
    if pair_key not in HIGHLIGHT:
        continue
    x, y = row['log_d'], row['sim']
    # Highlight ring
    ax.scatter([x],[y], s=120, facecolor='none', edgecolor='#222',
               linewidth=1.4, zorder=5)
    label = f"{DISPLAY[row['a']]}–{DISPLAY[row['b']]}"
    dx, dy, ha, va = LABEL_OFFSETS[pair_key]
    ax.annotate(label, (x, y), xytext=(x+dx, y+dy),
                ha=ha, va=va, fontsize=9.4, fontweight='bold', color='#111',
                arrowprops=dict(arrowstyle='-', color='#666', linewidth=0.7,
                                shrinkA=4, shrinkB=4),
                zorder=6,
                bbox=dict(boxstyle='round,pad=0.22', facecolor='white',
                          edgecolor='none', alpha=0.92))

# Equation inset (clean, with proper minus sign and spacing)
eq_text = (f"Baseline:  similarity = {intercept:.3f} {'−' if slope<0 else '+'} "
           f"{abs(slope):.3f} × ln(distance)\n"
           f"R² = {r2:.3f}   ·   n = 190 cuisine pairs")
ax.text(0.025, 0.04, eq_text,
        transform=ax.transAxes,
        fontsize=10, color='#222', family='monospace', linespacing=1.5,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#f7f7f4',
                  edgecolor='#bbb', linewidth=0.6))

# Axes
ax.set_xlabel('Log geographic distance between cuisine anchors (ln km)',
              fontsize=11, color='#222', labelpad=10)
ax.set_ylabel('Cosine similarity of filtered ingredient profiles',
              fontsize=11, color='#222', labelpad=10)
ax.grid(True, linestyle=':', linewidth=0.5, color='#bbb', alpha=0.6)
ax.set_axisbelow(True)
for spine in ('top','right'):
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#888'); ax.spines['bottom'].set_color('#888')
ax.tick_params(colors='#444')

# Legend
leg = ax.legend(loc='upper right', frameon=False, fontsize=9.5,
                handletextpad=0.4, borderaxespad=0.5)

# Title — neutral, descriptive
fig.text(0.5, 0.95,
         'Distance baseline for cuisine similarity',
         ha='center', va='center',
         fontsize=15, fontweight='bold', color='#111')
fig.text(0.5, 0.913,
         'Each point is one of 190 cuisine pairs. Labeled points are the strongest positive residuals.',
         ha='center', va='center',
         fontsize=10.5, color='#444', style='italic')

out = '/home/claude/v4_02_method_residual_baseline.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
print(f"Reconstruction: intercept={intercept:.3f}, slope={slope:.4f}, R²={r2:.3f}")
print(f"  (Published values: intercept=1.273, slope=-0.116, R²=0.355)")

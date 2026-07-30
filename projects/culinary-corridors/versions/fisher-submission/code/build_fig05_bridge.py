"""
Improved bridge-index figure: world map of cuisine anchors sized by
bridge score, paired with a horizontal bar chart of top scores. Both
panels visually emphasize the regional-balance finding: 9 of 10 top
bridges are non-Asian.
"""
import sys, os
sys.path.insert(0, '/home/claude/v4')
import figdata as D

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

NE = '/home/claude/ne_repo'

LAND_COLOR  = '#f3e8ce'
OCEAN_COLOR = '#d3e3ec'
COAST_COLOR = '#5d6770'
BORDER_COLOR= '#a9b3bd'

# Color palette: blue for Asian cuisines (1 of top 10), warm tones for non-Asian
COLOR_ASIAN     = '#1f5fa3'
COLOR_NONASIAN  = '#c45a2e'
COLOR_OTHER     = '#bbbbbb'

ASIAN_SET = {'Filipino', 'Chinese', 'Japanese', 'Korean', 'Thai', 'Vietnamese'}

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})

fig = plt.figure(figsize=(16, 8.0), facecolor='white')

# ---- LEFT PANEL: WORLD MAP ----
ax_map = plt.axes([0.03, 0.10, 0.62, 0.78], projection=ccrs.Robinson(central_longitude=20))
ax_map.set_global()

land  = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_land.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=LAND_COLOR, edgecolor='none')
ocean = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_ocean.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=OCEAN_COLOR, edgecolor='none')
coast = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_coastline.shp').geometries(),
                       ccrs.PlateCarree(), facecolor='none', edgecolor=COAST_COLOR, linewidth=0.4)
borders = ShapelyFeature(Reader(f'{NE}/110m_cultural/ne_110m_admin_0_countries.shp').geometries(),
                         ccrs.PlateCarree(), facecolor='none', edgecolor=BORDER_COLOR, linewidth=0.25)

ax_map.add_feature(ocean)
ax_map.add_feature(land)
ax_map.add_feature(borders)
ax_map.add_feature(coast)

# subtle graticule
ax_map.gridlines(draw_labels=False, linewidth=0.3, color='#aab4be',
                 alpha=0.5, linestyle=':',
                 xlocs=range(-180, 181, 30), ylocs=range(-60, 91, 30))

# Bridge scores as a dict for lookup
bridge_dict = dict(D.BRIDGE_SCORES)
TEXT_STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

# Plot all anchors. Top-10 bridges get color + size by score; others are small grey.
for name, (lat, lon) in D.ANCHORS.items():
    if name in ('Anchor_A', 'Anchor_B'):
        ax_map.plot(lon, lat, 'o',
                    markerfacecolor='white',
                    markeredgecolor='#888',
                    markersize=4,
                    markeredgewidth=0.8,
                    transform=ccrs.PlateCarree(),
                    zorder=4, alpha=0.7)
        continue

    if name in bridge_dict:
        score = bridge_dict[name]
        color = COLOR_ASIAN if name in ASIAN_SET else COLOR_NONASIAN
        size = 6 + 36 * score   # diameter scales with score
        ax_map.plot(lon, lat, 'o',
                    markerfacecolor=color,
                    markeredgecolor='white',
                    markersize=size,
                    markeredgewidth=1.5,
                    transform=ccrs.PlateCarree(),
                    zorder=6, alpha=0.92)
    else:
        # corpus anchor not in top-10 bridges
        ax_map.plot(lon, lat, 'o',
                    markerfacecolor=COLOR_OTHER,
                    markeredgecolor='white',
                    markersize=5,
                    markeredgewidth=1.0,
                    transform=ccrs.PlateCarree(),
                    zorder=5, alpha=0.9)

# Label only the top-10 bridges
LABEL_OFFSETS = {
    'Filipino':    (  4,  0, 'left'),
    'Russian':     (  0,  6, 'center'),
    'Southern_US': (  4,  3, 'left'),
    'Jamaican':    (  4, -3, 'left'),
    'French':      (  -8,  -8, 'center'),
    'Spanish':     (  -10, -3, 'right'),
    'British':     ( -8,  6, 'right'),
    'Irish':       ( -10, -2, 'right'),
    'Italian':     (  10, -2, 'left'),
    'Brazilian':   (  4,  0, 'left'),
}
for name, _score in D.BRIDGE_SCORES:
    lat, lon = D.ANCHORS[name]
    dx, dy, ha = LABEL_OFFSETS.get(name, (4, 0, 'left'))
    label = name.replace('_', ' ')
    ax_map.text(lon + dx, lat + dy, label,
                fontsize=9.5, ha=ha, va='center',
                color='#111',
                fontweight='semibold',
                transform=ccrs.PlateCarree(),
                path_effects=TEXT_STROKE,
                zorder=8)

# Map title
fig.text(0.34, 0.94,
         'Bridge cuisines: where residual culinary similarity concentrates',
         ha='center', va='center',
         fontsize=14, fontweight='bold', color='#111')
fig.text(0.34, 0.905,
         'Circle size ∝ residual bridge score. Three structural geographies: Pacific-archipelagic, Eurasian continental, and Atlantic-rim.',
         ha='center', va='center',
         fontsize=10.5, color='#444', style='italic')

# Map legend
ax_leg = fig.add_axes([0.03, 0.04, 0.62, 0.05])
ax_leg.axis('off')
ax_leg.set_xlim(0, 1); ax_leg.set_ylim(0, 1)
ax_leg.plot([0.03], [0.5], 'o',
            markerfacecolor=COLOR_ASIAN,
            markeredgecolor='white',
            markersize=18, markeredgewidth=1.5)
ax_leg.text(0.06, 0.5, 'Pacific-archipelagic anchor', fontsize=9.5, va='center', color='#222')
ax_leg.plot([0.27], [0.5], 'o',
            markerfacecolor=COLOR_NONASIAN,
            markeredgecolor='white',
            markersize=18, markeredgewidth=1.5)
ax_leg.text(0.305, 0.5, 'Eurasian / Atlantic-rim anchor', fontsize=9.5, va='center', color='#222')
ax_leg.plot([0.55], [0.5], 'o',
            markerfacecolor=COLOR_OTHER,
            markeredgecolor='white',
            markersize=8, markeredgewidth=1.0)
ax_leg.text(0.57, 0.5, 'Other corpus anchor', fontsize=9.5, va='center', color='#222')
ax_leg.plot([0.74], [0.5], 'o',
            markerfacecolor='white',
            markeredgecolor='#888',
            markersize=6, markeredgewidth=0.8)
ax_leg.text(0.76, 0.5, 'Anchor with less certain identity', fontsize=9.5, va='center', color='#222')

# ---- RIGHT PANEL: HORIZONTAL BAR CHART ----
ax_bar = plt.axes([0.71, 0.13, 0.26, 0.72])
names = [n for n, _s in D.BRIDGE_SCORES][::-1]   # reverse so top is at top
scores = [s for _n, s in D.BRIDGE_SCORES][::-1]
colors = [COLOR_ASIAN if n in ASIAN_SET else COLOR_NONASIAN for n in names]
display_names = [n.replace('_', ' ') for n in names]

bars = ax_bar.barh(display_names, scores, color=colors, edgecolor='white', linewidth=1.2,
                   height=0.72)
# Score labels at end of each bar
for bar, score in zip(bars, scores):
    ax_bar.text(bar.get_width() + 0.014,
                bar.get_y() + bar.get_height()/2,
                f'{score:.2f}',
                va='center', fontsize=9.5, color='#222',
                fontweight='semibold')

ax_bar.set_xlim(0, 1.0)
ax_bar.set_xlabel('Residual bridge score', fontsize=10, color='#333')
ax_bar.set_title('Top 10 bridge cuisines',
                 fontsize=12, fontweight='bold', color='#111', loc='left', pad=14)
ax_bar.set_axisbelow(True)
ax_bar.grid(axis='x', linestyle=':', color='#bbb', alpha=0.7)
for spine in ('top', 'right'):
    ax_bar.spines[spine].set_visible(False)
ax_bar.spines['left'].set_color('#aaa')
ax_bar.spines['bottom'].set_color('#aaa')
ax_bar.tick_params(colors='#444')

# Highlight the Filipino entry — describe its structural role (Pacific-archipelagic anchor)
# rather than framing it as the regional-balance outlier.
for i, n in enumerate(names):
    if n == 'Filipino':
        ax_bar.text(scores[i] + 0.10,
                    i,
                    '← Pacific-archipelagic\n   anchor',
                    va='center', ha='left', fontsize=8.5,
                    color=COLOR_ASIAN, style='italic',
                    fontweight='semibold')

# Bottom caveat
fig.text(0.84, 0.07,
         'Bridge score is a spatial-network position,\n'
         'not a causal identity. After distance is modeled,\n'
         'these cuisines participate in multiple\n'
         'unexpectedly strong residual links.',
         ha='center', va='top', fontsize=8.5, color='#444', style='italic')

# Save
out = '/home/claude/v4/figures/05_bridge_index_map_and_chart.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
print(f"Size: {os.path.getsize(out)} bytes")

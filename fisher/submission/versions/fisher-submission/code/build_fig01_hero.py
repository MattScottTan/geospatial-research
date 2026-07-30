"""
Improved hero figure: residual culinary corridors on a real world basemap.
Uses Robinson projection + Natural Earth land/ocean/coastline.
Great-circle interpolation for residual links (not straight lat/long lines).
"""
import sys
sys.path.insert(0, '/home/claude/v4')
import figdata as D

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import numpy as np

NE = '/home/claude/ne_repo'

# ----- styling -----
LAND_COLOR    = '#f3e8ce'
OCEAN_COLOR   = '#d3e3ec'
COAST_COLOR   = '#5d6770'
BORDER_COLOR  = '#a9b3bd'

ASIA_BLUE     = '#1f5fa3'
GLOBAL_ORANGE = '#c45a2e'
ANCHOR_FILL   = '#2d2d2d'
ANCHOR_EDGE   = 'white'

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
})

fig = plt.figure(figsize=(15, 8.5), facecolor='white')
ax = plt.axes([0.02, 0.10, 0.96, 0.78], projection=ccrs.Robinson(central_longitude=20))
ax.set_global()

# Basemap
land  = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_land.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=LAND_COLOR, edgecolor='none')
ocean = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_ocean.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=OCEAN_COLOR, edgecolor='none')
coast = ShapelyFeature(Reader(f'{NE}/110m_physical/ne_110m_coastline.shp').geometries(),
                       ccrs.PlateCarree(), facecolor='none', edgecolor=COAST_COLOR, linewidth=0.4)
borders = ShapelyFeature(Reader(f'{NE}/110m_cultural/ne_110m_admin_0_countries.shp').geometries(),
                         ccrs.PlateCarree(), facecolor='none', edgecolor=BORDER_COLOR, linewidth=0.25)

ax.add_feature(ocean)
ax.add_feature(land)
ax.add_feature(borders)
ax.add_feature(coast)

# subtle graticule for spatial orientation
gl = ax.gridlines(draw_labels=False, linewidth=0.3, color='#aab4be',
                  alpha=0.5, linestyle=':',
                  xlocs=range(-180, 181, 30), ylocs=range(-60, 91, 30))

# ---- draw residual links as great circles ----
# E/SE Asia focused case (blue)
for a, b, r, _typ in D.FOCUSED_LINKS:
    lat_a, lon_a = D.ANCHORS[a]
    lat_b, lon_b = D.ANCHORS[b]
    ax.plot([lon_a, lon_b], [lat_a, lat_b],
            color=ASIA_BLUE,
            linewidth=1.0 + 12 * r,
            alpha=0.85,
            transform=ccrs.Geodetic(),
            zorder=4,
            solid_capstyle='round')

# Long-distance residual outliers from method figure (orange, narrower)
for a, b in D.LONG_DISTANCE_OUTLIERS:
    lat_a, lon_a = D.ANCHORS[a]
    lat_b, lon_b = D.ANCHORS[b]
    ax.plot([lon_a, lon_b], [lat_a, lat_b],
            color=GLOBAL_ORANGE,
            linewidth=1.4,
            alpha=0.75,
            transform=ccrs.Geodetic(),
            zorder=3,
            solid_capstyle='round',
            linestyle='-')

# ---- draw cuisine anchors ----
for name, (lat, lon) in D.ANCHORS.items():
    if name in ('Anchor_A','Anchor_B'):
        # additional corpus anchors with identity less certain — render as
        # smaller open circles so the corpus footprint is honest
        ax.plot(lon, lat, 'o',
                markerfacecolor='white',
                markeredgecolor='#666',
                markersize=4.0,
                markeredgewidth=0.9,
                transform=ccrs.PlateCarree(),
                zorder=5,
                alpha=0.8)
    else:
        ax.plot(lon, lat, 'o',
                markerfacecolor=ANCHOR_FILL,
                markeredgecolor=ANCHOR_EDGE,
                markersize=5.4,
                markeredgewidth=1.0,
                transform=ccrs.PlateCarree(),
                zorder=6)

# ---- label anchors (skip the unidentified Anchor_A/B) ----
LABEL_OFFSETS = {  # (dx, dy, ha)
    'Chinese':      ( -3,  4, 'right'),
    'Japanese':     (  4,  0, 'left'),
    'Korean':       (  0,  5, 'center'),
    'Thai':         ( -3, -2, 'right'),
    'Vietnamese':   ( -3, -5, 'right'),
    'Filipino':     (  4,  0, 'left'),
    'Russian':      (  0,  5, 'center'),
    'French':       ( -2, -4, 'right'),
    'Spanish':      ( -3, -3, 'right'),
    'British':      ( -3,  4, 'right'),
    'Irish':        ( -3, -3, 'right'),
    'Italian':      (  3, -3, 'left'),
    'Greek':        (  3,  3, 'left'),
    'Southern_US':  (  3,  3, 'left'),
    'Cajun_Creole': ( -3,  -1, 'right'),
    'Mexican':      (  0, -5, 'center'),
    'Jamaican':     (  3, -3, 'left'),
    'Brazilian':    (  3,  0, 'left'),
}

import matplotlib.patheffects as pe
TEXT_STROKE = [pe.withStroke(linewidth=2.5, foreground='white')]

for name, (lat, lon) in D.ANCHORS.items():
    if name in ('Anchor_A','Anchor_B'):
        continue
    dx, dy, ha = LABEL_OFFSETS.get(name, (3, 0, 'left'))
    label = name.replace('_', ' ')
    ax.text(lon + dx, lat + dy, label,
            fontsize=8.8, ha=ha, va='center',
            color='#111',
            transform=ccrs.PlateCarree(),
            zorder=7,
            fontweight='semibold',
            path_effects=TEXT_STROKE)

# ---- title ----
fig.text(0.5, 0.94,
         'Culinary Corridors: candidate residual food-similarity links across the corpus',
         ha='center', va='center',
         fontsize=16, fontweight='bold', color='#111')
fig.text(0.5, 0.905,
         'Cuisine pairs more similar than geographic distance alone predicts, drawn as great-circle links',
         ha='center', va='center',
         fontsize=11, color='#444', style='italic')

# ---- legend ----
legend_x = 0.03
legend_y = 0.04
ax_leg = fig.add_axes([legend_x, legend_y, 0.55, 0.07])
ax_leg.axis('off')
ax_leg.set_xlim(0, 1); ax_leg.set_ylim(0, 1)

# Asia line sample
ax_leg.plot([0.02, 0.10], [0.78, 0.78], color=ASIA_BLUE, linewidth=4.5, solid_capstyle='round')
ax_leg.text(0.115, 0.78, 'East/Southeast Asia focused-case links',
            fontsize=10, va='center', color='#222')
ax_leg.text(0.115, 0.50, 'Line width ∝ residual strength',
            fontsize=8.5, va='center', color='#666', style='italic')

# Orange line sample
ax_leg.plot([0.02, 0.10], [0.18, 0.18], color=GLOBAL_ORANGE, linewidth=2, solid_capstyle='round')
ax_leg.text(0.115, 0.18, 'Long-distance residual outliers from the global model',
            fontsize=10, va='center', color='#222')

# Anchor samples (push to the right so they don't collide)
ax_leg.plot([0.70], [0.78], 'o',
            markerfacecolor=ANCHOR_FILL,
            markeredgecolor=ANCHOR_EDGE,
            markersize=5.4, markeredgewidth=1.0)
ax_leg.text(0.725, 0.78, 'Labeled cuisine anchor',
            fontsize=10, va='center', color='#222')

ax_leg.plot([0.70], [0.18], 'o',
            markerfacecolor='white',
            markeredgecolor='#666',
            markersize=4.0, markeredgewidth=0.9)
ax_leg.text(0.725, 0.18, 'Additional corpus anchor (less certain)',
            fontsize=10, va='center', color='#222')

# ---- corpus-coverage caveat box ----
caveat_text = (
    "Corpus-coverage note. The map's coverage reflects the cuisine-labeled\n"
    "recipe corpus, not world food geography. Large regions (most of Africa,\n"
    "most of South Asia, the Middle East, Oceania) are absent because the\n"
    "corpus does not contain enough labeled cuisines there. Residual links\n"
    "are candidate spatial associations — not proven trade, migration,\n"
    "colonial, or maritime routes."
)
fig.text(0.99, 0.05, caveat_text,
         ha='right', va='bottom',
         fontsize=8, color='#333',
         bbox=dict(facecolor='white', edgecolor='#cccccc',
                   boxstyle='round,pad=0.5', alpha=0.94))

# Save
out = '/home/claude/v4/figures/01_hero_world_corridors.png'
import os
os.makedirs(os.path.dirname(out), exist_ok=True)
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
print(f"Size: {os.path.getsize(out)} bytes")

"""
Improved primary case figure: East/Southeast Asia residual cuisine links
shown on a real regional basemap with country fills and coastlines.
Width encodes residual strength; color encodes spatial link type.
"""
import sys, os
sys.path.insert(0, '/home/claude/v4')
import figdata as D

import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

NE = '/home/claude/ne_repo'
TEXT_STROKE = [pe.withStroke(linewidth=2.6, foreground='white')]

# styling
LAND  = '#f3e8ce'
OCEAN = '#cfdfe9'
COAST = '#3f4a55'
BORDER = '#8e98a3'

LINK_COLORS = {
    'mainland_adjacency': '#1f5fa3',
    'regional_proximity': '#2c8caf',
    'island_maritime':    '#9c4a99',
}
LINK_LABELS = {
    'mainland_adjacency': 'Mainland adjacency',
    'regional_proximity': 'Regional proximity',
    'island_maritime':    'Island / maritime',
}

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})

fig = plt.figure(figsize=(13.5, 9), facecolor='white')
ax = plt.axes([0.03, 0.10, 0.72, 0.82],
              projection=ccrs.PlateCarree())
ax.set_extent([93, 145, 4, 50], crs=ccrs.PlateCarree())

# Use 50m resolution for nicer regional detail
land  = ShapelyFeature(Reader(f'{NE}/50m_physical/ne_50m_land.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=LAND, edgecolor='none')
ocean = ShapelyFeature(Reader(f'{NE}/50m_physical/ne_50m_ocean.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=OCEAN, edgecolor='none')
coast = ShapelyFeature(Reader(f'{NE}/50m_physical/ne_50m_coastline.shp').geometries(),
                       ccrs.PlateCarree(), facecolor='none', edgecolor=COAST, linewidth=0.5)
borders = ShapelyFeature(Reader(f'{NE}/50m_cultural/ne_50m_admin_0_countries.shp').geometries(),
                         ccrs.PlateCarree(), facecolor='none', edgecolor=BORDER, linewidth=0.4,
                         linestyle='-')
rivers = ShapelyFeature(Reader(f'{NE}/50m_physical/ne_50m_rivers_lake_centerlines.shp').geometries(),
                        ccrs.PlateCarree(), facecolor='none', edgecolor='#9eb4c4', linewidth=0.4)
lakes = ShapelyFeature(Reader(f'{NE}/50m_physical/ne_50m_lakes.shp').geometries(),
                       ccrs.PlateCarree(), facecolor=OCEAN, edgecolor=COAST, linewidth=0.3)

ax.add_feature(ocean)
ax.add_feature(land)
ax.add_feature(rivers)
ax.add_feature(lakes)
ax.add_feature(borders)
ax.add_feature(coast)

gl = ax.gridlines(draw_labels=True, linewidth=0.3, color='#9eb4c4',
                  alpha=0.5, linestyle=':',
                  xlocs=range(95, 145, 10), ylocs=range(0, 51, 10))
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 8, 'color': '#666'}
gl.ylabel_style = {'size': 8, 'color': '#666'}

# subset the cuisines we care about
ESEA = ['Chinese', 'Japanese', 'Korean', 'Thai', 'Vietnamese', 'Filipino']

# draw links
for a, b, r, link_type in D.FOCUSED_LINKS:
    lat_a, lon_a = D.ANCHORS[a]
    lat_b, lon_b = D.ANCHORS[b]
    ax.plot([lon_a, lon_b], [lat_a, lat_b],
            color=LINK_COLORS[link_type],
            linewidth=1.2 + 14 * r,
            alpha=0.80,
            transform=ccrs.Geodetic(),
            zorder=4,
            solid_capstyle='round')
    # Place a tiny residual value annotation along the line midpoint
    mid_lon = (lon_a + lon_b) / 2
    mid_lat = (lat_a + lat_b) / 2 + 0.5
    if r >= 0.20:  # only label the strongest
        ax.text(mid_lon, mid_lat, f'r={r:.2f}',
                fontsize=8, ha='center', va='bottom',
                color='#222', alpha=0.85,
                transform=ccrs.PlateCarree(),
                path_effects=TEXT_STROKE,
                zorder=5)

# draw anchors
for name in ESEA:
    lat, lon = D.ANCHORS[name]
    ax.plot(lon, lat, 'o',
            markerfacecolor='#1d1d1d',
            markeredgecolor='white',
            markersize=8,
            markeredgewidth=1.4,
            transform=ccrs.PlateCarree(),
            zorder=6)

# label anchors
LABEL_OFFSETS_RG = {
    'Chinese':    ( -1.5,  1.0, 'right'),
    'Japanese':   (  1.5,  0.0, 'left'),
    'Korean':     (  1.5,  1.5, 'left'),
    'Thai':       ( -1.5,  0.5, 'right'),
    'Vietnamese': (  1.5,  -1.5, 'left'),
    'Filipino':   (  1.5,  0.0, 'left'),
}
for name in ESEA:
    lat, lon = D.ANCHORS[name]
    dx, dy, ha = LABEL_OFFSETS_RG.get(name, (1.5, 0, 'left'))
    ax.text(lon + dx, lat + dy, name,
            fontsize=12, fontweight='bold',
            ha=ha, va='center', color='#111',
            transform=ccrs.PlateCarree(),
            zorder=7,
            path_effects=TEXT_STROKE)

# inline geographical context labels (greyed)
context_labels = [
    (104, 32, 'CHINA'),
    (138, 39, 'JAPAN'),
    (128, 40, 'KOREA'),
    (105, 17, 'INDOCHINA'),
    (118, 11, 'PHILIPPINES'),
    (115, 19, 'South China\nSea'),
    (130, 36, 'Sea of\nJapan'),
]
for lon, lat, txt in context_labels:
    ax.text(lon, lat, txt,
            fontsize=8.5,
            color='#5a6470',
            ha='center', va='center',
            transform=ccrs.PlateCarree(),
            alpha=0.85,
            style='italic' if txt.endswith('Sea') or 'Japan' in txt and len(txt) > 6 else 'normal',
            zorder=2,
            path_effects=[pe.withStroke(linewidth=2.5, foreground='white')])

# Title
fig.text(0.5, 0.96,
         'East/Southeast Asia: residual cuisine links over regional geography',
         ha='center', va='center',
         fontsize=15.5, fontweight='bold', color='#111')
fig.text(0.5, 0.925,
         'The strongest focused-case residuals — pairs more similar than distance alone predicts',
         ha='center', va='center',
         fontsize=11, color='#444', style='italic')

# Right-side panel: legend + ranking
ax_panel = fig.add_axes([0.78, 0.14, 0.20, 0.74])
ax_panel.axis('off')
ax_panel.set_xlim(0, 1); ax_panel.set_ylim(0, 1)

ax_panel.text(0.0, 0.97, 'Reading the map',
              fontsize=12, fontweight='bold', color='#111', va='top')

# Link type legend
y = 0.88
ax_panel.text(0.0, y, 'Link type', fontsize=10, fontweight='semibold', color='#222', va='top')
y -= 0.05
for typ, label in LINK_LABELS.items():
    ax_panel.plot([0.02, 0.16], [y, y], color=LINK_COLORS[typ],
                  linewidth=4, solid_capstyle='round')
    ax_panel.text(0.20, y, label, fontsize=9.5, va='center', color='#222')
    y -= 0.05

# Width reading
y -= 0.02
ax_panel.text(0.0, y, 'Line width ∝ residual strength', fontsize=8.5, va='top',
              color='#666', style='italic')
y -= 0.04
ax_panel.text(0.0, y,
              'residual = observed similarity\n           − predicted from distance',
              fontsize=8.5, va='top', color='#666', style='italic',
              family='monospace')

# Top residual links table
y -= 0.13
ax_panel.text(0.0, y, 'Top residual links', fontsize=10, fontweight='semibold',
              color='#222', va='top')
y -= 0.05
top_links = sorted(D.FOCUSED_LINKS, key=lambda t: -t[2])[:5]
for i, (a, b, r, _typ) in enumerate(top_links, 1):
    ax_panel.text(0.0, y, f'{i}.', fontsize=9.5, color='#444', va='top', fontweight='bold')
    ax_panel.text(0.07, y, f'{a}–{b}',
                  fontsize=9.5, color='#222', va='top')
    ax_panel.text(1.0, y, f'r = {r:.2f}',
                  fontsize=9.5, color='#222', va='top', ha='right',
                  family='monospace')
    y -= 0.045

# Caveat
y -= 0.04
ax_panel.text(0.0, y,
              'Strongest focused inference case;\n'
              'still non-causal. Residual links are\n'
              'spatial associations, not proven\n'
              'historical routes.',
              fontsize=8.5, va='top', color='#444', style='italic')

# Save
out = '/home/claude/v4/figures/03_primary_case_regional_map.png'
plt.savefig(out, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved {out}")
print(f"Size: {os.path.getsize(out)} bytes")

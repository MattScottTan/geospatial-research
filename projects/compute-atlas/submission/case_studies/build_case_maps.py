from __future__ import annotations

from pathlib import Path
import json

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import Point, Polygon
from pyproj import Geod

ROOT = Path('/mnt/data/submission_workspace/AI_Compute_Accessibility_Atlas_Full')
OUT = ROOT / 'final_submission' / 'case_studies'
GEOD = Geod(ellps='WGS84')

CITY_CFG = {
    'singapore': {'city': 'Singapore', 'country': 'Singapore', 'radius_km': 2000, 'rings': [250, 500, 1000]},
    'seoul': {'city': 'Seoul', 'country': 'Korea, South', 'radius_km': 2000, 'rings': [250, 500, 1000]},
    'ho_chi_minh_city': {'city': 'Ho Chi Minh City', 'country': 'Vietnam', 'radius_km': 2500, 'rings': [500, 1000, 1500]},
    'lagos': {'city': 'Lagos', 'country': 'Nigeria', 'radius_km': 4500, 'rings': [1000, 2000, 4000]},
}


def geodesic_circle(lon, lat, radius_km, n=180):
    az = np.linspace(0, 360, n)
    pts = [GEOD.fwd(lon, lat, a, radius_km * 1000)[:2] for a in az]
    return Polygon(pts)


def load():
    metrics = pd.read_csv(ROOT / 'outputs/tables/city_access_metrics.csv')
    ai = pd.read_csv(ROOT / 'outputs/tables/city_access_ai.csv')
    inst = pd.read_csv(ROOT / 'outputs/tables/openalex_institutions_top.csv')
    bundle = pd.read_csv(ROOT / 'final_submission/originality/final/bundle_city_scores.csv')
    priority = pd.read_csv(ROOT / 'outputs/tables/priority_cities.csv')
    regions = gpd.read_file(ROOT / 'data/processed/cloud_regions.gpkg')
    world = gpd.read_file(ROOT / 'data/raw/ne_110m_admin_0_countries.geojson')
    return metrics, ai, inst, bundle, priority, regions, world


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0088
    lat1 = np.radians(lat1); lon1=np.radians(lon1); lat2=np.radians(lat2); lon2=np.radians(lon2)
    dlat=lat2-lat1; dlon=lon2-lon1
    a=np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2*R*np.arcsin(np.sqrt(a))


def classify_level(value, breaks):
    for label, cond in breaks:
        if cond(value):
            return label
    return 'mixed'


def make_maps_and_scorecards():
    metrics, ai, inst, bundle, priority, regions, world = load()
    cross_rows = []
    for key, cfg in CITY_CFG.items():
        city = cfg['city']; country = cfg['country']
        city_dir = OUT / key
        reg_dir = city_dir / 'regional_context'; loc_dir = city_dir / 'local_ecosystem'
        reg_dir.mkdir(parents=True, exist_ok=True); loc_dir.mkdir(parents=True, exist_ok=True)
        m = metrics[(metrics['city']==city) & (metrics['country']==country)].iloc[0]
        b = bundle[(bundle['city']==city) & (bundle['country']==country)].iloc[0]
        a = ai[(ai['city']==city) & (ai['country']==country)]
        a_works = int(a['openalex_ai_works_recent'].iloc[0]) if len(a) else 0
        a_inst = int(a['openalex_ai_institution_count'].iloc[0]) if len(a) else 0
        city_pt = Point(m['lng'], m['lat'])

        regions = regions.copy()
        regions['dist_to_city'] = haversine(m['lat'], m['lng'], regions['lat'].to_numpy(), regions['lon'].to_numpy())
        near_regions = regions[regions['dist_to_city'] <= cfg['radius_km']].copy().sort_values('dist_to_city')

        # Regional context map
        ring_geoms = gpd.GeoDataFrame({'ring_km':cfg['rings']}, geometry=[geodesic_circle(m['lng'], m['lat'], r) for r in cfg['rings']], crs='EPSG:4326')
        extent_geom = geodesic_circle(m['lng'], m['lat'], cfg['radius_km'])
        bbox = extent_geom.bounds
        world_clip = world.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
        fig, ax = plt.subplots(figsize=(10.8, 7.2))
        world_clip.plot(ax=ax, color='#f4f4f4', edgecolor='#bdbdbd', linewidth=0.5)
        ring_geoms.boundary.plot(ax=ax, color='#c7c7c7', linewidth=0.8, linestyle='--')
        # provider colors without hard-coding too many aesthetics? acceptable in code for saved figs.
        provider_colors = {'aws':'#1f77b4','azure':'#2ca02c','gcp':'#d62728'}
        for provider, sub in near_regions.groupby('provider'):
            ax.scatter(sub['lon'], sub['lat'], s=30, color=provider_colors.get(provider,'#555555'), alpha=0.85, label=provider.upper())
        ax.scatter([m['lng']], [m['lat']], marker='*', s=260, color='black', edgecolor='white', linewidth=0.6, zorder=5)
        # label the nearest region per provider to reduce clutter
        label_rows = near_regions.sort_values('dist_to_city').groupby('provider', as_index=False).first()
        offsets = [(8,6),(8,-10),(-70,8),(-70,-12)]
        for (__, r), (dx, dy) in zip(label_rows.iterrows(), offsets):
            ax.annotate(r['location_name'], (r['lon'], r['lat']), xytext=(dx, dy), textcoords='offset points', fontsize=8.5,
                        bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.75), alpha=0.95)
        ax.annotate(city, (m['lng'], m['lat']), xytext=(8,8), textcoords='offset points', fontsize=10, weight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.75))
        ax.set_title(f'{city}: Regional Context', fontsize=15, weight='bold')
        subtitle = f"Nearest region {m['dist_km_nearest_region']:.1f} km away | providers within 1000 km: {int(b['providers_within_1000'])}"
        ax.text(0.02, 0.93, subtitle, transform=ax.transAxes, fontsize=10,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='#cccccc', alpha=0.9))
        ax.legend(loc='upper right', frameon=True, fontsize=9, facecolor='white', framealpha=0.9)
        ax.set_xlim(bbox[0], bbox[2]); ax.set_ylim(bbox[1], bbox[3]); ax.set_axis_off(); fig.tight_layout()
        regional_png = reg_dir / f'{key}_regional_context.png'
        fig.savefig(regional_png, dpi=220, bbox_inches='tight'); plt.close(fig)
        (reg_dir / 'map_spec.json').write_text(json.dumps({'city':city,'country':country,'radius_km':cfg['radius_km'],'rings':cfg['rings']}, indent=2))

        # Local ecosystem map
        local_inst = inst[(inst['geo_city']==city) & (inst['geo_country_code']==m['iso2'])].copy()
        if len(local_inst) == 0:
            local_inst = inst[inst['geo_city']==city].copy()
        fig, ax = plt.subplots(figsize=(8.4, 7.2))
        ax.scatter([m['lng']], [m['lat']], marker='*', s=260, color='black', edgecolor='white', linewidth=0.6, zorder=5, label='City anchor')
        if len(local_inst):
            sizes = np.clip(np.sqrt(local_inst['ai_works_count_recent'].fillna(1))*12, 40, 220)
            ax.scatter(local_inst['geo_lon'], local_inst['geo_lat'], s=sizes, color='#1f77b4', alpha=0.75, label='Top institution anchors')
            label_inst = local_inst.sort_values('ai_works_count_recent', ascending=False).head(3)
            offsets_local = [(8,6),(8,-10),(-70,8)]
            for (__, r), (dx, dy) in zip(label_inst.iterrows(), offsets_local):
                ax.annotate(r['institution_name'], (r['geo_lon'], r['geo_lat']), xytext=(dx, dy), textcoords='offset points', fontsize=8.5,
                            bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.75), alpha=0.95)
        else:
            ax.text(0.5, 0.52, 'No top-institution anchors\nin delivered subset', transform=ax.transAxes, ha='center', va='center', fontsize=11,
                    bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='#999999'))
        ax.annotate(city, (m['lng'], m['lat']), xytext=(8,8), textcoords='offset points', fontsize=10, weight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.75))
        ax.set_title(f'{city}: Local Ecosystem', fontsize=15, weight='bold')
        note = f"Bundle score {b['bundle_score']:.1f} | top-institution anchors {int(b['top_inst_count'])} | AI works {a_works}"
        ax.text(0.02, 0.93, note, transform=ax.transAxes, fontsize=10,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec='#cccccc', alpha=0.9))
        # local extent
        pts_lon = [m['lng']] + list(local_inst['geo_lon']) if len(local_inst) else [m['lng']]
        pts_lat = [m['lat']] + list(local_inst['geo_lat']) if len(local_inst) else [m['lat']]
        xpad = max(0.25, (max(pts_lon)-min(pts_lon))*1.5 if len(pts_lon)>1 else 0.25)
        ypad = max(0.20, (max(pts_lat)-min(pts_lat))*1.5 if len(pts_lat)>1 else 0.20)
        ax.set_xlim(min(pts_lon)-xpad, max(pts_lon)+xpad)
        ax.set_ylim(min(pts_lat)-ypad, max(pts_lat)+ypad)
        ax.grid(alpha=0.2, linestyle=':')
        ax.legend(loc='upper right', frameon=True, fontsize=9, facecolor='white', framealpha=0.9)
        fig.tight_layout()
        local_png = loc_dir / f'{key}_local_ecosystem.png'
        fig.savefig(local_png, dpi=220, bbox_inches='tight'); plt.close(fig)
        (loc_dir / 'map_spec.json').write_text(json.dumps({'city':city,'country':country,'local_institution_count':int(len(local_inst))}, indent=2))

        # scorecard
        compute_label = classify_level(float(m['dist_km_nearest_region']), [
            ('very strong', lambda v: v <= 50),
            ('strong', lambda v: v <= 250),
            ('mixed', lambda v: v <= 1000),
            ('weak', lambda v: True),
        ])
        conn_label = classify_level(int(b['providers_within_1000']), [
            ('very strong', lambda v: v >= 3),
            ('strong', lambda v: v == 2),
            ('mixed', lambda v: v == 1),
            ('weak', lambda v: v == 0),
        ])
        inst_label = classify_level(int(b['top_inst_count']), [
            ('strong', lambda v: v >= 3),
            ('mixed', lambda v: v >= 1),
            ('weak', lambda v: v == 0),
        ])
        infra_label = classify_level(float(b['bundle_score']), [
            ('very strong', lambda v: v >= 80),
            ('strong', lambda v: v >= 65),
            ('mixed', lambda v: v >= 45),
            ('weak', lambda v: True),
        ])
        if city == 'Singapore':
            policy_line = 'Alignment benchmark: shows what a fully reinforced compute-opportunity bundle looks like.'
            takeaway = 'Singapore aligns compute access, redundancy, institutional depth, and city-scale opportunity.'
            quadrant = 'near compute / high AI'
        elif city == 'Seoul':
            policy_line = 'Overlay-limit case: useful for explaining why research output is not the whole AI economy.'
            takeaway = 'Seoul is compute-rich but comparatively quiet in the delivered overlay, making it a strong exception case.'
            quadrant = 'near compute / low AI'
        elif city == 'Ho Chi Minh City':
            policy_line = 'Offsetting-factors case: use to show that weaker compute proximity does not eliminate AI momentum.'
            takeaway = 'Ho Chi Minh City outperforms what distance alone would predict.'
            quadrant = 'far compute / high AI'
        else:
            policy_line = 'Priority-city case: the public-interest example of stacked infrastructure disadvantage.'
            takeaway = 'Lagos combines large urban scale with weak compute proximity and no observed works in the delivered overlay.'
            quadrant = 'far compute / low AI'
        scorecard = f'''# {city} Scorecard

- **Quadrant:** {quadrant}
- **Compute access:** {compute_label} ({m['dist_km_nearest_region']:.1f} km to nearest region)
- **Connectivity / provider diversity:** {conn_label} ({int(b['providers_within_1000'])} providers within 1,000 km; {int(b['regions_within_1500'])} regions within 1,500 km)
- **Institutions:** {inst_label} ({int(b['top_inst_count'])} top-institution anchors; {int(b['top_inst_ai_works'])} recent AI works in anchor institutions)
- **Infrastructure bundle:** {infra_label} (bundle score {b['bundle_score']:.1f})
- **Policy / interpretive role:** {policy_line}
- **Takeaway:** {takeaway}
'''
        (city_dir / 'scorecard.md').write_text(scorecard)

        cross_rows.append({
            'city': city,
            'country': country,
            'quadrant': quadrant,
            'dist_km_nearest_region': round(float(m['dist_km_nearest_region']),1),
            'bundle_score': round(float(b['bundle_score']),1),
            'providers_within_1000': int(b['providers_within_1000']),
            'regions_within_1500': int(b['regions_within_1500']),
            'top_inst_count': int(b['top_inst_count']),
            'top_inst_ai_works': int(b['top_inst_ai_works']),
            'recent_ai_works_overlay': a_works,
            'population': int(m['population']),
            'takeaway': takeaway,
        })

    pd.DataFrame(cross_rows).to_csv(OUT / 'cross_case_table.csv', index=False)


if __name__ == '__main__':
    make_maps_and_scorecards()

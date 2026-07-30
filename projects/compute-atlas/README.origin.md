# AI Compute Accessibility Atlas (Project #1)

This repository builds a **global, city-level atlas** of:

1) **Compute accessibility** — *physical proximity* from cities to the nearest hyperscaler **cloud region** (AWS / Azure / Google Cloud), measured in **kilometers**.

2) **AI research activity** — city-level counts of AI-related scholarly works from **OpenAlex**, using the topic filter and overlay files you provided.

It then analyzes how these two spatial layers relate, using **two spatial-statistical model tracks**:

- **Model 1 (B+D):** interpretable driver regression + **Gaussian Process (Matérn) residual field**
- **Model 2 (C+D):** interpretable driver regression + **CAR / GMRF spatial random effect** on a kNN city graph

The output is a **PDF atlas**, reproducible code, and GIS exports (GeoPackage / GeoJSON / GeoTIFF).

---

## Repository layout

- `src/`
  - `pipeline.py` — end-to-end data processing, models, rasters, and figures
- `data/raw/`
  - `worldcities.csv` — global cities dataset (CC-BY-4.0)
  - `cloud_regions_*.csv` — region coordinate lists (AWS/Azure/GCP) (ODbL-derived)
  - `openalex_ai_city_overlay.csv` — **provided by you**
  - `openalex_ai_institutions_top.csv` — **provided by you**
  - `openalex_topics_used.json` — **provided by you**
  - `ne_110m_admin_0_countries.geojson` — Natural Earth base map (public domain)
- `data/processed/`
  - `cities.gpkg`, `cloud_regions.gpkg`
- `outputs/`
  - `figures/` — PNGs used in the report
  - `tables/` — CSV + JSON summaries
  - `gis/` — GeoPackage, GeoJSON, GeoTIFF rasters
- `report/`
  - `main.tex` + `figures/` + `tables/` — LaTeX sources
- `deliverables/`
  - `ai_compute_accessibility_atlas.pdf`

---

## Quickstart (cross-platform)

### 1) Create and activate a virtual environment

#### Windows (PowerShell)
If you see: **"running scripts is disabled on this system"** when activating, you have two options:

**Option A (recommended): enable local script activation for your user**
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then activate:
```powershell
.\.venv\Scripts\Activate.ps1
```

**Option B: use CMD activation (no execution-policy changes)**
Open `cmd.exe` and run:
```bat
.\.venv\Scripts\activate.bat
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

> **Windows note (geospatial stack):**
> This repo uses the `pyogrio` GeoPandas I/O backend so the geospatial stack stays wheel-backed on current Windows Python releases.
> If pip fails, use **conda** instead:
> ```bash
> conda create -n aiaccess python=3.11 -y
> conda activate aiaccess
> conda install -c conda-forge geopandas rasterio shapely pyproj pyogrio -y
> pip install -r requirements.txt
> ```

### 3) Run the full pipeline

From the repo root:
```bash
python src/pipeline.py all
```

This will create:
- processed datasets in `data/processed/`
- tables in `outputs/tables/`
- GIS layers in `outputs/gis/`
- figures in `outputs/figures/` and `report/figures/`

### 4) Build the PDF report

You need a LaTeX distribution with `latexmk`:
- Windows: MiKTeX
- macOS: MacTeX
- Linux: TeX Live

Then:
```bash
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final PDF will be at:
- `report/main.pdf`
- (and copied into) `deliverables/ai_compute_accessibility_atlas.pdf`

---

## Rebuilding / modifying the OpenAlex overlay

This repo expects you to provide these files (already included here):
- `data/raw/openalex_ai_city_overlay.csv`
- `data/raw/openalex_ai_institutions_top.csv`
- `data/raw/openalex_topics_used.json`

If you want to regenerate them:
1) Use your OpenAlex script / workflow
2) Copy the outputs into `data/raw/`
3) Re-run:
```bash
python src/pipeline.py openalex
python src/pipeline.py model_gp
python src/pipeline.py model_car
python src/pipeline.py figures
```

---

## Key outputs (GIS)

- `outputs/gis/ai_access_cities.gpkg` — cities + distance + access score + nearest region
- `outputs/gis/ai_access_ai_cities.gpkg` — OpenAlex overlay joined to cities + access metrics
- `outputs/gis/ai_access_surface_distance.tif` — global raster distance-to-nearest-region (1° grid)
- `outputs/gis/ai_research_pred_gp.tif` — global raster predicted AI research (Model 1, 1° grid)
- `outputs/gis/ai_research_pred_car.tif` — global raster predicted AI research (Model 2 via IDW, 1° grid)

All rasters are EPSG:4326 (lat/lon).

---

## Data sources and licensing (high level)

- **OpenAlex overlay**: created by your script from OpenAlex (open catalog)
- **World cities**: `condwanaland/worldcities` (CC-BY-4.0; derived from SimpleMaps)
- **Cloud regions**: `dgl/cloud-regions` (derived from OpenStreetMap; ODbL)
- **Base map**: Natural Earth (public domain)

See `references/` for copied license text where available.

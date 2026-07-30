# Local Run and Submit Guide

This is the final local handoff guide for the EIP submission package.

## 1. What to read first

1. `report/main.pdf` — the authoritative final report
2. `final_submission/storymap/final_storymap_script.md` — the final StoryMap copy deck
3. `final_submission/notebooks/analysis_storymap_notebook.ipynb` — the full reproducible walkthrough in final submission order
4. `final_submission/notebooks/results_walkthrough.ipynb` — the shorter results walkthrough
5. `final_submission/storymap/arcgis_handoff.md` — the manual ArcGIS/StoryMaps steps

## 2. Local rerun sequence

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-extended.txt
python src/pipeline.py all
python final_submission/originality/build_prototypes.py
python final_submission/case_studies/build_case_maps.py
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd ..
```

### Windows note
Use PowerShell activation instead:

```powershell
.\.venv\Scripts\Activate.ps1
```

and use backslash paths when running commands if preferred.

## 3. Notebook order

Open these notebooks in this order:

1. `final_submission/notebooks/analysis_storymap_notebook.ipynb`
2. `final_submission/notebooks/results_walkthrough.ipynb`

The first notebook follows the full submission narrative. The second is the shorter guided walkthrough.

## 4. What to upload to ArcGIS Online later

Use the prepared packet under:

- `final_submission/storymap/upload_packet/layers/`
- `final_submission/storymap/upload_packet/images/`

Then follow:

- `final_submission/storymap/webmap_specs.md`
- `final_submission/storymap/arcgis_handoff.md`

## 5. What requires Harvard login

A Harvard ArcGIS Online / StoryMaps account is required for:
- hosted-layer upload
- web-map creation in Map Viewer
- StoryMap assembly and publication
- public-sharing configuration and signed-out QA

Everything else in this package can be completed locally.

## 6. Remaining manual inputs

Final public StoryMap publication still needs:
- submitter bio text
- submitter headshot

See `final_submission/storymap/bio_and_photo_requirements.md`.

## 7. What the final package contains

- authoritative report source and PDF
- full final_submission folder
- refreshed atlas outputs
- originality outputs
- four case-study modules
- StoryMap package and upload packet
- notebooks
- run, QA, and ArcGIS handoff instructions

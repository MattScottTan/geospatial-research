# ArcGIS Handoff

This file explains exactly what still requires manual ArcGIS Online / StoryMaps steps and whether a Harvard account should be sufficient.

## What can already be done locally

Everything in the local final package can be prepared without logging in:
- final report PDF
- StoryMap script
- captions and alt text
- upload packet of local media and layer files
- notebooks
- case-study maps
- originality figures
- source table and run instructions

## What requires ArcGIS Online login

A Harvard ArcGIS Online account should be sufficient for the following manual steps:
1. Upload `ai_access_cities.geojson`, `cities_with_hotspots.geojson`, `priority_cities.geojson`, and `cloud_regions.gpkg` as hosted layers.
2. Build the three required web maps:
   - `Global Compute Accessibility`
   - `AI Research and Hot Spots`
   - `AI Deserts and Priority Cities`
3. Create a new StoryMap and paste in the section copy from `final_storymap_script.md`.
4. Insert the required hosted maps and static images from `upload_packet/`.
5. Turn on public sharing and test the story signed out in an incognito window.

## Exact manual sequence

### Step 1 — Upload layers
- Go to ArcGIS Online > Content > My content > New item.
- Use the four layer files in `upload_packet/layers/`.
- Publish each as a hosted feature layer.
- Keep the titles exactly as listed in `webmap_specs.md` and the older upload guide.

### Step 2 — Assemble web maps
- Follow `webmap_specs.md`.
- Save the three maps into the same project folder.

### Step 3 — Create the StoryMap
- Open ArcGIS StoryMaps.
- Create a blank story.
- Use the title and subtitle from `final_storymap_script.md`.
- Follow the section order in that file exactly.
- Insert the hosted maps where the script calls for web maps.
- Insert static PNGs from `upload_packet/images/` everywhere else.

### Step 4 — QA before submission
- Test public sharing while signed out.
- Check desktop and mobile layout.
- Confirm every figure has the matching caption and alt text from `captions_and_alt_text.md`.
- Add bio and headshot once available.

## Login / entitlement notes

- **Harvard ArcGIS Online / StoryMaps:** required and expected for live assembly and publication.
- **Harvard ArcGIS Pro / CGA licensing:** not required for the current local package.
- **StreetMap Premium / Business Analyst:** not required for the current local package.

## If your Harvard login fails

Use the fully local package first:
- read the report PDF
- inspect the notebooks
- review the StoryMap script and upload packet

Then contact Harvard CGA / your AGOL administrator for StoryMaps access.

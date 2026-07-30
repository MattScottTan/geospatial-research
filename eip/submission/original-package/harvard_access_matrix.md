# Harvard Access / Login Matrix

Date: 2026-03-14 11:58 AM America/New_York

This matrix separates what can be completed entirely locally from what requires HarvardKey, ArcGIS Online/StoryMaps access, ArcGIS Pro/CGA-managed licensing, or other gated Harvard/CGA resources.

## Summary

- **Local only:** core atlas rerun, report rewrite/build, notebooks, most originality prototyping with public data, StoryMap script, captions/alt text, upload packet preparation, ZIP packaging.
- **Harvard login likely required:** final ArcGIS Online layer upload, web map assembly, StoryMap assembly/publication, any use of Harvard ArcGIS Online named-user services, and any licensed Esri add-ons tied to Harvard AGOL.
- **Harvard/CGA license or lab access may be required:** ArcGIS Pro named-user workflows, StreetMap Premium, Business Analyst Online/data, and any CGA-specific hosted resources not publicly downloadable.

## Step-by-step matrix

| Step / artifact | Can be completed locally? | Harvard / login required? | Likely tool / service | Fallback / note |
|---|---:|---:|---|---|
| Core atlas rerun (`python src/pipeline.py all`) | Yes | No | Local Python stack | Preferred default |
| LaTeX report build (`report/main.tex` -> PDF) | Yes | No | Local TeX distribution | Preferred default |
| Stage 4–6 reruns | Yes | No | Local Python stack + public APIs where scripted | Live data pulls may drift from frozen outputs |
| StoryMap script writing | Yes | No | Local markdown/text workflow | Preferred default |
| StoryMap asset manifest, alt text, upload packet | Yes | No | Local file prep | Preferred default |
| Exporting local PNG/PDF assets | Yes | No | Local Python/Matplotlib/LaTeX | Preferred default |
| ArcGIS Online layer upload | No | **Yes** | Harvard ArcGIS Online org | Manual user login step |
| ArcGIS Online web map assembly | No | **Yes** | ArcGIS Online Map Viewer | Manual user login step |
| ArcGIS StoryMaps assembly / publication | No | **Yes** | ArcGIS StoryMaps in Harvard AGOL | Manual user login step |
| Public share / signed-out QA in AGOL | Partly | **Yes** for publishing; no for public-view test | AGOL + browser | Requires manual publish/share configuration |
| ArcGIS Pro desktop workflows | Maybe | **Usually yes** | Harvard/CGA ArcGIS Pro named-user license | Use local Python / public GIS alternatives if unavailable |
| StreetMap Premium routing / network analysis | No, unless prelicensed | **Likely yes** | CGA Esri licensed data / ArcGIS Pro | Public road/network alternatives if needed |
| Business Analyst Online/data | No, unless already licensed | **Likely yes** | Harvard AGOL + BA entitlement | Replace with public demographic/economic proxies if needed |
| Living Atlas layers (public subset) | Often yes | Sometimes | ArcGIS Online / Living Atlas | Prefer public or exported layers when possible |
| Harvard Geospatial Library / CGA-managed resources | Maybe | Often | HGL / CGA distribution | Use public substitutes when sufficient |
| Geotweet Archive / other CGA-hosted special datasets | No by default | **Likely yes / request-based** | CGA-managed resource | Do not make critical path unless access is confirmed |

## Practical guidance for this submission

### Safe local-first path
Use local tools for:
- all baseline analysis reruns
- all originality prototyping that can be done from current repo + public data
- all report and notebook work
- all case-study map composition that can be exported locally
- all StoryMap writing and packaging docs

### Manual Harvard account steps to expect later
The user should expect to log in with a Harvard-affiliated ArcGIS Online account for:
1. uploading hosted layers
2. building web maps
3. assembling the StoryMap
4. setting public-sharing permissions
5. checking signed-out public access after publication

### High-value gated options
Use only if they materially improve originality and can be supported by the user’s Harvard account:
- ArcGIS Pro desktop-only analyses or layout exports
- StreetMap Premium / network-analysis workflows
- Business Analyst layers or services

### Recommendation
Treat Harvard/CGA-gated tools as **enhancements**, not as the single point of failure for the final package. Every critical submission artifact should still have a local-prep version and a manual-login handoff note.

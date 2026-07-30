# EIP Award Project Package — "Cloudy with a Chance of Compute"

## What This Package Contains

This is the complete planning and reference package for improving the **AI Compute Accessibility Atlas** project to win the Harvard CGA **Esri Innovation Program (EIP) Student of the Year Award**.

---

## Directory Structure

```
eip_project_package/
├── README.md                          ← You are here
├── worker_plan/
│   └── WORK.md                        ← THE MAIN DELIVERABLE: Worker agent execution plan
├── project_docs/
│   ├── AWARD_PLAYBOOK.md              ← Rubric, checklist, templates for EIP + Fisher
│   ├── WINNER_MATRIX.md               ← Analysis of 18 past EIP/Fisher winners
│   ├── SUBMISSION_GAP_ANALYSIS.md     ← Current project scored against rubric (3.95/5.00)
│   ├── REVISION_CHECKLIST.md          ← Section-by-section editing guide
│   ├── CONTINUATION_WORK.md           ← Prior session state and verified numbers
│   ├── SOURCES_CREDITS_TOOLS.md       ← Ready-to-paste Sources/Credits section
│   ├── HERO_MAP_INSTRUCTIONS.md       ← ArcGIS Online click-by-click for hero map
│   └── SPATIAL_STATS_ARCGIS_INSTRUCTIONS.md ← ArcGIS Pro instructions for Moran's I and Gi*
└── original_report/
    └── main.pdf                       ← Current project report (LaTeX-compiled PDF)
```

---

## How to Use This Package

### Step 1: Start with WORK.md
The file `worker_plan/WORK.md` is the master execution plan. It contains:
- **40+ atomic tasks** organized into 7 tracks (A through G)
- **A worker driver prompt** (Section 5) ready to paste into any Claude/agent session
- **Acceptance checks** (Section 2) that define what "done" looks like
- **Code snippets** for spatial statistics (Moran's I, Getis-Ord Gi*) and data preparation
- **Priority ordering** so the worker always knows what to do next

### Step 2: Give the worker agent the WORK.md + your project repo ZIP
The worker loop is:
1. Read WORK.md
2. Pick highest-priority unblocked task
3. Execute it
4. Update WORK.md (mark done, record results, add learnings)
5. Repeat

### Step 3: Reference the project_docs as needed
The project docs provide context the worker may need:
- **AWARD_PLAYBOOK.md** — What judges look for, weighted rubric, failure modes
- **WINNER_MATRIX.md** — What past winners did (6 detailed extractions)
- **SUBMISSION_GAP_ANALYSIS.md** — Where the project currently stands vs. winners
- **CONTINUATION_WORK.md** — Verified numbers, completed revisions, remaining work
- **REVISION_CHECKLIST.md** — Per-section editing instructions

---

## Key Deadlines
- **EIP Submission:** March 15, 2026, 11:59 PM EDT
- **Fisher Prize:** May 3, 2026

## Key Gaps to Close (from analysis)
1. **Esri technology is absent** — Must add ArcGIS-native spatial statistics + interactive StoryMap
2. **No StoryMap exists** — Must translate LaTeX report into ArcGIS StoryMap
3. **Policy impact undersold** — Must reframe around "AI deserts" and priority cities
4. **Cartography is matplotlib defaults** — Must rebuild all figures to professional standard
5. **References lack GIS literature** — Must add spatial accessibility and LISA citations

## Current Score: 3.95 / 5.00
- Framing: 5/5 (strong)
- Architecture: 4/5 (needs tightening)
- GIS/Cartography: 3/5 (biggest gap)
- Evidence/Analysis: 4/5 (needs Esri-native stats)
- Originality: 5/5 (strong)
- Packaging/Polish: 3/5 (no bio, no sources section, no custom theme)

**Target after improvements: 4.5+ / 5.00**

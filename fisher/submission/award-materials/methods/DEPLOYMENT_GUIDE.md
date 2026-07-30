# Deploying `bridges_interactive.html`

The interactive map is a single self-contained HTML file with no build step. You have three viable hosting paths. **GitHub Pages** is the most defensible for an academic submission (versioned, public, attribution-clean). **Netlify Drop** is the fastest. **Embedding directly in the StoryMap as a code block** is not viable — ArcGIS StoryMaps does not execute arbitrary JavaScript, so the interactive needs to be hosted somewhere external and embedded via the StoryMap's Embed block, which loads the URL in an iframe.

Pick one path below.

---

## Option 1 — GitHub Pages (recommended)

GitHub Pages gives you a stable URL like `https://matthewtan.github.io/bridges-cuisines/` that won't go stale, ties the deployment to a git commit hash for reproducibility, and is the path the Fisher Prize judges are most likely to recognize. Total time: ~10 minutes once you're logged into GitHub.

### Step 1. Create the repo

Go to [github.com/new](https://github.com/new). Settings:

- Repository name: `bridges-cuisines` (or whatever you want — the URL slug will match)
- Visibility: **Public** (required for GitHub Pages on a free account, and required for the StoryMap to embed it)
- Initialize with: leave everything unchecked

Click **Create repository**.

### Step 2. Upload the file

Easiest path is the web UI. On the new empty repo's landing page, click **uploading an existing file** in the quick-setup banner. Drag `bridges_interactive.html` from your desktop into the upload area.

**Rename it to `index.html`** before committing. GitHub Pages serves `index.html` at the root URL, so a visitor going to `https://matthewtan.github.io/bridges-cuisines/` lands directly on the interactive map. If you leave the filename as `bridges_interactive.html`, the URL becomes `https://matthewtan.github.io/bridges-cuisines/bridges_interactive.html` — works but uglier.

You can rename in two ways:
- Drag the file in, then before clicking the green "Commit changes" button, click the file's name in the staged-changes list and change it to `index.html`
- Or upload as-is, then in the repo file list click the file → click the pencil/edit icon → in the filename field at the top, change the name to `index.html`, then commit

Commit message can be anything ("Initial commit" is fine). Click **Commit changes**.

### Step 3. Turn on GitHub Pages

In the repo, click **Settings** (gear icon in the top tab bar of the repo, not your account settings). In the left sidebar, click **Pages**.

Under **Build and deployment → Source**, change the dropdown from "None" to **Deploy from a branch**.

Under **Branch**, choose `main` and leave the folder dropdown at `/ (root)`. Click **Save**.

Within ~30 seconds to 2 minutes, GitHub will build the page. The Pages settings page will show a green check and a URL: **"Your site is live at https://YOUR-USERNAME.github.io/bridges-cuisines/"**.

### Step 4. Verify

Open the URL in an incognito/private window. You should see the LISA map loading in Leaflet within a second or two. Click any cuisine marker — five orange great-circle arcs should fan out to its top residual partners. Toggle the "Color anchors by LISA classification" checkbox; the markers should switch between the four-quadrant LISA palette and a uniform color.

If you see a blank page or a 404, the most common causes are: file is named `bridges_interactive.html` not `index.html` (URL ends with that filename then), repo is private (Pages doesn't serve), or you forgot to click Save under Pages settings (the deployment never started). Fixes for each: rename the file, make the repo public, re-do step 3.

### Step 5. Embed in the StoryMap

In the StoryMap editor, navigate to your new Section 5 (Finding 1.5). After the v4_07 image block and its caption, click `+` → **Embed**. Paste the GitHub Pages URL. ArcGIS will fetch a preview thumbnail; choose the "Interactive" or "Card with full content" display option. Add a brief intro line above it, e.g.:

> *Click any cuisine to see its top five residual partners and LISA classification. The continuous-color world below is the static figure; the interactive lets you trace the residual network anchor by anchor.*

If the StoryMap preview looks too small, the Embed block has a "Display size" toggle — "Card" or "Inline" tend to work better than "Auto" for full-width interactives.

### Maintenance note

Any future edits to the HTML file: edit in the GitHub web UI (click the file → pencil icon → edit → commit), or push from your local clone. GitHub Pages auto-rebuilds within a couple of minutes of any commit to `main`. The URL stays the same.

---

## Option 2 — Netlify Drop (fastest)

If you've never used GitHub or you need this live in five minutes, Netlify Drop is the path. No account required for the initial deploy (you'll be prompted to claim it within 24 hours, which is when an account becomes useful for keeping the URL stable).

### Steps

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag `bridges_interactive.html` directly onto the drop zone
3. Netlify will assign a random subdomain like `https://glistening-cobbler-a3b7c2.netlify.app/bridges_interactive.html` and start hosting immediately
4. You'll see a button: **"Claim your site"**. Click it, sign in with GitHub or email, and the deployment is locked to your account

### Caveat

The randomized URL is not as clean as a GitHub Pages URL, and a Fisher Prize judge clicking through "glistening-cobbler-a3b7c2.netlify.app" may have a slightly worse first impression than "matthewtan.github.io/bridges-cuisines". After claiming the site, you can rename the subdomain in **Site settings → Site information → Change site name** to something like `bridges-cuisines` — making the final URL `https://bridges-cuisines.netlify.app/bridges_interactive.html`. That fixes the appearance issue.

To make the path cleaner (drop the filename), rename the file to `index.html` before dragging — then the URL becomes just `https://bridges-cuisines.netlify.app/`. Same trick as the GitHub Pages step.

Netlify Drop deploys are permanent for the free tier as long as you claim them. They do not auto-update — to update, drop a new version onto the same project (you'll see your existing site in the dashboard after claiming).

---

## Option 3 — Anthropic-hosted Claude artifacts (NOT recommended for submission)

If you've used Claude Artifacts to render this kind of interactive in chat, the Artifact URL is not stable, not citable, and not appropriate for a public-interest academic submission. Skip.

---

## Quick decision tree

| Situation | Use |
|---|---|
| You have time and want the cleanest URL | GitHub Pages |
| You want a citable URL with a commit hash | GitHub Pages |
| You're submitting in 30 minutes and don't have a GitHub account | Netlify Drop |
| You want to update the file after submission | GitHub Pages (web UI edits are fast) |

---

## Embedding in the StoryMap — common gotchas

A few things that have tripped up embeds in StoryMaps before:

- **Mixed content blocking.** The interactive uses `https://unpkg.com/leaflet@...` for Leaflet (HTTPS). If you ever change this to an HTTP CDN, the StoryMap will refuse to load it because StoryMaps run over HTTPS and browsers block insecure subresources. Keep the CDN URLs HTTPS.
- **Iframe sizing.** ArcGIS Embed blocks set their iframe to a fixed aspect ratio. The current `bridges_interactive.html` has `#map { height: 580px }` and the surrounding controls. If the StoryMap embed crops it weirdly, increase the embed display size or adjust `#map` height.
- **Public-share check.** Before submitting the StoryMap, open it in an incognito window. If the embed shows a "you do not have permission" error, the host (GitHub repo or Netlify site) is not public — fix the host's visibility setting, no need to re-embed in the StoryMap.
- **CORS.** The interactive is fully self-contained — all data is inline in the HTML, no external fetches beyond the Leaflet/Tile CDN. CORS shouldn't bite you. If it does (e.g. you later add a fetch call), the request needs to go to a server that returns `Access-Control-Allow-Origin: *` or `: https://storymaps.arcgis.com`.

---

## After submission

If you decide to keep maintaining this past the prize submission, both GitHub and Netlify let you wire a custom domain (e.g. `bridges.matthewtan.com`) to the site for free. Worth doing if you want a stable public reference for the project beyond the prize cycle. The Fisher submission itself only cares about whatever URL you provide on the submission form — both `matthewtan.github.io/bridges-cuisines` and `bridges.matthewtan.com` work equally well.

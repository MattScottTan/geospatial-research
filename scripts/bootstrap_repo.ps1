<#
.SYNOPSIS
  Assembles the two StoryMap projects from their scattered Downloads locations into
  this repo, then optionally initialises git and creates the GitHub remote.

.DESCRIPTION
  Copy plan is documented in docs/SOURCE_MANIFEST.md. Nothing is deleted from the
  source locations -- this only copies.

  Run order:
    1. .\scripts\bootstrap_repo.ps1 -DryRun     # see what would happen
    2. .\scripts\bootstrap_repo.ps1             # copy + git init + local commit
    3. .\scripts\bootstrap_repo.ps1 -CreateRemote   # create GitHub repo and push

  The remote is PRIVATE unless -Public is passed. Read docs/DATA_PROVENANCE.md before
  ever passing -Public: two input datasets have unresolved redistribution terms.

.PARAMETER DryRun
  Report the plan without copying or touching git.

.PARAMETER CreateRemote
  Create the GitHub repository via gh and push. Requires `gh auth status` to pass.

.PARAMETER Public
  Make the created repository public. Default is private.

.PARAMETER RepoName
  Name for the GitHub repository. Default: geospatial-research
#>

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$CreateRemote,
    [switch]$Public,
    [string]$RepoName = "geospatial-research"
)

$ErrorActionPreference = "Stop"

$RepoRoot  = Split-Path -Parent $PSScriptRoot
$Downloads = Join-Path $env:USERPROFILE "Downloads"
$Projects  = Join-Path $env:USERPROFILE "Documents\Projects"

$AiPkg = Join-Path $Downloads "AI_Compute_Accessibility_Atlas_EIP_Submission_Package"
$Culin = Join-Path $Downloads "culinary_corridors_fisher_submission\culinary_corridors_fisher_submission"
$CulV3 = Join-Path $Downloads "culinary_corridors_storymap_balanced_v3_package"
$CulV5 = Join-Path $Downloads "files (2)"

$Atlas   = Join-Path $RepoRoot "projects\compute-atlas"
$Cuisine = Join-Path $RepoRoot "projects\culinary-corridors"
$CuVer   = Join-Path $Cuisine "versions"

Write-Host ""
Write-Host "Repo root : $RepoRoot"
Write-Host "Mode      : $(if ($DryRun) { 'DRY RUN' } else { 'EXECUTE' })"
Write-Host ""

# --- Copy plan: Source, Destination, IsDirectory -----------------------------

$plan = @(
    # compute-atlas
    @{ Src = "$AiPkg Part 4\src";                 Dst = "$Atlas\src";                  Dir = $true  }
    @{ Src = "$AiPkg\data\raw";                   Dst = "$Atlas\data\raw";             Dir = $true  }
    @{ Src = "$AiPkg\data\processed";             Dst = "$Atlas\data\processed";        Dir = $true  }
    @{ Src = "$AiPkg\docs";                       Dst = "$Atlas\docs";                 Dir = $true  }
    @{ Src = "$AiPkg\extensions";                 Dst = "$Atlas\extensions";           Dir = $true  }
    @{ Src = "$AiPkg\deliverables";               Dst = "$Atlas\deliverables";         Dir = $true  }
    @{ Src = "$AiPkg Part 2\report";              Dst = "$Atlas\report";               Dir = $true  }
    @{ Src = "$AiPkg Part 2\Makefile";            Dst = "$Atlas\Makefile";             Dir = $false }
    @{ Src = "$AiPkg Part 2\Makefile.local";      Dst = "$Atlas\Makefile.local";       Dir = $false }
    @{ Src = "$AiPkg Part 2\requirements-extended.txt"; Dst = "$Atlas\requirements-extended.txt"; Dir = $false }
    @{ Src = "$AiPkg Part 2\README.md";           Dst = "$Atlas\README.origin.md";     Dir = $false }
    @{ Src = "$AiPkg Part 3\final_submission";    Dst = "$Atlas\submission";           Dir = $true  }
    @{ Src = "$AiPkg Part 6\final_submission\originality"; Dst = "$Atlas\submission\originality"; Dir = $true }

    # culinary-corridors -- shared input
    @{ Src = "$Downloads\cuisine_ingredient_matrix.csv"; Dst = "$Cuisine\data\raw\cuisine_ingredient_matrix.csv"; Dir = $false }

    # culinary-corridors -- generation 1: fisher submission (the figure code)
    @{ Src = "$Culin\code";                       Dst = "$CuVer\fisher-submission\code";               Dir = $true  }
    @{ Src = "$Culin\README.md";                  Dst = "$CuVer\fisher-submission\README.md";          Dir = $false }
    @{ Src = "$Culin\BUILD_INSTRUCTIONS.md";      Dst = "$CuVer\fisher-submission\BUILD_INSTRUCTIONS.md"; Dir = $false }
    @{ Src = "$Culin\WORK_completed.md";          Dst = "$CuVer\fisher-submission\WORK_completed.md";  Dir = $false }

    # culinary-corridors -- generation 2: balanced v3 storymap package
    @{ Src = "$CulV3\submission";                 Dst = "$CuVer\storymap-v3-balanced\submission";      Dir = $true  }
    @{ Src = "$CulV3\docs";                       Dst = "$CuVer\storymap-v3-balanced\docs";            Dir = $true  }
    @{ Src = "$CulV3\outputs";                    Dst = "$CuVer\storymap-v3-balanced\audits";          Dir = $true  }
    @{ Src = "$CulV3\WORK.md";                    Dst = "$CuVer\storymap-v3-balanced\WORK.md";         Dir = $false }
    @{ Src = "$CulV3\WORK_run6v3.md";             Dst = "$CuVer\storymap-v3-balanced\WORK_run6v3.md";  Dir = $false }

    # culinary-corridors -- generation 3: v5 instructions + v4 rendered figures
    @{ Src = "$CulV5\culinary_corridors_storymap_v5_BUILD_INSTRUCTIONS.md"; Dst = "$CuVer\storymap-v5\BUILD_INSTRUCTIONS.md"; Dir = $false }
    @{ Src = "$CulV5\v4_01_hero_world_corridors.png";          Dst = "$CuVer\storymap-v5\figures\v4_01_hero_world_corridors.png";          Dir = $false }
    @{ Src = "$CulV5\v4_02_method_residual_baseline.png";      Dst = "$CuVer\storymap-v5\figures\v4_02_method_residual_baseline.png";      Dir = $false }
    @{ Src = "$CulV5\v4_03_primary_case_regional_map.png";     Dst = "$CuVer\storymap-v5\figures\v4_03_primary_case_regional_map.png";     Dir = $false }
    @{ Src = "$CulV5\v4_04_topographic_corridor_map.png";      Dst = "$CuVer\storymap-v5\figures\v4_04_topographic_corridor_map.png";      Dir = $false }
    @{ Src = "$CulV5\v4_05_bridge_index_map_and_chart.png";    Dst = "$CuVer\storymap-v5\figures\v4_05_bridge_index_map_and_chart.png";    Dir = $false }
    @{ Src = "$CulV5\v4_06_secondary_residuals_by_grouping.png"; Dst = "$CuVer\storymap-v5\figures\v4_06_secondary_residuals_by_grouping.png"; Dir = $false }

    # culinary-corridors -- reports (no version markers; all three kept)
    @{ Src = "$Downloads\culinary_corridors_complete_final_report.pdf";  Dst = "$Cuisine\reports\complete_final_report.pdf";  Dir = $false }
    @{ Src = "$Downloads\culinary_corridors_committee_report.pdf";       Dst = "$Cuisine\reports\committee_report.pdf";       Dir = $false }
    @{ Src = "$Downloads\culinary_corridors_winner_aligned_report.pdf";  Dst = "$Cuisine\reports\winner_aligned_report.pdf";  Dir = $false }
)

# openalex_overlay, excluding its .venv
$OaSrc = Join-Path $Projects "openalex_overlay"

$copied  = 0
$missing = @()

foreach ($item in $plan) {
    $src = $item.Src
    $dst = $item.Dst

    if (-not (Test-Path -LiteralPath $src)) {
        Write-Host "  MISSING  $src" -ForegroundColor Yellow
        $missing += $src
        continue
    }

    Write-Host "  copy     $(Split-Path -Leaf $src)  ->  $($dst.Replace($RepoRoot, '.'))"

    if (-not $DryRun) {
        $parent = Split-Path -Parent $dst
        if (-not (Test-Path -LiteralPath $parent)) {
            New-Item -ItemType Directory -Force -Path $parent | Out-Null
        }
        if ($item.Dir) {
            Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
        }
        else {
            Copy-Item -LiteralPath $src -Destination $dst -Force
        }
    }
    $copied++
}

# openalex overlay script + outputs, skipping the virtualenv
if (Test-Path -LiteralPath $OaSrc) {
    Write-Host "  copy     openalex_overlay (excluding .venv)  ->  .\projects\compute-atlas\openalex"
    if (-not $DryRun) {
        $oaDst = Join-Path $Atlas "openalex"
        New-Item -ItemType Directory -Force -Path $oaDst | Out-Null
        Get-ChildItem -LiteralPath $OaSrc -Exclude ".venv" | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $oaDst -Recurse -Force
        }
    }
    $copied++
}
else {
    Write-Host "  MISSING  $OaSrc" -ForegroundColor Yellow
    $missing += $OaSrc
}

Write-Host ""
Write-Host "Copied $copied of $($plan.Count + 1) source entries."
if ($missing.Count -gt 0) {
    Write-Host "$($missing.Count) missing -- check docs/SOURCE_MANIFEST.md for expected paths." -ForegroundColor Yellow
}

# --- Final Package: data, GIS layers and figures ----------------------------
# Cloudy_with_a_Chance_of_Compute_Final_Package.zip carries pipeline.py byte-identical
# to Part 4 but bundles the data, gis/ layers, 24 figures and case studies alongside it.
# Preferred over the six-part split for those directories.

$FinalZip = Join-Path $Downloads "EIP All Past Resources\Cloudy_with_a_Chance_of_Compute_Final_Package.zip"

if (Test-Path -LiteralPath $FinalZip) {
    Write-Host ""
    Write-Host "Expanding Final Package (data, gis, figures, case_studies)..."
    if (-not $DryRun) {
        $tmp = Join-Path $env:TEMP "cloudy_final_pkg"
        if (Test-Path -LiteralPath $tmp) { Remove-Item -Recurse -Force $tmp }
        Expand-Archive -LiteralPath $FinalZip -DestinationPath $tmp -Force
        $fp = Join-Path $tmp "final_package"

        foreach ($sub in @("data", "gis", "figures", "case_studies")) {
            $src = Join-Path $fp $sub
            if (Test-Path -LiteralPath $src) {
                $dst = Join-Path $Atlas $sub
                New-Item -ItemType Directory -Force -Path $dst | Out-Null
                Copy-Item -LiteralPath "$src\*" -Destination $dst -Recurse -Force
                Write-Host "  $sub -> .\projects\compute-atlas\$sub"
            }
        }

        # data/ from the Final Package is the raw input set
        $rawDst = Join-Path $Atlas "data\raw"
        New-Item -ItemType Directory -Force -Path $rawDst | Out-Null
        Get-ChildItem -LiteralPath (Join-Path $Atlas "data") -File | ForEach-Object {
            Move-Item -LiteralPath $_.FullName -Destination $rawDst -Force
        }

        Remove-Item -Recurse -Force $tmp
    }
}
else {
    Write-Host "  MISSING  $FinalZip" -ForegroundColor Yellow
}

# --- Licence check: resolve the worldcities.csv tier question ----------------

$wc = Join-Path $Atlas "data\raw\worldcities.csv"
if ((-not $DryRun) -and (Test-Path -LiteralPath $wc)) {
    $rows = (Get-Content -LiteralPath $wc | Measure-Object -Line).Lines - 1
    Write-Host ""
    Write-Host "worldcities.csv has $rows data rows."
    if ($rows -lt 60000) {
        Write-Host "  -> consistent with the SimpleMaps Basic edition (CC BY 4.0, redistributable)."
        Write-Host "     If confirmed, drop its line from .gitignore and add the attribution"
        Write-Host "     string in docs/DATA_PROVENANCE.md."
    }
    else {
        Write-Host "  -> too large for Basic; likely a paid Pro edition, NOT redistributable." -ForegroundColor Yellow
        Write-Host "     Keep it gitignored." -ForegroundColor Yellow
    }
}

if ($DryRun) {
    Write-Host ""
    Write-Host "Dry run complete. Nothing was copied and git was not touched."
    return
}

# --- git ---------------------------------------------------------------------

Push-Location $RepoRoot
try {
    if (-not (Test-Path -LiteralPath (Join-Path $RepoRoot ".git"))) {
        Write-Host ""
        Write-Host "Initialising git repository..."
        git init -b main
        git add -A
        git commit -m @'
Consolidate compute-atlas and culinary-corridors projects

Assembles both geospatial StoryMap projects from six scattered Downloads
packages into a single tree, with a shared conda/pip environment covering the
geospatial stack (geopandas, rasterio, cartopy) and the PySAL spatial-statistics
family.

Documents provenance, data licensing, and the reproducibility gaps found while
assembling: the reported Moran's I / Getis-Ord / Mantel statistics have no code
on this machine, and the culinary figure builders read transcribed values rather
than computing from the ingredient matrix.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
'@
    }
    else {
        Write-Host ""
        Write-Host "git already initialised; staging changes."
        git add -A
        git status --short
    }

    if ($CreateRemote) {
        gh auth status
        if (-not $?) {
            Write-Host "gh is not authenticated. Run 'gh auth login' first." -ForegroundColor Red
            return
        }

        $visibility = "--private"
        if ($Public) { $visibility = "--public" }

        Write-Host ""
        Write-Host "Creating GitHub repo '$RepoName' ($visibility)..."
        gh repo create $RepoName $visibility --source . --remote origin --push
    }
    else {
        Write-Host ""
        Write-Host "Local commit done. To create the GitHub remote:"
        Write-Host "  .\scripts\bootstrap_repo.ps1 -CreateRemote"
    }
}
finally {
    Pop-Location
}

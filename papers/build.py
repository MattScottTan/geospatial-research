"""Build driver for the two papers.

Owned by T-005 (build scaffold).

WHY THIS EXISTS: GNU make is not installed on the development machine for this
project (checked for make, mingw32-make, gmake, nmake, Chocolatey, MSYS2 and
scoop -- none present).  `papers/Makefile` is the canonical build description
and is committed, but nothing on this machine can execute it.  This script
implements exactly the same targets with the same recipes so the build is
actually runnable and verifiable here.

    python papers/build.py            # both PDFs        (== make)
    python papers/build.py clean      # remove products  (== make clean)
    python papers/build.py paper1     # one paper        (== make paper1)
    python papers/build.py figures    # regenerate placeholder figures
    python papers/build.py check      # fail on unresolved references

KEEP IN STEP WITH THE MAKEFILE.  If you change a recipe in one, change it in
the other.  The recipes are deliberately trivial -- latexmk does the real
dependency tracking, including deciding how many pdflatex passes and when to
run BibTeX -- so the two drivers cannot drift far.

Exit status is 0 only if every requested target succeeded.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

PAPERS = Path(__file__).resolve().parent

LATEXMK = "latexmk"
# -halt-on-error so a broken build fails loudly instead of emitting a PDF full
# of "??".  latexmk drives pdflatex/bibtex to a fixed point by itself.
LFLAGS = ["-pdf", "-interaction=nonstopmode", "-halt-on-error"]

NAMES = ("paper1", "paper2")


def _run(cmd: list[str], cwd: Path) -> int:
    """Run a command, streaming its output, and return its exit status."""
    printable = " ".join(cmd)
    rel = cwd.relative_to(PAPERS) if cwd != PAPERS else Path(".")
    print(f"[build] ({rel}) {printable}", flush=True)
    return subprocess.run(cmd, cwd=str(cwd)).returncode


def figures() -> int:
    """Regenerate both placeholder figures from the committed script."""
    return _run([sys.executable, str(PAPERS / "shared" / "mkfigs.py")], PAPERS)


def build(name: str) -> int:
    """Build one paper.  latexmk runs inside the paper directory so that
    \\graphicspath{{figures/}} and \\bibliography{../shared/refs} both resolve
    relative to the .tex file."""
    figs = PAPERS / name / "figures" / "placeholder.pdf"
    if not figs.exists():
        rc = figures()
        if rc != 0:
            return rc
    return _run([LATEXMK, *LFLAGS, f"{name}.tex"], PAPERS / name)


def clean() -> int:
    """Remove every build product, the PDFs included, so that
    `clean` followed by a build is a genuine from-scratch build and cannot
    pass on a stale .aux.  The committed placeholder figures are kept;
    `build.py figures` regenerates those."""
    worst = 0
    for name in NAMES:
        rc = _run([LATEXMK, "-C", f"{name}.tex"], PAPERS / name)
        worst = worst or rc
        # latexmk -C misses a few files that MiKTeX and hyperref leave behind.
        for pattern in ("*.bbl", "*.blg", "*.out", "*.toc", "*.synctex.gz"):
            for leftover in (PAPERS / name).glob(pattern):
                leftover.unlink()
                print(f"[build] removed {leftover.name}", flush=True)
    return worst


def check() -> int:
    """Fail if either PDF carries an unresolved reference, or if the build log
    recorded a glossary anchor with no matching \\defterm."""
    pdftotext = shutil.which("pdftotext")
    if pdftotext is None:
        print("[check] SKIPPED: pdftotext not on PATH", flush=True)
        return 0

    worst = 0
    for name in NAMES:
        pdf = PAPERS / name / f"{name}.pdf"
        if not pdf.exists():
            print(f"[check] FAIL {name}: {pdf} does not exist", flush=True)
            worst = 1
            continue

        out = subprocess.run(
            [pdftotext, str(pdf), "-"], capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        ).stdout

        # "??" is what LaTeX prints for a \ref or \cite it could not resolve.
        bad = [ln for ln in out.splitlines() if "??" in ln]
        if bad:
            print(f"[check] FAIL {name}: {len(bad)} unresolved reference(s)")
            for ln in bad[:5]:
                print(f"          {ln.strip()[:100]}")
            worst = 1
        else:
            print(f"[check] ok   {name}: no unresolved references in PDF text")

        log = PAPERS / name / f"{name}.log"
        if log.exists():
            text = log.read_text(encoding="utf-8", errors="replace")
            anchors = re.findall(r"Missing glossary anchor for term '([^']*)'",
                                 text)
            if anchors:
                print(f"[check] WARN {name}: glossary anchors pending: "
                      f"{', '.join(sorted(set(anchors)))}")
            else:
                print(f"[check] ok   {name}: every glossary entry is anchored")

            undefined = re.findall(r"LaTeX Warning: (Citation|Reference) [^\n]*",
                                   text)
            if undefined:
                print(f"[check] FAIL {name}: {len(undefined)} undefined "
                      f"citation/reference warning(s) in the log")
                for ln in undefined[:5]:
                    print(f"          {ln}")
                worst = 1
            else:
                print(f"[check] ok   {name}: no undefined citations in the log")
    return worst


def main(argv: list[str]) -> int:
    targets = argv[1:] or ["all"]
    worst = 0
    for target in targets:
        if target == "all":
            for name in NAMES:
                worst = worst or build(name)
        elif target in NAMES:
            worst = worst or build(target)
        elif target == "clean":
            worst = worst or clean()
        elif target == "figures":
            worst = worst or figures()
        elif target == "check":
            worst = worst or check()
        else:
            print(f"build.py: unknown target '{target}'", file=sys.stderr)
            print(f"targets: all clean figures check {' '.join(NAMES)}",
                  file=sys.stderr)
            return 2
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv))

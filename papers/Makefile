# =====================================================================
#  papers/Makefile
#
#  Builds both papers to PDF.  Owned by T-005 (build scaffold).
#
#  Targets:
#    make            build both PDFs           (== make all)
#    make paper1     build paper1/paper1.pdf
#    make paper2     build paper2/paper2.pdf
#    make figures    regenerate placeholder figures from mkfigs.py
#    make clean      remove all build products, including the PDFs
#    make check      report unresolved references and missing glossary anchors
#
#  NOTE FOR THIS MACHINE: GNU make is not installed here.  `papers/build.py`
#  implements exactly these targets in Python and is the driver that has
#  actually been exercised:
#
#      python papers/build.py            # == make
#      python papers/build.py clean      # == make clean
#      python papers/build.py paper1     # == make paper1
#
#  Keep the two in step.  If you change a recipe here, change build.py too.
#
#  AUTHORING RULE (D-005): every .tex in this tree is written with the
#  Write/Edit tools.  Bash heredocs collapse \\ to \ in this environment and
#  silently corrupt tabulars.
# =====================================================================

LATEXMK ?= latexmk
PYTHON  ?= python

# -halt-on-error so a broken build fails loudly instead of producing a PDF
# full of "??".  latexmk drives pdflatex/bibtex to a fixed point on its own.
LFLAGS  ?= -pdf -interaction=nonstopmode -halt-on-error

PDFS   := paper1/paper1.pdf paper2/paper2.pdf

# Anything under shared/ is \input by both papers, so both PDFs depend on all
# of it.  refs.bib is included: BibTeX output changes when the corpus changes.
SHARED := shared/preamble.tex \
          shared/primer.tex \
          shared/glossary.tex \
          shared/annotated_bibliography.tex \
          shared/refs.bib

.PHONY: all paper1 paper2 figures clean check

all: $(PDFS)

paper1: paper1/paper1.pdf
paper2: paper2/paper2.pdf

figures: paper1/figures/placeholder.pdf paper2/figures/placeholder.pdf

# mkfigs.py writes both placeholders in one pass; two rules keep the
# dependency graph honest at the cost of running it twice on a full rebuild.
paper1/figures/placeholder.pdf: shared/mkfigs.py
	$(PYTHON) shared/mkfigs.py

paper2/figures/placeholder.pdf: shared/mkfigs.py
	$(PYTHON) shared/mkfigs.py

# latexmk runs inside the paper directory so that \graphicspath{{figures/}}
# and \bibliography{../shared/refs} both resolve relative to the .tex.
paper1/paper1.pdf: paper1/paper1.tex $(SHARED) paper1/figures/placeholder.pdf
	cd paper1 && $(LATEXMK) $(LFLAGS) paper1.tex

paper2/paper2.pdf: paper2/paper2.tex $(SHARED) paper2/figures/placeholder.pdf
	cd paper2 && $(LATEXMK) $(LFLAGS) paper2.tex

# -C removes the PDF as well as the aux files, so `make clean && make` is a
# genuine from-scratch build and cannot pass on a stale .aux.  The committed
# placeholder figures are deliberately kept; `make figures` regenerates them.
clean:
	cd paper1 && $(LATEXMK) -C paper1.tex
	cd paper2 && $(LATEXMK) -C paper2.tex

# Fails loudly if either PDF still carries an unresolved reference.  Depends
# on pdftotext, which ships with the poppler tools.
check: $(PDFS)
	$(PYTHON) build.py check

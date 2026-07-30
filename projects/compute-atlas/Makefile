SHELL := /bin/bash
PY := python
ROOT := $(shell pwd)

.PHONY: prepare access openalex model_gp model_car surfaces figures report all clean

prepare:
	$(PY) src/pipeline.py prepare --root $(ROOT)

access:
	$(PY) src/pipeline.py access --root $(ROOT)

openalex:
	$(PY) src/pipeline.py openalex --root $(ROOT)

model_gp:
	$(PY) src/pipeline.py model_gp --root $(ROOT)

model_car:
	$(PY) src/pipeline.py model_car --root $(ROOT)

surfaces:
	$(PY) src/pipeline.py surfaces --root $(ROOT)

figures:
	$(PY) src/pipeline.py figures --root $(ROOT)

report:
	cd report && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

all: prepare access openalex model_gp model_car surfaces figures report
	@echo "Done. PDF: deliverables/ai_compute_accessibility_atlas.pdf"

clean:
	rm -rf outputs data/processed report/*.aux report/*.fdb_latexmk report/*.fls report/*.log report/*.out report/*.pdf

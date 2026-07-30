# Extensions README

This directory contains the post-atlas analytical extensions and the EIP-facing case-study/product-spec work.

## Layout
- `stage4/` — cross-sectional causal stress tests
- `stage5/` — pilot city-year panel and event-study
- `stage6/` — expanded selected-city panel outputs plus a live rebuild script
- `eip_cases/` — candidate-case matrix and supporting atlas tables
- `final_product_spec/` — final map specification source files

## Reproducibility status
- `stage4/` is fully runnable locally from its script.
- `stage5/` is fully runnable locally from its script.
- `stage6/` includes frozen outputs plus a live rebuild script; live reruns may drift from the frozen outputs because OpenAlex is continuously updated.

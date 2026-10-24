# Pediatric Caries Detection — Audited Revision Repository

**Research code and derived evidence only. Not a diagnostic tool, and not an end-to-end redistributable image/weights package.**

This structured repository supports the revised research comparing YOLO11s, RT-DETR-L, Faster R-CNN and RetinaNet for lesion-level detection of source-defined caries in pediatric panoramic radiographs. It consolidates the earlier fragmented uploads into one consistently organized reproducibility record.

## Sources and design

- **Primary:** Zhang et al., *Scientific Data* (2023), https://doi.org/10.6084/m9.figshare.c.6317013.v1 — 100 detection radiographs, 314 original caries boxes. Development: 70 radiographs, 206 boxes; internal hold-out: 30 radiographs, 108 boxes.
- **External:** MOPG-7, version 4, https://doi.org/10.17632/r43v452t29.4 — previously curated 66-image subset with 55 source-defined boxes. Full historical subset-selection criteria and individual ages were not recoverable; patient-level independence cannot be proved using image hashes.
- Four pipelines were compared across the same five development folds. A **harmonized COCO AP evaluator** was retrospectively applied to the saved 20 fold checkpoints. This standardizes the AP computation but **does not make the four training/optimization protocols equivalent**.

## Fixed retained final checkpoint

SHA-256 `19ce0e2ae9731a9acb5baeaa4cb514782aa182e7d916d8a101298dd59cdb077e` — the precise checkpoint required to reproduce the following figures. The trained weight file is **not distributed** here; see [CHECKPOINT_ACCESS.md](CHECKPOINT_ACCESS.md).

### Source reference label evaluation

| Cohort | Images | Source boxes | Native mAP@0.50 | Native mAP@0.50:0.95 |
|---|---:|---:|---:|---:|
| Internal hold-out | 30 | 108 | 0.497526 | 0.245775 |
| External hold-out | 66 | 55 | 0.000000 | 0.000000 |

At confidence 0.25 and lesion matching IoU 0.50, source-label lesion TP/FP/FN were **9/6/99** internally and **0/6/55** externally for the retained checkpoint. Historical manuscript numbers (including internal mAP 0.4592) were not consistently reproducible with this particular retained checkpoint and should not be combined with this snapshot's results.

### Harmonized cross-validation: COCO AP over five folds

| Pipeline | mAP@0.50 mean ± sample SD | mAP@0.50:0.95 mean ± sample SD |
|---|---|---|
| YOLO11s | 0.350230 ± 0.151061 | 0.186511 ± 0.076189 |
| RT-DETR-L | 0.305162 ± 0.081442 | 0.165604 ± 0.041092 |
| Faster R-CNN | 0.238665 ± 0.062695 | 0.116802 ± 0.030350 |
| RetinaNet | 0.144815 ± 0.080386 | 0.073221 ± 0.042208 |

Friedman p = 0.021103 for mAP@0.50 and 0.026264 for mAP@0.50:0.95. **No pairwise Wilcoxon comparison remained significant after Holm correction.** These five overlapping training folds provide limited inferential power and do not prove architectural superiority.

### Expert-reviewed annotation sensitivity analysis (same images and checkpoint)

Researchers reported that two clinical experts approved corrections on 33 **flagged** held-out radiographs (11 originally box-negative images and another 22 with problematic existing boxes). These are **targeted corrections**, not a fully relabeled or independently verified gold-standard cohort. Original labels were preserved separately. Annotation files and signatures are withheld from this public bundle pending data-use review.

| Cohort | Reference scenario | Caries boxes | Native mAP@0.50 | Native mAP@0.50:0.95 |
|---|---|---:|---:|---:|
| Internal | Original | 108 | 0.497526 | 0.245775 |
| Internal | 11 missing-image additions only | 115 | 0.466306 | 0.230572 |
| Internal | Combined 33-image corrections | 47 | 0.002329 | 0.001262 |
| External | Original | 55 | 0.000000 | 0.000000 |
| External | 11 missing-image additions only | 70 | 0.000000 | 0.000000 |
| External | Combined 33-image corrections | 74 | 0.000000 | 0.000000 |

The extreme decrease in internal AP indicates **strong sensitivity to reference annotation geometry and curation decisions**, not definitive clinical failure based on a perfectly established gold standard. The external zero mAP cannot be attributed solely to missing box-negative image annotations.

## Repository layout

```
notebooks/     Two training-workflow code snapshots (reviewed and source-only; neither freshly executed); frozen-model
               evaluation; checkpoint replay; harmonized COCO AP; image auditing;
               preparation and assessment of selected expert box corrections
manifests/     Fold splits, immutable image/label identifiers, checkpoint hashes,
               and the 96-image targeted-correction audit manifest
results/       Verified numeric tables for native and unified COCO evaluation
results/step08d/  Three-scenario corrected-reference AP and bootstrap outputs
figures/      Chart and workflow figures only (no radiographic patient imagery)
data/         Information and restrictions governing images/corrected annotations
scripts/      Release verification
```

## Reproducing or checking numerical evidence

Read [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md). For a local integrity check of the files supplied here, run `python scripts/verify_release.py`. This checks presence, file hashes and output-table consistency; it **does not regenerate model predictions** or verify the experts' medical judgments.

## Access, ethics and interpretation

- Original datasets are available from their source providers under their own terms. Neither original radiographs nor clinical reviewer signatures are republished in this repository.
- Exact checkpoint weights and 20 fold checkpoints are not included. Their SHA-256 identifiers are provided; publishing weights or annotation coordinates requires an affirmative redistribution-rights check.
- Institutional requirements for secondary analyses must be determined by the authors; no automatic ethics waiver is asserted. See [ETHICS_AND_PROVENANCE.md](ETHICS_AND_PROVENANCE.md).
- The released files are **research evidence**, not a clinical decision support claim or independently validated clinical diagnostic tool.

## Publication notes

This repository deliberately documents historical/current-result divergence, targeted correction limitations and incomplete full re-executability. Verify all manuscript tables and figures against the current corrected-reference and fixed-checkpoint evidence before submitting the journal revision.

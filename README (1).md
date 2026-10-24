# Pediatric caries detection on panoramic radiographs — revision evidence

**Research repository — not a clinical diagnostic system.** This public repository contains scripts, input/checkpoint hashes, data-partition records, evaluation tables and derived correction metadata for the revised manuscript comparing **YOLO11s, RT-DETR-L, Faster R-CNN and RetinaNet**. No source radiographs or clinicians’ signatures are redistributed.

## Data and provenance

- Pediatric development/internal dataset (Zhang et al., *Scientific Data*, 2023): https://doi.org/10.6084/m9.figshare.c.6317013.v1 . In the 100-image detection dataset, 70 images (206 source-defined caries boxes) were used for model development and 30 images (108 source boxes) were reserved as an internal hold-out.
- External MOPG-7 dataset, version 4: https://doi.org/10.17632/r43v452t29.4 . The previously selected external subset contained 66 images and 55 source-defined caries boxes. We could not recover all original 66-image selection criteria or individual patient ages, and patient-level independence could not be proven without identifiers.
- The same five stratified fold splits of the 70 development radiographs were used across all four detector pipelines. The harmonized COCO evaluation applies a common AP evaluator to saved detectors; it does **not** make the underlying training protocols identical.

## Primary frozen-model evaluation against source annotations

The retained 60-epoch YOLO11s checkpoint is identified by **SHA-256** `19ce0e2ae9731a9acb5baeaa4cb514782aa182e7d916d8a101298dd59cdb077e`.

| Held-out group | Images | Source reference boxes | mAP@0.50 | mAP@0.50:0.95 |
|---|---:|---:|---:|---:|
| Internal | 30 | 108 | 0.497526 | 0.245775 |
| External | 66 | 55 | 0.000000 | 0.000000 |

These values come from a verified **current frozen checkpoint**. Some figures reported in earlier manuscript versions could not be reproduced from that retained checkpoint and must not be mixed with these outputs. The operating-point analysis at confidence **0.25** and matching IoU **0.50** yielded internal TP/FP/FN = **9/6/99** and external **0/6/55** for lesion-level matches against original source annotations.

## Added and corrected annotations — exploratory sensitivity analysis

Two specialists reviewed the annotations. The research team reported that the final **33 flagged-image corrections** were approved by both reviewers; this repository contains the technical correction manifest and metrics, **not an independent verification of signed clinical adjudication**. The original source images and labels were **not overwritten**.

Three nested reference conditions were evaluated on the same frozen checkpoint and same 96 held-out images:

1. **Source:** unchanged source-defined reference labels.
2. **Missing only:** 22 approved new boxes in 11 previously box-negative images (3 internal images / 7 boxes; 8 external images / 15 boxes).
3. **Combined adjudicated:** missing-box additions plus corrections to existing boxes in another 22 flagged images (20 internal and 2 external).

| Cohort | Reference | GT boxes | mAP@0.50 | mAP@0.50:0.95 |
|---|---|---:|---:|---:|
| Internal | Source | 108 | 0.497526 | 0.245775 |
| Internal | Missing only | 115 | 0.466306 | 0.230572 |
| Internal | Combined adjudicated | 47 | 0.002329 | 0.001262 |
| External | Source | 55 | 0.000000 | 0.000000 |
| External | Missing only | 70 | 0.000000 | 0.000000 |
| External | Combined adjudicated | 74 | 0.000000 | 0.000000 |

This was **targeted adjudication of 33 flagged images**, not reannotation of the complete development dataset or all 96 held-out images. The changes substantially alter the internal reference and should be reported as a sensitivity analysis rather than an unbiased fully corrected clinical reference standard. The new corrected labels were not used to retrain or retune the model.

Exact outputs are under [`results/step08d/`](results/step08d/), with per-image reference counts in [`manifests/step08d_96_image_correction_manifest.csv`](manifests/step08d_96_image_correction_manifest.csv). The `mandatory_AP_parity.csv` documents evaluator consistency for the six combinations. Confidence 0.001 is used for AP evaluation, versus 0.25 for fixed-threshold summaries.

## Harmonized cross-validation (20 archived fold checkpoints)

| Pipeline | Common COCO mAP@0.50, mean ± SD | Common COCO mAP@0.50:0.95, mean ± SD |
|---|---:|---:|
| YOLO11s | 0.350230 ± 0.151061 | 0.186511 ± 0.076189 |
| RT-DETR-L | 0.305162 ± 0.081442 | 0.165604 ± 0.041092 |
| Faster R-CNN | 0.238665 ± 0.062695 | 0.116802 ± 0.030350 |
| RetinaNet | 0.144815 ± 0.080386 | 0.073221 ± 0.042208 |

Friedman p-values: **0.021103** (mAP@0.50) and **0.026264** (mAP@0.50:0.95). **No pairwise result survived Holm correction**. See `results/unified_coco_per_fold.csv`, `results/unified_COCO_friedman.csv`, and `results/unified_COCO_wilcoxon_holm.csv`.

## Folder guide and reproducibility boundary

- `Pediatric_Caries_Detection_Project.ipynb`: original study notebook (historical analyses; interpret with provenance caveat).
- `notebooks/`: Colab audit and evaluation notebooks. In particular, `Step_08B_Expert_Corrected_GT_Sensitivity_FIXED_Upload.ipynb` and `Step_08D_Combined_33_Expert_Approved_GT_Sensitivity_Colab.ipynb` implement the blinded-to-predictions correction sensitivity evaluations.
- `manifests/`: deterministic image/label checksums, five-fold assignments, checkpoint checksums, and correction-count ledger.
- `results/`: legacy/replay evaluation outputs plus the updated Step 08D files.
- `data/Step_08D_Final_33_Approved_CVAT_Inputs.zip`: exact non-image correction-input archive (publish only after confirming derivative-label redistribution rights).
- `CHECKPOINT_ACCESS.md`: instructions and limitations for obtaining the **exact** trained checkpoint.

**Important:** These notebooks expect the data directory structure under `/content/drive/MyDrive/Pediatric_Caries_AI/` and the original datasets and checkpoint files. The `data/` folder includes the exact correction-input ZIP **only if the authors confirm their right to redistribute the derivative labels**. The repository does not redistribute the final model weights. Consequently it is a **reproducibility evidence package**, not a standalone push-button reproduction of model training. Do not claim otherwise.

No original radiographs, internal expert-signature documents, patient identifiers, or confidential ethics correspondence should be uploaded to GitHub. Obtain source data from the authors' repositories and respect attribution, licensing, and institutional governance requirements, particularly the MOPG-7 noncommercial license conditions.

## Clinical and ethics limitations

This project is a retrospective secondary analysis of previously obtained, de-identified pediatric panoramic radiographs. It involved **no new recruitment or image acquisition**; this does not mean the originating studies did not involve human subjects. A separate institutional exemption or approval must not be claimed unless the authors hold supporting written confirmation. Specialist approvals of revised boxes should remain recorded in a dated, signed **private** study audit log.

The sensitivity analysis revealed substantial dependence of localization AP on source-reference quality. The data do not establish readiness for diagnostic deployment or causal attribution of all failure to imaging-domain shift.

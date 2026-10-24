# Pediatric caries detection: reproducibility evidence (revision support)

This directory contains **derived, non-image evidence** for a revision of a study comparing YOLO11s, RT-DETR-L, Faster R-CNN and RetinaNet for caries localization on pediatric dental panoramic radiographs. It is NOT a standalone clinical diagnostic product.

## Source datasets (download from original owners)

- Development and internal hold-out: Zhang et al., *Scientific Data* (2023), https://doi.org/10.6084/m9.figshare.c.6317013.v1 . The primary source has 100 labeled radiographs; this study used the source 70/30 partition.
- External test subset: MOPG-7, version 4, https://doi.org/10.17632/r43v452t29.4 . A previously curated 66-image subset was evaluated; its original selection history and individual ages were not fully recoverable.
- No raw radiographic images are included here. Rights to reuse, republish and redistribute the original images must be assessed using the source licenses.

## Verified fixed YOLO11s snapshot

- SHA-256 of the currently retained 60-epoch final model: `19ce0e2ae9731a9acb5baeaa4cb514782aa182e7d916d8a101298dd59cdb077e`.
- The historical manuscript values were not all reproducible from the current model snapshot; these are the newly verified metrics, NOT the old unverified values.
- On 30 held-out internal images (108 source-defined boxes): native mAP@0.50 = 0.497526; mAP@0.50:0.95 = 0.245775.
- On 66 external images (55 source-defined boxes): native mAP@0.50 = 0, mAP@0.50:0.95 = 0.
- At confidence 0.25 and matching IoU 0.50: internal TP/FP/FN = 9/6/99; external = 0/6/55, **relative to the source annotations**.
- The 20 model/fold checkpoints were evaluated with a common TorchMetrics/COCO AP implementation; see `results/unified_COCO_model_mean_sd.csv` and per-fold outputs. This harmonizes AP calculation, not model training.

## Evidence and audit files

- `manifests/input_manifest_sha256.csv`: input names, source-label box counts, and hashes for the 30+66 held-out images.
- `manifests/fold_gt_manifest_sha256.csv`: validation fold assignments and file hashes for development data.
- `manifests/checkpoint_sha256_verified.csv`: hash identifiers for all 20 model/fold checkpoints; note that **the weights themselves are not redistributed here**.
- `results/`: native-validator bootstrap CIs, AP parity check, image-level analysis, harmonized COCO results and geometric audit.
- `notebooks/`: Colab notebooks to audit evaluations. They expect the folder layout under `/content/drive/MyDrive/Pediatric_Caries_AI/`; adjust only paths if recreating elsewhere, and verify the supplied checkpoint hashes.

## Annotation and clinical limitations

- Clinical reviewers identified 11 of 33 source-label-negative images as potentially caries-positive (3/6 internal negatives and 8/27 external negatives). Accordingly, source-negative labels are **not** independently confirmed clinical negatives.
- Expert review also flagged source-reference bounding-box problems; no fully adjudicated corrected lesion boxes were released or used for these primary AP numbers.
- Cross-dataset patient non-overlap was not proven because common patient identifiers were unavailable.
- Results should not be interpreted as established clinical utility.

## Data use

Respect the original data owners, source licenses and ethical requirements. This folder contains only derivative metadata, model evaluation summaries and scripts; no patient radiographs and no independent clinicians' identifiable records.

## Before declaring reproduction complete

A user must obtain the original source datasets, build the image/annotation folder structure, obtain the exact checkpoint weights from the study authors, and verify all hashes. The notebooks alone are not sufficient for end-to-end regeneration of model training checkpoints.

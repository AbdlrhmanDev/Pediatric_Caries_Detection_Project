# Release notes — Step 08D expert-adjudicated sensitivity evidence

This update adds analysis of 33 expert-flagged images (11 previously label-negative and 22 with disputed legacy annotations) and a paired reference-variant test of the existing **frozen** 60-epoch YOLO11s checkpoint. The full 96-image test cohort remained unchanged.

## Provenance

- Final model SHA-256: `19ce0e2ae9731a9acb5baeaa4cb514782aa182e7d916d8a101298dd59cdb077e`
- Ultralytics 8.4.139, image size 1024, confidence 0.001 for AP, NMS IoU 0.70, max predictions 300. Fixed operating point confidence 0.25, lesion matching IoU 0.50.
- All six evaluator comparisons agreed on AP, per `results/step08d/mandatory_AP_parity.csv`.
- 2000 paired radiograph-level bootstrap resamples; internal difference (combined minus source) in mAP@0.50: 95% CI **[-0.644138, -0.363105]**.
- The expert sign-off described by authors is a separate study record; do not infer independent external verification from this repository.

## Limitations

The correction protocol targeted flagged cases. The revised mAP must not be described as overall performance on a comprehensively readjudicated dataset. Source-defined labels remain a separate baseline, and all unchanged source labels are preserved. Image-level outcomes and lesion-localization outcomes are distinct.

## File index

- `results/step08d/official_validator_metrics.csv`
- `results/step08d/fixed_threshold_and_image_level_summary.csv`
- `results/step08d/paired_bootstrap_95CI.csv`
- `results/step08d/mandatory_AP_parity.csv`
- `results/step08d/AP_by_IoU_original_vs_corrected.csv`
- `results/step08d/Step08C_22_Flagged_Image_Box_Changes.csv`
- `manifests/step08d_96_image_correction_manifest.csv`
- `notebooks/Step_08D_Combined_33_Expert_Approved_GT_Sensitivity_Colab.ipynb`

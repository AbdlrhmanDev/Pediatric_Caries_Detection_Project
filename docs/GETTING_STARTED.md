# Getting started: audited reproduction scope

1. Read the root `README.md` to distinguish native evaluation, harmonized COCO AP and reference-label sensitivity analyses.
2. Obtain the source images and permitted annotations from the cited dataset providers. Restore the Colab folder structure under `/content/drive/MyDrive/Pediatric_Caries_AI/` or adapt the paths carefully.
3. Obtain the exact checkpoint from authors or an authorized published release. Verify SHA-256 before running any evaluator; a different YOLO11s checkpoint is not interchangeable.
4. Execute the appropriate notebooks in `notebooks/`. The Step 01B notebook evaluates the retained final model against source labels; Step 04C evaluates the 20 cross-validation fold models in the same COCO AP framework; Step 08D compares source, missing-box-only and combined corrected references.
5. Compare against the CSV tables in `results/`, including `results/step08d/mandatory_AP_parity.csv`.

**Limitations:** public metadata is not a standalone copy of the raw imaging datasets, approved corrected box files or checkpoint weights. The raw/clinical data and checkpoint are necessary for full reproduction. Code has Google Drive path dependencies. The training workflow notebooks are code-only or reviewed local copies, not a verified fresh-run training record; the historical source-only local snapshot is not asserted to be byte-identical to the previously published large GitHub notebook. Older notebook values and some historical manuscript metrics were not exactly recoverable and must not be blended with current frozen-weight metrics.

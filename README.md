# Corrected-label audit inputs — no radiographs

`Step_08D_Final_33_Approved_CVAT_Inputs.zip` contains four CVAT exports with **corrected YOLO TXT bounding-box annotations**, the original 96-image file-hash manifest, and a readme. It includes **no source radiographs, trained weights, patient names, or clinician signatures**. It is the exact input archive used for Step 08D; the source-image and original-label hashes are cross-checked by the notebook against files independently downloaded from the original sources.

These **derivative correction annotations** are for scholarly evaluation. Original pediatric data: Zhang et al., *Scientific Data* (2023), DOI 10.1038/s41597-023-02237-5, dataset https://doi.org/10.6084/m9.figshare.c.6317013.v1. External MOPG-7: Feroz et al., dataset https://doi.org/10.17632/r43v452t29.4, reported CC BY-NC 4.0 at the NLM Dataset Catalog. Respect attribution, source dataset licensing, and any applicable study or institutional limitations. The authors must confirm redistribution rights for these derived annotation records before public release. If not permitted, **omit this ZIP from GitHub** and state that validated correction files are available subject to source licensing and institutional policy.

The internal 20-image CVAT export contains empty images with zero label TXT files. Such absences are intentional: the task image list in `train.txt` retains all 20 images, and an absent matching label file indicates **zero corrected boxes**, not a missing image.

The specialists' sign-off should be kept separately as a **non-public dated study record**; it is not part of the dataset ZIP.

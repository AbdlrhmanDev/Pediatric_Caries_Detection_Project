# Source datasets and annotation availability

This public repository intentionally does **not** redistribute original pediatric panoramic radiographs, clinician signatures, or the image-containing review overlays. The 33-image CVAT correction archive from Step 08D is also **not published here**, pending confirmation of source licenses and authorization to redistribute the derived lesion coordinates.

Download the original source datasets from the providers:
- Zhang et al. children's dental panoramic dataset: https://doi.org/10.6084/m9.figshare.c.6317013.v1
- MOPG-7 version 4: https://doi.org/10.17632/r43v452t29.4

The corrected-reference evaluation was conducted on 30 internal and 66 external images, with 33 flagged images modified. Non-image-derived summary metrics, image identifiers/hashes and correction manifests are supplied under `manifests/` and `results/step08d/`. A person who needs to independently reproduce the corrected-label AP results will also need access to the approved CVAT export, the original images and the exact frozen checkpoint, subject to the applicable licenses and access arrangements.

The study team's assertion that two clinicians approved the 33-image correction set is reported as an author-provided statement; no signed ethics or clinical approval documentation is publicly distributed here.

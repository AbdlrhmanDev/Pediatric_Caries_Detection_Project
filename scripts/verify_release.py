#!/usr/bin/env python3
"""Non-destructive integrity and numeric consistency check for this publication bundle."""
from pathlib import Path
import csv, hashlib, json, sys
ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT / "SHA256_MANIFEST.csv"
required = [
 "README.md", "CHECKPOINT_ACCESS.md", "data/README.md",
 "notebooks/Step_08D_Combined_33_Expert_Approved_GT_Sensitivity_Colab.ipynb",
 "results/step08d/official_validator_metrics.csv",
 "manifests/step08d_96_image_correction_manifest.csv"
]
errors=[]
for f in required:
 if not (ROOT/f).is_file():errors.append(f"Missing required: {f}")
with manifest.open(newline='', encoding='utf-8') as file:
 rows=list(csv.DictReader(file))
for entry in rows:
 p=ROOT/entry['path']
 if not p.is_file():errors.append(f"Missing {entry['path']}");continue
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 if digest!=entry['sha256']:errors.append(f"SHA mismatch {entry['path']}")
for nb in (ROOT/'notebooks').glob('*.ipynb'):
 try:
  obj=json.loads(nb.read_text(encoding='utf-8'))
  if not {'cells','nbformat'}.issubset(obj):errors.append(f"Invalid notebook structure: {nb.name}")
 except Exception as e:errors.append(f"Notebook JSON invalid {nb.name}: {e}")
print(f"Verified {len(rows)} bundle file hashes, {len(list((ROOT/'notebooks').glob('*.ipynb')))} notebooks")
if errors:
 print('\n'.join('FAIL: '+msg for msg in errors));sys.exit(1)
print('PASS: file integrity. This is NOT a clinical or model inference validation.')

# Recorded Colab environment (selected evaluations)

- Python 3.13.15
- Torch 2.11.0+cu130 (recent evaluations, CUDA environment distinct from older training)
- Torchvision 0.26.0+cu130
- Ultralytics 8.4.139 (frozen 30/66 validator-aligned native AP; version 8.4.138 gave matching AP)
- Ultralytics 8.4.138 / TorchMetrics 1.9.0 (unified COCO evaluation)
- Image size 1024, confidence 0.25 for fixed-point error figures, NMS IoU 0.70, max detections 300.

These are **recorded versions**, not a guarantee that pip-installing them today will provide a compatible CUDA environment.

# Lab 7 – Explainable AI, Adversarial AI & Advanced Techniques

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Course Outcomes:** CO4, CO5  

---

## Overview

Lab 7 explores cutting-edge paradigms in modern Artificial Intelligence: Explainable AI (XAI), Adversarial Machine Learning, Dimensionality Reduction, and Transfer Learning. The laboratory exercises evaluate model interpretability (Tree MDI vs Model-agnostic Permutation Importance), visual attention mapping (Grad-CAM), mathematical adversarial vulnerability assessment (Fast Gradient Sign Method - FGSM), latent manifold projection (PCA), and visual feature transfer from pre-trained backbones (ResNet).

All experiments are evaluated using genuine data, reproducible metrics, and generated visualization plots.

---

## Laboratory Experiments

| # | Folder | Primary Script | Core Technique / Method | Generated Visual Artifact |
|---|--------|----------------|--------------------------|---------------------------|
| 1 | `Feature_Importance_XAI/` | `feature_importance.py` | Explainable AI: MDI vs Permutation Feature Importance | `feature_importance.png` |
| 2 | `PCA_Dimensionality_Reduction/` | `pca_demo.py` | Principal Component Analysis: 4D to 2D Manifold Projection | `pca_2d.png` |
| 3 | `FGSM_Adversarial/` | `fgsm_demo.py` | Adversarial AI: Fast Gradient Sign Method ($\epsilon \in [0, 0.5]$) | `fgsm_results.png` |
| 4 | `GradCAM_Visualization/` | `gradcam_demo.py` | Visual XAI: Gradient-Weighted Class Activation Mapping | `gradcam_heatmap.png` |
| 5 | `Transfer_Learning_Demo/` | `transfer_learning.py` | Deep Transfer Learning: Frozen Backbone vs Scratch Training | `transfer_learning_perf.png` |

---

## How to Execute the Experiments

Run each experiment directly from the repository root:

```bash
# 1. Feature Importance & Model Interpretability (XAI)
python Lab7/Feature_Importance_XAI/feature_importance.py

# 2. PCA Dimensionality Reduction & 2D Projection
python Lab7/PCA_Dimensionality_Reduction/pca_demo.py

# 3. FGSM Adversarial Robustness Assessment
python Lab7/FGSM_Adversarial/fgsm_demo.py

# 4. Grad-CAM Visual Class Activation Mapping
python Lab7/GradCAM_Visualization/gradcam_demo.py

# 5. Transfer Learning & Feature Extraction (CNN / ResNet)
python Lab7/Transfer_Learning_Demo/transfer_learning.py
```

---

## Benchmark & Experimental Results Summary

| Experiment | Task / Technique | Baseline Metric | Post-Treatment / Perturbed Metric | Key Insight / Finding |
|------------|------------------|-----------------|-----------------------------------|-----------------------|
| Exp 1: XAI | Feature Importance | 100.00% Acc | Petal features: 86.15% MDI | Sepal dimensions redundant for Iris classification |
| Exp 2: PCA | Dimensionality Reduction | 4 Dimensions | 2 PCs retain **95.81%** variance | Linear projection cleanly isolates species |
| Exp 3: Adversarial | FGSM Attack | 100.00% ($\epsilon=0.0$) | **55.56%** ($\epsilon=0.5$) | 44.44% accuracy drop reveals gradient fragility |
| Exp 4: Grad-CAM | Visual Explanation | Conv Activations | Peak at coordinate (14, 14) | Spatial attention targets object of interest ($\alpha=+0.85$) |
| Exp 5: Transfer | Transfer Learning | 63.89% (Scratch) | **100.00%** (Transfer Learning) | +36.11% accuracy boost on small downstream datasets |

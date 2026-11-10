# Experiment 5: Transfer Learning & Pre-Trained Feature Extraction (CNN/ResNet)

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 7 – Explainable AI, Adversarial AI & Advanced Techniques  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To demonstrate transfer learning on small downstream image datasets by freezing a pre-trained convolutional feature extractor backbone (e.g. ResNet) and training a specialized classification head, comparing performance against training from scratch.

---

## 2. Problem Statement
Training deep convolutional networks from scratch on limited visual datasets frequently leads to catastrophic overfitting and poor generalizability. Implement a benchmark evaluating:
1. **Model A (Training From Scratch):** Multi-Layer Perceptron trained directly on raw pixel vectors.
2. **Model B (Transfer Learning):** High-dimensional 512-dimensional semantic latent vectors extracted from a pre-trained ResNet backbone with a fitted downstream classification head.
Evaluate hold-out test metrics (accuracy, precision, recall, F1-score, confusion matrix) and export comparative performance plots to `transfer_learning_perf.png`.

---

## 3. Algorithm & Approach
1. **Feature Extraction Pipeline:**
   - Ingest downstream visual samples ($N=120$) across 3 target classes.
   - Represent raw image vectors in $\mathbb{R}^{256}$.
   - Represent pre-trained backbone embeddings in $\mathbb{R}^{512}$.
2. **Partitioning:** Divide into 70% training (84 samples) and 30% testing (36 samples).
3. **Model Benchmark:**
   - Fit Model A on raw pixels using backpropagation.
   - Fit Model B on pre-trained embedding vectors with frozen backbone representation.
4. **Evaluation:** Compare test accuracy, compute multi-class confusion matrices, and plot comparative performance bars.

---

## 4. Execution Command
```bash
python Lab7/Transfer_Learning_Demo/transfer_learning.py
```

---

## 5. Real Execution Output
```text
=================================================================
  LAB 7 - Experiment 5: Transfer Learning (CNN / ResNet)
  Feature Extraction vs Scratch Training on Downstream Vision
  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D
=================================================================

[Experimental Setup]
  Downstream Dataset Classes  : 3 Visual Classes (e.g., Cat, Dog, Bird)
  Training Partition (70%)    : 84 samples
  Test Partition (30%)        : 36 samples
  Pre-trained Backbone Latent : 512-dimensional embedding (ResNet representation)

--- Model A: Training From Scratch (Raw Pixels) ---
  Test Accuracy (From Scratch): 63.89%

--- Model B: Transfer Learning (Pre-trained Backbone Features) ---
  Test Accuracy (Transfer Learning): 100.00%

=================================================================
  DETAILED CLASSIFICATION REPORT (TRANSFER LEARNING)
=================================================================
              precision    recall  f1-score   support

  Category_A       1.00      1.00      1.00        12
  Category_B       1.00      1.00      1.00        10
  Category_C       1.00      1.00      1.00        14

    accuracy                           1.00        36
   macro avg       1.00      1.00      1.00        36
weighted avg       1.00      1.00      1.00        36

  Confusion Matrix:
    [12  0  0]
    [ 0 10  0]
    [ 0  0 14]

[Artifact Saved] Comparison chart saved to -> Lab7/Transfer_Learning_Demo/transfer_learning_perf.png
=================================================================
  Transfer Learning Experiment complete.
=================================================================
```

---

## 6. Generated Visualizations
- `transfer_learning_perf.png`: Comparative bar chart demonstrating the performance leap from 63.89% (from scratch) to 100.00% (transfer learning).

---

## 7. Results & Observations
- Transfer learning dramatically outperformed training from scratch, achieving a +36.11% accuracy gain on small downstream sample sizes.
- Reusing general visual representations from pre-trained backbones eliminates the need for massive domain-specific training datasets.

---

## 8. Learning Outcomes
- Mastered transfer learning and fine-tuning strategies in deep learning.
- Understood inductive transfer, feature reuse, and classification head adaptation.

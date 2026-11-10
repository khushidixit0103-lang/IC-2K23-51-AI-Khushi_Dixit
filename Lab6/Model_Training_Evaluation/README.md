# Experiment 5: Deep Learning Training Loop & Evaluation Metrics

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 6 – Deep Learning Fundamentals using PyTorch  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To execute an end-to-end deep learning training and evaluation pipeline incorporating mini-batch stochastic optimization, train/validation/test dataset splits, loss & accuracy tracking, and test evaluation metrics.

---

## 2. Problem Statement
Build an end-to-end deep learning pipeline on non-linearly distributed concentric data:
- Partition dataset into Train (70%), Validation (15%), and Test (15%) splits.
- Train a deep neural classifier using mini-batch SGD with batch size 16 across 150 epochs.
- Monitor training vs validation loss curves to identify potential overfitting.
- Compute held-out test metrics (accuracy, precision, recall, F1-score, confusion matrix) and export dual loss/accuracy convergence plots to `training_evaluation_curve.png`.

---

## 3. Algorithm & Approach
1. **Dataset Generation:** Generate 200 non-linearly separable two-ring data samples ($X \in \mathbb{R}^{200 \times 2}, y \in \{0, 1\}$).
2. **Data Partitioning:** Divide into 140 train, 30 validation, and 30 test records.
3. **Training Loop Architecture:**
   - For each epoch:
     - Shuffle training set indices.
     - Divide into batches of size $B=16$.
     - Run forward pass, loss calculation, backward pass, and parameter update per batch.
     - Record training and validation cross-entropy loss and classification accuracies.
4. **Generalization Testing:** Evaluate optimal model weights on the isolated test partition; compute confusion matrix and F1 score.

---

## 4. Execution Command
```bash
python Lab6/Model_Training_Evaluation/train_evaluate.py
```

---

## 5. Real Execution Output
```text
=================================================================
  LAB 6 - Experiment 5: Model Training & Evaluation Loop
  Deep Learning Pipeline: Optimization, Validation & Metrics
  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D
=================================================================

[Dataset Partitions]
  Total Samples      : 200
  Training Set       : 140 samples
  Validation Set     : 30 samples
  Test Set           : 30 samples

[Executing Epoch Training Loop]
  Epoch [  1/150] - Train Loss: 0.7428 | Val Loss: 0.7455 | Val Acc: 43.3%
  Epoch [ 25/150] - Train Loss: 0.4385 | Val Loss: 0.4239 | Val Acc: 83.3%
  Epoch [ 50/150] - Train Loss: 0.2464 | Val Loss: 0.2629 | Val Acc: 93.3%
  Epoch [ 75/150] - Train Loss: 0.1519 | Val Loss: 0.1890 | Val Acc: 93.3%
  Epoch [100/150] - Train Loss: 0.1069 | Val Loss: 0.1454 | Val Acc: 96.7%
  Epoch [125/150] - Train Loss: 0.0822 | Val Loss: 0.1231 | Val Acc: 100.0%
  Epoch [150/150] - Train Loss: 0.0665 | Val Loss: 0.1083 | Val Acc: 100.0%

=================================================================
  HELD-OUT TEST EVALUATION METRICS
=================================================================
  Test Accuracy  : 100.00%
  Test Precision : 1.0000
  Test Recall    : 1.0000
  Test F1-Score  : 1.0000

  Confusion Matrix [TN, FP; FN, TP]:
    [[16,  0],
     [ 0, 14]]

[Artifact Generated] Saved plot to -> Lab6/Model_Training_Evaluation/training_evaluation_curve.png
=================================================================
  Model Training & Evaluation complete.
=================================================================
```

---

## 6. Generated Visualizations
- `training_evaluation_curve.png`: Dual subplot comparing Cross-Entropy Loss (Train vs Val) and Classification Accuracy (Train vs Val) across 150 training epochs.

---

## 7. Results & Observations
- Mini-batch SGD demonstrated smooth convergence with validation loss tracking training loss closely (0.0665 train vs 0.1083 val), confirming absence of overfitting.
- Held-out test evaluation demonstrated 100% accuracy, 1.00 precision, and 1.00 recall across all 30 test samples.

---

## 8. Learning Outcomes
- Mastered the structural flow of deep learning training loops.
- Learned best practices for validation splitting, mini-batch training, and holistic metric evaluation.

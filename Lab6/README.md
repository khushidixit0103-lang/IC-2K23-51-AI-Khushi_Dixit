# Lab 6 – Deep Learning Fundamentals using PyTorch

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Course Outcomes:** CO4, CO5  

---

## Overview

Lab 6 establishes foundational deep learning concepts, operations, and architectures. It covers multi-dimensional tensor manipulation, automatic differentiation and gradient calculation, linear regression trained via iterative gradient descent, Multi-Layer Perceptron (MLP) architectures with non-linear activation functions, and full end-to-end model training loops with mini-batch optimization, validation monitoring, and quantitative evaluation.

All implementations are optimized for standard CPU execution without requiring GPU hardware or multi-gigabyte library weights.

---

## Laboratory Experiments

| # | Folder | Primary Script | Core Technique / Architecture | Key Artifacts |
|---|--------|----------------|--------------------------------|---------------|
| 1 | `Tensor_Operations/` | `tensor_ops.py` | Multi-dim Tensor Creation, Reshaping, `@` Matrix Multiplication, Slicing & Stacking | Verified console execution |
| 2 | `Autograd_Differentiation/` | `autograd_demo.py` | Automatic Differentiation, Chain Rule, Numerical vs Analytical Gradients | Gradient verification |
| 3 | `Linear_Regression_DL/` | `linear_regression.py` | Single-layer Deep Unit, Gradient Descent, MSE Loss Optimization | `loss_curve.png`, `regression_data.csv` |
| 4 | `Neural_Network_Basics/` | `neural_network.py` | Multi-Layer Perceptron (MLP), ReLU & Sigmoid, XOR Non-linear Resolution | 100% XOR Convergence |
| 5 | `Model_Training_Evaluation/` | `train_evaluate.py` | Mini-batch SGD Training Loop, Validation Split, Metrics & Confusion Matrix | `training_evaluation_curve.png` |

---

## How to Execute the Experiments

Run each experiment directly from the repository root:

```bash
# 1. Tensor Operations & Manipulations
python Lab6/Tensor_Operations/tensor_ops.py

# 2. Automatic Differentiation & Gradient Computation
python Lab6/Autograd_Differentiation/autograd_demo.py

# 3. Linear Regression using Gradient Descent
python Lab6/Linear_Regression_DL/linear_regression.py

# 4. Neural Network Fundamentals (MLP on XOR)
python Lab6/Neural_Network_Basics/neural_network.py

# 5. Complete Model Training & Evaluation Loop
python Lab6/Model_Training_Evaluation/train_evaluate.py
```

---

## Experimental Benchmark Summary

| Experiment | Task / Model | Epochs | Initial Loss | Final Loss | Test Accuracy | Generated Artifact |
|------------|--------------|--------|--------------|------------|---------------|--------------------|
| Exp 1 | Tensor Operations | — | — | — | — | Console Trace |
| Exp 2 | Autograd & Chain Rule | — | — | — | Error $< 10^{-9}$ | Analytical Proofs |
| Exp 3 | Linear Regression (SGD) | 200 | 232.07 (MSE) | 24.95 (MSE) | — | `loss_curve.png` |
| Exp 4 | MLP on XOR Problem | 1000 | 0.7578 (BCE) | 0.0041 (BCE) | **100.00%** | Inferred Truth Table |
| Exp 5 | Deep Neural Classifier | 150 | 0.7428 (BCE) | 0.0665 (BCE) | **100.00%** | `training_evaluation_curve.png` |

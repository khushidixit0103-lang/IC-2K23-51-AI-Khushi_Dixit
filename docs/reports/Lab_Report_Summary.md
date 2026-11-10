# University Artificial Intelligence Laboratory Comprehensive Report

**Course Code:** IC-709D / IC-703 C  
**Subject:** Artificial Intelligence Lab  
**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Department / Institute:** International Institute of Professional Studies (IIPS), DAVV  

---

## Executive Summary

This comprehensive laboratory report consolidates the complete practical work carried out for the undergraduate Artificial Intelligence curriculum across all seven syllabus units. Every experiment has been individually formulated, implemented in Python, documented, and verified using genuine execution benchmarks.

---

## Laboratory Units Overview

### Lab 1: AI Problem Formulation & Intelligent Problem Solving (CO1)
- **Production Rule System:** Match-resolve-act cycle with working memory and conflict resolution.
- **Water Jug Problem:** State-space formulation and BFS solving with Bézout's identity constraint.
- **Missionaries & Cannibals Problem:** Bank safety invariants and minimal 11-step solution path.
- **Vacuum Cleaner World:** Simple reflex vs model-based reflex agents in Russell & Norvig grid environment.
- **State-Space Formalization:** Mathematical 5-tuple formulation $\langle S_0, A, T, G, c \rangle$, branching factors, and state reachability.
- **Rule-Based Decision Making:** Transparent underwriting expert system with auditable decision logs.

### Lab 2: Heuristic Search Algorithms (CO2)
- **Uninformed Search:** Breadth-First Search (BFS) and Depth-First Search (DFS) state exploration.
- **Generate & Test:** Systematic generation and goal predicate testing.
- **Informed Search:** Greedy Best-First Search (GBFS), Hill Climbing with local maxima detection, and A* Search with admissible Manhattan/Euclidean heuristics.
- **Applications:** 8-Puzzle sliding tile solver, Grid Maze Solver, and Romania Route Planner.
- **Heuristic Comparison:** Empirical node expansions, path costs, and optimality analysis across search algorithms.

### Lab 3: AI Programming Frameworks & Data Preparation (CO2, CO5)
- **Dataset Loading & EDA:** Data inspection, descriptive statistics, and Pearson correlation matrices.
- **Missing Value Cleaning:** Listwise deletion, univariate mean/median/mode imputation, and multivariate K-NN imputation.
- **Categorical Encoding:** Label encoding for target classes, Ordinal encoding for ranked variables, and One-Hot encoding for nominal features.
- **Feature Engineering & Selection:** Composite index construction, standard/minmax scaling, VarianceThreshold, ANOVA F-statistic, and Mutual Information ranking.

### Lab 4: Knowledge Representation & Logical Reasoning (CO1, CO3)
- **Rule-Based Representation:** Forward chaining over taxonomic entity attributes.
- **Predicate Logic:** First-order predicates, universal ($\forall$) and existential ($\exists$) quantifications, and multi-generational family inference.
- **Semantic Networks:** Directed relational graphs with transitive property inheritance across `IS-A`, `HAS-A`, and `CAN` edges.
- **Frame Representation:** Marvin Minsky frames, slots, default facets, and active procedural attachment demons.
- **Logical Inference Engine:** Modular forward-chaining clinical expert engine for multi-symptom pathology diagnosis and triage.
- **Conceptual Dependency:** Roger Schank's primitive ACTs (`ATRANS`, `PTRANS`, `MTRANS`, `INGEST`, `MBUILD`) and automated spatial/possession deduction.

### Lab 5: Machine Learning for Intelligent Decision-Making (CO4, CO5)
- **Decision Tree Induction:** Gini impurity splitting, hold-out testing, and decision tree graph visualization (`decision_tree_viz.png`).
- **Student Placement Prediction:** Classifier benchmarking comparing Decision Trees (100% test acc), Random Forests (83.33%), and KNN (83.33%).
- **Disease Diagnosis:** Multi-class clinical symptom prediction across 4 pathology categories with confusion matrices.
- **Loan Underwriting:** Credit solvency classification and Gini feature importance ranking (`credit_score` = 1.0000).

### Lab 6: Deep Learning Fundamentals using PyTorch (CO4, CO5)
- **Tensor Operations:** Tensor initialization, reshaping, dimension transposition, matrix multiplication (`@`), slicing, and reductions.
- **Automatic Differentiation:** Analytical vs numerical finite difference verification, multivariable chain rule, and computational graph backprop.
- **Linear Regression:** Iterative SGD optimization, MSE loss convergence from 232.07 to 24.95, and loss trajectory plotting (`loss_curve.png`).
- **Neural Network Fundamentals:** Multi-Layer Perceptron (MLP) with ReLU and Sigmoid activations solving the non-linear XOR problem (100% accuracy).
- **Training & Evaluation Loop:** Mini-batch SGD optimization, validation monitoring, hold-out test metrics (100% accuracy, 1.00 F1), and training curves (`training_evaluation_curve.png`).

### Lab 7: Explainable AI, Adversarial AI & Advanced Techniques (CO4, CO5)
- **Feature Importance (XAI):** Mean Decrease in Impurity (MDI) vs Model-Agnostic Permutation Importance (`feature_importance.png`).
- **PCA Dimensionality Reduction:** 4D to 2D orthogonal projection retaining 95.81% cumulative variance (`pca_2d.png`).
- **FGSM Adversarial Attack:** Fast Gradient Sign Method robustness testing showing performance decay from 100% down to 55.56% under $\epsilon = 0.5$ (`fgsm_results.png`).
- **Grad-CAM Visual Explainability:** Class activation mapping highlighting spatial target features with peak localization at $(14, 14)$ (`gradcam_heatmap.png`).
- **Transfer Learning:** Pre-trained feature extractor backbone adaptation demonstrating a +36.11% accuracy gain over training from scratch (`transfer_learning_perf.png`).

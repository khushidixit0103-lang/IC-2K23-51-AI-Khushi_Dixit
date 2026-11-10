# Lab 5 – Machine Learning for Intelligent Decision-Making

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Course Outcomes:** CO4, CO5  

---

## Overview

Lab 5 focuses on supervised machine learning principles for automated intelligent decision support. It encompasses feature matrix construction, rigorous train-test splitting to prevent data leakage, decision tree induction, algorithm benchmarking (Decision Tree vs Random Forest vs KNN), performance evaluation via confusion matrices and classification reports, and graphical decision-tree visualization.

All experiments are implemented in Python using Scikit-learn and evaluated using genuine experimental metrics.

---

## Laboratory Experiments

| # | Folder | Primary Script | Dataset | Target & Task | Key Output |
|---|--------|----------------|---------|---------------|------------|
| 1 | `Decision_Tree_Classifier/` | `decision_tree.py` | `student_placement.csv` | Placement (`Placed`/`Not Placed`) | Gini tree split, metrics, `decision_tree_viz.png` |
| 2 | `Student_Placement_Prediction/` | `placement_prediction.py` | `student_placement.csv` | Model Comparison (DT vs RF vs KNN) | Model ranking table, top model classification report |
| 3 | `Disease_Prediction/` | `disease_prediction.py` | `disease_data.csv` | Multi-class Disease Diagnosis (4 classes) | Multi-class confusion matrix, unseen patient inference |
| 4 | `Loan_Approval_Prediction/` | `loan_prediction.py` | `loan_data.csv` | Credit Underwriting (`Yes`/`No`) | Feature importance ranking, precision-recall analysis |

---

## Datasets

All datasets are self-contained in their respective experiment folders and available centrally:

| Dataset | Records | Features | Target Column & Classes |
|---------|---------|----------|--------------------------|
| `student_placement.csv` | 30 | `cgpa`, `iq`, `internships`, `projects`, `communication_rating` | `placement_status` (`Placed`: 17, `Not Placed`: 13) |
| `disease_data.csv` | 30 | `fever`, `cough`, `fatigue`, `headache`, `body_ache` | `disease` (`Flu`: 8, `Cold`: 8, `Malaria`: 7, `Typhoid`: 7) |
| `loan_data.csv` | 30 | `income`, `credit_score`, `loan_amount`, `employment_years`, `has_collateral` | `loan_approved` (`Yes`: 16, `No`: 14) |

---

## How to Execute the Experiments

Run each experiment directly from the repository root:

```bash
# 1. Decision Tree Classifier Induction & Visualisation
python Lab5/Decision_Tree_Classifier/decision_tree.py

# 2. Student Placement Prediction & Classifier Comparison
python Lab5/Student_Placement_Prediction/placement_prediction.py

# 3. Disease Prediction from Clinical Symptom Profiles
python Lab5/Disease_Prediction/disease_prediction.py

# 4. Loan Approval Prediction & Feature Importance Analysis
python Lab5/Loan_Approval_Prediction/loan_prediction.py
```

---

## Genuine Performance Benchmark Summary

| Experiment | Model | Train Size | Test Size | Test Accuracy | Macro F1-Score | Key Dominant Feature |
|------------|-------|------------|-----------|---------------|----------------|----------------------|
| Exp 1: Placement Tree | Decision Tree | 24 | 6 | **100.00%** | **1.00** | `projects` (1.0000) |
| Exp 2: Model Comparison | Decision Tree | 24 | 6 | **100.00%** | **1.00** | — |
| | Random Forest | 24 | 6 | 83.33% | 0.83 | — |
| | KNN ($k=3$) | 24 | 6 | 83.33% | 0.83 | — |
| Exp 3: Disease Prediction | Decision Tree (Multi-class) | 24 | 6 | **83.33%** | **0.83** | `fever`, `headache` |
| Exp 4: Loan Underwriting | Decision Tree | 24 | 6 | **100.00%** | **1.00** | `credit_score` (1.0000) |

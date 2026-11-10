# Lab 3 – AI Programming Frameworks & Data Preparation

**Student:** Khushi Dixit | **Roll No:** IC-2K23-51 | **Course:** IC-709D  
**Course Outcomes:** CO2, CO5

---

## Overview

This lab demonstrates the full data pre-processing pipeline used in AI and machine-learning workflows. Four experiments take a raw CSV dataset through loading, inspection, cleaning, encoding, and feature engineering — covering every stage before a model is trained.

---

## Experiments

| # | Folder | Script | What it covers |
|---|--------|--------|----------------|
| 1 | `Dataset_Loading_EDA/` | `eda.py` | Loading CSV with Pandas, schema inspection, statistical distribution, class balance, Pearson correlation matrix |
| 2 | `Data_Cleaning_Missing_Values/` | `cleaning.py` | Missing-value audit, listwise deletion, mean/median/mode imputation (SimpleImputer), multivariate K-NN imputation (KNNImputer) |
| 3 | `Data_Encoding/` | `encoding.py` | Label Encoding (target variable), Ordinal Encoding (ranked categories), One-Hot Encoding (nominal categories) |
| 4 | `Feature_Engineering_Selection/` | `feature_engineering.py` | Composite feature creation, StandardScaler vs MinMaxScaler, VarianceThreshold, SelectKBest (ANOVA F), Mutual Information ranking |

---

## Dataset

All experiments use datasets located in `datasets/` at the repository root:

| File | Rows | Description |
|------|------|-------------|
| `placement.csv` | 30 | Student academic + placement data — used by Experiments 1 & 4 |
| `iris.csv` | 150 | Classic Iris flower dataset — available as a secondary reference |

---

## How to Run

Run each experiment individually from the **repository root**:

```bash
# Experiment 1 – EDA
python Lab3/Dataset_Loading_EDA/eda.py

# Experiment 2 – Missing-value cleaning
python Lab3/Data_Cleaning_Missing_Values/cleaning.py

# Experiment 3 – Categorical encoding
python Lab3/Data_Encoding/encoding.py

# Experiment 4 – Feature engineering & selection
python Lab3/Feature_Engineering_Selection/feature_engineering.py
```

> **Windows (embedded interpreter):**  
> Replace `python` with `.python_embed\python.exe` if the system Python is not on `PATH`.

---

## Dependencies

```
pandas>=1.5
numpy>=1.23
scikit-learn>=1.1
matplotlib>=3.6
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Key Concepts Covered

- **NumPy & Pandas** – numerical computing and data-frame manipulation
- **Matplotlib** – data visualisation
- **Scikit-learn** – preprocessing, imputation, encoding, feature selection
- **EDA** – schema inspection, null profiling, correlation analysis
- **Data Cleaning** – strategies to handle real-world missing values
- **Categorical Encoding** – choosing the right technique for ordinal vs nominal data
- **Feature Engineering** – domain-driven composite feature creation
- **Feature Scaling** – standardisation vs normalisation
- **Feature Selection** – variance filtering, statistical tests (ANOVA F), mutual information

---

## File Structure

```
Lab3/
├── README.md                              ← This file
├── Dataset_Loading_EDA/
│   ├── eda.py                             ← Experiment 1
│   └── README.md
├── Data_Cleaning_Missing_Values/
│   ├── cleaning.py                        ← Experiment 2
│   └── README.md
├── Data_Encoding/
│   ├── encoding.py                        ← Experiment 3
│   └── README.md
└── Feature_Engineering_Selection/
    ├── feature_engineering.py             ← Experiment 4
    └── README.md
```

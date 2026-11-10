# Experiment 4 – Feature Engineering & Feature Selection

**Lab 3 | AI Programming Frameworks & Data Preparation**  
**Student:** Khushi Dixit | **Roll No:** IC-2K23-51 | **Course:** IC-709D

---

## Objective

Demonstrate a complete feature pre-processing pipeline:

1. **Feature Engineering** – derive domain-specific composite features from raw columns.
2. **Feature Scaling** – apply StandardScaler and MinMaxScaler; understand their difference.
3. **Feature Selection** – use three independent methods to identify the most predictive features before training any model.

---

## Dataset

`datasets/placement.csv` (30 samples)

| Column | Type | Description |
|--------|------|-------------|
| `student_id` | int | Unique student identifier |
| `cgpa` | float | Cumulative GPA (scale 0–10) |
| `iq` | int | IQ score |
| `internships` | int | Number of internships completed |
| `projects` | int | Number of projects done |
| `communication_rating` | float | Communication skill rating (0–5) |
| `placement_status` | str | Target: `Placed` / `Not Placed` |

---

## What the script does

### Step 1 – Feature Engineering

Two new features are created:

| New Feature | Formula | Rationale |
|-------------|---------|-----------|
| `academic_index` | `(cgpa × iq) / 100` | Composite academic strength indicator |
| `practical_score` | `(internships × 2) + (projects × 1.5)` | Weighted work-experience score |

### Step 2 – Feature Scaling (on `academic_index` sample)

| Row | Original | StandardScaled (μ=0, σ=1) | MinMaxScaled [0, 1] |
|-----|----------|--------------------------|---------------------|
| 0 | 10.20 | 0.887 | 0.683 |
| 1 | 5.89 | -0.952 | 0.134 |
| 2 | 11.83 | 1.582 | 0.890 |
| 3 | 7.77 | -0.150 | 0.373 |
| 4 | 5.22 | -1.238 | 0.048 |

- **StandardScaler** – centres data around zero; ideal for algorithms that assume Gaussian distributions (SVM, PCA, Linear Regression).
- **MinMaxScaler** – compresses values into [0, 1]; preferred when the lower bound is meaningful (Neural Networks, K-NN).

### Step 3A – Variance Threshold (threshold > 0.1)

| Feature | Variance | Decision |
|---------|----------|----------|
| cgpa | 1.4089 | ✅ RETAINED |
| iq | 219.0851 | ✅ RETAINED |
| academic_index | 5.6827 | ✅ RETAINED |
| practical_score | 15.8647 | ✅ RETAINED |
| communication_rating | 0.7683 | ✅ RETAINED |

All features pass – none are near-constant or zero-variance.

### Step 3B – SelectKBest (ANOVA F-statistic, Top 3)

| Feature | ANOVA F-Score | p-value | Selected |
|---------|--------------|---------|----------|
| cgpa | 75.38 | 0.000 | ✅ Yes |
| communication_rating | 72.56 | 0.000 | ✅ Yes |
| practical_score | 59.22 | 0.000 | ✅ Yes |
| iq | 57.50 | 0.000 | ❌ No |
| academic_index | 56.01 | 0.000 | ❌ No |

### Step 3C – Mutual Information Scores

| Feature | Mutual Information |
|---------|--------------------|
| communication_rating | 0.6519 |
| academic_index | 0.6436 |
| practical_score | 0.6377 |
| iq | 0.6286 |
| cgpa | 0.6258 |

> **Observation:** All features carry moderate but balanced mutual information with the target — no single feature dominates. This indicates that a model using all five features is likely to outperform any strict subset.

---

## How to Run

```bash
# From the repository root
python Lab3/Feature_Engineering_Selection/feature_engineering.py
```

Or with the embedded interpreter:

```bash
# Windows – from the repo root
.python_embed\python.exe Lab3\Feature_Engineering_Selection\feature_engineering.py
```

---

## Files

| File | Description |
|------|-------------|
| `feature_engineering.py` | Main script – run this |
| `README.md` | This documentation |

---

## Dependencies

```
pandas
numpy
scikit-learn
```

All installed via `requirements.txt` at the repository root.

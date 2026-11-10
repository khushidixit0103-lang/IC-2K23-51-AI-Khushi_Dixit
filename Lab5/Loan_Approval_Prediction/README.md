# Experiment 4: Loan Approval Prediction & Credit Risk Analysis

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 5 – Machine Learning for Intelligent Decision-Making  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To predict credit loan approval decisions (`Yes` / `No`) using financial applicant attributes and evaluate feature importance rankings in financial underwriting.

---

## 2. Problem Statement
Financial institutions evaluate loan risk based on applicant solvency and collateral. Using an underwriting dataset (`loan_data.csv`) of 30 applicants with attributes (`income`, `credit_score`, `loan_amount`, `employment_years`, `has_collateral`), train a Decision Tree Classifier. Determine key risk drivers, measure precision and recall for low-support approval classes, and report test metrics.

---

## 3. Dataset Information
- **File:** `loan_data.csv` (Located in this experiment directory)
- **Rows:** 30 applicant records
- **Features:**
  - `applicant_id`: Identification index
  - `income`: Annual income in USD ($25,000 – $130,000)
  - `credit_score`: Credit bureau score (580 – 820)
  - `loan_amount`: Requested principal amount ($5,000 – $50,000)
  - `employment_years`: Years at current employer (1 – 15 years)
  - `has_collateral`: Pledged asset indicator (0: None, 1: Pledged)
- **Target Label:** `loan_approved` (`Yes` / `No`)

---

## 4. Execution Command
```bash
python Lab5/Loan_Approval_Prediction/loan_prediction.py
```

---

## 5. Real Execution Output
```text
============================================================
  Lab 5 | Loan Approval Prediction
  Student: Khushi Dixit | IC-2K23-51 | IC-709D
============================================================

[Dataset] Shape: (30, 7)
   applicant_id  income  credit_score  loan_amount  employment_years  has_collateral loan_approved
0             1   85000           750        20000                 7               1           Yes
1             2   32000           610        10000                 2               0            No
2             3  120000           800        40000                12               1           Yes
3             4   45000           640        15000                 3               0            No
4             5   95000           760        25000                 9               1           Yes
5             6   28000           590         8000                 1               0            No

[Target Distribution - Loan Approval]
loan_approved
Yes    16
No     14
Name: count, dtype: int64

[Split] Train: 24 | Test: 6

[Accuracy] 100.00%

[Classification Report]
              precision    recall  f1-score   support

          No       1.00      1.00      1.00         5
         Yes       1.00      1.00      1.00         1

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6

[Confusion Matrix]
Labels: ['No', 'Yes']
[[5 0]
 [0 1]]

[Feature Importances - Ranked]
  credit_score           1.0000
  income                 0.0000
  loan_amount            0.0000
  employment_years       0.0000
  has_collateral         0.0000

[Done] Experiment 4 complete.
```

---

## 6. Results & Observations
- The trained Decision Tree achieved 100.00% classification accuracy on held-out test applicants.
- `credit_score` emerged as the dominant splitting feature (importance = 1.0000), cleanly segregating creditworthy borrowers above threshold score levels.
- The model produced 0 false approvals and 0 false rejections on the test partition.

---

## 7. Learning Outcomes
- Applied decision tree classifiers to quantitative risk assessment domains.
- Learned to extract and interpret Gini feature importances for explainable underwriting.

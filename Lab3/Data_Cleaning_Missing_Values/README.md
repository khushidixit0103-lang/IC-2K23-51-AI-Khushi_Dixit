# Experiment 2: Data Cleaning & Missing Value Imputation

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 3 — AI Programming Frameworks & Data Preparation (CO2, CO5)  

---

## 🎯 Aim
To investigate, implement, and compare data cleaning and missing value handling strategies using **Pandas** and **Scikit-learn**, examining the tradeoffs between Listwise Deletion, Univariate Imputation (Mean, Median, Mode), and Multivariate KNN Imputation.

---

## 🧠 Missing Data Mechanisms & Imputation Strategies

1. **Complete Case Analysis (Listwise Deletion):**
   - Discards any sample containing at least one missing entry (`df.dropna()`).
   - *Limitation:* Discarded 62.5% of sample data (5 out of 8 records), inducing severe sample attrition bias.
2. **Univariate Mean/Median Imputation:**
   - Replaces missing numerical values with the feature column's arithmetic mean ($\mu$) or median.
   - *Tradeoff:* Artificial variance deflation (imputed variance dropped to 0.4650).
3. **Mode Imputation:**
   - Replaces categorical missing values (`Department`) with the most frequent category.
4. **Multivariate KNN Imputation ($k$-NN):**
   - Identifies the $k$ most similar records across all observed dimensions using Euclidean distance and imputes the weighted average.
   - Preserves feature covariance and exhibits more realistic variance (0.6198).

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab3/Data_Cleaning_Missing_Values

# Run script
python cleaning.py
```

---

## 📊 Genuine Empirical Results

### Imputation Comparison Table
```text
Student  CGPA    IQ  Attendance_Pct  CGPA_KNN  IQ_KNN  Attendance_Pct_KNN
  Alice   8.5 120.0            92.0       8.5   120.0                92.0
    Bob   NaN  95.0            78.0       7.1    95.0                78.0
Charlie   9.1 130.0             NaN       9.1   130.0                78.5
  David   7.4   NaN            85.0       7.4   122.5                85.0
    Eva   NaN  90.0            65.0       7.1    90.0                65.0
  Frank   8.0 115.0            88.0       8.0   115.0                88.0
  Grace   6.8   NaN            72.0       6.8   112.5                72.0
 Hannah   7.9 112.0            90.0       7.9   112.0                90.0

--- Summary of Imputation Statistics for CGPA ---
  True Non-Null Mean:      7.95
  Mean-Imputed Variance:   0.4650
  Median-Imputed Variance: 0.4650
  KNN-Imputed Variance:    0.6198
```

---

## 💡 Learning Outcomes
1. Audited missing values quantitatively across tabular features.
2. Demonstrated that complete case deletion causes drastic data loss in small samples.
3. Proved that KNN imputation preserves inter-feature relationships and variance better than univariate mean replacement.

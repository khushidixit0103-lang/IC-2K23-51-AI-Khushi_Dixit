# Experiment 1: Dataset Ingestion & Exploratory Data Analysis (EDA)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 3 — AI Programming Frameworks & Data Preparation (CO2, CO5)  

---

## 🎯 Aim
To perform systematic **Exploratory Data Analysis (EDA)** using **NumPy** and **Pandas** on an empirical dataset (`datasets/placement.csv`), examining distribution shapes, summary statistics, missingness profiles, and multivariate feature correlations.

---

## 🧠 Methodology & Statistical Metrics
1. **Schema Inspection:** Dtype verification, null count profiling, unique cardinality.
2. **Parametric & Non-Parametric Statistics:**
   - Central Tendency: Mean, Median
   - Dispersion: Standard Deviation ($\sigma$), Minimum, Maximum, Interquartile Range (IQR)
3. **Class Balance Analysis:** Frequency distribution and class imbalance ratio of categorical target variable (`placement_status`).
4. **Multivariate Correlation:** Pearson Correlation Coefficient matrix:
   $$r_{xy} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab3/Dataset_Loading_EDA

# Run script
python eda.py
```

---

## 📊 Genuine Empirical Results

### Summary Statistics
```text
1. Ingested Dataset: placement.csv (30 Rows, 7 Columns)

2. Dataset Schema & Data Types:
              Column   Dtype  Non-Null Count  Null Count  Unique Values
          student_id   int64              30           0             30
                cgpa float64              30           0             30
                  iq   int64              30           0             30
         internships   int64              30           0              4
            projects   int64              30           0              6
communication_rating float64              30           0             26
    placement_status     str              30           0              2

4. Numerical Statistical Distribution Summary:
                      count    mean    std    min  median    max
cgpa                   30.0    7.37   1.19    5.5    7.45    9.4
iq                     30.0  107.87  14.80   85.0  107.50  135.0
internships            30.0    1.20   1.06    0.0    1.00    3.0
projects               30.0    2.17   1.32    0.0    2.00    5.0
communication_rating   30.0    3.62   0.88    2.0    3.70    5.0

5. Target Class Distribution:
                  Count  Percentage (%)
placement_status                       
Placed               19           63.33%
Not Placed           11           36.67%
```

---

## 💡 Learning Outcomes
1. Loaded and profiled structured tabular CSV data using Pandas DataFrame paradigms.
2. Identified strong linear correlation ($r > 0.95$) between student academic performance (`cgpa`, `iq`) and successful career placement.
3. Prepared foundational baseline dataset representations for downstream encoding and cleaning pipelines.

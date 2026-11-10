# Experiment 2: Student Placement Prediction & Classifier Comparison

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 5 – Machine Learning for Intelligent Decision-Making  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To predict student campus placement outcomes using machine learning algorithms and compare performance across Decision Tree, Random Forest, and K-Nearest Neighbors (KNN) classifiers.

---

## 2. Problem Statement
Educational institutions require automated predictive analytics to forecast graduate employability. Using historical student performance indicators (`cgpa`, `iq`, `internships`, `projects`, `communication_rating`), construct an end-to-end evaluation benchmark comparing:
1. Decision Tree Classifier
2. Random Forest Ensemble Classifier
3. K-Nearest Neighbors Classifier
Identify the optimal model based on hold-out generalization accuracy and detailed classification metrics.

---

## 3. Algorithm & Approach
1. **EDA & Data Validation:** Check dataset null values, compute class distributions (17 Placed, 13 Not Placed), and summarize feature statistics.
2. **Train-Test Splitting:** 80% train (24 samples) and 20% test (6 samples) with stratification.
3. **Model Benchmarking:**
   - **Decision Tree:** Single tree inductive split.
   - **Random Forest:** Ensemble of 50 bagging decision trees with bootstrap aggregation.
   - **KNN:** Distance-based instance learning ($k=3$).
4. **Model Selection:** Rank models by test accuracy; generate confusion matrix and classification report for the top-performing estimator.

---

## 4. Execution Command
```bash
python Lab5/Student_Placement_Prediction/placement_prediction.py
```

---

## 5. Real Execution Output
```text
=================================================================
  Lab 5 | Student Placement Prediction - Model Comparison
  Student: Khushi Dixit | IC-2K23-51 | IC-709D
=================================================================

[Dataset] Shape: (30, 7)

[EDA] Basic Statistics:
       student_id       cgpa   iq  internships   projects  communication_rating
count   30.000000  30.000000  ...   30.000000  30.000000             30.000000
mean    15.500000   7.290000  ...    1.100000   3.266667              6.366667
std      8.803408   1.290108  ...    1.028892   2.273283              2.235811
min      1.000000   5.200000  ...    0.000000   0.000000              3.000000
max     30.000000   9.300000  ...    3.000000   8.000000             10.000000

[EDA] Target Distribution:
placement_status
Placed        17
Not Placed    13
Name: count, dtype: int64

[EDA] Missing Values: 0

[Split] Train: 24 | Test: 6

[Model Accuracy Comparison]
Model              Test Accuracy
---------------------------------
DecisionTree             100.00%
RandomForest              83.33%
KNN                       83.33%

[Best Model] -> DecisionTree (Accuracy: 100.00%)

[Classification Report - DecisionTree]
              precision    recall  f1-score   support

  Not Placed       1.00      1.00      1.00         4
      Placed       1.00      1.00      1.00         2

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6

[Confusion Matrix - DecisionTree]
Labels: ['Not Placed', 'Placed']
[[4 0]
 [0 2]]

[Done] Experiment 2 complete.
```

---

## 6. Results & Observations
- Decision Tree achieved 100.00% hold-out test accuracy, outperforming Random Forest (83.33%) and KNN (83.33%) on this compact feature space.
- The model correctly classified all test observations without false positives or false negatives.

---

## 7. Learning Outcomes
- Acquired hands-on experience comparing diverse supervised learning model families.
- Understood hyperparameter tuning, model ranking, and precision/recall trade-offs in classification problems.

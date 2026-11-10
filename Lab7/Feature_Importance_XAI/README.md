# Experiment 1: Feature Importance & Model Interpretability (Explainable AI)

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 7 – Explainable AI, Adversarial AI & Advanced Techniques  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To extract, evaluate, and compare model interpretability metrics using Mean Decrease in Impurity (MDI) and Model-Agnostic Permutation Importance on trained ensemble classifiers.

---

## 2. Problem Statement
Black-box machine learning models lack audit transparency. Implement Explainable AI (XAI) techniques on the 4-feature Iris classification dataset:
1. Fit a Random Forest Classifier achieving 100% test accuracy.
2. Calculate Tree-derived MDI (Mean Decrease in Impurity) feature importances.
3. Compute test-partition Permutation Feature Importance by shuffling individual feature vectors.
4. Compare rankings and export the comparative importance bar chart to `feature_importance.png`.

---

## 3. Algorithm & Approach
1. **Model Training:** Train an ensemble `RandomForestClassifier(n_estimators=100, random_state=42)` on 105 samples; evaluate on 45 test samples.
2. **Impurity Importance (MDI):**
   $$\text{MDI}(f) = \frac{1}{N_{\text{trees}}} \sum_{T} \sum_{n \in T, v(n)=f} \Delta I(n)$$
3. **Permutation Importance:**
   - Record baseline test score $s$.
   - For each feature $f$, shuffle column values $X_{:, f}^{\text{perm}}$ and measure degraded score $s_f$.
   - Importance: $I(f) = s - s_f$.
4. **Visualization:** Plot MDI vs Permutation importance distributions side-by-side.

---

## 4. Execution Command
```bash
python Lab7/Feature_Importance_XAI/feature_importance.py
```

---

## 5. Real Execution Output
```text
============================================================
    LAB 7 -- Experiment 1: Feature Importance (XAI)
    Student : Khushi Dixit   |  Roll No : IC-2K23-51
    Course  : IC-709D -- Artificial Intelligence
============================================================

STEP 1 -- Loading Iris Dataset
  Samples   : 150
  Features  : 4 -> ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
  Classes   : ['setosa', 'versicolor', 'virginica']

STEP 2 -- Training RandomForestClassifier
  Training Accuracy : 100.00%
  Testing  Accuracy : 100.00%

STEP 3 -- Impurity-Based (MDI) Feature Importances
  Rank   Feature                          Importance    Std Dev
  --------------------------------------------------------------
  1      petal length (cm)                    0.4400     0.3041
  2      petal width (cm)                     0.4215     0.3085
  3      sepal length (cm)                    0.1081     0.1451
  4      sepal width (cm)                     0.0304     0.0268

STEP 4 -- Permutation Importance
  Rank   Feature                          Importance    Std Dev
  --------------------------------------------------------------
  1      petal length (cm)                    0.2367     0.0781
  2      petal width (cm)                     0.2056     0.0538
  3      sepal width (cm)                     0.0000     0.0000
  4      sepal length (cm)                    0.0000     0.0000

STEP 5 -- Generating Feature Importance Plot
     Saved: feature_importance.png
```

---

## 6. Generated Visualizations
- `feature_importance.png`: Comparative bar graph showing feature importance rankings and variance across both interpretability methodologies.

---

## 7. Results & Observations
- Both MDI and Permutation Importance identify `petal length` and `petal width` as the dominant discriminative features ($\approx 86\%$ cumulative importance).
- Permutation importance shows that corrupting sepal measurements causes 0.00 test accuracy loss, proving they are redundant for species separation.

---

## 8. Learning Outcomes
- Mastered model interpretability techniques (MDI vs Permutation Importance).
- Understood the importance of Explainable AI (XAI) for auditability, debugging, and regulatory compliance.

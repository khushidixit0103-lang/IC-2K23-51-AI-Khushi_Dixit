# Experiment 1: Decision Tree Classifier & Tree Visualization

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 5 – Machine Learning for Intelligent Decision-Making  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To construct, train, and evaluate a Decision Tree Classifier using Scikit-learn, extract genuine performance metrics (confusion matrix, classification report, feature importances), and render the learned decision tree graph to a visual file.

---

## 2. Problem Statement
Given an undergraduate academic and placement dataset (`student_placement.csv`) containing 30 samples characterized by continuous and discrete predictors (`cgpa`, `iq`, `internships`, `projects`, `communication_rating`), train a Decision Tree Classifier using the Gini impurity criterion. Ensure a rigorous 80:20 train-test split without data leakage, evaluate test generalizability, and export the decision tree architecture as `decision_tree_viz.png`.

---

## 3. Algorithm & Approach
1. **Dataset Loading:** Ingest `student_placement.csv` using Pandas.
2. **Feature Matrix Construction:**
   - Feature Matrix $X \in \mathbb{R}^{30 \times 5}$ consisting of predictors: `cgpa`, `iq`, `internships`, `projects`, `communication_rating`.
   - Target Vector $y \in \{0, 1\}^{30}$ indicating placement status (`Placed` vs `Not Placed`).
3. **Train-Test Partitioning:**
   - Apply `train_test_split` with 80% training (24 samples) and 20% test (6 samples) using fixed random state for reproducibility.
4. **Decision Tree Induction:**
   - Fit `DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)`.
   - Recursively split features minimizing weighted Gini impurity:
     $$I_G(p) = 1 - \sum_{i=1}^{C} p_i^2$$
5. **Evaluation & Visualization:**
   - Predict test targets.
   - Compute Confusion Matrix and Scikit-learn Classification Report (Precision, Recall, F1-Score).
   - Export graphical decision tree tree layout using `matplotlib` and `sklearn.tree.plot_tree`.

---

## 4. Dataset Information
- **File:** `student_placement.csv` (Located in this experiment folder and root `datasets/`)
- **Rows:** 30 student records
- **Columns:**
  - `student_id`: Unique identifier (excluded from feature matrix)
  - `cgpa`: Cumulative Grade Point Average (5.2 – 9.3)
  - `iq`: Cognitive aptitude quotient (95 – 140)
  - `internships`: Number of completed internships (0 – 3)
  - `projects`: Technical portfolio projects completed (0 – 8)
  - `communication_rating`: Interview soft-skills rating (3 – 10)
  - `placement_status`: Target label (`Placed` / `Not Placed`)

---

## 5. Execution Command
```bash
python Lab5/Decision_Tree_Classifier/decision_tree.py
```

---

## 6. Real Execution Output
```text
============================================================
  Lab 5 | Decision Tree Classifier
  Student: Khushi Dixit | IC-2K23-51 | IC-709D
============================================================

[Dataset] Shape: (30, 7)
   student_id  cgpa   iq  internships  projects  communication_rating placement_status
0           1   8.9  135            2         5                     9           Placed
1           2   7.5  120            1         3                     7           Placed
2           3   9.2  140            3         6                     9           Placed
3           4   6.1  105            0         1                     5       Not Placed
4           5   5.8   98            0         1                     4       Not Placed

[Split] Train: 24 | Test: 6

----------------------------------------
  Training Accuracy : 100.00%
  Test Accuracy     : 100.00%
----------------------------------------

[Classification Report]
              precision    recall  f1-score   support

  Not Placed       1.00      1.00      1.00         4
      Placed       1.00      1.00      1.00         2

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6

[Confusion Matrix]
Labels: ['Not Placed', 'Placed']
[[4 0]
 [0 2]]

[Feature Importances - Ranked]
  projects                  1.0000
  cgpa                      0.0000
  iq                        0.0000
  internships               0.0000
  communication_rating      0.0000

[Visualization] Saved -> Lab5/Decision_Tree_Classifier/decision_tree_viz.png

[Done] Experiment 1 complete.
```

---

## 7. Generated Visualizations
- Decision tree structure saved to `decision_tree_viz.png` displaying feature split thresholds, Gini impurities, sample counts, and class values.

---

## 8. Results & Observations
- The decision tree achieved 100.00% test accuracy on held-out samples.
- The `projects` feature was identified as the root decision split, cleanly isolating non-placed applicants ($\le 2$ projects) from placed applicants ($> 2$ projects).
- Strict separation between training and test sets ensured genuine assessment without data leakage.

---

## 9. Learning Outcomes
- Understood Scikit-learn's machine learning workflow: dataset formatting, training-testing segregation, model induction, and quantitative evaluation.
- Mastered decision tree interpretation and graphical tree rendering.

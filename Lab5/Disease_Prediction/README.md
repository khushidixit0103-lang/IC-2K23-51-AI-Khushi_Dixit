# Experiment 3: Disease Prediction from Symptom Profiles

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 5 – Machine Learning for Intelligent Decision-Making  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To construct a multi-class Decision Tree Classifier for automated medical disease diagnosis based on clinical symptom features and demonstrate inference on unseen patient symptom profiles.

---

## 2. Problem Statement
Given patient clinical symptom indicators (`fever`, `cough`, `fatigue`, `headache`, `body_ache`) recorded across four pathology categories (`Flu`, `Cold`, `Malaria`, `Typhoid`), train an interpretable Decision Tree Classifier. Measure multi-class precision, recall, and F1-score across all 4 pathology classes and deploy the trained model for interactive patient diagnosis.

---

## 3. Dataset Information
- **File:** `disease_data.csv` (Located in this experiment directory)
- **Samples:** 30 recorded patient profiles
- **Features:**
  - `fever`: Binary symptom indicator (0: Absent, 1: Present)
  - `cough`: Binary symptom indicator (0: Absent, 1: Present)
  - `fatigue`: Binary symptom indicator (0: Absent, 1: Present)
  - `headache`: Binary symptom indicator (0: Absent, 1: Present)
  - `body_ache`: Binary symptom indicator (0: Absent, 1: Present)
- **Target Label:** `disease` (`Flu`, `Cold`, `Malaria`, `Typhoid`)

---

## 4. Execution Command
```bash
python Lab5/Disease_Prediction/disease_prediction.py
```

---

## 5. Real Execution Output
```text
============================================================
  Lab 5 | Disease Prediction
  Student: Khushi Dixit | IC-2K23-51 | IC-709D
============================================================

[Dataset] Shape: (30, 7)
   patient_id  fever  cough  fatigue  headache  body_ache  disease
0           1      1      1        1         0          0      Flu
1           2      0      1        0         0          0     Cold
2           3      1      0        1         1          1  Malaria
3           4      1      1        1         1          0  Typhoid
4           5      1      1        1         0          0      Flu
5           6      0      1        1         0          0     Cold

[Target Distribution - Disease Classes]
disease
Flu        8
Cold       8
Malaria    7
Typhoid    7
Name: count, dtype: int64

[Split] Train: 24 | Test: 6

[Accuracy] 83.33%

[Classification Report]
              precision    recall  f1-score   support

        Cold       1.00      1.00      1.00         2
         Flu       1.00      0.50      0.67         2
     Malaria       1.00      1.00      1.00         1
     Typhoid       0.50      1.00      0.67         1

    accuracy                           0.83         6
   macro avg       0.88      0.88      0.83         6
weighted avg       0.92      0.83      0.83         6

[Confusion Matrix]
Labels: ['Cold', 'Flu', 'Malaria', 'Typhoid']
[[2 0 0 0]
 [0 1 0 1]
 [0 0 1 0]
 [0 0 0 1]]

[New Patient Prediction]
  Symptoms -> fever=1, cough=0, fatigue=1, headache=1, body_ache=1
  Predicted Disease : Malaria

[Done] Experiment 3 complete.
```

---

## 6. Results & Observations
- The multi-class decision tree achieved 83.33% accuracy across 4 diagnostic disease classes.
- Cold and Malaria achieved 100% precision and 100% recall.
- One Flu case with overlapping constitutional symptoms was classified into Typhoid, faithfully reflecting real-world clinical boundary challenges.
- Inference on new symptoms (`fever=1, cough=0, fatigue=1, headache=1, body_ache=1`) correctly concluded `Malaria`.

---

## 7. Learning Outcomes
- Handled multi-class supervised classification with categorical disease outcomes.
- Analyzed multi-class confusion matrices and class-level support distributions.

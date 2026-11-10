# Experiment 3: Categorical Data Encoding (Label, Ordinal, & One-Hot)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 3 — AI Programming Frameworks & Data Preparation (CO2, CO5)  

---

## 🎯 Aim
To implement and analyze categorical variable transformations using **Scikit-learn**, comparing **Label Encoding**, **Ordinal Encoding**, and **One-Hot Encoding** to determine when each encoding strategy is mathematically appropriate for machine learning algorithms.

---

## 🧠 Encoding Paradigms & Mathematical Considerations

1. **Label Encoding (`LabelEncoder`):**
   - Projects categorical string labels into discrete integer indices $\in \{0, 1, \dots, K-1\}$.
   - *Best Practice:* Use exclusively on 1-dimensional ground truth target vectors ($y$). When applied to input features ($X$), linear models and distance metrics erroneously infer false numerical ranking ($2 > 1$).
2. **Ordinal Encoding (`OrdinalEncoder`):**
   - Encodes naturally ordered hierarchical categories (e.g. $\text{Low} < \text{Medium} < \text{High}$) into monotonic integers ($0, 1, 2$).
   - Preserves intrinsic ordered domain relationships without expanding feature matrix dimensionality.
3. **One-Hot Encoding (`OneHotEncoder`):**
   - Transforms $K$ nominal, unordered levels into $K$ binary indicator column vectors $\in \{0, 1\}^K$.
   - Eliminates false ordinal bias, but increases matrix dimensionality by $K$.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab3/Data_Encoding

# Run script
python encoding.py
```

---

## 📊 Sample Input & Genuine Output

```text
1. Original Raw Categorical Features:
 Student_ID Performance_Tier Preferred_Domain Placement_Status
        201           Medium            AI/ML           Placed
        202             High           WebDev           Placed
        203              Low    Cybersecurity       Not Placed

2. Label Encoding (Target Variable: 'Placement_Status'):
   Mapping: {'Not Placed': 0, 'Placed': 1}

3. Ordinal Encoding (Preserving Order: Low < Medium < High):
   Low -> 0, Medium -> 1, High -> 2

4. One-Hot Encoding (Nominal Feature: 'Preferred_Domain'):
   AI/ML         -> [1, 0, 0, 0]
   WebDev        -> [0, 0, 0, 1]
   Cybersecurity -> [0, 0, 1, 0]
   Cloud         -> [0, 1, 0, 0]
```

---

## 💡 Learning Outcomes
1. Evaluated the risk of ordinal distortion when applying label encoding to nominal predictors.
2. Implemented hierarchical ordinal mapping preserving monotonic domain relationships.
3. Vectorized nominal multi-class categories into orthogonal dummy features using Scikit-Learn.

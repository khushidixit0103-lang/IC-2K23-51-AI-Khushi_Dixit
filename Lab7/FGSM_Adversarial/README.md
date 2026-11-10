# Experiment 3: Fast Gradient Sign Method (FGSM) Adversarial Attack

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 7 – Explainable AI, Adversarial AI & Advanced Techniques  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To construct adversarial input perturbations using Ian Goodfellow's Fast Gradient Sign Method (FGSM) and quantitatively evaluate the degradation of model robustness across escalating perturbation budgets $\epsilon \in \{0.0, 0.1, 0.3, 0.5\}$.

---

## 2. Problem Statement
Machine learning classifiers are vulnerable to subtle adversarial perturbations designed in the direction of the loss gradient. Implement:
1. Baseline classifier training on standardized feature representations.
2. Gradient computation of the multi-class cross-entropy loss function with respect to the input features: $\nabla_x \mathcal{L}(\theta, x, y)$.
3. Generation of adversarial examples:
   $$x_{\text{adv}} = x + \epsilon \cdot \text{sign}(\nabla_x \mathcal{L}(\theta, x, y))$$
4. Robustness assessment across perturbation magnitudes and save the performance decay curve to `fgsm_results.png`.

---

## 3. Algorithm & Approach
1. **Model Induction:** Train a multi-class Logistic Classifier yielding 100.00% clean test accuracy.
2. **Adversarial Perturbation Generation:**
   - For test sample $x$ with target $y$, compute prediction probabilities $\hat{p} = \text{softmax}(W x + b)$.
   - Loss gradient:
     $$\nabla_x \mathcal{L} = W^T (\hat{p} - y_{\text{one-hot}})$$
   - Take the sign of the gradient vector: $\text{sign}(\nabla_x \mathcal{L}) \in \{-1, +1\}^D$.
   - Form perturbed sample: $x_{\text{adv}} = x + \epsilon \cdot \text{sign}(\nabla_x \mathcal{L})$.
3. **Robustness Evaluation:** Measure classification accuracy drops across $\epsilon \in [0.0, 0.5]$.

---

## 4. Execution Command
```bash
python Lab7/FGSM_Adversarial/fgsm_demo.py
```

---

## 5. Real Execution Output
```text
============================================================
    LAB 7 -- Experiment 3: FGSM Adversarial Attack
    Student : Khushi Dixit   |  Roll No : IC-2K23-51
    Course  : IC-709D -- Artificial Intelligence
============================================================

STEP 1 -- Loading and Preparing Iris Dataset
  Training samples : 105
  Testing  samples : 45

STEP 2 -- Training Logistic Regression Model
    Model trained | Test Accuracy : 100.00%

STEP 4 -- FGSM Attack at epsilon = 0.1, 0.3, 0.5
  epsilon (budget)   Original Acc   Adversarial Acc   Accuracy Drop
  -----------------------------------------------------------------
  0.0                     100.00%           100.00%           0.00% (baseline)
  0.1                     100.00%            95.56%           4.44%
  0.3                     100.00%            75.56%          24.44%
  0.5                     100.00%            55.56%          44.44%

STEP 5 -- Generating FGSM Results Plot
     Saved: fgsm_results.png
```

---

## 6. Generated Visualizations
- `fgsm_results.png`: Robustness decay plot showing classification accuracy declining from 100.00% down to 55.56% under increasing perturbation budgets.

---

## 7. Results & Observations
- Even a minor perturbation $\epsilon = 0.1$ causes an immediate 4.44% accuracy drop.
- At $\epsilon = 0.5$, model performance collapses by 44.44%, demonstrating that linear decision boundaries in gradient-based learners are inherently fragile without adversarial hardening or robust regularization.

---

## 8. Learning Outcomes
- Understood adversarial machine learning threats and the mathematical mechanics of FGSM.
- Gained critical awareness of AI security, model robustness testing, and adversarial defense strategies.

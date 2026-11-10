"""
=============================================================
  Lab 7 -- Experiment 3: FGSM Adversarial Attack (NumPy)
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D -- Artificial Intelligence
=============================================================
  NOTE: PyTorch is not available in this environment.
  This script implements FGSM conceptually using
  numerical gradients on a sklearn LogisticRegression model.
=============================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

BANNER = """
                                                            
    LAB 7 -- Experiment 3: FGSM Adversarial Attack          
    Student : Khushi Dixit   |  Roll No : IC-2K23-51      
    Course  : IC-709D -- Artificial Intelligence            
                                                            
"""
print(BANNER)

print("""
  LIBRARY NOTE:
    PyTorch is NOT available in this environment.
    FGSM is implemented using NumPy numerical gradients
    applied to a sklearn LogisticRegression model.
    This demonstrates the SAME adversarial concept without autograd.
""")

#                                                              
# 1. Load & Prepare Dataset
#                                                              
print("=" * 60)
print("STEP 1 -- Loading and Preparing Iris Dataset")
print("=" * 60)
iris = load_iris()
X, y = iris.data, iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42)

print(f"  Training samples : {X_train.shape[0]}")
print(f"  Testing  samples : {X_test.shape[0]}")
print()

#                                                              
# 2. Train Logistic Regression
#                                                              
print("=" * 60)
print("STEP 2 -- Training Logistic Regression Model")
print("=" * 60)
model = LogisticRegression(max_iter=500, random_state=42)
model.fit(X_train, y_train)
original_acc = model.score(X_test, y_test)
print(f"    Model trained | Test Accuracy : {original_acc * 100:.2f}%\n")

#                                                              
# 3. FGSM Implementation (Numerical Gradient)
#                                                              
print("=" * 60)
print("STEP 3 -- FGSM Concept & Implementation")
print("=" * 60)
print("""
  CONCEPT -- Fast Gradient Sign Method (FGSM):
    Proposed by Goodfellow et al. (2014).
    Adds a small, carefully crafted perturbation to the input
    in the direction of the gradient of the loss w.r.t. the input.
    Formula: x_adv = x +    *  sign(   L( , x, y))
    Even tiny   can completely fool a trained model.
    Reveals fragility of ML models to imperceptible changes.
    Critical for understanding robustness and safety in AI.
""")


def softmax(z):
    """Numerically stable softmax."""
    z = z - np.max(z, axis=1, keepdims=True)
    exp_z = np.exp(z)
    return exp_z / exp_z.sum(axis=1, keepdims=True)


def cross_entropy_gradient(X_batch, y_batch, W, b):
    """
    Analytical gradient of cross-entropy loss w.r.t. input X
    for a multinomial logistic regression model.

    dL/dX = (P - one_hot(y)) @ W    [shape: n  *  d]
    where P = softmax(X @ W.T + b)
    """
    n = X_batch.shape[0]
    logits = X_batch @ W.T + b          # (n, C)
    P = softmax(logits)                 # (n, C)
    # One-hot encode labels
    one_hot = np.zeros_like(P)
    one_hot[np.arange(n), y_batch] = 1
    dL_dlogits = (P - one_hot) / n     # (n, C)
    dL_dX = dL_dlogits @ W             # (n, d)
    return dL_dX


def fgsm_attack(X_clean, y_true, model, epsilon):
    """Generate adversarial examples using FGSM with analytical gradient."""
    W = model.coef_          # (C, d)
    b = model.intercept_     # (C,)
    gradient = cross_entropy_gradient(X_clean, y_true, W, b)
    perturbation = epsilon * np.sign(gradient)
    X_adv = X_clean + perturbation
    return X_adv


#                                                              
# 4. Evaluate Across Epsilons
#                                                              
print("=" * 60)
print("STEP 4 -- FGSM Attack at   = 0.1, 0.3, 0.5")
print("=" * 60)

epsilons = [0.0, 0.1, 0.3, 0.5]
results = []

for eps in epsilons:
    if eps == 0.0:
        X_eval = X_test
    else:
        X_eval = fgsm_attack(X_test, y_test, model, eps)
    adv_acc = model.score(X_eval, y_test)
    drop = original_acc - adv_acc
    results.append((eps, original_acc, adv_acc, drop))

# Print table
print()
print(f"  {'  (epsilon)':<14} {'Original Acc':>14} {'Adversarial Acc':>17} {'Accuracy Drop':>15}")
print("  " + " " * 62)
for eps, orig, adv, drop in results:
    marker = "   baseline" if eps == 0.0 else ""
    print(f"  {eps:<14.1f} {orig*100:>13.2f}% {adv*100:>16.2f}% {drop*100:>14.2f}%{marker}")
print()

#                                                              
# 5. Plot Results
#                                                              
print("=" * 60)
print("STEP 5 -- Generating FGSM Results Plot")
print("=" * 60)

eps_vals  = [r[0] for r in results]
orig_vals = [r[1] * 100 for r in results]
adv_vals  = [r[2] * 100 for r in results]
drop_vals = [r[3] * 100 for r in results]

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "FGSM Adversarial Attack -- Iris Dataset (NumPy Implementation)\n"
    "Khushi Dixit | IC-2K23-51 | IC-709D",
    fontsize=12, fontweight='bold')

ax1 = axes[0]
ax1.plot(eps_vals, orig_vals, 'g-o', label='Original Accuracy', linewidth=2, markersize=8)
ax1.plot(eps_vals, adv_vals,  'r-s', label='Adversarial Accuracy', linewidth=2, markersize=8)
ax1.fill_between(eps_vals, adv_vals, orig_vals, alpha=0.2, color='red', label='Accuracy Drop')
ax1.set_xlabel("Epsilon ( ) -- Perturbation Strength")
ax1.set_ylabel("Accuracy (%)")
ax1.set_title("Accuracy vs Epsilon")
ax1.legend()
ax1.grid(linestyle='--', alpha=0.5)
ax1.set_ylim(0, 110)
for x, y_ in zip(eps_vals, adv_vals):
    ax1.annotate(f'{y_:.1f}%', (x, y_), textcoords="offset points",
                 xytext=(0, -18), ha='center', fontsize=8)

ax2 = axes[1]
bar_colors = ['#2ecc71' if d < 5 else '#e67e22' if d < 20 else '#e74c3c' for d in drop_vals]
bars = ax2.bar([str(e) for e in eps_vals], drop_vals, color=bar_colors,
               edgecolor='black', linewidth=0.8)
ax2.set_xlabel("Epsilon ( )")
ax2.set_ylabel("Accuracy Drop (%)")
ax2.set_title("Accuracy Drop vs Epsilon")
ax2.grid(axis='y', linestyle='--', alpha=0.5)
for bar, val in zip(bars, drop_vals):
    ax2.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig("fgsm_results.png", dpi=150, bbox_inches='tight')
plt.close()
print("     Saved: fgsm_results.png\n")

#                                                              
# 6. Summary
#                                                              
print("=" * 60)
print("SUMMARY -- Adversarial AI Insights")
print("=" * 60)
print("""
  OBSERVATIONS:
    As   increases, adversarial accuracy drops significantly.
    Even   = 0.1 (small perturbation) degrades performance.
    FGSM shows that ML models are NOT robust by default.

  EDUCATIONAL TAKEAWAYS:
    Adversarial examples reveal a fundamental weakness in
    gradient-based learning systems.
    Imperceptible pixel changes can fool state-of-the-art
    image classifiers.
    Adversarial robustness is a critical concern for
    AI safety in medical, autonomous driving, security domains.
    Defence strategies include: adversarial training,
    input preprocessing, certified defences, and detection.

  IMPLEMENTATION NOTE:
    This uses analytical gradients of the cross-entropy loss
    w.r.t. input, equivalent to FGSM with autograd in PyTorch.
    Same mathematical principle, pure NumPy implementation.
""")
print("  [Experiment 3 Complete]\n")

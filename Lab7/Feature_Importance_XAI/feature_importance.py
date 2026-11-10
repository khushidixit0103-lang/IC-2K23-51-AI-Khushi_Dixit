"""
=============================================================
  Lab 7 -- Experiment 1: Feature Importance (XAI)
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D -- Artificial Intelligence
=============================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split

#                                                              
BANNER = """
                                                            
    LAB 7 -- Experiment 1: Feature Importance (XAI)         
    Student : Khushi Dixit   |  Roll No : IC-2K23-51      
    Course  : IC-709D -- Artificial Intelligence            
                                                            
"""
print(BANNER)

#                                                              
# 1. Load Dataset
#                                                              
print("=" * 60)
print("STEP 1 -- Loading Iris Dataset")
print("=" * 60)
iris = load_iris()
X, y = iris.data, iris.target
feature_names = iris.feature_names
class_names = iris.target_names

print(f"  Samples   : {X.shape[0]}")
print(f"  Features  : {X.shape[1]} -> {feature_names}")
print(f"  Classes   : {list(class_names)}\n")

#                                                              
# 2. Train Random Forest
#                                                              
print("=" * 60)
print("STEP 2 -- Training RandomForestClassifier")
print("=" * 60)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
train_acc = clf.score(X_train, y_train)
test_acc  = clf.score(X_test, y_test)
print(f"  Training Accuracy : {train_acc * 100:.2f}%")
print(f"  Testing  Accuracy : {test_acc  * 100:.2f}%\n")

#                                                              
# 3. Impurity-based Feature Importance (MDI)
#                                                              
print("=" * 60)
print("STEP 3 -- Impurity-Based (MDI) Feature Importances")
print("=" * 60)
print("""
  CONCEPT -- Mean Decrease in Impurity (MDI):
    Measures how much each feature reduces impurity
    (Gini / entropy) averaged over all trees.
    Higher value = more important for splitting.
    Computed directly from training; fast but can be
    biased toward high-cardinality features.
""")

mdi_importances = clf.feature_importances_
mdi_std = np.std([tree.feature_importances_ for tree in clf.estimators_], axis=0)
mdi_indices = np.argsort(mdi_importances)[::-1]

print(f"  {'Rank':<6} {'Feature':<30} {'Importance':>12} {'Std Dev':>10}")
print("  " + "-" * 62)
for rank, idx in enumerate(mdi_indices, start=1):
    print(f"  {rank:<6} {feature_names[idx]:<30} {mdi_importances[idx]:>12.4f} {mdi_std[idx]:>10.4f}")
print()

#                                                              
# 4. Permutation Importance
#                                                              
print("=" * 60)
print("STEP 4 -- Permutation Importance")
print("=" * 60)
print("""
  CONCEPT -- Permutation Importance:
    Randomly shuffles one feature column at a time and
    measures the resulting drop in model performance.
    Higher drop = more important feature.
    Model-agnostic: works with any estimator.
    Reflects impact on actual test performance (not training).
    More reliable than MDI for correlated features.
""")

perm_result = permutation_importance(
    clf, X_test, y_test, n_repeats=30, random_state=42)
perm_importances = perm_result.importances_mean
perm_std         = perm_result.importances_std
perm_indices     = np.argsort(perm_importances)[::-1]

print(f"  {'Rank':<6} {'Feature':<30} {'Importance':>12} {'Std Dev':>10}")
print("  " + "-" * 62)
for rank, idx in enumerate(perm_indices, start=1):
    print(f"  {rank:<6} {feature_names[idx]:<30} {perm_importances[idx]:>12.4f} {perm_std[idx]:>10.4f}")
print()

#                                                              
# 5. Plot
#                                                              
print("=" * 60)
print("STEP 5 -- Generating Feature Importance Plot")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(
    "Feature Importance -- Iris Dataset\n"
    "Khushi Dixit | IC-2K23-51 | IC-709D",
    fontsize=13, fontweight='bold')

# MDI
ax1 = axes[0]
colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(feature_names)))
bars1 = ax1.bar(
    range(len(feature_names)),
    mdi_importances[mdi_indices],
    yerr=mdi_std[mdi_indices],
    color=[colors[i] for i in range(len(feature_names))],
    capsize=5, edgecolor='black', linewidth=0.8)
ax1.set_xticks(range(len(feature_names)))
ax1.set_xticklabels([feature_names[i] for i in mdi_indices], rotation=20, ha='right', fontsize=9)
ax1.set_title("MDI Feature Importance\n(Mean Decrease in Impurity)", fontsize=11)
ax1.set_ylabel("Importance Score")
ax1.set_xlabel("Feature")
ax1.grid(axis='y', linestyle='--', alpha=0.5)
for bar, val in zip(bars1, mdi_importances[mdi_indices]):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{val:.3f}', ha='center', va='bottom', fontsize=8)

# Permutation
ax2 = axes[1]
bars2 = ax2.bar(
    range(len(feature_names)),
    perm_importances[perm_indices],
    yerr=perm_std[perm_indices],
    color=[colors[i] for i in range(len(feature_names))],
    capsize=5, edgecolor='black', linewidth=0.8)
ax2.set_xticks(range(len(feature_names)))
ax2.set_xticklabels([feature_names[i] for i in perm_indices], rotation=20, ha='right', fontsize=9)
ax2.set_title("Permutation Importance\n(Mean Accuracy Drop on Test Set)", fontsize=11)
ax2.set_ylabel("Mean Accuracy Decrease")
ax2.set_xlabel("Feature")
ax2.grid(axis='y', linestyle='--', alpha=0.5)
for bar, val in zip(bars2, perm_importances[perm_indices]):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
             f'{val:.3f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150, bbox_inches='tight')
plt.close()
print("     Saved: feature_importance.png\n")

#                                                              
# 6. Summary
#                                                              
print("=" * 60)
print("SUMMARY -- Explainability Insights")
print("=" * 60)
print("""
  OBSERVATIONS:
    Both methods agree that 'petal length' and 'petal width'
    are the most discriminative features for Iris classification.
    'sepal width' consistently ranks lowest in importance.
    XAI (Explainable AI) enables us to TRUST and AUDIT models
    by revealing which inputs drive predictions.
    Feature importance is a key technique in responsible AI,
    helping detect bias and improve feature engineering.

  WHY XAI MATTERS:
    Transparency: understand WHY a model makes a prediction
    Accountability: audit models for fairness
    Debugging: identify irrelevant or harmful features
    Compliance: GDPR requires explainability in some decisions
""")
print("  [Experiment 1 Complete]\n")

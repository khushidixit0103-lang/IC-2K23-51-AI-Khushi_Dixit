# ============================================================
# Lab 5 - Experiment 1: Decision Tree Classifier
# Student: Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D
# Objective: Predict student placement using Decision Tree
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix
)

# ── Paths ────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(SCRIPT_DIR, "student_placement.csv")
VIZ_PATH   = os.path.join(SCRIPT_DIR, "decision_tree_viz.png")

print("=" * 60)
print("  Lab 5 | Decision Tree Classifier")
print("  Student: Khushi Dixit | IC-2K23-51 | IC-709D")
print("=" * 60)

# ── Load Data ────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
print(f"\n[Dataset] Shape: {df.shape}")
print(df.head())

# ── Features & Target ────────────────────────────────────────
FEATURES = ["cgpa", "iq", "internships", "projects", "communication_rating"]
TARGET   = "placement_status"

X = df[FEATURES]
y = df[TARGET]

le = LabelEncoder()
y_encoded = le.fit_transform(y)          # Not Placed=0, Placed=1

# ── Train / Test Split ───────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.20, random_state=42
)
print(f"\n[Split] Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

# ── Model ────────────────────────────────────────────────────
clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# ── Predictions ──────────────────────────────────────────────
y_pred_train = clf.predict(X_train)
y_pred_test  = clf.predict(X_test)

train_acc = accuracy_score(y_train, y_pred_train)
test_acc  = accuracy_score(y_test,  y_pred_test)

print("\n" + "-" * 40)
print(f"  Training Accuracy : {train_acc * 100:.2f}%")
print(f"  Test Accuracy     : {test_acc  * 100:.2f}%")
print("-" * 40)

# ── Classification Report ────────────────────────────────────
print("\n[Classification Report]")
print(classification_report(
    y_test, y_pred_test,
    target_names=le.classes_,
    zero_division=0
))

# ── Confusion Matrix ─────────────────────────────────────────
cm = confusion_matrix(y_test, y_pred_test)
print("[Confusion Matrix]")
print(f"Labels: {list(le.classes_)}")
print(cm)

# ── Feature Importances ──────────────────────────────────────
print("\n[Feature Importances -- Ranked]")
importances = pd.Series(clf.feature_importances_, index=FEATURES)
importances_sorted = importances.sort_values(ascending=False)
for feat, imp in importances_sorted.items():
    print(f"  {feat:<25} {imp:.4f}")

# ── Visualise Decision Tree ───────────────────────────────────
fig, ax = plt.subplots(figsize=(18, 8))
plot_tree(
    clf,
    feature_names=FEATURES,
    class_names=le.classes_,
    filled=True,
    rounded=True,
    ax=ax
)
plt.title("Decision Tree -- Student Placement", fontsize=14)
plt.tight_layout()
plt.savefig(VIZ_PATH, dpi=120)
plt.close()
print(f"\n[Visualization] Saved -> {VIZ_PATH}")
print("\n[Done] Experiment 1 complete.")

# ============================================================
# Lab 5 - Experiment 4: Loan Approval Prediction
# Student: Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D
# Objective: Predict loan approval using Decision Tree
# ============================================================

import os
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── Paths ─────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(SCRIPT_DIR, "loan_data.csv")

print("=" * 60)
print("  Lab 5 | Loan Approval Prediction")
print("  Student: Khushi Dixit | IC-2K23-51 | IC-709D")
print("=" * 60)

# ── Load Data ─────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
print(f"\n[Dataset] Shape: {df.shape}")
print(df.head(6))

# ── EDA ───────────────────────────────────────────────────────
print("\n[Target Distribution -- Loan Approval]")
print(df["loan_approved"].value_counts())
print("\n[Basic Statistics]")
print(df.describe())

# ── Features & Target ─────────────────────────────────────────
FEATURES = ["income", "credit_score", "loan_amount", "employment_years", "has_collateral"]
TARGET   = "loan_approved"

X = df[FEATURES]
y = df[TARGET]

le = LabelEncoder()
y_enc = le.fit_transform(y)          # No=0, Yes=1

# ── Train / Test Split ────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y_enc, test_size=0.20, random_state=42
)
print(f"\n[Split] Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

# ── Model ─────────────────────────────────────────────────────
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# ── Evaluation ────────────────────────────────────────────────
acc = accuracy_score(y_test, y_pred)
print(f"\n[Accuracy] {acc * 100:.2f}%")

print("\n[Classification Report]")
print(classification_report(
    y_test, y_pred,
    target_names=le.classes_,
    zero_division=0
))

print("[Confusion Matrix]")
print(f"Labels: {list(le.classes_)}")
print(confusion_matrix(y_test, y_pred))

# ── Feature Importances ───────────────────────────────────────
print("\n[Feature Importances -- Ranked]")
importances = pd.Series(clf.feature_importances_, index=FEATURES)
importances_sorted = importances.sort_values(ascending=False)
for feat, imp in importances_sorted.items():
    print(f"  {feat:<22} {imp:.4f}")

print("\n[Done] Experiment 4 complete.")

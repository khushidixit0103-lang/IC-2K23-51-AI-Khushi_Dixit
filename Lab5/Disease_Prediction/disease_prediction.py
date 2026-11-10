# ============================================================
# Lab 5 - Experiment 3: Disease Prediction
# Student: Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D
# Objective: Predict disease type from symptoms using Decision Tree
# ============================================================

import os
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── Paths ─────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(SCRIPT_DIR, "disease_data.csv")

print("=" * 60)
print("  Lab 5 | Disease Prediction")
print("  Student: Khushi Dixit | IC-2K23-51 | IC-709D")
print("=" * 60)

# ── Load Data ─────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
print(f"\n[Dataset] Shape: {df.shape}")
print(df.head(6))

# ── EDA ───────────────────────────────────────────────────────
print("\n[Target Distribution -- Disease Classes]")
print(df["disease"].value_counts())

# ── Features & Target ─────────────────────────────────────────
FEATURES = ["fever", "cough", "fatigue", "headache", "body_ache"]
TARGET   = "disease"

X = df[FEATURES]
y = df[TARGET]

# ── Train / Test Split ────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
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
print(classification_report(y_test, y_pred, zero_division=0))

print("[Confusion Matrix]")
classes = sorted(df[TARGET].unique())
print(f"Labels: {classes}")
print(confusion_matrix(y_test, y_pred, labels=classes))

# ── Predict for a New Patient ─────────────────────────────────
print("\n[New Patient Prediction]")
new_patient = pd.DataFrame(
    [[1, 0, 1, 1, 1]],
    columns=FEATURES
)
print(f"  Symptoms -- fever=1, cough=0, fatigue=1, headache=1, body_ache=1")
prediction = clf.predict(new_patient)[0]
print(f"  Predicted Disease : {prediction}")

print("\n[Done] Experiment 3 complete.")

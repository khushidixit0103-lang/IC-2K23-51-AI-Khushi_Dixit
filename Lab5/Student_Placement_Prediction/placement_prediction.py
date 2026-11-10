# ============================================================
# Lab 5 - Experiment 2: Student Placement Prediction
# Student: Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D
# Objective: Compare multiple classifiers for placement prediction
# ============================================================

import os
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── Paths ─────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH  = os.path.join(SCRIPT_DIR, "..", "Decision_Tree_Classifier", "student_placement.csv")

print("=" * 65)
print("  Lab 5 | Student Placement Prediction -- Model Comparison")
print("  Student: Khushi Dixit | IC-2K23-51 | IC-709D")
print("=" * 65)

# ── Load Data ─────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH)
print(f"\n[Dataset] Shape: {df.shape}")

# ── EDA Summary ───────────────────────────────────────────────
print("\n[EDA] Basic Statistics:")
print(df.describe())
print("\n[EDA] Target Distribution:")
print(df["placement_status"].value_counts())
print("\n[EDA] Missing Values:", df.isnull().sum().sum())

# ── Preprocessing ─────────────────────────────────────────────
FEATURES = ["cgpa", "iq", "internships", "projects", "communication_rating"]
TARGET   = "placement_status"

X = df[FEATURES]
y = df[TARGET]

le = LabelEncoder()
y_enc = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_enc, test_size=0.20, random_state=42
)
print(f"\n[Split] Train: {X_train.shape[0]} | Test: {X_test.shape[0]}")

# ── Models ────────────────────────────────────────────────────
models = {
    "DecisionTree" : DecisionTreeClassifier(max_depth=4, random_state=42),
    "RandomForest" : RandomForestClassifier(n_estimators=50, random_state=42),
    "KNN"          : KNeighborsClassifier(n_neighbors=3),
}

results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    results[name] = {"model": model, "accuracy": acc}

# ── Accuracy Comparison Table ─────────────────────────────────
print("\n[Model Accuracy Comparison]")
print(f"{'Model':<16} {'Test Accuracy':>15}")
print("-" * 33)
for name, info in results.items():
    print(f"{name:<16} {info['accuracy'] * 100:>14.2f}%")

# ── Best Model ────────────────────────────────────────────────
best_name  = max(results, key=lambda k: results[k]["accuracy"])
best_model = results[best_name]["model"]
best_pred  = best_model.predict(X_test)

print(f"\n[Best Model] -> {best_name} (Accuracy: {results[best_name]['accuracy']*100:.2f}%)")

print(f"\n[Classification Report -- {best_name}]")
print(classification_report(
    y_test, best_pred,
    target_names=le.classes_,
    zero_division=0
))

print(f"[Confusion Matrix -- {best_name}]")
print(f"Labels: {list(le.classes_)}")
print(confusion_matrix(y_test, best_pred))

print("\n[Done] Experiment 2 complete.")

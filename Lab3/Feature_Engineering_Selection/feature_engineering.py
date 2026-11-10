"""
Feature Engineering & Feature Selection Techniques
Lab 3 - AI Programming Frameworks & Data Preparation
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Demonstrates:
1. Feature Engineering:
   - Interaction feature creation (e.g., Composite Academic Index)
   - Ratio feature derivation
   - Feature Scaling: StandardScaler (z-score) vs MinMaxScaler ([0, 1])
2. Feature Selection:
   - VarianceThreshold (filtering low-variance constant noise)
   - SelectKBest using ANOVA F-value (f_classif)
   - Mutual Information (non-linear dependency ranking)
Applied to the Student Placement Dataset.
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif, mutual_info_classif


def run_feature_engineering(csv_path: str):
    print("=" * 70)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 3 (EXPERIMENT 4)")
    print("   Feature Engineering & Feature Selection Pipeline")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    df = pd.read_csv(csv_path)
    print(f"\n1. Ingested Dataset: {os.path.basename(csv_path)} ({len(df)} samples)")

    # 1. Feature Engineering: Deriving Domain Indicators
    df_eng = df.copy()
    # Composite Academic Index: CGPA scaled with IQ
    df_eng["academic_index"] = (df_eng["cgpa"] * df_eng["iq"]) / 100.0
    # Practical Experience Score
    df_eng["practical_score"] = (df_eng["internships"] * 2.0) + (df_eng["projects"] * 1.5)

    print("\n2. Derived Engineered Features:")
    print(df_eng[["student_id", "cgpa", "iq", "academic_index", "internships", "projects", "practical_score"]].head().to_string(index=False))

    # 2. Feature Scaling
    features_to_scale = ["cgpa", "iq", "academic_index", "practical_score", "communication_rating"]
    scaler_std = StandardScaler()
    scaler_minmax = MinMaxScaler()

    df_std = pd.DataFrame(scaler_std.fit_transform(df_eng[features_to_scale]), columns=[f"{c}_std" for c in features_to_scale])
    df_minmax = pd.DataFrame(scaler_minmax.fit_transform(df_eng[features_to_scale]), columns=[f"{c}_minmax" for c in features_to_scale])

    print("\n3. Scaling Comparison (Original vs StandardScaler vs MinMaxScaler):")
    sample_col = "academic_index"
    comp_df = pd.DataFrame({
        "Original": df_eng[sample_col].head(),
        "StandardScaled (mu=0, s=1)": df_std[f"{sample_col}_std"].head().round(3),
        "MinMaxScaled ([0, 1])": df_minmax[f"{sample_col}_minmax"].head().round(3),
    })
    print(comp_df.to_string())

    # 3. Feature Selection
    X = df_eng[features_to_scale]
    y = (df_eng["placement_status"] == "Placed").astype(int)

    # A. Variance Threshold
    selector_var = VarianceThreshold(threshold=0.1)
    selector_var.fit(X)
    print(f"\n4. Feature Selection A: Variance Threshold (> 0.1):")
    for feat, var in zip(X.columns, X.var()):
        status = "RETAINED" if var > 0.1 else "FILTERED"
        print(f"   - {feat:<22}: Variance = {var:.4f} -> [{status}]")

    # B. SelectKBest using ANOVA F-statistic
    selector_kbest = SelectKBest(score_func=f_classif, k=3)
    selector_kbest.fit(X, y)
    scores_df = pd.DataFrame({
        "Feature": X.columns,
        "ANOVA F-Score": selector_kbest.scores_.round(2),
        "p-value": selector_kbest.pvalues_.round(6),
        "Selected (Top 3)": selector_kbest.get_support()
    }).sort_values(by="ANOVA F-Score", ascending=False)

    print("\n5. Feature Selection B: SelectKBest (ANOVA F-statistic):")
    print(scores_df.to_string(index=False))

    # C. Mutual Information
    mi_scores = mutual_info_classif(X, y, random_state=42)
    mi_df = pd.DataFrame({
        "Feature": X.columns,
        "Mutual Information": mi_scores.round(4)
    }).sort_values(by="Mutual Information", ascending=False)

    print("\n6. Feature Selection C: Mutual Information Scores:")
    print(mi_df.to_string(index=False))


if __name__ == "__main__":
    curr = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.normpath(os.path.join(curr, "..", "..", "datasets", "placement.csv"))
    run_feature_engineering(csv_file)

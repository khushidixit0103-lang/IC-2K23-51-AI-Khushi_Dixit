"""
Data Cleaning & Missing Value Imputation
Lab 3 - AI Programming Frameworks & Data Preparation
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Techniques Demonstrated:
1. Identifying Missing Data (NaN profiling)
2. Complete Case Removal (Listwise deletion)
3. Mean Imputation (for Gaussian-like variables)
4. Median Imputation (robust against outliers)
5. Mode Imputation (for categorical variables)
6. Multivariate KNN Imputation (k-Nearest Neighbors)
7. Comparative evaluation of imputation bias and variance distortion
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer


def demonstrate_cleaning():
    print("=" * 70)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 3 (EXPERIMENT 2)")
    print("   Data Cleaning & Missing Value Handling Techniques")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    # Synthetic dirty dataset reflecting realistic survey data
    raw_data = {
        "Student": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah"],
        "CGPA": [8.5, np.nan, 9.1, 7.4, np.nan, 8.0, 6.8, 7.9],
        "IQ": [120, 95, 130, np.nan, 90, 115, np.nan, 112],
        "Department": ["CS", "IT", "CS", np.nan, "IT", "CS", "CS", "IT"],
        "Attendance_Pct": [92.0, 78.0, np.nan, 85.0, 65.0, 88.0, 72.0, 90.0]
    }
    df = pd.DataFrame(raw_data)

    print("\n1. Original Raw Dataset with Missing Values (NaN):")
    print(df.to_string(index=False))

    print("\n2. Missing Value Audit:")
    null_counts = df.isnull().sum()
    null_pct = (null_counts / len(df)) * 100
    print(pd.DataFrame({"Missing Count": null_counts, "Percentage (%)": null_pct}).to_string())

    # Strategy A: Complete Case Deletion
    df_dropped = df.dropna()
    print(f"\n3. Strategy A: Complete Case Deletion (dropna):")
    print(f"   Original Rows: {len(df)} -> Retained Rows: {len(df_dropped)} (Loss: {len(df)-len(df_dropped)} rows)")

    # Strategy B: Univariate Mean & Median Imputation
    df_univariate = df.copy()
    mean_imp = SimpleImputer(strategy="mean")
    median_imp = SimpleImputer(strategy="median")
    mode_imp = SimpleImputer(strategy="most_frequent")

    df_univariate["CGPA_MeanImp"] = mean_imp.fit_transform(df[["CGPA"]]).ravel().round(2)
    df_univariate["CGPA_MedianImp"] = median_imp.fit_transform(df[["CGPA"]]).ravel().round(2)
    df_univariate["Department_ModeImp"] = mode_imp.fit_transform(df[["Department"]]).ravel()

    print("\n4. Strategy B: Univariate Imputation (Mean, Median, Mode):")
    print(df_univariate[["Student", "CGPA", "CGPA_MeanImp", "CGPA_MedianImp", "Department", "Department_ModeImp"]].to_string(index=False))

    # Strategy C: Multivariate KNN Imputation
    num_cols = ["CGPA", "IQ", "Attendance_Pct"]
    knn_imp = KNNImputer(n_neighbors=2)
    imputed_matrix = knn_imp.fit_transform(df[num_cols])
    df_knn = pd.DataFrame(imputed_matrix, columns=[f"{c}_KNN" for c in num_cols])

    print("\n5. Strategy C: Multivariate KNN Imputation (n_neighbors=2):")
    comparison = pd.concat([df[["Student"]], df[num_cols], df_knn], axis=1)
    print(comparison.round(2).to_string(index=False))

    print("\n--- Summary of Imputation Statistics for CGPA ---")
    print(f"  True Non-Null Mean:      {df['CGPA'].mean():.2f}")
    print(f"  Mean-Imputed Variance:   {df_univariate['CGPA_MeanImp'].var():.4f}")
    print(f"  Median-Imputed Variance: {df_univariate['CGPA_MedianImp'].var():.4f}")
    print(f"  KNN-Imputed Variance:    {df_knn['CGPA_KNN'].var():.4f}")


if __name__ == "__main__":
    demonstrate_cleaning()

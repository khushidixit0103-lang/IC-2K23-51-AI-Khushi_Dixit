"""
Exploratory Data Analysis (EDA) & Dataset Loading
Lab 3 - AI Programming Frameworks & Data Preparation
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Covers:
- Dataset ingestion using Pandas from CSV
- Dimensionality, schema inspection, data types
- Summary statistics (mean, std, quartiles, IQR, skewness)
- Missing value profiling
- Feature correlation analysis
Applied to the Student Placement Dataset.
"""

import os
import pandas as pd
import numpy as np


def run_eda(dataset_path: str):
    print("=" * 70)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 3 (EXPERIMENT 1)")
    print("   Exploratory Data Analysis (EDA) with NumPy & Pandas")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at {dataset_path}")

    df = pd.read_csv(dataset_path)

    print(f"\n1. Ingested Dataset: {os.path.basename(dataset_path)}")
    print(f"   Total Instances (Rows):    {df.shape[0]}")
    print(f"   Total Attributes (Cols):   {df.shape[1]}")

    print("\n2. Dataset Schema & Data Types:")
    schema_df = pd.DataFrame({
        "Column": df.columns,
        "Dtype": df.dtypes.values,
        "Non-Null Count": df.notnull().sum().values,
        "Null Count": df.isnull().sum().values,
        "Unique Values": [df[c].nunique() for c in df.columns]
    })
    print(schema_df.to_string(index=False))

    print("\n3. First 5 Sample Instances:")
    print(df.head().to_string(index=False))

    print("\n4. Numerical Statistical Distribution Summary:")
    num_cols = df.select_dtypes(include=[np.number]).columns
    stats_df = df[num_cols].describe().T[["count", "mean", "std", "min", "50%", "max"]]
    stats_df = stats_df.rename(columns={"50%": "median"})
    print(stats_df.round(2).to_string())

    print("\n5. Categorical Class Distribution (Target Variable):")
    if "placement_status" in df.columns:
        counts = df["placement_status"].value_counts()
        percentages = df["placement_status"].value_counts(normalize=True) * 100
        dist_df = pd.DataFrame({"Count": counts, "Percentage (%)": percentages.round(2)})
        print(dist_df.to_string())

    print("\n6. Pearson Correlation Matrix (Numerical Features):")
    corr = df[num_cols].drop(columns=["student_id"], errors="ignore").corr()
    print(corr.round(3).to_string())

    return df


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.normpath(os.path.join(current_dir, "..", "..", "datasets", "placement.csv"))
    run_eda(data_path)

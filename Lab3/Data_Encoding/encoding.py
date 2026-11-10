"""
Categorical Data Encoding Techniques
Lab 3 - AI Programming Frameworks & Data Preparation
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Demonstrates:
1. Label Encoding (for target classification variables)
2. Ordinal Encoding (for naturally ordered attributes: Low, Medium, High)
3. One-Hot Encoding (for unordered nominal features: Red, Green, Blue)
4. Theoretical analysis of ordinal bias vs dummy variable trap
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder


def demonstrate_encoding():
    print("=" * 70)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 3 (EXPERIMENT 3)")
    print("   Categorical Data Encoding (Label, Ordinal, & One-Hot)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    raw_data = {
        "Student_ID": [201, 202, 203, 204, 205, 206],
        "Performance_Tier": ["Medium", "High", "Low", "Medium", "High", "Low"],
        "Preferred_Domain": ["AI/ML", "WebDev", "Cybersecurity", "AI/ML", "Cloud", "WebDev"],
        "Placement_Status": ["Placed", "Placed", "Not Placed", "Placed", "Placed", "Not Placed"]
    }
    df = pd.DataFrame(raw_data)

    print("\n1. Original Raw Categorical Features:")
    print(df.to_string(index=False))

    # 1. Label Encoding on Target Variable
    le = LabelEncoder()
    df["Placement_LabelEncoded"] = le.fit_transform(df["Placement_Status"])
    print("\n2. Label Encoding (Target Variable: 'Placement_Status'):")
    mapping = {cls: idx for idx, cls in enumerate(le.classes_)}
    print(f"   Mapping Dictionary: {mapping}")
    print(df[["Student_ID", "Placement_Status", "Placement_LabelEncoded"]].to_string(index=False))

    # 2. Ordinal Encoding with Explicit Hierarchy
    tier_order = [["Low", "Medium", "High"]]
    oe = OrdinalEncoder(categories=tier_order)
    df["Tier_OrdinalEncoded"] = oe.fit_transform(df[["Performance_Tier"]]).astype(int)
    print("\n3. Ordinal Encoding (Preserving Domain Order: Low < Medium < High):")
    print(df[["Student_ID", "Performance_Tier", "Tier_OrdinalEncoded"]].to_string(index=False))

    # 3. One-Hot Encoding on Nominal Feature
    ohe = OneHotEncoder(sparse_output=False, drop=None)
    ohe_matrix = ohe.fit_transform(df[["Preferred_Domain"]])
    ohe_cols = [f"Domain_{cat}" for cat in ohe.categories_[0]]
    df_ohe = pd.DataFrame(ohe_matrix.astype(int), columns=ohe_cols)

    print("\n4. One-Hot Encoding (Nominal Feature: 'Preferred_Domain'):")
    combined = pd.concat([df[["Student_ID", "Preferred_Domain"]], df_ohe], axis=1)
    print(combined.to_string(index=False))

    print("\n--- Encoding Comparison & Theoretical Insights ---")
    print("  * LabelEncoder: Best reserved for 1D target labels y. On features, it induces false mathematical ordering (e.g., 2 > 1).")
    print("  * OrdinalEncoder: Preserves monotonic ranking (Low=0, Medium=1, High=2), critical for tree and linear models.")
    print("  * OneHotEncoder: Prevents spurious ordinal bias on nominal values by projecting into orthogonal binary sub-dimensions.")


if __name__ == "__main__":
    demonstrate_encoding()

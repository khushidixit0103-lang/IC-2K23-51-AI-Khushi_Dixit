"""
=============================================================
  Lab 7 -- Experiment 2: PCA Dimensionality Reduction
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
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

BANNER = """
                                                            
    LAB 7 -- Experiment 2: PCA Dimensionality Reduction     
    Student : Khushi Dixit   |  Roll No : IC-2K23-51      
    Course  : IC-709D -- Artificial Intelligence            
                                                            
"""
print(BANNER)

#                                                              
# 1. Load & Standardise Dataset
#                                                              
print("=" * 60)
print("STEP 1 -- Loading and Standardising Iris Dataset")
print("=" * 60)
iris = load_iris()
X = iris.data          # (150, 4)
y = iris.target
feature_names = iris.feature_names
class_names   = iris.target_names
colors_map = {0: '#e74c3c', 1: '#2ecc71', 2: '#3498db'}
color_labels = [colors_map[c] for c in y]

print(f"  Dataset Shape : {X.shape}  (samples  *  features)")
print(f"  Features      : {feature_names}")
print()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("    Data standardised (zero mean, unit variance)\n")

#                                                              
# 2. PCA -> 2D
#                                                              
print("=" * 60)
print("STEP 2 -- PCA: 4D -> 2D Reduction")
print("=" * 60)
pca_2d = PCA(n_components=2)
X_2d   = pca_2d.fit_transform(X_scaled)

print(f"  Explained Variance Ratio (per component):")
for i, var in enumerate(pca_2d.explained_variance_ratio_):
    print(f"    PC{i+1}: {var * 100:.2f}%")
print(f"  Cumulative Explained Variance : "
      f"{pca_2d.explained_variance_ratio_.sum() * 100:.2f}%")
print()

#                                                              
# 3. PCA -> 3D
#                                                              
print("=" * 60)
print("STEP 3 -- PCA: 4D -> 3D Reduction")
print("=" * 60)
pca_3d = PCA(n_components=3)
X_3d   = pca_3d.fit_transform(X_scaled)

print(f"  Explained Variance Ratio (per component):")
for i, var in enumerate(pca_3d.explained_variance_ratio_):
    print(f"    PC{i+1}: {var * 100:.2f}%")
print(f"  Cumulative Explained Variance : "
      f"{pca_3d.explained_variance_ratio_.sum() * 100:.2f}%")
print()

#                                                              
# 4. Principal Component Loadings
#                                                              
print("=" * 60)
print("STEP 4 -- Principal Component Loadings (Eigenvectors)")
print("=" * 60)
print("""
  CONCEPT -- Loadings:
    Each principal component (PC) is a linear combination
    of the original features.
    The loading values show how much each original feature
    contributes to that PC.
    Large |loading| -> strong contribution.
""")
print(f"  {'Feature':<30} {'PC1':>10} {'PC2':>10}")
print("  " + "-" * 52)
for i, fname in enumerate(feature_names):
    pc1_load = pca_2d.components_[0][i]
    pc2_load = pca_2d.components_[1][i]
    print(f"  {fname:<30} {pc1_load:>10.4f} {pc2_load:>10.4f}")
print()

#                                                              
# 5. Reconstruction & Error
#                                                              
print("=" * 60)
print("STEP 5 -- Reconstruction from 2D -> 4D & Error")
print("=" * 60)
X_reconstructed = pca_2d.inverse_transform(X_2d)
reconstruction_error = np.mean(np.sum((X_scaled - X_reconstructed) ** 2, axis=1))
per_feature_error = np.mean((X_scaled - X_reconstructed) ** 2, axis=0)

print(f"  Mean Squared Reconstruction Error (overall) : {reconstruction_error:.4f}")
print()
print(f"  Per-feature MSE:")
for fname, err in zip(feature_names, per_feature_error):
    print(f"    {fname:<30} : {err:.4f}")
print()

#                                                              
# 6. 2D Scatter Plot
#                                                              
print("=" * 60)
print("STEP 6 -- Generating PCA 2D Scatter Plot")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(
    "PCA Dimensionality Reduction -- Iris Dataset\n"
    "Khushi Dixit | IC-2K23-51 | IC-709D",
    fontsize=13, fontweight='bold')

# 2D scatter
ax1 = axes[0]
for cls, cname in enumerate(class_names):
    mask = y == cls
    ax1.scatter(X_2d[mask, 0], X_2d[mask, 1],
                c=colors_map[cls], label=cname,
                edgecolors='black', linewidths=0.4, s=60, alpha=0.85)
ax1.set_xlabel(f"PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% variance)")
ax1.set_ylabel(f"PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% variance)")
ax1.set_title("PCA: 4D -> 2D Projection")
ax1.legend(title="Class", framealpha=0.7)
ax1.grid(linestyle='--', alpha=0.4)

# Explained variance bar chart
ax2 = axes[1]
pca_full = PCA(n_components=4)
pca_full.fit(X_scaled)
evr = pca_full.explained_variance_ratio_
cumulative = np.cumsum(evr)
ax2.bar(range(1, 5), evr * 100, color='#3498db', edgecolor='black',
        linewidth=0.8, label='Individual', alpha=0.8)
ax2.step(range(1, 5), cumulative * 100, where='mid',
         color='#e74c3c', linewidth=2, linestyle='--', label='Cumulative', marker='o')
ax2.set_xticks(range(1, 5))
ax2.set_xticklabels([f"PC{i}" for i in range(1, 5)])
ax2.set_xlabel("Principal Component")
ax2.set_ylabel("Explained Variance (%)")
ax2.set_title("Explained Variance by Component")
ax2.legend()
ax2.grid(axis='y', linestyle='--', alpha=0.4)
ax2.set_ylim(0, 115)
for i, (v, c) in enumerate(zip(evr * 100, cumulative * 100)):
    ax2.text(i + 1, v + 1.5, f'{v:.1f}%', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig("pca_2d.png", dpi=150, bbox_inches='tight')
plt.close()
print("     Saved: pca_2d.png\n")

#                                                              
# 7. Summary
#                                                              
print("=" * 60)
print("SUMMARY -- PCA Insights")
print("=" * 60)
print(f"""
  OBSERVATIONS:
    2 principal components capture {pca_2d.explained_variance_ratio_.sum()*100:.1f}% of total variance.
    3 principal components capture {pca_3d.explained_variance_ratio_.sum()*100:.1f}% of total variance.
    The scatter plot shows clear class separation even in 2D.
    Reconstruction from 2D has MSE = {reconstruction_error:.4f}
    (information lost by discarding 2 dimensions).

  WHY PCA MATTERS:
    Reduces computation time and memory
    Removes noise and redundant features
    Enables visualisation of high-dimensional data
    Prevents overfitting (fewer dimensions = simpler model)
""")
print("  [Experiment 2 Complete]\n")

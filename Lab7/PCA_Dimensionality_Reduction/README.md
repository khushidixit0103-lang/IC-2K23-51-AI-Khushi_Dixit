# Experiment 2: Principal Component Analysis (PCA) & Feature Visualisation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 7 – Explainable AI, Adversarial AI & Advanced Techniques  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To project high-dimensional multivariate data onto orthogonal low-dimensional latent subspaces using Principal Component Analysis (PCA), analyze explained variance ratios, and visualize class separations in 2D space.

---

## 2. Problem Statement
Given the 4-dimensional continuous feature space of the Iris dataset, perform linear dimensionality reduction using PCA:
1. Standardize features to zero mean and unit variance.
2. Compute covariance matrix eigenvalues and eigenvectors.
3. Project data onto 2D and 3D principal components.
4. Measure cumulative explained variance ratios and reconstruction error.
5. Generate a 2D scatter plot visualization saved to `pca_2d.png`.

---

## 3. Algorithm & Approach
1. **Standardization:**
   $$Z = \frac{X - \mu}{\sigma}$$
2. **Eigendecomposition of Covariance Matrix:**
   $$\Sigma = \frac{1}{n - 1} Z^T Z = V \Lambda V^T$$
   where $V$ are principal direction eigenvectors and $\Lambda$ are eigenvalues representing component variances.
3. **Dimensionality Reduction:**
   $$X_{2D} = Z \cdot W_{2}$$
   where $W_2$ consists of the top 2 eigenvectors.
4. **Reconstruction & Loss Evaluation:**
   $$\hat{Z} = X_{2D} \cdot W_2^T, \quad \text{MSE} = \frac{1}{N \cdot D} \|Z - \hat{Z}\|_F^2$$

---

## 4. Execution Command
```bash
python Lab7/PCA_Dimensionality_Reduction/pca_demo.py
```

---

## 5. Real Execution Output
```text
============================================================
    LAB 7 -- Experiment 2: PCA Dimensionality Reduction
    Student : Khushi Dixit   |  Roll No : IC-2K23-51
    Course  : IC-709D -- Artificial Intelligence
============================================================

STEP 1 -- Loading and Standardising Iris Dataset
  Dataset Shape : (150, 4) (samples x features)

STEP 2 -- PCA: 4D -> 2D Reduction
  Explained Variance Ratio (per component):
    PC1: 72.96%
    PC2: 22.85%
  Cumulative Explained Variance : 95.81%

STEP 3 -- PCA: 4D -> 3D Reduction
  Explained Variance Ratio (per component):
    PC1: 72.96%
    PC2: 22.85%
    PC3: 3.67%
  Cumulative Explained Variance : 99.48%

STEP 4 -- Principal Component Loadings (Eigenvectors)
  Feature                               PC1        PC2
  ----------------------------------------------------
  sepal length (cm)                  0.5211     0.3774
  sepal width (cm)                  -0.2693     0.9233
  petal length (cm)                  0.5804     0.0245
  petal width (cm)                   0.5649     0.0669

STEP 5 -- Reconstruction from 2D -> 4D & Error
  Mean Squared Reconstruction Error (overall) : 0.1675

STEP 6 -- Generating PCA 2D Scatter Plot
     Saved: pca_2d.png
```

---

## 6. Generated Visualizations
- `pca_2d.png`: 2D scatter plot projecting 150 instances across PC1 (72.96% variance) and PC2 (22.85% variance), clearly demarcating Iris Setosa from Versicolor and Virginica.

---

## 7. Results & Observations
- The first two principal components capture 95.81% of the total dataset variance, reducing dimensionality by 50% with negligible information loss (Reconstruction MSE = 0.1675).
- Iris Setosa separates linearly on PC1 alone.

---

## 8. Learning Outcomes
- Understood orthogonal matrix factorization, covariance analysis, and eigenvalue decomposition.
- Learned feature loading interpretation and high-dimensional data visualization.

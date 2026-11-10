# Experiment 1: Tensor Operations & Manipulations

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 6 – Deep Learning Fundamentals using PyTorch  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To implement fundamental tensor creation, shape manipulation, matrix multiplications, element-wise arithmetic, slicing, concatenation, and aggregation operations essential in deep learning computing pipelines.

---

## 2. Problem Statement
Tensors form the mathematical foundation of deep learning architectures. Explore core tensor mechanics:
1. Multi-dimensional tensor initialization (zeros, ones, random, identity, from nested lists).
2. Tensor reshaping, dimension permutation, and matrix transposition.
3. Linear algebra matrix multiplication (`torch.mm` / `@` operator).
4. Element-wise mathematical transformations (vectorized additions, square roots, exponentials, logarithms).
5. Multi-dimensional indexing, slicing, boolean masking, and dtype casting.
6. Concatenation and stacking along specified axes.

---

## 3. Algorithm & Approach
1. **Creation:** Construct N-dimensional tensor arrays with specified geometries and initializations.
2. **Reshaping:** Reorganize stride strides without duplicating memory buffers using `.reshape(rows, cols)` and transposition (`.T`).
3. **Linear Algebra:** Compute inner-dimension matrix products conforming to $(M \times K) \cdot (K \times N) \to (M \times N)$.
4. **Broadcasting & Stacking:** Demonstrate tensor broadcasting rules and concatenate along primary/secondary axes.
5. **Reductions:** Compute global and directional reductions (sum, mean, min, max, argmax, variance).

---

## 4. Dependencies
- Python 3.8+ (NumPy / PyTorch CPU-compatible)
- No GPU or external hardware accelerators required.

---

## 5. Execution Command
```bash
python Lab6/Tensor_Operations/tensor_ops.py
```

---

## 6. Sample Execution Output
```text
============================================================
   LAB 6 - Experiment 1: Tensor Operations
   Tensor Computing Pipeline (CPU-compatible)
   Student: Khushi Dixit | Roll No: IC-2K23-51
   Course : IC-709D
============================================================

============================================================
  1. Tensor Creation
============================================================
Zeros (3x3):
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

From list [[1,2,3],[4,5,6]]:
 [[1 2 3]
 [4 5 6]]

============================================================
  2. Reshape & Transpose
============================================================
Original 1D (0-11): [ 0  1  2  3  4  5  6  7  8  9 10 11]

Reshaped to (3,4):
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

Transposed (4,3):
 [[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]

============================================================
  3. Matrix Multiplication
============================================================
A @ B (matrix multiply):
 [[19. 22.]
 [43. 50.]]

============================================================
  8. Stack & Concatenate
============================================================
Concatenate along axis=0:
 [[1 2 3]
 [4 5 6]
 [7 8 9]
 [1 2 3]
 [4 5 6]
 [7 8 9]]
...
============================================================
  All Tensor Operations Completed Successfully!
============================================================
```

---

## 7. Results & Observations
- Successfully performed 9 fundamental tensor operations covering initialization, reshaping, algebra, reduction, and concatenation.
- Verified that tensor matrix multiplication (`A @ B`) adheres to algebraic dimensions and preserves numerical precision.

---

## 8. Learning Outcomes
- Mastered tensor indexing, dimension manipulating, and matrix operations.
- Built intuition for multidimensional memory layouts and tensor algebra in deep learning frameworks.

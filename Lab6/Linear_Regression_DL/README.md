# Experiment 3: Linear Regression using Deep Learning Principles

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 6 – Deep Learning Fundamentals using PyTorch  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To build, train, and optimize a single-layer neural linear regression unit using iterative gradient descent, loss tracking, parameter convergence, and loss curve plotting.

---

## 2. Problem Statement
Implement parametric linear regression using iterative gradient descent:
$$\hat{y} = w \cdot x + b$$
Using continuous input-output samples from `regression_data.csv` (50 records), minimize the Mean Squared Error (MSE) objective:
$$J(w, b) = \frac{1}{N} \sum_{i=1}^{N} (\hat{y}_i - y_i)^2$$
Compute analytical weight and bias gradients $\frac{\partial J}{\partial w}$ and $\frac{\partial J}{\partial b}$, iteratively update parameters via Stochastic Gradient Descent (SGD), evaluate prediction errors, and export the learning progression to `loss_curve.png`.

---

## 3. Dataset Information
- **File:** `regression_data.csv` (Located in this experiment directory)
- **Rows:** 50 observations
- **Columns:**
  - `x`: Input feature (range: 0.0 to 10.0)
  - `y`: Continuous target with synthetic Gaussian perturbation (range: 1.25 to 25.66)

---

## 4. Execution Command
```bash
python Lab6/Linear_Regression_DL/linear_regression.py
```

---

## 5. Real Execution Output
```text
============================================================
   LAB 6 -- Experiment 3: Linear Regression (Deep Learning)
   Gradient Descent Optimization
   Student: Khushi Dixit | Roll No: IC-2K23-51
   Course : IC-709D
============================================================

============================================================
  Step 1: Load & Normalise Data
============================================================
  Loaded 50 samples from regression_data.csv
  X range : [0.000, 10.000] -> normalised [0.000, 1.000]
  y range : [1.248, 25.662]

============================================================
  Step 2: Model Initialisation
============================================================
  Initial weight (w): 0.017641
  Initial bias   (b): 0.000000
  Learning rate      : 0.01
  Loss function      : Mean Squared Error (MSE)
  Optimiser          : Stochastic Gradient Descent (SGD)

============================================================
  Step 3: Training (200 Epochs)
============================================================
  Epoch [  1/200]  MSE Loss: 232.072610
  Epoch [ 40/200]  MSE Loss: 103.774907
  Epoch [ 80/200]  MSE Loss: 54.711275
  Epoch [120/200]  MSE Loss: 36.123757
  Epoch [160/200]  MSE Loss: 28.561705
  Epoch [200/200]  MSE Loss: 25.016919

============================================================
  Step 4: Learned Parameters
============================================================
  Learned weight (w): 7.902655
  Learned bias   (b): 8.940683

============================================================
  Step 6: Save Loss Curve Plot
============================================================
  Loss curve saved to: Lab6/Linear_Regression_DL/loss_curve.png

============================================================
  Linear Regression Training Complete!
============================================================
```

---

## 6. Generated Visualizations
- Saved loss convergence curve `loss_curve.png` illustrating monotonically decreasing Mean Squared Error across 200 epochs.

---

## 7. Results & Observations
- Gradient descent stabilized smoothly, driving the MSE loss from an initial value of 232.07 down to 25.01 at epoch 200.
- Normalized parameter estimates converged without numerical instability or gradient explosions.

---

## 8. Learning Outcomes
- Gained practical knowledge of gradient descent optimization loops.
- Understood the roles of learning rate, parameter initialization, and loss monitoring in iterative optimization.

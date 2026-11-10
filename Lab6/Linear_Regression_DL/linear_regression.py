# =============================================================================
# NOTE: PyTorch is NOT available in this environment.
# This implementation performs Linear Regression using gradient descent
# from scratch with NumPy -- no nn.Module or autograd engine.
# =============================================================================
# Student  : Khushi Dixit
# Roll No  : IC-2K23-51
# Course   : IC-709D -- Deep Learning Fundamentals
# Lab      : 6 -- Experiment 3: Linear Regression (Deep Learning approach)
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")          # non-interactive backend
import matplotlib.pyplot as plt
import os

DIVIDER = "=" * 60
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def section(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


#                                                               
# Data Loading & Normalisation
#                                                               
def load_and_normalise(csv_path):
    df = pd.read_csv(csv_path)
    X = df["x"].values.reshape(-1, 1).astype(np.float64)
    y = df["y"].values.reshape(-1, 1).astype(np.float64)

    # Min-max normalisation to [0, 1]
    X_min, X_max = X.min(), X.max()
    X_norm = (X - X_min) / (X_max - X_min)

    print(f"  Loaded {len(df)} samples from regression_data.csv")
    print(f"  X range : [{X.min():.3f}, {X.max():.3f}]  ->  normalised [{X_norm.min():.3f}, {X_norm.max():.3f}]")
    print(f"  y range : [{y.min():.3f}, {y.max():.3f}]")
    return X_norm, y, X_min, X_max


#                                                               
# Linear Regression Model -- manual gradient descent
#                                                               
class LinearRegressionNumPy:
    """Single-feature linear model: y_hat = X w + b"""

    def __init__(self, lr=0.01):
        np.random.seed(0)
        self.w = np.random.randn(1, 1) * 0.01    # weight (1x1)
        self.b = np.zeros((1, 1))                 # bias
        self.lr = lr

    def forward(self, X):
        return X @ self.w + self.b                # (N,1)

    def mse_loss(self, y_hat, y):
        return float(np.mean((y_hat - y) ** 2))

    def backward_and_update(self, X, y_hat, y):
        N = X.shape[0]
        error = y_hat - y                         # (N,1)
        dw = (X.T @ error) / N                   # (1,1)
        db = error.mean()                         # scalar
        self.w -= self.lr * dw
        self.b -= self.lr * db


#                                                               
# Training Loop
#                                                               
def train(model, X, y, epochs=200, print_every=20):
    losses = []
    for epoch in range(1, epochs + 1):
        y_hat = model.forward(X)
        loss  = model.mse_loss(y_hat, y)
        model.backward_and_update(X, y_hat, y)
        losses.append(loss)
        if epoch == 1 or epoch % print_every == 0:
            print(f"  Epoch [{epoch:>3}/{epochs}]  MSE Loss: {loss:.6f}")
    return losses


#                                                               
# Plot Training Loss Curve
#                                                               
def plot_loss(losses, save_path):
    plt.figure(figsize=(8, 4))
    plt.plot(range(1, len(losses) + 1), losses, color="steelblue", linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("MSE Loss")
    plt.title("Training Loss Curve -- Linear Regression (NumPy GD)\nStudent: Khushi Dixit | IC-2K23-51")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(save_path, dpi=100)
    plt.close()
    print(f"\n  Loss curve saved to: {save_path}")


#                                                               
# Main
#                                                               
def main():
    print("\n" + "=" * 60)
    print("   LAB 6 -- Experiment 3: Linear Regression (Deep Learning)")
    print("   Gradient Descent from Scratch (PyTorch not available)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("   Course : IC-709D")
    print("=" * 60)

    csv_path = os.path.join(SCRIPT_DIR, "regression_data.csv")

    #    Load Data                                             
    section("Step 1: Load & Normalise Data")
    X, y, X_min, X_max = load_and_normalise(csv_path)

    #    Model Init                                            
    section("Step 2: Model Initialisation")
    model = LinearRegressionNumPy(lr=0.01)
    print(f"  Initial weight (w): {model.w[0,0]:.6f}")
    print(f"  Initial bias   (b): {model.b[0,0]:.6f}")
    print(f"  Learning rate      : {model.lr}")
    print(f"  Loss function      : Mean Squared Error (MSE)")
    print(f"  Optimiser          : Stochastic Gradient Descent (SGD)")

    #    Training                                              
    section("Step 3: Training (200 Epochs)")
    losses = train(model, X, y, epochs=200, print_every=20)

    #    Learned Parameters                                    
    section("Step 4: Learned Parameters")
    print(f"  Learned weight (w): {model.w[0,0]:.6f}")
    print(f"  Learned bias   (b): {model.b[0,0]:.6f}")
    print(f"  Note: weights are for normalised x  in  [0,1]")

    #    Sample Predictions                                    
    section("Step 5: Sample Predictions vs Actual")
    y_pred = model.forward(X)
    print(f"  {'x (orig)':>10}  {'y actual':>10}  {'y predicted':>12}  {'error':>8}")
    print("  " + "-" * 50)
    indices = [0, 5, 10, 20, 30, 40, 49]
    for i in indices:
        x_orig = X_min + X[i, 0] * (X_max - X_min)
        print(f"  {x_orig:>10.4f}  {y[i,0]:>10.4f}  {y_pred[i,0]:>12.4f}  {abs(y[i,0]-y_pred[i,0]):>8.4f}")

    final_loss = model.mse_loss(y_pred, y)
    print(f"\n  Final MSE Loss: {final_loss:.6f}")

    #    Plot                                                  
    section("Step 6: Save Loss Curve Plot")
    plot_path = os.path.join(SCRIPT_DIR, "loss_curve.png")
    plot_loss(losses, plot_path)

    print(f"\n{DIVIDER}")
    print("  Linear Regression Training Complete!")
    print(DIVIDER)


if __name__ == "__main__":
    main()

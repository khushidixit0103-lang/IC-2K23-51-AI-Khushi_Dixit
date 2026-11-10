"""
=============================================================================
  Lab 6 - Experiment 5 : Deep Learning Model Training & Evaluation Loop
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D (Artificial Intelligence Lab)
  Topic    : Complete Training Loop, Mini-batch Optimizer, Validation & Metrics
=============================================================================
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# SYNTHETIC DATASET GENERATION (Non-linear Classification)
# ---------------------------------------------------------------------------

def generate_classification_data(n_samples: int = 200, seed: int = 42):
    np.random.seed(seed)
    # Two concentric circles
    n_per_class = n_samples // 2
    r_inner = np.random.uniform(0.0, 0.4, n_per_class)
    theta_inner = np.random.uniform(0, 2 * np.pi, n_per_class)
    X_inner = np.stack([r_inner * np.cos(theta_inner), r_inner * np.sin(theta_inner)], axis=1)
    y_inner = np.zeros((n_per_class, 1))

    r_outer = np.random.uniform(0.6, 1.0, n_per_class)
    theta_outer = np.random.uniform(0, 2 * np.pi, n_per_class)
    X_outer = np.stack([r_outer * np.cos(theta_outer), r_outer * np.sin(theta_outer)], axis=1)
    y_outer = np.ones((n_per_class, 1))

    X = np.vstack([X_inner, X_outer])
    y = np.vstack([y_inner, y_outer])

    # Shuffle
    indices = np.random.permutation(n_samples)
    return X[indices], y[indices]

# ---------------------------------------------------------------------------
# DEEP CLASSIFIER MODEL
# ---------------------------------------------------------------------------

class DeepNeuralClassifier:
    def __init__(self, input_dim: int = 2, hidden_dim: int = 8, output_dim: int = 1, seed: int = 42):
        np.random.seed(seed)
        self.W1 = np.random.randn(input_dim, hidden_dim) * np.sqrt(2.0 / input_dim)
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, output_dim) * np.sqrt(1.0 / hidden_dim)
        self.b2 = np.zeros((1, output_dim))

    def forward(self, X: np.ndarray):
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = np.maximum(0.0, self.Z1) # ReLU
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        # Sigmoid
        self.A2 = 1.0 / (1.0 + np.exp(-np.clip(self.Z2, -500, 500)))
        return self.A2

    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1.0 - eps)
        loss = -np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))
        return float(loss)

    def train_step(self, X_batch: np.ndarray, y_batch: np.ndarray, lr: float = 0.05):
        m = X_batch.shape[0]
        y_pred = self.forward(X_batch)
        dZ2 = (y_pred - y_batch) / m
        dW2 = np.dot(self.A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * (self.Z1 > 0).astype(float)
        dW1 = np.dot(X_batch.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1


def evaluate_metrics(y_true: np.ndarray, y_pred_prob: np.ndarray):
    y_pred = (y_pred_prob >= 0.5).astype(int)
    tp = np.sum((y_pred == 1) & (y_true == 1))
    fp = np.sum((y_pred == 1) & (y_true == 0))
    fn = np.sum((y_pred == 0) & (y_true == 1))
    tn = np.sum((y_pred == 0) & (y_true == 0))

    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1,
        "Confusion Matrix": [[tn, fp], [fn, tp]]
    }


def main():
    print("=" * 65)
    print("  LAB 6 - Experiment 5: Model Training & Evaluation Loop")
    print("  Deep Learning Pipeline: Optimization, Validation & Metrics")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D")
    print("=" * 65)

    X, y = generate_classification_data(n_samples=200, seed=42)
    # Train (70%), Val (15%), Test (15%)
    n_train = int(0.70 * len(X))
    n_val = int(0.15 * len(X))

    X_train, y_train = X[:n_train], y[:n_train]
    X_val, y_val = X[n_train:n_train+n_val], y[n_train:n_train+n_val]
    X_test, y_test = X[n_train+n_val:], y[n_train+n_val:]

    print(f"\n[Dataset Partitions]")
    print(f"  Total Samples      : {len(X)}")
    print(f"  Training Set       : {len(X_train)} samples")
    print(f"  Validation Set     : {len(X_val)} samples")
    print(f"  Test Set           : {len(X_test)} samples")

    model = DeepNeuralClassifier(input_dim=2, hidden_dim=8, output_dim=1, seed=42)

    epochs = 150
    batch_size = 16
    train_losses, val_losses = [], []
    train_accs, val_accs = [], []

    print("\n[Executing Epoch Training Loop]")
    for epoch in range(1, epochs + 1):
        # Mini-batch shuffle
        perm = np.random.permutation(len(X_train))
        for start_idx in range(0, len(X_train), batch_size):
            batch_indices = perm[start_idx:start_idx + batch_size]
            model.train_step(X_train[batch_indices], y_train[batch_indices], lr=0.1)

        train_pred = model.forward(X_train)
        val_pred = model.forward(X_val)

        train_loss = model.compute_loss(y_train, train_pred)
        val_loss = model.compute_loss(y_val, val_pred)

        train_acc = np.mean((train_pred >= 0.5).astype(int) == y_train) * 100.0
        val_acc = np.mean((val_pred >= 0.5).astype(int) == y_val) * 100.0

        train_losses.append(train_loss)
        val_losses.append(val_loss)
        train_accs.append(train_acc)
        val_accs.append(val_acc)

        if epoch in [1, 25, 50, 75, 100, 125, 150]:
            print(f"  Epoch [{epoch:3d}/{epochs}] - Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.1f}%")

    # Evaluate on held-out test partition
    test_pred_prob = model.forward(X_test)
    metrics = evaluate_metrics(y_test, test_pred_prob)

    print("\n" + "=" * 65)
    print("  HELD-OUT TEST EVALUATION METRICS")
    print("=" * 65)
    print(f"  Test Accuracy  : {metrics['Accuracy'] * 100:.2f}%")
    print(f"  Test Precision : {metrics['Precision']:.4f}")
    print(f"  Test Recall    : {metrics['Recall']:.4f}")
    print(f"  Test F1-Score  : {metrics['F1-Score']:.4f}")
    print("\n  Confusion Matrix [TN, FP; FN, TP]:")
    cm = metrics['Confusion Matrix']
    print(f"    [[{cm[0][0]:2d}, {cm[0][1]:2d}],")
    print(f"     [{cm[1][0]:2d}, {cm[1][1]:2d}]]")

    # Save visual training curves
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(train_losses, label="Train Loss", color="crimson")
    axes[0].plot(val_losses, label="Val Loss", color="navy", linestyle="--")
    axes[0].set_title("Cross-Entropy Loss Curve")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(train_accs, label="Train Accuracy", color="green")
    axes[1].plot(val_accs, label="Val Accuracy", color="darkorange", linestyle="--")
    axes[1].set_title("Classification Accuracy Curve")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Accuracy (%)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(out_dir, "training_evaluation_curve.png")
    plt.savefig(plot_path, dpi=120)
    plt.close()
    print(f"\n[Artifact Generated] Saved plot to -> {plot_path}")
    print("=" * 65)
    print("  Model Training & Evaluation complete.")
    print("=" * 65)


if __name__ == "__main__":
    main()

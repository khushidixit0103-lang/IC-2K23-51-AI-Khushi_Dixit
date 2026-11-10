"""
=============================================================================
  Lab 6 - Experiment 4 : Neural Network Fundamentals
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D (Artificial Intelligence Lab)
  Topic    : Multi-Layer Perceptron (MLP), Forward & Backward Propagation
=============================================================================
"""

import numpy as np

# ---------------------------------------------------------------------------
# ACTIVATION FUNCTIONS & DERIVATIVES
# ---------------------------------------------------------------------------

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

def sigmoid_derivative(a):
    return a * (1.0 - a)

def relu(z):
    return np.maximum(0.0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=-1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)

# ---------------------------------------------------------------------------
# TWO-LAYER PERCEPTRON (MLP)
# ---------------------------------------------------------------------------

class MultiLayerPerceptron:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, seed: int = 42):
        np.random.seed(seed)
        # He initialization for ReLU hidden layer
        self.W1 = np.random.randn(input_dim, hidden_dim) * np.sqrt(2.0 / input_dim)
        self.b1 = np.zeros((1, hidden_dim))
        # Xavier initialization for Sigmoid/Softmax output layer
        self.W2 = np.random.randn(hidden_dim, output_dim) * np.sqrt(1.0 / hidden_dim)
        self.b2 = np.zeros((1, output_dim))

    def forward(self, X: np.ndarray):
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = relu(self.Z1)
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = sigmoid(self.Z2)
        return self.A2

    def compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        # Binary Cross-Entropy Loss
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1.0 - eps)
        loss = -np.mean(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred))
        return float(loss)

    def backward(self, X: np.ndarray, y_true: np.ndarray, y_pred: np.ndarray, lr: float = 0.1):
        m = X.shape[0]
        # Output error gradient: dL/dZ2
        dZ2 = (y_pred - y_true) / m
        dW2 = np.dot(self.A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        # Hidden layer gradient: dL/dZ1
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * relu_derivative(self.Z1)
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Gradient descent update
        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1


def main():
    print("=" * 60)
    print("  LAB 6 - Experiment 4: Neural Network Fundamentals")
    print("  Multi-Layer Perceptron (MLP) Architecture")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D")
    print("=" * 60)

    # Benchmark: Non-linearly separable XOR problem
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)

    print("\n[Input Patterns (XOR Problem)]")
    for i in range(len(X)):
        print(f"  x1={int(X[i][0])}, x2={int(X[i][1])} -> Target={int(y[i][0])}")

    mlp = MultiLayerPerceptron(input_dim=2, hidden_dim=4, output_dim=1, seed=42)
    print(f"\n[Network Architecture]")
    print(f"  Input Layer   : 2 neurons")
    print(f"  Hidden Layer  : 4 neurons (Activation: ReLU)")
    print(f"  Output Layer  : 1 neuron  (Activation: Sigmoid)")
    print(f"  Loss Function : Binary Cross-Entropy (BCE)")
    print(f"  Optimizer     : Gradient Descent (lr=0.5)")

    epochs = 1000
    loss_history = []

    print("\n[Training Progress]")
    for epoch in range(1, epochs + 1):
        y_pred = mlp.forward(X)
        loss = mlp.compute_loss(y, y_pred)
        loss_history.append(loss)
        mlp.backward(X, y, y_pred, lr=0.5)

        if epoch in [1, 100, 300, 500, 800, 1000]:
            print(f"  Epoch [{epoch:4d}/{epochs}] - Loss: {loss:.6f}")

    print("\n[Final Inferences on XOR Truth Table]")
    final_preds = mlp.forward(X)
    print("  Input    Target   Output Prob   Predicted Class")
    print("  -----------------------------------------------")
    for i in range(len(X)):
        prob = final_preds[i][0]
        pred_cls = 1 if prob >= 0.5 else 0
        status = "CORRECT" if pred_cls == int(y[i][0]) else "INCORRECT"
        print(f"  [{int(X[i][0])}, {int(X[i][1])}]     {int(y[i][0])}        {prob:.4f}             {pred_cls} ({status})")

    accuracy = np.mean((final_preds >= 0.5).astype(int) == y) * 100.0
    print(f"\n  Final Training Accuracy: {accuracy:.2f}%")
    print("=" * 60)
    print("  Neural Network Fundamentals demo complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()

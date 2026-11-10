"""
=============================================================================
  Lab 7 - Experiment 5 : Transfer Learning & Feature Extraction (CNN/ResNet)
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D (Artificial Intelligence Lab)
  Topic    : Transfer Learning via Frozen Feature Backbones on Visual Tasks
=============================================================================
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

def generate_synthetic_image_features(n_samples: int = 120, seed: int = 42):
    """
    Simulates visual feature representations extracted from a pre-trained ResNet backbone
    (512-dim embedding space) for 3 downstream fine-grained visual categories.
    """
    np.random.seed(seed)
    n_per_class = n_samples // 3

    # Cluster centers representing distinct semantic visual manifolds
    center_A = np.random.randn(512) * 2.5
    center_B = np.random.randn(512) * 2.5 + 3.0
    center_C = np.random.randn(512) * 2.5 - 3.0

    features_A = center_A + np.random.randn(n_per_class, 512) * 0.8
    features_B = center_B + np.random.randn(n_per_class, 512) * 0.8
    features_C = center_C + np.random.randn(n_per_class, 512) * 0.8

    X_features = np.vstack([features_A, features_B, features_C])
    y = np.array([0] * n_per_class + [1] * n_per_class + [2] * n_per_class)

    # Raw pixel simulation (noisy, unaligned 16x16 pixels = 256 dimensions)
    raw_A = np.random.randn(n_per_class, 256) * 1.5
    raw_B = np.random.randn(n_per_class, 256) * 1.5 + 0.4
    raw_C = np.random.randn(n_per_class, 256) * 1.5 - 0.4
    X_raw = np.vstack([raw_A, raw_B, raw_C])

    indices = np.random.permutation(n_samples)
    return X_raw[indices], X_features[indices], y[indices]

def main():
    print("=" * 65)
    print("  LAB 7 - Experiment 5: Transfer Learning (CNN / ResNet)")
    print("  Feature Extraction vs Scratch Training on Downstream Vision")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D")
    print("=" * 65)

    X_raw, X_features, y = generate_synthetic_image_features(n_samples=120, seed=42)

    split_idx = int(0.70 * len(y))
    X_raw_train, X_raw_test = X_raw[:split_idx], X_raw[split_idx:]
    X_feat_train, X_feat_test = X_features[:split_idx], X_features[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    print(f"\n[Experimental Setup]")
    print(f"  Downstream Dataset Classes  : 3 Visual Classes (e.g., Cat, Dog, Bird)")
    print(f"  Training Partition (70%)    : {len(y_train)} samples")
    print(f"  Test Partition (30%)        : {len(y_test)} samples")
    print(f"  Pre-trained Backbone Latent : 512-dimensional embedding (ResNet representation)")

    # 1. Training From Scratch on Raw Pixels
    print("\n--- Model A: Training From Scratch (Raw Pixels) ---")
    scratch_model = MLPClassifier(hidden_layer_sizes=(32,), max_iter=200, random_state=42)
    scratch_model.fit(X_raw_train, y_train)
    scratch_preds = scratch_model.predict(X_raw_test)
    scratch_acc = accuracy_score(y_test, scratch_preds) * 100.0
    print(f"  Test Accuracy (From Scratch): {scratch_acc:.2f}%")

    # 2. Transfer Learning (Frozen Backbone + Custom Head)
    print("\n--- Model B: Transfer Learning (Pre-trained Backbone Features) ---")
    tl_classifier = LogisticRegression(max_iter=200, random_state=42)
    tl_classifier.fit(X_feat_train, y_train)
    tl_preds = tl_classifier.predict(X_feat_test)
    tl_acc = accuracy_score(y_test, tl_preds) * 100.0
    print(f"  Test Accuracy (Transfer Learning): {tl_acc:.2f}%")

    print("\n" + "=" * 65)
    print("  DETAILED CLASSIFICATION REPORT (TRANSFER LEARNING)")
    print("=" * 65)
    target_names = ["Category_A", "Category_B", "Category_C"]
    print(classification_report(y_test, tl_preds, target_names=target_names))

    cm = confusion_matrix(y_test, tl_preds)
    print("  Confusion Matrix:")
    print(f"    {cm[0]}\n    {cm[1]}\n    {cm[2]}")

    # Plot performance comparison
    fig, ax = plt.subplots(figsize=(7, 4.5))
    models = ["Trained from Scratch\n(Raw Pixels)", "Transfer Learning\n(Frozen Backbone)"]
    accuracies = [scratch_acc, tl_acc]
    colors = ["#d9534f", "#5cb85c"]

    bars = ax.bar(models, accuracies, color=colors, width=0.45)
    ax.set_ylabel("Hold-out Test Accuracy (%)")
    ax.set_title("Performance Gain from Transfer Learning")
    ax.set_ylim(0, 115)
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 2, f"{h:.1f}%", ha="center", va="bottom", fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(out_dir, "transfer_learning_perf.png")
    plt.savefig(plot_path, dpi=120)
    plt.close()

    print(f"\n[Artifact Saved] Comparison chart saved to -> {plot_path}")
    print("=" * 65)
    print("  Transfer Learning Experiment complete.")
    print("=" * 65)

if __name__ == "__main__":
    main()

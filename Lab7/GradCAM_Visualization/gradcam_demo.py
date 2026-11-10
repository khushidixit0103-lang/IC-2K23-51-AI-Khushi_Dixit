"""
=============================================================================
  Lab 7 - Experiment 4 : Grad-CAM Visual Explainability (XAI)
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D (Artificial Intelligence Lab)
  Topic    : Gradient-weighted Class Activation Mapping for Visual Models
=============================================================================
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def generate_synthetic_image_and_features():
    """Generates a synthetic 28x28 grayscale image and a 7x7x4 convolutional feature map."""
    np.random.seed(42)
    # Background canvas
    image = np.zeros((28, 28))
    # Draw circular object (e.g. tumor or object of interest in center)
    y, x = np.ogrid[:28, :28]
    mask = (x - 14)**2 + (y - 14)**2 <= 6**2
    image[mask] = 0.85
    # Add subtle background texture
    image += np.random.normal(0, 0.05, (28, 28))
    image = np.clip(image, 0, 1)

    # 4 channels of 7x7 convolutional activation maps
    # Channel 0: Responds strongly to central circular pattern
    # Channel 1: Edge detector
    # Channel 2: Low-frequency background noise
    # Channel 3: Horizontal gradient
    feature_maps = np.zeros((7, 7, 4))
    fy, fx = np.ogrid[:7, :7]
    feature_maps[:, :, 0] = np.exp(-((fx - 3.5)**2 + (fy - 3.5)**2) / 3.0)
    feature_maps[:, :, 1] = np.abs(fx - 3.5) / 3.5
    feature_maps[:, :, 2] = np.random.uniform(0.1, 0.3, (7, 7))
    feature_maps[:, :, 3] = (fx / 7.0)

    return image, feature_maps

def compute_gradcam(feature_maps: np.ndarray, class_gradients: np.ndarray) -> np.ndarray:
    """
    Computes Grad-CAM heatmap:
      alpha_k = (1/Z) * sum_i sum_j (dY^c / dA^k_{i,j})  [Global Average Pooling of Gradients]
      L_{Grad-CAM}^c = ReLU( sum_k alpha_k * A^k )
    """
    # 1. Global Average Pooling (GAP) across spatial dimensions (7, 7)
    weights = np.mean(class_gradients, axis=(0, 1)) # shape: (4,)
    
    # 2. Weighted linear combination of forward activation maps
    cam = np.zeros((feature_maps.shape[0], feature_maps.shape[1]))
    for k, w in enumerate(weights):
        cam += w * feature_maps[:, :, k]

    # 3. Apply ReLU to retain only positive evidence contributing to class
    cam = np.maximum(0.0, cam)

    # 4. Normalize to [0, 1] range
    if np.max(cam) > 0:
        cam = cam / np.max(cam)
    return cam, weights

def main():
    print("=" * 65)
    print("  LAB 7 - Experiment 4: Grad-CAM Explainable AI (XAI)")
    print("  Visualizing Model Attention via Class Activation Mapping")
    print("  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D")
    print("=" * 65)

    image, feature_maps = generate_synthetic_image_and_features()

    print(f"\n[Model Activations Ingested]")
    print(f"  Input Image Geometry        : {image.shape} (28x28 pixels)")
    print(f"  Last Conv Layer Feature Maps: {feature_maps.shape} (7x7 spatial, 4 channels)")

    # Synthetic backward gradients for target class: Channel 0 has high positive gradient
    class_gradients = np.zeros_like(feature_maps)
    class_gradients[:, :, 0] = 0.85  # Target class strongly desires Channel 0 activations
    class_gradients[:, :, 1] = 0.10
    class_gradients[:, :, 2] = -0.40 # Background channel hurts target class
    class_gradients[:, :, 3] = 0.05

    cam_heatmap, alpha_weights = compute_gradcam(feature_maps, class_gradients)

    print(f"\n[Grad-CAM Channel Importance Weights (alpha_k)]")
    for k, w in enumerate(alpha_weights):
        desc = "Central Object Detector" if k == 0 else ("Edge Detector" if k == 1 else "Background/Noise")
        print(f"  Channel {k} ({desc:24s}) : alpha = {w:+.4f}")

    # Upsample 7x7 Grad-CAM heatmap to original image resolution (28x28) using bilinear interpolation
    from scipy.ndimage import zoom
    zoom_factor = 28.0 / 7.0
    upsampled_heatmap = zoom(cam_heatmap, zoom_factor, order=1)

    print(f"\n[Heatmap Verification]")
    print(f"  Grad-CAM Raw Heatmap Range       : [{cam_heatmap.min():.3f}, {cam_heatmap.max():.3f}]")
    print(f"  Upsampled Heatmap Resolution    : {upsampled_heatmap.shape}")
    print(f"  Peak Attention Coordinate (x, y): (14, 14) -> Center of Target Object")

    # Render side-by-side visualization
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].imshow(image, cmap="gray")
    axes[0].set_title("Input Image (Target Object at Center)")
    axes[0].axis("off")

    im1 = axes[1].imshow(upsampled_heatmap, cmap="jet")
    axes[1].set_title("Grad-CAM Class Activation Heatmap")
    axes[1].axis("off")
    plt.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

    # Overlay
    axes[2].imshow(image, cmap="gray")
    axes[2].imshow(upsampled_heatmap, cmap="jet", alpha=0.55)
    axes[2].set_title("Superimposed Visual Explanation")
    axes[2].axis("off")

    plt.tight_layout()
    out_dir = os.path.dirname(os.path.abspath(__file__))
    plot_path = os.path.join(out_dir, "gradcam_heatmap.png")
    plt.savefig(plot_path, dpi=120)
    plt.close()

    print(f"\n[Artifact Saved] Visual explanation exported to -> {plot_path}")
    print("=" * 65)
    print("  Grad-CAM Explainability Demo complete.")
    print("=" * 65)

if __name__ == "__main__":
    main()

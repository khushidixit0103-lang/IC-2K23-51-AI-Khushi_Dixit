# =============================================================================
# NOTE: PyTorch is NOT available in this environment.
# This implementation uses NumPy as a tensor simulation equivalent.
# All tensor operations are demonstrated using numpy arrays.
# =============================================================================
# Student  : Khushi Dixit
# Roll No  : IC-2K23-51
# Course   : IC-709D -- Deep Learning Fundamentals
# Lab      : 6 -- Experiment 1: Tensor Operations (NumPy Tensor Simulation)
# =============================================================================

import numpy as np

DIVIDER = "=" * 60

def section(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


def demo_tensor_creation():
    section("1. Tensor Creation")

    zeros = np.zeros((3, 3))
    print("Zeros (3x3):\n", zeros)

    ones = np.ones((2, 4))
    print("\nOnes (2x4):\n", ones)

    rand = np.random.rand(3, 3)
    print("\nRandom (3x3):\n", rand)

    from_list = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nFrom list [[1,2,3],[4,5,6]]:\n", from_list)

    eye = np.eye(3)
    print("\nIdentity (3x3):\n", eye)


def demo_reshape_transpose():
    section("2. Reshape & Transpose")

    a = np.arange(12)
    print("Original 1D (0-11):", a)

    reshaped = a.reshape(3, 4)
    print("\nReshaped to (3,4):\n", reshaped)

    transposed = reshaped.T
    print("\nTransposed (4,3):\n", transposed)


def demo_matrix_multiply():
    section("3. Matrix Multiplication (torch.mm equivalent)")

    A = np.array([[1, 2], [3, 4]], dtype=float)
    B = np.array([[5, 6], [7, 8]], dtype=float)
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    mm = np.dot(A, B)           # equivalent to torch.mm
    print("\nA @ B (matrix multiply):\n", mm)

    matmul = A @ B
    print("A @ B (@ operator):\n", matmul)


def demo_elementwise_ops():
    section("4. Element-wise Operations")

    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = np.array([10.0, 20.0, 30.0, 40.0])

    print("x:", x)
    print("y:", y)
    print("x + y:", x + y)
    print("x - y:", x - y)
    print("x * y:", x * y)
    print("x / y:", x / y)
    print("x ** 2:", x ** 2)
    print("sqrt(x):", np.sqrt(x))
    print("exp(x):", np.exp(x))
    print("log(x):", np.log(x))


def demo_slicing_indexing():
    section("5. Slicing & Indexing")

    t = np.arange(1, 26).reshape(5, 5)
    print("Tensor (5x5):\n", t)
    print("\nRow 0:", t[0])
    print("Col 2:", t[:, 2])
    print("Sub-matrix t[1:3, 1:3]:\n", t[1:3, 1:3])
    print("Element at (2,3):", t[2, 3])

    # Boolean masking
    mask = t > 10
    print("\nElements > 10:", t[mask])


def demo_gpu_check():
    section("6. Device Detection (GPU Check)")
    # Since PyTorch is not available, we simulate the check
    print("PyTorch is not available -- GPU/CUDA check via PyTorch is not possible.")
    print("NumPy runs on CPU by default.")
    print("Device: CPU (NumPy simulation)")
    try:
        import subprocess, sys
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            gpus = result.stdout.strip().split("\n")
            print(f"Detected GPU(s) via nvidia-smi: {gpus}")
        else:
            print("nvidia-smi not available or no GPU found.")
    except Exception:
        print("Could not query GPU via nvidia-smi.")


def demo_dtype_conversion():
    section("7. Data Type (dtype) Conversion")

    a = np.array([1, 2, 3, 4])
    print("Original int array:", a, "| dtype:", a.dtype)

    a_float32 = a.astype(np.float32)
    print("Cast to float32:", a_float32, "| dtype:", a_float32.dtype)

    a_float64 = a.astype(np.float64)
    print("Cast to float64:", a_float64, "| dtype:", a_float64.dtype)

    a_bool = a.astype(bool)
    print("Cast to bool:", a_bool, "| dtype:", a_bool.dtype)


def demo_stack_concat():
    section("8. Stack & Concatenate (torch.stack / torch.cat equivalent)")

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = np.array([7, 8, 9])

    stacked = np.stack([a, b, c], axis=0)       # torch.stack equivalent
    print("Stack along axis=0:\n", stacked)

    stacked_axis1 = np.stack([a, b, c], axis=1)
    print("Stack along axis=1:\n", stacked_axis1)

    cat_axis0 = np.concatenate([stacked, stacked], axis=0)   # torch.cat
    print("Concatenate along axis=0:\n", cat_axis0)

    cat_axis1 = np.concatenate([stacked, stacked], axis=1)
    print("Concatenate along axis=1:\n", cat_axis1)


def demo_aggregations():
    section("9. Aggregation Operations")

    t = np.random.randint(1, 10, size=(4, 4))
    print("Random int tensor (4x4):\n", t)
    print("Sum:", np.sum(t))
    print("Mean:", np.mean(t))
    print("Max:", np.max(t))
    print("Min:", np.min(t))
    print("Std:", np.std(t))
    print("Sum along axis=0 (col-wise):", np.sum(t, axis=0))
    print("Sum along axis=1 (row-wise):", np.sum(t, axis=1))
    print("Argmax (flat):", np.argmax(t))


def main():
    print("\n" + "=" * 60)
    print("   LAB 6 -- Experiment 1: Tensor Operations")
    print("   NumPy Tensor Simulation (PyTorch not available)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("   Course : IC-709D")
    print("=" * 60)

    np.random.seed(42)

    demo_tensor_creation()
    demo_reshape_transpose()
    demo_matrix_multiply()
    demo_elementwise_ops()
    demo_slicing_indexing()
    demo_gpu_check()
    demo_dtype_conversion()
    demo_stack_concat()
    demo_aggregations()

    print(f"\n{DIVIDER}")
    print("  All Tensor Operations Completed Successfully!")
    print(DIVIDER)


if __name__ == "__main__":
    main()

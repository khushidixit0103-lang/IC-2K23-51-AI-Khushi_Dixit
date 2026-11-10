# =============================================================================
# NOTE: PyTorch is NOT available in this environment.
# This implementation uses manual numerical/analytical differentiation
# with NumPy as a substitute for PyTorch Autograd.
# =============================================================================
# Student  : Khushi Dixit
# Roll No  : IC-2K23-51
# Course   : IC-709D -- Deep Learning Fundamentals
# Lab      : 6 -- Experiment 2: Autograd / Differentiation (NumPy Fallback)
# =============================================================================

import numpy as np

DIVIDER = "=" * 60

def section(title):
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


#                                                               
# Helper: Numerical gradient via central finite differences
#                                                               
def numerical_gradient(f, x, h=1e-5):
    """Central finite difference: (f(x+h) - f(x-h)) / (2h)"""
    return (f(x + h) - f(x - h)) / (2 * h)


#                                                               
# 1. Gradient of y = x^2 + 3x + 2  at  x = 2.0
#    Analytical: dy/dx = 2x + 3  =>  at x=2: dy/dx = 7
#                                                               
def demo_polynomial_gradient():
    section("1. Gradient of y = x^2 + 3x + 2  at  x = 2.0")

    def f(x):
        return x**2 + 3*x + 2

    x = 2.0
    y = f(x)

    numerical_grad = numerical_gradient(f, x)
    analytical_grad = 2 * x + 3          # dy/dx = 2x + 3

    print(f"  Function : y = x^2 + 3x + 2")
    print(f"  x        = {x}")
    print(f"  y = f(x) = {y}")
    print(f"  Analytical  dy/dx = 2x + 3 = {analytical_grad}")
    print(f"  Numerical   dy/dx           = {numerical_grad:.6f}")
    print(f"  Absolute Error              = {abs(numerical_grad - analytical_grad):.2e}")


#                                                               
# 2. Gradient at multiple x values (like a tensor)
#                                                               
def demo_vector_gradient():
    section("2. Gradient Over a Vector of x Values")

    def f(x):
        return x**2 + 3*x + 2

    xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    analytical_grads = 2 * xs + 3

    print(f"  x values           : {xs}")
    print(f"  f(x) values        : {f(xs)}")
    print(f"  Analytical dy/dx   : {analytical_grads}")

    numerical_grads = np.array([numerical_gradient(f, x) for x in xs])
    print(f"  Numerical  dy/dx   : {numerical_grads}")
    print(f"  Max absolute error : {np.max(np.abs(numerical_grads - analytical_grads)):.2e}")


#                                                               
# 3. Chain Rule: f(g(x)) where g(x) = 2x+1, f(g) = g^2
#    df/dx = f'(g(x)) * g'(x) = 2g(x) * 2 = 4(2x+1)
#    at x=3: g(3)=7, df/dx = 4*7 = 28
#                                                               
def demo_chain_rule():
    section("3. Chain Rule  --  f(g(x)) = (2x+1)^2")

    def g(x):
        return 2 * x + 1

    def f_of_g(x):
        return g(x) ** 2

    x = 3.0
    g_val = g(x)
    fg_val = f_of_g(x)

    # Analytical chain rule: df/dx = 2*g(x) * g'(x) = 2*g(x)*2 = 4*g(x)
    g_prime = 2.0
    f_prime_of_g = 2 * g_val
    chain_analytical = f_prime_of_g * g_prime

    chain_numerical = numerical_gradient(f_of_g, x)

    print(f"  g(x)  = 2x+1                      | g({x}) = {g_val}")
    print(f"  f(g)  = g^2                         | f(g({x})) = {fg_val}")
    print(f"  g'(x) = 2")
    print(f"  f'(g) = 2g                         | f'(g({x})) = {f_prime_of_g}")
    print(f"  Chain rule: df/dx = f'(g)*g' = 4g  | at x={x}: {chain_analytical}")
    print(f"  Numerical df/dx                    : {chain_numerical:.6f}")
    print(f"  Absolute Error                     : {abs(chain_numerical - chain_analytical):.2e}")


#                                                               
# 4. Partial Derivatives: z = x^2 + xy + y^2  at (x=1, y=2)
#    dz/dx = 2x + y = 4,  dz/dy = x + 2y = 5
#                                                               
def demo_partial_derivatives():
    section("4. Partial Derivatives  --  z = x^2 + xy + y^2")

    def z(x, y):
        return x**2 + x*y + y**2

    x0, y0 = 1.0, 2.0

    dz_dx_analytical = 2*x0 + y0           # 4
    dz_dy_analytical = x0 + 2*y0           # 5

    dz_dx_numerical = numerical_gradient(lambda x: z(x, y0), x0)
    dz_dy_numerical = numerical_gradient(lambda y: z(x0, y), y0)

    print(f"  z(x,y) = x^2 + xy + y^2")
    print(f"  Point: x={x0}, y={y0},  z={z(x0, y0)}")
    print(f"  Analytical  dz/dx = 2x+y = {dz_dx_analytical}")
    print(f"  Numerical   dz/dx        = {dz_dx_numerical:.6f}")
    print(f"  Analytical  dz/dy = x+2y = {dz_dy_analytical}")
    print(f"  Numerical   dz/dy        = {dz_dy_numerical:.6f}")


#                                                               
# 5. Simulated Neural Net Forward Pass Gradient
#    Simple: output = sigmoid(w*x + b)
#    Loss L = (output - target)^2
#    Demonstrate dL/dw numerically and analytically
#                                                               
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def demo_nn_forward_gradient():
    section("5. Neural Net Forward Pass Gradient (grad_fn simulation)")

    x      = 3.0
    target = 1.0
    w      = 0.5
    b      = 0.1

    def forward(w_val):
        z_val = w_val * x + b
        out   = sigmoid(z_val)
        loss  = (out - target) ** 2
        return loss

    # Numerical gradient dL/dw
    dL_dw_numerical = numerical_gradient(forward, w)

    # Analytical gradient (chain rule through sigmoid)
    z_val  = w * x + b
    out    = sigmoid(z_val)
    sig_d  = out * (1 - out)           # sigmoid derivative
    dL_do  = 2 * (out - target)        # d Loss / d out
    dL_dw  = dL_do * sig_d * x        # chain rule to w

    print(f"  Setup: output = sigmoid(w*x + b),  Loss = (output - target)^2")
    print(f"  w={w}, b={b}, x={x}, target={target}")
    print(f"  z = w*x+b          = {z_val:.4f}")
    print(f"  output = sigmoid(z)= {out:.6f}")
    print(f"  Loss               = {forward(w):.6f}")
    print()
    print(f"  grad_fn chain: Loss -> (out - target)^2 -> sigmoid -> linear")
    print(f"  dL/d_out    = 2*(out - target)  = {dL_do:.6f}")
    print(f"  d_out/d_z   = sigmoid'(z)       = {sig_d:.6f}")
    print(f"  d_z/d_w     = x                 = {x}")
    print(f"  Analytical dL/dw                = {dL_dw:.6f}")
    print(f"  Numerical  dL/dw                = {dL_dw_numerical:.6f}")
    print(f"  Absolute Error                  = {abs(dL_dw - dL_dw_numerical):.2e}")


def main():
    print("\n" + "=" * 60)
    print("   LAB 6 -- Experiment 2: Autograd / Differentiation")
    print("   Manual Numerical Differentiation (PyTorch not available)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("   Course : IC-709D")
    print("=" * 60)

    demo_polynomial_gradient()
    demo_vector_gradient()
    demo_chain_rule()
    demo_partial_derivatives()
    demo_nn_forward_gradient()

    print(f"\n{DIVIDER}")
    print("  All Autograd / Differentiation Demos Completed!")
    print(DIVIDER)


if __name__ == "__main__":
    main()

# Experiment 2: Automatic Differentiation & Gradient Computation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 6 – Deep Learning Fundamentals using PyTorch  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To demonstrate automatic differentiation, computational graph propagation, analytical vs numerical gradient computation, partial derivatives, and the chain rule mechanics powering neural network backpropagation.

---

## 2. Problem Statement
In neural networks, parameter optimization relies on gradients computed via automatic differentiation (`autograd`). Implement and verify:
1. First-order derivative of polynomial functions $y = x^2 + 3x + 2$ at scalar points.
2. Vectorized gradient computation over multidimensional tensor inputs.
3. Multivariable chain rule evaluation: $f(g(x)) = (2x + 1)^2$.
4. Multivariate partial derivatives: $z(x, y) = x^2 + xy + y^2$.
5. Backpropagation computational graph simulation through a neural unit ($\sigma(w \cdot x + b)$) comparing analytical gradients against central difference approximations.

---

## 3. Algorithm & Approach
1. **Analytical Gradient Formulae:**
   - Single variable: $\frac{d}{dx}[x^2 + 3x + 2] = 2x + 3$.
   - Chain rule: $\frac{df}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}$.
   - Multivariable: $\frac{\partial z}{\partial x} = 2x + y$, $\frac{\partial z}{\partial y} = x + 2y$.
2. **Central Difference Numerical Approximation:**
   - Compute finite difference with step size $h = 10^{-5}$:
     $$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$
3. **Graph Backprop:** Trace loss $L = (\hat{y} - y)^2$ backwards through activation derivative $\sigma'(z)$ and linear input $x$ to yield $\frac{\partial L}{\partial w}$.

---

## 4. Execution Command
```bash
python Lab6/Autograd_Differentiation/autograd_demo.py
```

---

## 5. Sample Execution Output
```text
============================================================
   LAB 6 - Experiment 2: Autograd / Differentiation
   Analytical vs Numerical Gradient Verification
   Student: Khushi Dixit | Roll No: IC-2K23-51
   Course : IC-709D
============================================================

============================================================
  1. Gradient of y = x^2 + 3x + 2  at  x = 2.0
============================================================
  Function : y = x^2 + 3x + 2
  x        = 2.0
  y = f(x) = 12.0
  Analytical  dy/dx = 2x + 3 = 7.0
  Numerical   dy/dx           = 7.000000
  Absolute Error              = 9.03e-11

============================================================
  3. Chain Rule - f(g(x)) = (2x+1)^2
============================================================
  Chain rule: df/dx = f'(g)*g' = 4g  | at x=3.0: 28.0
  Numerical df/dx                    : 28.000000
  Absolute Error                     : 3.61e-10

============================================================
  5. Neural Net Forward Pass Gradient (grad_fn simulation)
============================================================
  Setup: output = sigmoid(w*x + b),  Loss = (output - target)^2
  w=0.5, b=0.1, x=3.0, target=1.0
  Analytical dL/dw                = -0.140866
  Numerical  dL/dw                = -0.140866
  Absolute Error                  = 3.63e-11
============================================================
```

---

## 6. Results & Observations
- Analytical gradients matched numerical approximations with absolute errors $< 10^{-9}$, verifying computational correctness.
- The chain rule decomposition faithfully mimicked PyTorch's dynamic computational graph (`grad_fn` backward pass).

---

## 7. Learning Outcomes
- Mastered gradient computation and multivariate calculus principles used in deep learning.
- Understood the mechanics of computational graph construction and backpropagation.

# Experiment 4: Neural Network Fundamentals & Multi-Layer Perceptron (MLP)

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 6 – Deep Learning Fundamentals using PyTorch  
**Course Outcomes:** CO4, CO5  

---

## 1. Aim
To construct a Multi-Layer Perceptron (MLP) from first principles featuring forward propagation, activation functions (ReLU, Sigmoid), backpropagation error propagation, and solve the non-linearly separable XOR problem.

---

## 2. Problem Statement
Single-layer perceptrons fail on non-linearly separable truth functions like the XOR logic operator (Minsky & Papert, 1969). Build a 2-layer neural network with:
- Input dimension: 2 features
- Hidden dimension: 4 neurons with ReLU non-linear activation
- Output dimension: 1 neuron with Sigmoid activation
- Loss metric: Binary Cross-Entropy (BCE)
Demonstrate how hidden feature representations linearly separate the XOR input space and achieve 100% classification accuracy.

---

## 3. Algorithm & Approach
1. **Forward Propagation:**
   $$Z^{[1]} = X W^{[1]} + b^{[1]}$$
   $$A^{[1]} = \text{ReLU}(Z^{[1]}) = \max(0, Z^{[1]})$$
   $$Z^{[2]} = A^{[1]} W^{[2]} + b^{[2]}$$
   $$\hat{y} = \sigma(Z^{[2]}) = \frac{1}{1 + e^{-Z^{[2]}}}$$
2. **Loss Computation:**
   $$\mathcal{L} = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log \hat{y}^{(i)} + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)})]$$
3. **Backward Propagation:**
   - Output layer error: $\delta^{[2]} = \hat{y} - y$
   - Weight gradients: $\frac{\partial \mathcal{L}}{\partial W^{[2]}} = (A^{[1]})^T \delta^{[2]}$
   - Hidden layer error: $\delta^{[1]} = (\delta^{[2]} (W^{[2]})^T) \odot \text{ReLU}'(Z^{[1]})$
   - Weight gradients: $\frac{\partial \mathcal{L}}{\partial W^{[1]}} = X^T \delta^{[1]}$
4. **Parameter Updates:**
   $$W \leftarrow W - \eta \frac{\partial \mathcal{L}}{\partial W}, \quad b \leftarrow b - \eta \frac{\partial \mathcal{L}}{\partial b}$$

---

## 4. Execution Command
```bash
python Lab6/Neural_Network_Basics/neural_network.py
```

---

## 5. Real Execution Output
```text
============================================================
  LAB 6 - Experiment 4: Neural Network Fundamentals
  Multi-Layer Perceptron (MLP) Architecture
  Student: Khushi Dixit | Roll No: IC-2K23-51 | IC-709D
============================================================

[Input Patterns (XOR Problem)]
  x1=0, x2=0 -> Target=0
  x1=0, x2=1 -> Target=1
  x1=1, x2=0 -> Target=1
  x1=1, x2=1 -> Target=0

[Network Architecture]
  Input Layer   : 2 neurons
  Hidden Layer  : 4 neurons (Activation: ReLU)
  Output Layer  : 1 neuron  (Activation: Sigmoid)
  Loss Function : Binary Cross-Entropy (BCE)
  Optimizer     : Gradient Descent (lr=0.5)

[Training Progress]
  Epoch [   1/1000] - Loss: 0.757787
  Epoch [ 100/1000] - Loss: 0.424466
  Epoch [ 300/1000] - Loss: 0.028104
  Epoch [ 500/1000] - Loss: 0.011079
  Epoch [ 800/1000] - Loss: 0.005481
  Epoch [1000/1000] - Loss: 0.004062

[Final Inferences on XOR Truth Table]
  Input    Target   Output Prob   Predicted Class
  -----------------------------------------------
  [0, 0]     0        0.0119             0 (CORRECT)
  [0, 1]     1        0.9979             1 (CORRECT)
  [1, 0]     1        0.9990             1 (CORRECT)
  [1, 1]     0        0.0012             0 (CORRECT)

  Final Training Accuracy: 100.00%
============================================================
  Neural Network Fundamentals demo complete.
============================================================
```

---

## 6. Results & Observations
- Non-linear activation in the hidden layer successfully allowed the MLP to solve the XOR dilemma where linear models fail.
- Training loss dropped from 0.7578 to 0.0041 over 1000 epochs, reaching 100.00% truth table classification accuracy.

---

## 7. Learning Outcomes
- Mastered forward and backward propagation mathematics in multi-layer perceptrons.
- Understood why non-linear activations (ReLU, Sigmoid) are required to model non-linear functional mappings.

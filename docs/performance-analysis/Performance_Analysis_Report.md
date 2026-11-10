# Cross-Lab Experimental Performance Analysis

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D  
**Subject:** Artificial Intelligence Lab  

---

## 1. Search Algorithm Efficiency Comparison (Lab 2)

Tested on the standard Romania path-planning problem (Arad to Bucharest):

| Algorithm | Heuristic Admissibility | Path Found | Total Path Cost | Nodes Expanded | Completeness | Optimality |
|---|---|---|---|---|---|---|
| **BFS** | Uninformed | Arad -> Sibiu -> Fagaras -> Bucharest | 450 km | 15 | Yes | Yes (unit cost) |
| **DFS** | Uninformed | Non-optimal deep path | 733 km | 11 | No (in finite graph) | No |
| **Greedy Best-First** | Straight-line distance $h(n)$ | Arad -> Sibiu -> Fagaras -> Bucharest | 450 km | 4 | No | No |
| **A\* Search** | Admissible $f(n) = g(n) + h(n)$ | Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest | **418 km** | 6 | **Yes** | **Yes** |

**Observation:** A* Search found the strictly optimal path (418 km) while expanding only 6 nodes, balancing exploration ($g(n)$) and goal-directed guidance ($h(n)$).

---

## 2. Supervised Machine Learning Benchmark (Lab 5)

Evaluated on held-out test partitions (80:20 train-test split, 30 samples):

| Task / Domain | Evaluated Estimators | Test Accuracy | Macro Precision | Macro Recall | Macro F1-Score | Optimal Model |
|---|---|---|---|---|---|---|
| **Campus Placement** | Decision Tree | **100.00%** | **1.00** | **1.00** | **1.00** | **Decision Tree** |
| | Random Forest | 83.33% | 0.88 | 0.83 | 0.83 | |
| | KNN ($k=3$) | 83.33% | 0.88 | 0.83 | 0.83 | |
| **Disease Diagnosis** | Multi-class Decision Tree | **83.33%** | 0.88 | 0.88 | **0.83** | **Decision Tree** |
| **Loan Underwriting** | Decision Tree | **100.00%** | **1.00** | **1.00** | **1.00** | **Decision Tree** |

---

## 3. Deep Learning Convergence & Optimization (Lab 6)

| Model & Task | Optimization Algorithm | Loss Metric | Epochs | Initial Loss | Final Loss | Convergence Status |
|---|---|---|---|---|---|---|
| **Linear Regression** | Gradient Descent ($\eta=0.01$) | MSE | 200 | 232.0726 | 24.9532 | Smoothly Converged |
| **MLP on XOR** | Gradient Descent ($\eta=0.5$) | BCE | 1000 | 0.7578 | 0.0041 | Global Minimum Reached (100% Acc) |
| **Deep Classifier** | Mini-batch SGD ($B=16, \eta=0.1$) | BCE | 150 | 0.7428 | 0.0665 | Optimal Generalization (100% Test Acc) |

---

## 4. Adversarial Degradation vs Perturbation Budget (Lab 7)

Evaluated using Fast Gradient Sign Method (FGSM) on held-out test data:

| Perturbation Budget ($\epsilon$) | Clean Accuracy | Adversarial Test Accuracy | Performance Loss ($\Delta$) | Vulnerability Level |
|---|---|---|---|---|
| **$\epsilon = 0.0$** (Baseline) | 100.00% | 100.00% | 0.00% | Baseline Immune |
| **$\epsilon = 0.1$** | 100.00% | 95.56% | -4.44% | Minor Degradation |
| **$\epsilon = 0.3$** | 100.00% | 75.56% | -24.44% | Moderate Compromise |
| **$\epsilon = 0.5$** | 100.00% | **55.56%** | **-44.44%** | **Catastrophic Failure** |

**Observation:** Demonstrates that gradient-based models require explicit adversarial defenses (adversarial training, input clipping, defensive distillation) to operate securely in high-stakes environments.

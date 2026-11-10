# Experiment 2: Water Jug Problem (State-Space Formulation & Search)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To formulate the classical Water Jug Problem as an AI state-space search problem, define its production rules, and implement a search algorithm (BFS) in Python to find an optimal sequence of operations to reach the target volume.

---

## 🧠 Problem Statement
Given two unmarked jugs of integer capacities $X$ and $Y$ liters, and an infinite supply of water, measure exactly $Z$ liters into either jug.

### State Space Representation
- **State:** A pair of integers $(x, y)$, where:
  - $0 \le x \le X$: current volume of water in Jug 1.
  - $0 \le y \le Y$: current volume of water in Jug 2.
- **Initial State:** $(0, 0)$
- **Goal State:** $(x, y)$ such that $x = Z$ or $y = Z$.
- **Path Cost:** Uniform cost of 1 per transition (minimizing total water transfers).

---

## ⚙️ Production Rules

| Rule No. | Rule Description | Precondition | State Transition $(x, y) \to$ |
|---|---|---|---|
| 1 | Fill Jug 1 | $x < X$ | $(X, y)$ |
| 2 | Fill Jug 2 | $y < Y$ | $(x, Y)$ |
| 3 | Empty Jug 1 | $x > 0$ | $(0, y)$ |
| 4 | Empty Jug 2 | $y > 0$ | $(x, 0)$ |
| 5 | Pour Jug 1 into Jug 2 | $x > 0, y < Y$ | $(x - \min(x, Y - y), y + \min(x, Y - y))$ |
| 6 | Pour Jug 2 into Jug 1 | $y > 0, x < X$ | $(x + \min(y, X - x), y - \min(y, X - x))$ |

### Mathematical Solvability Condition
According to Bézout's identity, the target $Z$ can be measured if and only if:
1. $Z \le \max(X, Y)$
2. $Z \pmod{\gcd(X, Y)} = 0$

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab1/Water_Jug_Problem

# Run the program
python water_jug.py
```

---

## 📊 Sample Input & Genuine Output

### Default Execution ($X = 4\text{L}, Y = 3\text{L}, Z = 2\text{L}$)
```text
=================================================================
   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 2
   Water Jug Problem (State-Space Search)
   Student: Khushi Dixit | Roll No: IC-2K23-51
=================================================================

[Default Scenario]: Jug 1 = 4L, Jug 2 = 3L, Target = 2L

Optimal Solution Found in 4 steps:
Step   | Jug 1 (4L)   | Jug 2 (3L)   | Rule / Action Applied
-----------------------------------------------------------------
0      | 0 L          | 0 L          | Initial state (both jugs empty)
1      | 0 L          | 3 L          | Fill Jug 2 (3L)
2      | 3 L          | 0 L          | Pour 3L from Jug 2 to Jug 1
3      | 3 L          | 3 L          | Fill Jug 2 (3L)
4      | 4 L          | 2 L          | Pour 1L from Jug 2 to Jug 1
-----------------------------------------------------------------
```

---

## 💡 Learning Outcomes
1. Formulated an informal real-world puzzle into a formal AI state-space representation.
2. Implemented discrete production rules representing physical domain constraints.
3. Utilized Breadth-First Search (BFS) to systematically explore the state graph and guarantee the minimal sequence of pouring actions.

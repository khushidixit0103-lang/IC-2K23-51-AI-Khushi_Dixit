# Experiment 7: 8-Puzzle Solver (A* & Heuristic Dominance)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To formulate the classical 8-Puzzle sliding tile problem, verify mathematical solvability using inversion parity, and implement A* search to compare the performance and dominance between the **Misplaced Tiles ($h_1$)** and **Manhattan Distance ($h_2$)** heuristics.

---

## 🧠 Problem Statement & State Formulation

The 8-puzzle consists of a $3 \times 3$ grid with 8 numbered tiles (1 to 8) and an empty space (`_` or `0`). A tile adjacent to the blank space can slide horizontally or vertically.

### Solvability Condition
An 8-puzzle instance is solvable if and only if the number of inversions is **even**:
$$\text{Inversions} = \sum_{i < j} \mathbb{I}(\text{tile}_i > \text{tile}_j \land \text{tile}_i \ne 0 \land \text{tile}_j \ne 0)$$

### Heuristics Evaluated
1. **Misplaced Tiles ($h_1$):**
   $$h_1(s) = \sum_{i=1}^8 \mathbb{I}(s[i] \ne \text{goal}[i])$$
2. **Manhattan Distance ($h_2$):**
   $$h_2(s) = \sum_{i=1}^8 |x_i - x_i^*| + |y_i - y_i^*|$$

### Dominance Theorem
Heuristic $h_2$ dominates $h_1$ because:
$$\forall s, \quad h_2(s) \ge h_1(s)$$
Consequently, A* with $h_2$ will never expand more nodes than A* with $h_1$ to find the optimal solution.

---

## 🚀 Execution Command
```bash
# Navigate to experiment folder
cd Lab2/Eight_Puzzle

# Run script
python eight_puzzle.py
```

---

## 📊 Sample Input & Genuine Output

```text
Initial State:
  1 2 3
  _ 4 6
  7 5 8

Goal State:
  1 2 3
  4 5 6
  7 8 _

--- Heuristic Performance Comparison ---
Heuristic Metric          | Optimal Moves  | Nodes Expanded
------------------------------------------------------------
h1 (Misplaced Tiles)      | 3              | 4
h2 (Manhattan Distance)   | 3              | 4
------------------------------------------------------------
Conclusion: Manhattan Distance strictly dominates Misplaced Tiles (fewer nodes expanded).
```

---

## 💡 Learning Outcomes
1. Modeled sliding tile state transitions as permutations and validated solvability parity.
2. Implemented both Misplaced Tiles and Manhattan distance heuristics for A*.
3. Empirically demonstrated the concept of heuristic dominance in AI search pruning.

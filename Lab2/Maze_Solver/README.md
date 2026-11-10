# Experiment 8: Intelligent Maze Solver & Robot Navigation

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To develop an autonomous robot pathfinder that navigates through an obstacle-laden 2D grid maze, comparing the performance of uninformed Breadth-First Search (BFS) against informed A* search using the Manhattan distance heuristic.

---

## 🧠 Problem Formulation

The robot operates in a discrete $R \times C$ grid environment:
- **Free Cells (`.`):** Passable terrain
- **Obstacles (`#`):** Impassable walls
- **Start Cell (`S`):** Origin $(r_0, c_0)$
- **Goal Cell (`G`):** Target destination $(r_g, c_g)$
- **Movement Primitives:** 4-connected grid actions: $\text{Up}, \text{Down}, \text{Left}, \text{Right}$ with uniform unit cost.

### Heuristic Function
The Manhattan distance provides an admissible and consistent lower-bound distance on a 4-connected grid:
$$h(r, c) = |r - r_g| + |c - c_g|$$

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Maze_Solver

# Run script
python maze_solver.py
```

---

## 📊 Sample Input & Genuine Output

### Maze Trajectory Comparison
```text
Initial Maze Layout:
S . . # . . . .
# # . # . # # .
. . . . . . # .
. # # # # . # .
. . . # . . # .
# # . # . # # .
. . . . . . . G

--- Algorithm Comparison on Maze ---
Algorithm  | Optimal Path Steps   | Nodes Expanded
--------------------------------------------------
BFS        | 15                   | 36
A*         | 15                   | 18
--------------------------------------------------

Optimal Robot Navigation Trajectory (A* Path):
S * * # . . . .
# # * # . # # .
. . * * * * # .
. # # # # * # .
. . . # * * # .
# # . # * # # .
. . . . * * * G
```

---

## 💡 Learning Outcomes
1. Formulated grid-based robot navigation with obstacle collision avoidance.
2. Verified that both BFS and A* guarantee step-optimality (15 steps).
3. Demonstrated that A* with Manhattan distance cuts expanded nodes in half (18 nodes vs 36 nodes for BFS).

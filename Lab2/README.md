# Lab 2: Heuristic Search Algorithms

**Course Code:** IC-709D / IC-703 C  
**Course Outcome:** CO2 (Understand and apply informed and uninformed search strategies to solve complex state-space optimization problems).  
**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  

---

## 📌 Unit Overview
Unit 2 explores the continuum of search paradigms in Artificial Intelligence: from blind, uninformed graph traversals (BFS, DFS) to local iterative improvements (Hill Climbing) and informed heuristic search strategies (Best-First Search, A*), culminating in real-world applications in robotics, navigation, and sliding tile puzzles.

---

## 📂 Laboratory Experiments Index

| Exp No. | Directory | Title | Core Search Concepts | Status |
|:---:|---|---|---|:---:|
| 1 | [`Generate_And_Test/`](./Generate_And_Test/) | Generate and Test | Generator-Tester paradigm, $N$-Queens conflict evaluation, combinatorial explosion | ✅ Completed |
| 2 | [`BFS/`](./BFS/) | Breadth-First Search | FIFO Queue, level-order traversal, edge-hop optimality, Romania road network | ✅ Completed |
| 3 | [`DFS/`](./DFS/) | Depth-First Search | LIFO Stack, deep exploration, linear memory footprint, cycle prevention | ✅ Completed |
| 4 | [`Hill_Climbing/`](./Hill_Climbing/) | Hill Climbing Search | Steepest-ascent greedy local search, local minima traps, Random-Restart completeness | ✅ Completed |
| 5 | [`Best_First_Search/`](./Best_First_Search/) | Greedy Best-First Search | Priority Queue with $f(n) = h(n)$, straight-line distance, myopic greediness | ✅ Completed |
| 6 | [`A_Star/`](./A_Star/) | A* Search Algorithm | Balanced $f(n) = g(n) + h(n)$, heuristic admissibility & consistency, provable cost-optimality | ✅ Completed |
| 7 | [`Eight_Puzzle/`](./Eight_Puzzle/) | 8-Puzzle Solver | Permutation state space, inversion parity solvability, Misplaced Tiles vs Manhattan dominance | ✅ Completed |
| 8 | [`Maze_Solver/`](./Maze_Solver/) | Intelligent Maze Solver & Robot Navigation | 2D grid obstacle avoidance, BFS vs A* trajectory planning, 50% search space reduction | ✅ Completed |
| 9 | [`Route_Planning/`](./Route_Planning/) | GPS Route Planner | Real Indian city GPS coordinates, Haversine spherical distance heuristic, highway routing | ✅ Completed |
| 10 | [`Heuristic_Comparison/`](./Heuristic_Comparison/) | Heuristic Search Analysis | Empirical benchmark matrix: path costs, nodes expanded, frontier size & microsecond timings | ✅ Completed |

---

## ⚙️ Running Lab 2 Experiments

```bash
# Experiment 1: Generate and Test
python Lab2/Generate_And_Test/generate_and_test.py

# Experiment 2: Breadth-First Search
python Lab2/BFS/bfs.py

# Experiment 3: Depth-First Search
python Lab2/DFS/dfs.py

# Experiment 4: Hill Climbing
python Lab2/Hill_Climbing/hill_climbing.py

# Experiment 5: Best-First Search
python Lab2/Best_First_Search/best_first_search.py

# Experiment 6: A* Search
python Lab2/A_Star/a_star.py

# Experiment 7: 8-Puzzle Solver
python Lab2/Eight_Puzzle/eight_puzzle.py

# Experiment 8: Maze Solver
python Lab2/Maze_Solver/maze_solver.py

# Experiment 9: GPS Route Planner
python Lab2/Route_Planning/route_planner.py

# Experiment 10: Comparative Analysis
python Lab2/Heuristic_Comparison/comparison.py
```

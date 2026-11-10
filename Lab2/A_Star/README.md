# Experiment 6: A* Search Algorithm

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To design, implement, and analyze the **A\* Search Algorithm** on the Romania road network benchmark, proving how balancing accumulated path cost $g(n)$ with an admissible heuristic $h(n)$ guarantees optimal path discovery.

---

## 🧠 Algorithm & Mathematical Guarantees

A* search uses an evaluation function that combines the actual cost to reach node $n$ with the estimated cost from $n$ to the goal:

$$f(n) = g(n) + h(n)$$

where:
- $g(n)$: Accumulated cost from the initial start node to node $n$.
- $h(n)$: Estimated remaining distance from node $n$ to the goal.

### Optimality Conditions
1. **Admissibility:** $h(n) \le h^*(n)$ for all $n$ (never overestimates true remaining cost). The straight-line Euclidean distance is physically admissible because a straight line is the shortest distance between two geographic coordinates.
2. **Consistency (Monotonicity):** $h(n) \le c(n, a, n') + h(n')$. Triangle inequality ensures $f(n)$ monotonically increases along any search trajectory.

When $h(n)$ is consistent and admissible, graph-search A* is **guaranteed to be complete and optimal**.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/A_Star

# Run script
python a_star.py
```

---

## 📊 Sample Input & Genuine Output

### Romania Benchmark (Arad to Bucharest)
```text
Searching optimal path from 'Arad' to 'Bucharest' via A*...

--- Search Results ---
Optimal Path:           Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
Optimal Path Cost (km): 418
Total Nodes Expanded:   6

Detailed Node Expansion Log (f = g + h):
Node             | g(n)     | h(n)     | f(n)    
----------------------------------------------
Arad             | 0        | 366      | 366     
Sibiu            | 140      | 253      | 393     
Rimnicu Vilcea   | 220      | 193      | 413     
Fagaras          | 239      | 176      | 415     
Pitesti          | 317      | 100      | 417     
Bucharest        | 418      | 0        | 418     
```

---

## 💡 Learning Outcomes
1. Implemented priority-queue evaluation balancing exact past cost $g(n)$ and prospective heuristic $h(n)$.
2. Proved that while Greedy Best-First prematurely took the Fagaras route (450 km), A* successfully found the true optimal route via Rimnicu Vilcea & Pitesti (418 km).
3. Demonstrated that A* expands the minimum number of nodes required to guarantee optimality among all admissible search algorithms.

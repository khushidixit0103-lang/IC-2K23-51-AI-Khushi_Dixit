# Experiment 10: Comparative Evaluation of Heuristic & Uninformed Search

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To conduct a rigorous empirical and theoretical comparison of uninformed search (**BFS**, **DFS**) and informed heuristic search (**Greedy Best-First Search**, **A\***) on a standardized road network benchmark, evaluating:
1. Solution Quality (total path cost in km)
2. Search Efficiency (nodes expanded)
3. Space Consumption (maximum frontier size)
4. Empirical Execution Time ($\mu s$)

---

## 🧠 Experimental Setup
- **Benchmark Problem:** Route finding on the Romania road network from **Arad** to **Bucharest**.
- **Edge Weights:** Actual highway driving distance in kilometers.
- **Heuristic:** Straight-line Euclidean distance to Bucharest ($h_{\text{SLD}}$).

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Heuristic_Comparison

# Run script
python comparison.py
```

---

## 📊 Genuine Empirical Results

| Algorithm | Solution Cost (km) | Nodes Expanded | Max Frontier | Execution Time ($\mu s$) | Optimality Guarantee |
|---|:---:|:---:|:---:|:---:|:---:|
| **BFS** | 450 km | 9 | 5 | 22.3 $\mu s$ | Shortest in edge hops, not cost |
| **DFS** | 450 km | 4 | 5 | 16.0 $\mu s$ | Non-optimal |
| **Greedy Best-First** | 450 km | 4 | 5 | 11.8 $\mu s$ | Non-optimal (myopic $h(n)$) |
| **A\* Search** | **418 km** | 6 | 6 | 18.3 $\mu s$ | **Guaranteed Cost-Optimal** |

### Solution Paths Discovered
- **BFS:** `Arad -> Sibiu -> Fagaras -> Bucharest` ($450$ km)
- **DFS:** `Arad -> Sibiu -> Fagaras -> Bucharest` ($450$ km)
- **Greedy Best-First:** `Arad -> Sibiu -> Fagaras -> Bucharest` ($450$ km)
- **A\* Search:** `Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest` (**$418$ km**)

---

## 💡 Key Analytical Findings
1. **The Cost of Greediness:** Greedy Best-First Search selected Fagaras because its straight-line distance appeared small ($176$ km vs $193$ km for Rimnicu Vilcea), oblivious to the expensive $211$ km highway connecting Fagaras to Bucharest.
2. **A\* Optimality:** By evaluating $f(n) = g(n) + h(n)$, A* properly balanced historical path expenditure against future estimates, discovering the global minimum cost path ($418$ km).
3. **Search Space Pruning:** Informed heuristic searches pruned unpromising subtrees, exploring only 4–6 nodes compared to unguided BFS which explored 9 nodes.

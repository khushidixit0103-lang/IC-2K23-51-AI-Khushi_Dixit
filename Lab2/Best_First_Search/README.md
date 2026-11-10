# Experiment 5: Greedy Best-First Search (GBFS)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To design, implement, and analyze the **Greedy Best-First Search (GBFS)** informed search algorithm on the Romania road network benchmark, evaluating how an estimated distance heuristic guides search trajectory.

---

## 🧠 Algorithm & Evaluation Function

Greedy Best-First Search attempts to minimize estimated cost to the goal by selecting the frontier node that appears closest according to a heuristic function:

$$f(n) = h(n)$$

where $h(n)$ is the straight-line Euclidean distance from node $n$ to the goal (Bucharest).

- **Data Structure:** Min-Priority Queue (Heap) ordered strictly by $h(n)$
- **Completeness:** Incomplete on infinite spaces, but complete on finite graphs with a closed list (`visited`)
- **Optimality:** Non-optimal (can be tricked into selecting a path that seems close in straight-line distance but accumulates higher ground travel cost)
- **Time Complexity:** $O(b^m)$ in worst-case; with a good heuristic, it can reduce toward $O(b \times d)$
- **Space Complexity:** $O(b^m)$ (keeps all frontier nodes in memory)

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Best_First_Search

# Run script
python best_first_search.py
```

---

## 📊 Sample Input & Genuine Output

### Romania Benchmark (Arad to Bucharest)
```text
Searching path from 'Arad' to 'Bucharest' using Greedy Best-First Search...

--- Search Results ---
Discovered Path:        Arad -> Sibiu -> Fagaras -> Bucharest
Total Path Cost (km):   450
Total Nodes Expanded:   4

Node Expansion Order:
Arad -> Sibiu -> Fagaras -> Bucharest
```

---

## 💡 Learning Outcomes
1. Implemented an informed search strategy using priority queue heuristics.
2. Observed the myopic nature of pure greedy evaluation: it ignores accumulated path cost $g(n)$, which can yield suboptimal total path distance.
3. Prepared the theoretical framework for combining $g(n)$ and $h(n)$ in the $A^*$ search algorithm.

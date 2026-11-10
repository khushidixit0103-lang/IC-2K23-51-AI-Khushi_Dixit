# Experiment 3: Depth-First Search (DFS)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To implement and analyze **Depth-First Search (DFS)** for graph traversal using a LIFO stack, examining its deep-exploration trajectory, space complexity benefits, and non-optimality characteristics.

---

## 🧠 Algorithm & Theoretical Complexity

Depth-First Search always expands the deepest node in the current frontier of the search tree.

- **Data Structure:** Last-In-First-Out (LIFO) Stack
- **Completeness:** Complete on finite state graphs when augmented with cycle detection (`visited` set)
- **Optimality:** Non-optimal (can return arbitrarily sub-optimal or meandering paths depending on branch ordering)
- **Time Complexity:** $O(b^m)$, where $m$ is the maximum depth of the state space
- **Space Complexity:** $O(b \times m)$ (linear memory: stores only a single path from root to leaf along with remaining unexpanded siblings)

---

## 🚀 Execution Command
```bash
# Navigate to DFS directory
cd Lab2/DFS

# Run script
python dfs.py
```

---

## 📊 Sample Input & Genuine Output

### Romania Map Traversal (Arad -> Bucharest)
```text
Searching path from 'Arad' to 'Bucharest' using DFS...

--- Search Results ---
Discovered Path:     Arad -> Sibiu -> Fagaras -> Bucharest
Path Length (hops):  3
Total Nodes Expanded: 4
Max Frontier Size:   5

Node Expansion Order:
Arad -> Sibiu -> Fagaras -> Bucharest
```

---

## 💡 Learning Outcomes
1. Implemented stack-based graph traversal with cycle avoidance.
2. Contrasted DFS's low linear memory footprint $O(b \times m)$ against BFS's exponential memory requirements $O(b^d)$.
3. Understood why DFS does not guarantee shortest-hop paths on general graphs.

# Experiment 2: Breadth-First Search (BFS)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To implement and analyze **Breadth-First Search (BFS)** for unweighted graph traversal, examining its queue-based FIFO frontier management, completeness, and step-optimality on the Romania road network benchmark.

---

## 🧠 Algorithm & Theoretical Complexity

Breadth-First Search explores a graph level by level. It always expands the shallowest unexpanded frontier node first.

- **Data Structure:** First-In-First-Out (FIFO) Queue
- **Completeness:** Complete (guaranteed to find a solution if branching factor $b$ is finite)
- **Optimality:** Optimal when step costs are identical / unweighted
- **Time Complexity:** $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the shallowest goal
- **Space Complexity:** $O(b^d)$ (memory-intensive: holds all generated nodes in frontier)

---

## 🚀 Execution Command
```bash
# Navigate to BFS directory
cd Lab2/BFS

# Run script
python bfs.py
```

---

## 📊 Sample Input & Genuine Output

### Romania Map Traversal (Arad -> Bucharest)
```text
Searching path from 'Arad' to 'Bucharest' on Romania Map...

--- Search Results ---
Optimal Path:        Arad -> Sibiu -> Fagaras -> Bucharest
Path Length (hops):  3
Total Nodes Expanded: 9
Max Frontier Size:   5

Node Expansion Order:
Arad -> Sibiu -> Timisoara -> Zerind -> Fagaras -> Oradea -> Rimnicu Vilcea -> Lugoj -> Bucharest
```

---

## 💡 Learning Outcomes
1. Implemented level-order graph exploration using a FIFO queue.
2. Verified that BFS guarantees the minimum-hop path (3 hops from Arad to Bucharest).
3. Observed that the maximum frontier size expands exponentially with search depth.

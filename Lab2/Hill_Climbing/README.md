# Experiment 4: Hill Climbing Search (Steepest-Ascent & Random-Restart)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To implement the **Hill Climbing** local heuristic search algorithm on the 8-Queens problem, observe its failure modes (local minima, ridges, plateaus), and demonstrate how **Random-Restart Hill Climbing** restores global completeness.

---

## 🧠 Algorithm & Local Search Mechanics

Hill climbing is an iterative optimization algorithm that starts with an arbitrary solution and attempts to find a better solution by incrementally mutating a single element.

### Variants
1. **Steepest-Ascent Hill Climbing:** Evaluates all possible successor neighbors ($8 \times 7 = 56$ moves) and moves deterministically to the neighbor with the best heuristic improvement.
   - *Failure Mode:* Terminates at local minima or plateaus where no neighbor is strictly better than the current state.
2. **Random-Restart Hill Climbing:** Conducts repeated steepest-ascent searches from independently drawn random initial states until the global optimum ($h = 0$) is found.

### Heuristic Function
$$h(s) = \text{number of mutually attacking queen pairs on rows and diagonals}$$
A state with $h(s) = 0$ is a global optimum.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Hill_Climbing

# Run script
python hill_climbing.py
```

---

## 📊 Genuine Experimental Results

### Single-Run Steepest-Ascent vs Random-Restart
```text
--- Testing Single-Run Steepest-Ascent Hill Climbing ---
Run 01: Trapped in local minimum (h = 1) after 4 steps.
Run 02: Success! Found global optimum h=0 in 5 steps.
Run 03: Trapped in local minimum (h = 2) after 2 steps.
Run 04: Trapped in local minimum (h = 1) after 2 steps.
Run 05: Success! Found global optimum h=0 in 4 steps.
Run 06: Trapped in local minimum (h = 1) after 3 steps.
Run 07: Trapped in local minimum (h = 2) after 1 steps.
Run 08: Trapped in local minimum (h = 1) after 3 steps.
Run 09: Trapped in local minimum (h = 1) after 4 steps.
Run 10: Trapped in local minimum (h = 2) after 2 steps.

Steepest-Ascent Success Rate: 20.0% (2/10)
Observation: Pure hill climbing gets trapped in local minima/shoulders.

--- Testing Random-Restart Hill Climbing ---
Global Optimum Found: [3, 5, 7, 1, 6, 0, 2, 4]
  Heuristic Conflicts h(s): 0
  Restarts Required:        16
  Total Steps Taken:        52
```

---

## 💡 Learning Outcomes
1. Modeled local search optimization without maintaining a global search tree.
2. Quantified how pure greedy local choices lead to premature entrapment in local optima (20% success rate).
3. Demonstrated that Random-Restart guarantees completeness by exploring diverse basins of attraction.

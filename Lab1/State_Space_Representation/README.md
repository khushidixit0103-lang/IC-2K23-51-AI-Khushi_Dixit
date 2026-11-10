# Experiment 5: Formal State-Space Representation & Branching Analysis

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To formally define the mathematical 5-tuple formulation of an Artificial Intelligence problem in state space, analyze graph-theoretic properties (reachable states, branching factor, state graph connectivity), and implement a generic search agent in Python.

---

## 🧠 Problem Formulation (The 5-Tuple Paradigm)

An AI problem is formally specified by the 5-tuple $\langle S_0, A, T, G, c \rangle$:
1. **Initial State ($S_0$):** The configuration where the agent begins ($\text{Start} = (0, 0)$).
2. **Action Space ($A(s)$):** The set of legal actions applicable from state $s$ ($\{\text{Up}, \text{Down}, \text{Left}, \text{Right}\}$).
3. **Transition Model ($T(s, a) = s'$):** The deterministic outcome state resulting from taking action $a$ in state $s$.
4. **Goal Test ($G(s)$):** A boolean predicate returning `True` if $s$ satisfies the termination condition ($\text{Goal} = (3, 3)$).
5. **Path Cost ($c(s, a, s')$):** The cost function assigned to transitioning from $s$ to $s'$ via $a$ (uniform cost $1.0$).

---

## ⚙️ Branching Factor Metrics
- **Reachable States ($|V|$):** The total number of valid nodes reachable from $S_0$.
- **State Transitions ($|E|$):** The total directed edges in the state graph.
- **Branching Factor ($b$):** The number of valid outgoing edges from a state.
  - $b_{\text{max}} = \max_{s \in V} |A(s)|$
  - $b_{\text{avg}} = \frac{1}{|V|} \sum_{s \in V} |A(s)|$

---

## 🚀 Execution Command
```bash
# Navigate to experiment folder
cd Lab1/State_Space_Representation

# Execute script
python state_space.py
```

---

## 📊 Sample Input & Genuine Output

### State-Space Graph Metrics & Solution
```text
Grid World State Space Visualization:
[S]  .   .   . 
 .  [#] [#]  . 
 .   .  [#]  . 
 .   .   .  [G]
Legend: [S]=Start, [G]=Goal, [#]=Obstacle, [*]=Solution Path, [.]=Open Cell

--- State-Space Graph Metrics ---
  Reachable States (Vertices):        13
  Total Directed Transitions (Edges): 28
  Maximum Branching Factor (b_max):   3
  Minimum Branching Factor (b_min):   2
  Average Branching Factor (b_avg):   2.15

Optimal Path to Goal Found in 6 steps:
  Step 0: Action = START  -> State = (0, 0)
  Step 1: Action = Down   -> State = (1, 0)
  Step 2: Action = Down   -> State = (2, 0)
  Step 3: Action = Down   -> State = (3, 0)
  Step 4: Action = Right  -> State = (3, 1)
  Step 5: Action = Right  -> State = (3, 2)
  Step 6: Action = Right  -> State = (3, 3)

Grid World State Space Visualization:
[S]  .   .   . 
 *  [#] [#]  . 
 *   .  [#]  . 
 *   *   *  [G]
```

---

## 💡 Learning Outcomes
1. Formulated AI problems using the formal 5-tuple mathematical definition.
2. Understood how topological constraints and obstacles restrict graph connectivity.
3. Computed critical complexity metrics such as effective branching factor and search depth.

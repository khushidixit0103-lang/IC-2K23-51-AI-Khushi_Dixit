# Experiment 3: Missionaries and Cannibals Problem

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To formulate the classical Missionaries and Cannibals river crossing dilemma as a formal AI state-space search problem with safety constraints, and implement a Breadth-First Search (BFS) solution in Python to find the optimal sequence of crossings.

---

## 🧠 Problem Statement
Three missionaries and three cannibals are on the left bank of a river. They must all cross to the right bank using a boat that can carry at most two people. The boat cannot cross by itself (requires at least one rower). 

**Critical Constraint:** At no point on either the left bank, the right bank, or in the boat may cannibals outnumber missionaries, or the cannibals will overpower and eat the missionaries.

---

## ⚙️ State-Space Representation

- **State Representation:** A 3-tuple $(M_L, C_L, B)$ where:
  - $M_L \in \{0, 1, 2, 3\}$: Missionaries on the left bank
  - $C_L \in \{0, 1, 2, 3\}$: Cannibals on the left bank
  - $B \in \{0, 1\}$: Boat location ($1$ = Left bank, $0$ = Right bank)
  - Right bank inhabitants: $M_R = 3 - M_L$ and $C_R = 3 - C_L$.
- **Initial State:** $(3, 3, 1)$
- **Goal State:** $(0, 0, 0)$
- **Validity Invariants:**
  - $0 \le M_L \le 3$ and $0 \le C_L \le 3$
  - If $M_L > 0$, then $M_L \ge C_L$
  - If $M_R > 0$, then $M_R \ge C_R$
- **Operators:** Allowed boat transfers $(m, c) \in \{(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)\}$.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab1/Missionaries_Cannibals

# Run script
python missionaries_cannibals.py
```

---

## 📊 Sample Input & Genuine Output

### Execution Trace (Optimal 11 Crossings)
```text
======================================================================
   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 3
   Missionaries and Cannibals Problem (State-Space Search)
   Student: Khushi Dixit | Roll No: IC-2K23-51
======================================================================

Solution Found in 11 crossings:
----------------------------------------------------------------------
Step 00: Initial state (everyone on Left bank)
         Left: MMMCCC [BOAT] ~~~ River ~~~        Right:       
----------------------------------------------------------------------
Step 01: Cross -> 0 Missionary(ies), 2 Cannibal(s) to Right bank
         Left: MMMC          ~~~ River ~~~ [BOAT] Right: CC    
----------------------------------------------------------------------
Step 02: Return <- 0 Missionary(ies), 1 Cannibal(s) to Left bank
         Left: MMMCC  [BOAT] ~~~ River ~~~        Right: C     
----------------------------------------------------------------------
Step 03: Cross -> 0 Missionary(ies), 2 Cannibal(s) to Right bank
         Left: MMM           ~~~ River ~~~ [BOAT] Right: CCC   
----------------------------------------------------------------------
Step 04: Return <- 0 Missionary(ies), 1 Cannibal(s) to Left bank
         Left: MMMC   [BOAT] ~~~ River ~~~        Right: CC    
----------------------------------------------------------------------
Step 05: Cross -> 2 Missionary(ies), 0 Cannibal(s) to Right bank
         Left: MC            ~~~ River ~~~ [BOAT] Right: MMCC  
----------------------------------------------------------------------
Step 06: Return <- 1 Missionary(ies), 1 Cannibal(s) to Left bank
         Left: MMCC   [BOAT] ~~~ River ~~~        Right: MC    
----------------------------------------------------------------------
Step 07: Cross -> 2 Missionary(ies), 0 Cannibal(s) to Right bank
         Left: CC            ~~~ River ~~~ [BOAT] Right: MMMC  
----------------------------------------------------------------------
Step 08: Return <- 0 Missionary(ies), 1 Cannibal(s) to Left bank
         Left: CCC    [BOAT] ~~~ River ~~~        Right: MMM   
----------------------------------------------------------------------
Step 09: Cross -> 0 Missionary(ies), 2 Cannibal(s) to Right bank
         Left: C             ~~~ River ~~~ [BOAT] Right: MMMCC 
----------------------------------------------------------------------
Step 10: Return <- 1 Missionary(ies), 0 Cannibal(s) to Left bank
         Left: MC     [BOAT] ~~~ River ~~~        Right: MMCC  
----------------------------------------------------------------------
Step 11: Cross -> 1 Missionary(ies), 1 Cannibal(s) to Right bank
         Left:               ~~~ River ~~~ [BOAT] Right: MMMCCC
----------------------------------------------------------------------
```

---

## 💡 Learning Outcomes
1. Formulated constrained search problems where intermediate invalid states must be pruned dynamically.
2. Understood state-space graph traversal and cycle elimination using closed sets (`visited`).
3. Proved that BFS guarantees finding the minimum possible number of crossings (11 steps).

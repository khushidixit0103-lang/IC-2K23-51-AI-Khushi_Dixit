# Experiment 1: Generate and Test Search Paradigm

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To design, implement, and analyze the **Generate and Test** search algorithm in Python on the classic $N$-Queens problem, observing its state space generation characteristics, test predicate evaluation, and combinatorial scaling.

---

## 🧠 Problem Statement
Generate and Test is the foundational brute-force / heuristic search paradigm in Artificial Intelligence. The system consists of:
1. **Generator:** A systematic procedure that enumerates potential solutions (states) in the hypothesis space.
2. **Tester:** A verification module that tests whether a generated candidate satisfies all constraints / reaches the goal condition $h(s) = 0$.

In the $N$-Queens formulation, $N$ non-attacking queens must be positioned on an $N \times N$ chessboard such that no two queens share the same row, column, or diagonal.

---

## ⚙️ Algorithm Steps & Pseudocode

```text
Algorithm GenerateAndTest(Problem):
    Loop:
        state <- GenerateNextCandidate(Problem.StateSpace)
        If state is NULL (exhausted):
            Return FAILURE
        If Test(state) == TRUE (Goal reached, conflicts == 0):
            Return state
```

### Heuristic Evaluation Metric
$h(s) = \text{number of mutually attacking queen pairs}$.  
A goal state is reached when $h(s) = 0$.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Generate_And_Test

# Execute script
python generate_and_test.py
```

---

## 📊 Genuine Experimental Results

| Problem Instance | Solution Configuration | Heuristic Conflicts $h(s)$ | Nodes Generated | Boards Tested | Execution Time (ms) |
|---|---|:---:|:---:|:---:|:---:|
| **4-Queens** | `[1, 3, 0, 2]` | 0 | 269 | 115 | 0.22 ms |
| **5-Queens** | `[0, 2, 4, 1, 3]` | 0 | 809 | 359 | 0.87 ms |
| **8-Queens** | `[0, 4, 7, 5, 2, 6, 1, 3]` | 0 | 2,785,400 | 1,299,852 | 7,877.77 ms |

---

## 💡 Learning Outcomes
1. Understood the decoupling between the candidate generator and the constraint evaluator in AI search.
2. Observed the exponential combinatorial explosion ($O(N^N)$) inherent to unguided Generate and Test.
3. Established the foundational baseline motivating informed heuristic search techniques (Hill Climbing, Best-First Search, A*).

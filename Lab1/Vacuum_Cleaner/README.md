# Experiment 4: Vacuum Cleaner Problem (Intelligent Agents)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To formulate the classical Russell & Norvig Vacuum Cleaner World, model its PEAS (Performance measure, Environment, Actuators, Sensors) framework, and implement both a **Simple Reflex Agent** and a **Model-Based Reflex Agent** to analyze intelligent decision-making.

---

## 🧠 Problem Statement
The vacuum environment consists of two locations: Room $A$ and Room $B$. Each room can either be **Clean** or **Dirty**. An intelligent vacuum cleaner operates within this world to ensure all locations are cleaned while optimizing its performance measure.

### PEAS Framework
- **Performance Measure:** $+10$ points for cleaning a dirty room, $+5$ per step for each clean room in the environment, $-1$ point per movement action (`Left`/`Right`), $-2$ points per `Suck` action.
- **Environment:** Discrete, fully observable, static, deterministic 2-room grid ($A$ and $B$).
- **Actuators:** `Left`, `Right`, `Suck`, `NoOp`.
- **Sensors:** Location sensor ($A$ or $B$), dirt sensor (`Clean` or `Dirty`).

---

## ⚙️ Agents Implemented

1. **Simple Reflex Agent:**
   - Stateless condition-action rules:
     - `IF Status == Dirty THEN Suck`
     - `IF Location == A THEN Right`
     - `IF Location == B THEN Left`
   - *Limitation:* Lacks memory; endlessly traverses back and forth even when both rooms are already clean.

2. **Model-Based Reflex Agent:**
   - Maintains internal world state memory (`model: {A: status, B: status}`).
   - Updates internal memory with each observation.
   - Halts with `NoOp` once all rooms are verified clean, conserving energy and stopping unnecessary thrashing.

---

## 🚀 Execution Command
```bash
# Navigate to experiment folder
cd Lab1/Vacuum_Cleaner

# Execute script
python vacuum_cleaner.py
```

---

## 📊 Sample Input & Genuine Output

### Comparative Trace for Scenario 1 (Both Rooms Dirty)
```text
================ Scenario 1 ================

--- Running Simple Reflex Agent Simulation ---
Initial State: Location=A, Rooms={'A': 'Dirty', 'B': 'Dirty'}
Step  | Location   | Percept    | Action     | Performance
-------------------------------------------------------
1     | A          | Dirty      | Suck       | 13        
2     | B          | Clean      | Right      | 17        
3     | B          | Dirty      | Suck       | 35        
4     | A          | Clean      | Left       | 44        
5     | B          | Clean      | Right      | 53        
Final Room States: {'A': 'Clean', 'B': 'Clean'}
Total Cumulative Score: 53

--- Running Model-Based Reflex Agent Simulation ---
Initial State: Location=A, Rooms={'A': 'Dirty', 'B': 'Dirty'}
Step  | Location   | Percept    | Action     | Performance
-------------------------------------------------------
1     | A          | Dirty      | Suck       | 13        
2     | B          | Clean      | Right      | 17        
3     | B          | Dirty      | Suck       | 35        
4     | B          | Clean      | NoOp       | 45        
Goal Reached: All rooms cleaned in 4 steps!
Final Room States: {'A': 'Clean', 'B': 'Clean'}
Total Cumulative Score: 45
```

---

## 💡 Learning Outcomes
1. Modeled an intelligent agent using the formal PEAS paradigm.
2. Implemented condition-action rules for reflex behavior.
3. Demonstrated that a model-based agent with internal state prevents oscillatory infinite loops and achieves goal termination gracefully.

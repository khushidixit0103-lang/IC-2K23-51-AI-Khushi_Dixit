# Experiment 1: Production Rule System (Forward-Chaining Inference Engine)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To understand, design, and implement a rule-based production system in Python featuring:
1. Working Memory (Fact Base / Current World State)
2. Knowledge Base (Set of Condition-Action IF-THEN Rules with priorities)
3. Inference Engine (Forward Chaining executing Match-Resolve-Act cycles)

---

## 🧠 Problem Statement
In Artificial Intelligence, a production system is a cognitive architecture and rule-based expert paradigm used to deduce new knowledge or formulate actions from known premises. The system must maintain working memory, evaluate which rules match current conditions, resolve conflicts using explicit rule priorities, fire actions that modify working memory, and terminate when no further rules are applicable.

---

## ⚙️ Algorithm & Architecture

### Components
1. **Working Memory (WM):** A dynamic set of known facts.
2. **Rule Base (KB):** Rules of structure `IF <conditions> THEN <action>` with assigned priority values.
3. **Inference Engine Cycle:**
   - **Match:** Scan the Knowledge Base to determine all rules whose premises are satisfied by facts currently in Working Memory.
   - **Conflict Resolution:** If multiple rules match, select the rule with the highest numerical priority that has not yet fired.
   - **Act:** Execute the chosen rule's action, assert the new deduction into Working Memory, and mark the rule as fired.
   - **Terminate:** Halt when the conflict set is empty or a goal state is reached.

### Pseudocode
```text
Algorithm ForwardChainingInference(Rules, WorkingMemory):
    FiredRules <- EmptySet
    Loop:
        ConflictSet <- []
        For each Rule in Rules:
            If Rule not in FiredRules and Rule.Condition(WorkingMemory) is TRUE:
                Add Rule to ConflictSet
        If ConflictSet is Empty:
            Exit Loop
        Sort ConflictSet by Rule.Priority descending
        SelectedRule <- ConflictSet[0]
        NewFact <- SelectedRule.Fire(WorkingMemory)
        Add SelectedRule to FiredRules
        If NewFact not in WorkingMemory:
            Add NewFact to WorkingMemory
    Return WorkingMemory
```

---

## 📦 Dependencies
- Python 3.10+ (Standard Library: `typing`, `sys`)
- No third-party packages required for this core logic.

---

## 🚀 Execution Command
Run the script from the experiment directory or repository root:

```bash
# Navigate to experiment folder
cd Lab1/Production_Rule_System

# Execute the script
python production_system.py
```

---

## 📊 Sample Input & Genuine Output

### Default Execution Trace
```text
=================================================================
   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 1
   Production Rule System (Inference Engine)
   Student: Khushi Dixit | Roll No: IC-2K23-51
=================================================================

[Default Test Scenario]: Autonomous Vehicle Sensor Data
Initial Working Memory: ['path_clear', 'speed_limit_40', 'traffic_light_green']

Running Forward-Chaining Inference Engine...

--- Inference Execution Trace ---
  Cycle 1: Fired [Traffic_Signal_Green_Clear] (Priority 50) -> Deduced: 'accelerate_and_proceed'
  Cycle 2: Fired [Speed_Limit_Advisory] (Priority 40) -> Deduced: 'maintain_speed_under_40'
  Cycle 3: No more applicable rules. Inference halted.

--- Final Working Memory State ---
  * accelerate_and_proceed
  * maintain_speed_under_40
  * path_clear
  * speed_limit_40
  * traffic_light_green
```

---

## 💡 Learning Outcomes
1. Understood the tripartite architecture of production systems (Rule Base, Working Memory, Inference Engine).
2. Implemented the Match-Resolve-Act forward chaining algorithm with priority-based conflict resolution.
3. Observed how symbolic knowledge representation enables declarative reasoning and modular system expansion.

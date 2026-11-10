# Experiment 3: Semantic Network Knowledge Representation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To construct a Semantic Network using a directed labelled graph representation and implement property inheritance across taxonomic hierarchies (`IS-A`, `HAS-A`, `CAN`, `PART-OF`).

---

## 2. Problem Statement
Model the biological taxonomy of the animal kingdom as a semantic network where:
- Nodes represent conceptual entities (e.g., `Animal`, `Vertebrate`, `Mammal`, `Bird`, `Fish`, `Dog`, `Eagle`, `Salmon`).
- Directed edges represent relational semantics:
  - `IS-A` (Taxonomic subclass / instance-of)
  - `HAS-A` (Attribute possession, e.g., Fur, Gills, Backbone, Feathers)
  - `CAN` (Behavioral capabilities, e.g., Bark, Fly, Breathe, Move)
  - `PART-OF` (Component relationship, e.g., Paw -> Dog, Wing -> Bird)
Demonstrate how child nodes automatically inherit attributes and behaviors from ancestor nodes via graph traversal.

---

## 3. Algorithm & Approach
1. **Graph Structure:** Represent network as an adjacency graph where each node contains incoming and outgoing labeled relations.
2. **Inheritance Mechanism (Breadth-First / Depth-First Traversal):**
   - When querying a property (`HAS-A` or `CAN`) for a node $N$, inspect direct edges.
   - If not found or when aggregating all inherited attributes, traverse `IS-A` links up the conceptual hierarchy:
     $$N \xrightarrow{\text{IS-A}} C_1 \xrightarrow{\text{IS-A}} C_2 \xrightarrow{\text{IS-A}} \dots \xrightarrow{\text{IS-A}} \text{Root}$$
   - Accumulate attributes from all reached ancestors without duplication.
3. **Query Engine:** Provide lookups for immediate relations, full ancestor chains, and aggregated inherited properties.

---

## 4. Dependencies
- Python 3.8+ (Standard Library: `collections`, `typing`)
- No third-party packages required.

---

## 5. Execution Command
```bash
python Lab4/Semantic_Network/semantic_network.py
```

---

## 6. Sample Execution Output
```text
======================================================================
  SEMANTIC NETWORK KNOWLEDGE REPRESENTATION
  Domain : Animal Kingdom
======================================================================

[BUILDING SEMANTIC NETWORK - Animal Domain]
  [Node added] 'Animal'
  [Node added] 'Life'
  [Relation added] 'Animal' -[HAS-A]-> 'Life'
  [Node added] 'Breathe'
  [Relation added] 'Animal' -[CAN]-> 'Breathe'
  [Relation added] 'Vertebrate' -[IS-A]-> 'Animal'
  [Relation added] 'Mammal' -[IS-A]-> 'Vertebrate'
  [Relation added] 'Dog' -[IS-A]-> 'Mammal'
  ...

--- Node: 'Dog' ---
  IS-A ancestors:
    -- Mammal  (depth 1)
      -- Vertebrate  (depth 2)
        -- Animal  (depth 3)
  Inherited HAS-A : ['Tail', 'Fur', 'Backbone', 'Life']
  Inherited CAN   : ['Bark', 'RegulateBodyTemp', 'Breathe', 'Move']
  Inherited PART-OF usage: []

--- Node: 'Eagle' ---
  IS-A ancestors:
    -- Bird  (depth 1)
      -- Vertebrate  (depth 2)
        -- Animal  (depth 3)
  Inherited HAS-A : ['SharpTalons', 'Feathers', 'Backbone', 'Life']
  Inherited CAN   : ['Fly', 'LayEggs', 'Breathe', 'Move']

======================================================================
  Semantic Network demo complete.
======================================================================
```

---

## 7. Results & Observations
- Demonstrates cognitive economy: High-level attributes like `Breathe`, `Move`, and `Life` are stored only once at `Animal`, yet queried seamlessly at leaf nodes (`Dog`, `Eagle`, `Salmon`).
- Graph traversal cleanly resolved multi-level inheritance trees up to depth 3 without cyclic traps.

---

## 8. Learning Outcomes
- Gained practical expertise in building graph-based knowledge representations.
- Understood taxonomic hierarchies, relational labeling, and transitive property inheritance.

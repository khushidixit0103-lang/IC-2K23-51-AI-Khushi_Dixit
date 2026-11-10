# Lab 4 – Knowledge Representation & Logical Reasoning

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Course Outcomes:** CO1, CO3  

---

## Overview

Lab 4 explores the core paradigms used in Artificial Intelligence to formally encode knowledge and perform automated reasoning. The experiments cover production rules, first-order predicate logic, semantic networks, frame systems, logical forward-chaining expert engines, and Roger Schank's Conceptual Dependency (CD) theory.

---

## Laboratory Experiments

| # | Folder | Primary Script | Core Technique / Domain | Course Outcomes |
|---|--------|----------------|--------------------------|-----------------|
| 1 | `Rule_Based_KR/` | `rule_based.py` | Production Rule System, Working Memory assertion, Conflict Resolution | CO1, CO3 |
| 2 | `Predicate_Logic/` | `predicate_logic.py` | First-Order Predicate Logic, Universal & Existential Quantifiers | CO1, CO3 |
| 3 | `Semantic_Network/` | `semantic_network.py` | Directed Relational Graphs, `IS-A` / `HAS-A` / `CAN` Inheritance | CO1, CO3 |
| 4 | `Frame_Representation/` | `frame_representation.py` | Frames, Slots, Facets, Default Inheritance & Procedural Demons | CO1, CO3 |
| 5 | `Logical_Inference_Engine/` | `inference_engine.py` | Forward-Chaining Medical Diagnostic Engine & Clinical Triage | CO1, CO3 |
| 6 | `Conceptual_Dependency/` | `conceptual_dependency.py` | Roger Schank's Primitive ACTs, Conceptual Cases, Semantic Inferences | CO1, CO3 |

---

## How to Execute the Experiments

All experiments are self-contained and run directly from the repository root:

```bash
# 1. Rule-Based Knowledge Representation
python Lab4/Rule_Based_KR/rule_based.py

# 2. Predicate Logic & Quantification
python Lab4/Predicate_Logic/predicate_logic.py

# 3. Semantic Network Construction & Inheritance
python Lab4/Semantic_Network/semantic_network.py

# 4. Frame Representation & Procedural Attachments
python Lab4/Frame_Representation/frame_representation.py

# 5. Modular Logical Inference Engine
python Lab4/Logical_Inference_Engine/inference_engine.py

# 6. Conceptual Dependency (CD) Theory
python Lab4/Conceptual_Dependency/conceptual_dependency.py
```

---

## Verification & Key Results Summary

* **Rule-Based System:** Accurately classified entities into biological classes and deduced warm-blooded vertebrate statuses via multi-step rule firing.
* **Predicate Logic:** Successfully derived 21 family relationship assertions and verified universal truth and existential witnesses over domain individuals.
* **Semantic Network:** Propagated inherited attributes (`Backbone`, `Life`, `Breathe`) up to depth 3 across taxonomic tree structures.
* **Frames:** Demonstrated prototype inheritance with slot default values and dynamic recalculation via `if-needed` and `if-added` demons.
* **Logical Inference Engine:** Evaluated multi-symptom medical rules to infer 4 patient diagnoses and 4 targeted clinical treatments across 2 execution passes.
* **Conceptual Dependency:** Decomposed natural language statements into canonical primitives (`ATRANS`, `PTRANS`, `MTRANS`, `INGEST`, `MBUILD`) and verified automated spatial/ownership inferences.

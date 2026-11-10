# Experiment 6: Conceptual Dependency (CD) Knowledge Representation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To represent natural language semantics using Roger Schank's Conceptual Dependency (CD) framework and demonstrate unambiguous semantic decomposition using primitive ACTs.

---

## 2. Problem Statement
Natural language statements exhibit syntactic surface variability that masks underlying semantic equivalence. Roger Schank's Conceptual Dependency model overcomes this by mapping sentences into language-independent conceptual primitives:
- Primitive ACTs: `ATRANS`, `PTRANS`, `PROPEL`, `MOVE`, `GRASP`, `INGEST`, `EXPEL`, `MTRANS`, `MBUILD`, `SPEAK`, `ATTEND`.
- Conceptual cases: Actor ($PP$), Object ($PP$), Recipient Case ($R: \text{From} \to \text{To}$), Direction Case ($D: \text{From} \to \text{To}$), and Instrumental ACT ($I$).

Model representative semantic sentences (giving, driving, teaching, eating, deciding) into structured CD frames and demonstrate reasoning on resulting primitive representations.

---

## 3. Algorithm & Approach
1. **Conceptual Structure Class:** Model a CD frame with fields for:
   - Surface sentence & tense (`PAST`, `PRESENT`, `FUTURE`)
   - Actor (Physical Producer - $PP$)
   - Primitive ACT (Action)
   - Object (Theme / Item acted upon)
   - Recipient Case ($R$) and Direction Case ($D$)
   - Instrumental ACT ($I$) representing sub-actions necessary to execute the main action.
2. **Decomposition Mapping:**
   - *"John gave Mary a book"* $\implies$ `ATRANS` of `Book` from `John` to `Mary`.
   - *"Dishan drove from Campus to Library"* $\implies$ `PTRANS` of `Dishan` with instrument `MOVE(Car Controls)`.
   - *"The professor told the students the exam date"* $\implies$ `MTRANS` of mental concept from teacher to students.
   - *"Alice ate an apple"* $\implies$ `INGEST` of `Apple` into stomach with instrument `GRASP(Spoon)`.
   - *"Bob decided to study AI"* $\implies$ `MBUILD` creating new thought in memory.
3. **Automated Inference:**
   - Infer current possession from `ATRANS`.
   - Infer current physical location from `PTRANS`.

---

## 4. Dependencies
- Python 3.8+ (Standard Library)
- No third-party packages required.

---

## 5. Execution Command
```bash
python Lab4/Conceptual_Dependency/conceptual_dependency.py
```

---

## 6. Sample Execution Output
```text
======================================================================
  CONCEPTUAL DEPENDENCY (CD) KNOWLEDGE REPRESENTATION
  Framework : Roger Schank Primitive ACT Representation
  Student   : Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D
======================================================================

[DEMONSTRATING 5 CONCEPTUAL DEPENDENCY STRUCTURES]

--- Case 1 ---
  Surface Sentence : "John gave Mary a book."
  Tense            : PAST
  Actor (PP)       : John
  <===> ACT       : ATRANS
    <-o (Object)   : Book
    <-R (Recipient): [FROM: John] -> [TO: Mary]
--------------------------------------------------
--- Case 2 ---
  Surface Sentence : "Dishan drove from Campus to Library."
  Tense            : PAST
  Actor (PP)       : Dishan
  <===> ACT       : PTRANS
    <-o (Object)   : Dishan
    <-D (Direction): [FROM: Campus] -> [TO: Library]
    <-I (Instrument):
      Surface Sentence : "Dishan operated the car controls."
      Tense            : PAST
      Actor (PP)       : Dishan
      <===> ACT       : MOVE
        <-o (Object)   : Hands/Feet
        <-D (Direction): [FROM: Neutral] -> [TO: Car Controls]
...

[INFERENCE FROM CD PRIMITIVES]
  Rule: If ACT == ATRANS and recipient_to != None:
    Deduce: New owner of object is recipient_to.
  > Statement: "John gave Mary a book."
    Inference: Mary now possesses Book.
  Rule: If ACT == PTRANS and direction_to != None:
    Deduce: Current location of actor/object is direction_to.
  > Statement: "Dishan drove from Campus to Library."
    Inference: Dishan is now at Library.

======================================================================
  Conceptual Dependency Representation complete.
======================================================================
```

---

## 7. Results & Observations
- Surface linguistic differences are mapped onto unified primitive structures, facilitating canonical semantic querying.
- Domain-independent inference rules easily deduce implicit consequences (e.g. transfer of ownership or change of spatial coordinate) directly from primitive ACT types.

---

## 8. Learning Outcomes
- Gained comprehensive understanding of Roger Schank's Conceptual Dependency theory.
- Learned how to decompose complex sentences into primitive ACTs, conceptual cases, and instrumental sub-actions.

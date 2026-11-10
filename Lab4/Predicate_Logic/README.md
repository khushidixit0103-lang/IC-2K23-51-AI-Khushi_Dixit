# Experiment 2: Predicate Logic Knowledge Representation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To represent relational knowledge using First-Order Predicate Logic (FOPL) and perform deductive reasoning through forward-chaining inference with universal and existential quantifiers.

---

## 2. Problem Statement
Model a family relationship domain using first-order predicates:
- Base facts: `parent(X, Y)`, `male(X)`, `female(X)`
- Inference rules:
  - $\forall X, Y: \text{parent}(X, Y) \land \text{male}(X) \implies \text{father}(X, Y)$
  - $\forall X, Y, Z: \text{parent}(X, Y) \land \text{parent}(Y, Z) \implies \text{grandparent}(X, Z)$
  - $\forall X, Y, Z: \text{parent}(Z, X) \land \text{parent}(Z, Y) \land (X \neq Y) \implies \text{sibling}(X, Y)$
  - Transitive ancestor closure: $\forall X, Y: \text{parent}(X, Y) \implies \text{ancestor}(X, Y)$, and $\forall X, Y, Z: \text{parent}(X, Y) \land \text{ancestor}(Y, Z) \implies \text{ancestor}(X, Z)$.

Demonstrate verification of universal statements ($\forall$) and existential queries ($\exists$).

---

## 3. Algorithm & Approach
1. **Fact Base:** Store ground atomic formulas as tuples `(predicate_name, arg1, arg2, ...)`.
2. **Rule Evaluation:** Iterate over rule definitions. Each rule specifies pattern bindings over candidate arguments from the fact base.
3. **Unification & Substitution:** Match variable arguments across conjoined premises to verify consistency.
4. **Iterative Deduction:** Add newly inferred facts to the knowledge base until fixed-point closure is reached.
5. **Quantifier Evaluation:**
   - Universal ($\forall X$): Verify proposition holds across every domain entity satisfying the antecedent.
   - Existential ($\exists X$): Search for at least one entity (witness) satisfying the predicate.

---

## 4. Dependencies
- Python 3.8+ (Standard Library)
- No third-party packages required.

---

## 5. Execution Command
```bash
python Lab4/Predicate_Logic/predicate_logic.py
```

---

## 6. Sample Execution Output
```text
======================================================================
  PREDICATE LOGIC REPRESENTATION SYSTEM
  Domain : Family Relationships
======================================================================

[INITIAL FACTS]
  parent(tom, bob)
  parent(tom, liz)
  parent(bob, ann)
  parent(bob, pat)
  parent(pat, jim)
  male(tom)
  male(bob)
  male(pat)
  male(jim)
  female(liz)
  female(ann)

[FORWARD CHAINING] Deriving new facts...
  Derived: father(tom, bob)
  Derived: father(tom, liz)
  Derived: father(bob, ann)
  Derived: father(bob, pat)
  Derived: father(pat, jim)
  Derived: grandparent(tom, ann)
  Derived: grandparent(tom, pat)
  Derived: grandparent(bob, jim)
  Derived: sibling(ann, pat)
  Derived: sibling(bob, liz)
  Derived: ancestor(tom, ann)
  Derived: ancestor(tom, jim)
  ...

[UNIVERSAL] For all X: parent(X, ann) -> ancestor(X, ann)
  parent(bob, ann) is True  ->  ancestor(bob, ann) = True
  Universal statement holds: True

[EXISTENTIAL] EXISTS X: father(X, bob)?
  Yes - father(tom, bob) is True

======================================================================
  Predicate Logic demo complete.
======================================================================
```

---

## 7. Results & Observations
- First-order logic rules accurately inferred complex, multi-generational relationships from minimal atomic facts.
- Transitive closure successfully resolved multi-hop ancestry queries (e.g., `ancestor(tom, jim)` across 3 generations).
- Universal and existential quantification checks completed with zero ambiguity.

---

## 8. Learning Outcomes
- Mastered first-order relational knowledge representation.
- Understood variable binding, logical conjunction, and forward-chaining deduction in relational domain knowledge bases.

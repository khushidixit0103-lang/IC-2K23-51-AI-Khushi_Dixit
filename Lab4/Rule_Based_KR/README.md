# Experiment 1: Rule-Based Knowledge Representation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To represent domain knowledge using an IF-THEN production rule system and derive inferred facts using forward-chaining inference over working memory.

---

## 2. Problem Statement
Given an animal classification domain with observed biological attributes (feathers, flight capability, egg laying, fur, gills, body temperature regulation), model knowledge as a formal rule base. The system must iteratively evaluate antecedents against known facts, resolve conflicts, assert consequent facts into working memory, and deduce higher-order biological categories (e.g., Bird, Fish, Mammal, Warm-Blooded Vertebrate).

---

## 3. Algorithm & Approach
1. **Fact Representation:** Represent entity attributes as key-value pairs or predicate tuples in Working Memory (WM).
2. **Rule Base:** Encode conditional rules with pattern-matching antecedents (IF condition) and consequent assertions (THEN action).
3. **Forward-Chaining Match-Resolve-Act Loop:**
   - **Match:** Scan rules whose antecedents are satisfied by current WM facts.
   - **Resolve:** Select rules that have not yet fired for the entity.
   - **Act:** Add new inferred conclusions into WM.
4. **Termination:** Stop when no additional rules can fire (quiescence).

### Pseudocode
```text
Algorithm ForwardChainingRuleEngine(Facts, Rules):
    InferredFacts = {}
    repeat:
        new_derived = False
        for rule in Rules:
            if rule.conditions_match(Facts) and rule.id not in FiredRules:
                Facts.add(rule.consequent)
                InferredFacts.add(rule.consequent)
                FiredRules.add(rule.id)
                new_derived = True
    until new_derived is False
    return InferredFacts
```

---

## 4. Dependencies
- Python 3.8+ (Standard Library: `typing`, `collections`)
- No third-party packages required.

---

## 5. Input Format
Entities with boolean attribute dictionaries defined in the knowledge base:
```python
{
    "tweety": {"has_feathers": True, "can_fly": True, "lays_eggs": True, "warm_blooded": True},
    "nemo":   {"has_gills": True, "lays_eggs": True, "warm_blooded": False},
    "rex":    {"has_fur": True, "warm_blooded": True, "lays_eggs": False}
}
```

---

## 6. Execution Command
```bash
python Lab4/Rule_Based_KR/rule_based.py
```

---

## 7. Sample Execution Output
```text
======================================================================
  RULE-BASED KNOWLEDGE REPRESENTATION SYSTEM
  Domain : Animal Classification
======================================================================

--- Processing entity: 'TWEETY' ---
    Known facts : {'has_feathers': True, 'can_fly': True, 'lays_eggs': True, 'has_fur': False, 'has_gills': False, 'warm_blooded': True}
    [RULE FIRED] R1: Bird Classifier  ->  tweety : is_bird
    [RULE FIRED] R5: Warm-Vertebrate Deduction  ->  tweety : is_warm_blooded_vertebrate
    Conclusions : {'is_warm_blooded_vertebrate', 'is_bird'}

--- Processing entity: 'NEMO' ---
    Known facts : {'has_feathers': False, 'can_fly': False, 'lays_eggs': True, 'has_fur': False, 'has_gills': True, 'warm_blooded': False}
    [RULE FIRED] R2: Fish Classifier  ->  nemo : is_fish
    [RULE FIRED] R4: Can-Swim Deduction  ->  nemo : can_swim
    Conclusions : {'can_swim', 'is_fish'}

--- Processing entity: 'REX' ---
    Known facts : {'has_feathers': False, 'can_fly': False, 'lays_eggs': False, 'has_fur': True, 'has_gills': False, 'warm_blooded': True}
    [RULE FIRED] R3: Mammal Classifier  ->  rex : is_mammal
    [RULE FIRED] R5: Warm-Vertebrate Deduction  ->  rex : is_warm_blooded_vertebrate
    Conclusions : {'is_warm_blooded_vertebrate', 'is_mammal'}

======================================================================
  SUMMARY OF DERIVED KNOWLEDGE
======================================================================
  tweety     ->  is_warm_blooded_vertebrate, is_bird
  nemo       ->  can_swim, is_fish
  rex        ->  is_warm_blooded_vertebrate, is_mammal
  leo        ->  is_warm_blooded_vertebrate, is_mammal
  dory       ->  can_swim, is_fish
======================================================================
```

---

## 8. Results & Observations
- The production system successfully deduced high-level taxonomical classifications without manual hardcoding of intermediate labels.
- Multi-step forward chaining allowed secondary rules (e.g., Warm-Blooded Vertebrate classification) to trigger after primary rules (e.g., Bird / Mammal) established initial classifications.

---

## 9. Learning Outcomes
- Understood declarative knowledge representation via conditional production rules.
- Learned the dynamics of working memory assertion and conflict resolution during automated inference.

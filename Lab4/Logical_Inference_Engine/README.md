# Experiment 5: Logical Inference Engine (Medical & Diagnostic Domain)

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To construct a complete modular forward-chaining logical rule engine operating over medical diagnostic rules to infer patient conditions and recommend clinical treatment paths.

---

## 2. Problem Statement
Design an expert inference engine equipped with:
- Clinical observation facts: e.g. `has_symptom(patient, fever)`, `has_symptom(patient, cough)`, `vaccinated(patient)`.
- Multi-premise diagnostic rules:
  - Fever + Cough + Sore Throat $\implies$ Flu
  - Fever + Headache + Body Ache $\implies$ Viral Fever
  - Sneezing + Runny Nose + Mild Fever $\implies$ Common Cold
  - Chest Pain + Shortness of Breath + Fatigue $\implies$ Cardiac Risk
  - Flu + Vaccinated $\implies$ Mild Flu
  - Secondary treatment rules prescribing rest, antiviral therapies, decongestants, or emergency cardiovascular triage.
Demonstrate iterative multi-pass inference until fixed-point quiescence is reached, accompanied by a full audit log of rule firing.

---

## 3. Algorithm & Approach
1. **Rule Engine Architecture:**
   - **Knowledge Base (KB):** Set of implication rules $R_i: P_1 \land P_2 \dots \land P_k \implies C$.
   - **Fact Base (FB):** Set of active ground predicates.
   - **Inference Cycle:**
     1. Loop over each rule in KB.
     2. Evaluate whether all antecedent premises $P_j$ are unified/present in FB.
     3. If satisfied and consequent $C \notin FB$:
        - Fire rule $R_i$.
        - Assert $C$ into FB.
        - Log firing event in execution audit trace.
     4. Repeat until a full pass across KB yields zero new assertions.
2. **Explainability:** Generate a structured audit trail detailing every derived diagnosis and recommended therapeutic intervention.

---

## 4. Dependencies
- Python 3.8+ (Standard Library)
- No external packages required.

---

## 5. Execution Command
```bash
python Lab4/Logical_Inference_Engine/inference_engine.py
```

---

## 6. Sample Execution Output
```text
======================================================================
  LOGICAL FORWARD-CHAINING INFERENCE ENGINE
  Domain : Medical Diagnosis
======================================================================

  Initial Facts:
    * has_symptom(patient1, cough)
    * has_symptom(patient1, fever)
    * has_symptom(patient1, sore_throat)
    * has_symptom(patient2, body_ache)
    * has_symptom(patient2, fever)
    * has_symptom(patient2, headache)
    * has_symptom(patient3, mild_fever)
    * has_symptom(patient3, runny_nose)
    * has_symptom(patient3, sneezing)
    * has_symptom(patient4, chest_pain)
    * has_symptom(patient4, fatigue)
    * has_symptom(patient4, shortness_of_breath)
    * vaccinated(patient1)

  Loaded 10 rules.

[FORWARD CHAINING - starting inference loop]
  Iter 1: [R01 - Flu (fever + cough + sore_throat)] fires  ->  diagnosed(patient1, flu)
  Iter 1: [R02 - Viral Fever (fever + headache + body_ache)] fires  ->  diagnosed(patient2, viral_fever)
  Iter 1: [R03 - Common Cold (sneezing + runny_nose + mild_fever)] fires  ->  diagnosed(patient3, common_cold)
  Iter 1: [R04 - Cardiac Risk (chest_pain + shortness_of_breath + fatigue)] fires  ->  diagnosed(patient4, cardiac_risk)
  Iter 1: [R05 - Mild Flu (flu + vaccinated -> mild_flu)] fires  ->  classified_as(patient1, mild_flu)
  Iter 1: [R06 - Recommend rest for flu] fires  ->  treatment(patient1, rest_and_fluids)
  Iter 1: [R07 - Recommend antivirals for viral_fever] fires  ->  treatment(patient2, antiviral_medication)
  Iter 1: [R08 - Recommend decongestant for common_cold] fires  ->  treatment(patient3, decongestant)
  Iter 1: [R09 - Urgent care for cardiac_risk] fires  ->  treatment(patient4, emergency_care)
  Iter 1: [R10 - High priority for cardiac_risk] fires  ->  priority(patient4, high)
  Iter 2: No new facts derived - inference complete.

======================================================================
  INFERENCE REPORT
======================================================================

  Diagnoses:
    - diagnosed(patient1, flu)
    - diagnosed(patient2, viral_fever)
    - diagnosed(patient3, common_cold)
    - diagnosed(patient4, cardiac_risk)

  Treatments:
    - treatment(patient1, rest_and_fluids)
    - treatment(patient2, antiviral_medication)
    - treatment(patient3, decongestant)
    - treatment(patient4, emergency_care)
======================================================================
```

---

## 7. Results & Observations
- In iteration 1, primary symptom-based rules fired to establish diagnostic hypotheses for all 4 patients.
- Concurrently, secondary rules chained upon newly derived diagnoses to assign treatments (`treatment(patient4, emergency_care)`) and clinical priority rankings (`priority(patient4, high)`).
- Execution ceased cleanly at iteration 2 upon complete deduction saturation.

---

## 8. Learning Outcomes
- Built an industrial-style forward-chaining expert reasoning engine from first principles.
- Understood multi-stage reasoning loops, conflict management, and automated diagnostic decision-making.

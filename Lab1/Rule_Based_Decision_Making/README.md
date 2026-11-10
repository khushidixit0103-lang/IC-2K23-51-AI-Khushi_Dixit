# Experiment 6: Rule-Based Decision Making System (Expert Engine)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 1 — AI Problem Formulation & Intelligent Problem Solving (CO1)  

---

## 🎯 Aim
To design and implement an intelligent rule-based decision support system that models multi-attribute domain knowledge, executes prioritized decision rules, and generates human-interpretable audit explanations for credit underwriting.

---

## 🧠 Problem Statement
Automated financial underwriting requires transparent, deterministic, and explainable AI mechanisms. A statistical black box cannot easily explain why an applicant was rejected without complex post-hoc tools. A rule-based decision-making system explicitly maps criteria (Credit Score, Annual Income, Debt-to-Income Ratio, Employment History) to definitive credit categories (`Prime Approval`, `Standard Approval`, `Conditional Approval`, `Rejected`) with full auditability.

---

## ⚙️ Knowledge Base Underwriting Rules

1. **Rule_HardCreditFloor:** $\text{CreditScore} < 550 \implies \text{REJECTED}$
2. **Rule_ExcessiveDTI:** $\text{DTI} > 50\% \implies \text{REJECTED}$
3. **Rule_PrimeTierApproval:** $\text{CreditScore} \ge 750 \land \text{DTI} \le 30\% \land \text{Employment} \ge 2 \implies \text{APPROVED (PRIME)}$
4. **Rule_StandardTierApproval:** $\text{CreditScore} \ge 680 \land \text{DTI} \le 40\% \land \text{Income} \ge \$40,000 \implies \text{APPROVED (STANDARD)}$
5. **Rule_ConditionalSubprime:** $600 \le \text{CreditScore} < 680 \land \text{Income} \ge \$35,000 \land \text{DTI} \le 45\% \implies \text{CONDITIONALLY APPROVED}$

---

## 🚀 Execution Command
```bash
# Navigate to experiment folder
cd Lab1/Rule_Based_Decision_Making

# Execute script
python decision_system.py
```

---

## 📊 Sample Input & Genuine Output

```text
=================================================================
   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 6
   Rule-Based Decision Making System (Expert Engine)
   Student: Khushi Dixit | Roll No: IC-2K23-51
=================================================================

--- Evaluating Automated Test Profiles ---

=======================================================
  Applicant: Aarav Sharma
  Credit Score: 780 | Income: $85,000.00
  DTI: 24.0% | Employment: 4 yrs
  FINAL DECISION: [APPROVED (PRIME)]
  Rules Fired:    Rule_PrimeTierApproval
  Audit Rationale:
    - Excellent credit profile (>=750), low DTI (<=30%), and stable employment history (>=2 yrs).
=======================================================

=======================================================
  Applicant: Vikram Singh
  Credit Score: 520 | Income: $60,000.00
  DTI: 25.0% | Employment: 5 yrs
  FINAL DECISION: [REJECTED]
  Rules Fired:    Rule_HardCreditFloor
  Audit Rationale:
    - Credit score below minimum underwriting floor (550).
=======================================================
```

---

## 💡 Learning Outcomes
1. Designed an expert rule engine for automated, transparent decision making.
2. Modeled multi-attribute decision criteria using conjunctive and disjunctive predicates.
3. Implemented transparent explanation logging for automated auditing and regulatory compliance.

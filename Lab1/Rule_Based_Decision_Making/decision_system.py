"""
Rule-Based Decision Making System
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

An intelligent rule-based decision support system for financial loan underwriting:
- Input attributes: Credit Score, Annual Income, Debt-to-Income Ratio, Employment Years
- Inference: Declarative rules with transparent audit justification
- Decision outcomes: APPROVED, CONDITIONALLY_APPROVED, REJECTED
"""

from typing import Dict, Any, List, Tuple


class ApplicantProfile:
    """Encapsulates applicant financial metrics."""

    def __init__(self, name: str, credit_score: int, annual_income: float,
                 debt_to_income: float, employment_years: int):
        self.name = name
        self.credit_score = credit_score
        self.annual_income = annual_income
        self.debt_to_income = debt_to_income  # Percentage, e.g. 28.5%
        self.employment_years = employment_years


class RuleBasedDecisionEngine:
    """Evaluates multi-attribute rules to produce deterministic, auditable decisions."""

    def evaluate(self, applicant: ApplicantProfile) -> Dict[str, Any]:
        reasons: List[str] = []
        rules_fired: List[str] = []
        decision: str = "PENDING"

        # Hard rejection constraints
        if applicant.credit_score < 550:
            decision = "REJECTED"
            rules_fired.append("Rule_HardCreditFloor")
            reasons.append("Credit score below minimum underwriting floor (550).")
            return self._build_result(decision, rules_fired, reasons)

        if applicant.debt_to_income > 50.0:
            decision = "REJECTED"
            rules_fired.append("Rule_ExcessiveDTI")
            reasons.append("Debt-to-Income ratio exceeds maximum risk threshold (50%).")
            return self._build_result(decision, rules_fired, reasons)

        # Tier 1: Prime Approval
        if applicant.credit_score >= 750 and applicant.debt_to_income <= 30.0 and applicant.employment_years >= 2:
            decision = "APPROVED (PRIME)"
            rules_fired.append("Rule_PrimeTierApproval")
            reasons.append("Excellent credit profile (>=750), low DTI (<=30%), and stable employment history (>=2 yrs).")
            return self._build_result(decision, rules_fired, reasons)

        # Tier 2: Standard Approval
        if applicant.credit_score >= 680 and applicant.debt_to_income <= 40.0 and applicant.annual_income >= 40000:
            decision = "APPROVED (STANDARD)"
            rules_fired.append("Rule_StandardTierApproval")
            reasons.append("Adequate credit rating (>=680), healthy income (>=40,000), and acceptable DTI (<=40%).")
            return self._build_result(decision, rules_fired, reasons)

        # Tier 3: Conditional Approval (Requires Co-Signer / Higher Collateral)
        if (600 <= applicant.credit_score < 680) and applicant.annual_income >= 35000 and applicant.debt_to_income <= 45.0:
            decision = "CONDITIONALLY_APPROVED"
            rules_fired.append("Rule_ConditionalSubprime")
            reasons.append("Moderate credit score (600-679); requires co-signer verification and mandatory debt review.")
            return self._build_result(decision, rules_fired, reasons)

        # Default fallback
        decision = "REJECTED"
        rules_fired.append("Rule_DefaultUnderwritingThreshold")
        reasons.append("Applicant profile does not satisfy any positive underwriting rule thresholds.")
        return self._build_result(decision, rules_fired, reasons)

    def _build_result(self, decision: str, rules: List[str], reasons: List[str]) -> Dict[str, Any]:
        return {
            "decision": decision,
            "rules_fired": rules,
            "reasons": reasons
        }


def display_decision(applicant: ApplicantProfile, result: Dict[str, Any]):
    print(f"\n=======================================================")
    print(f"  Applicant: {applicant.name}")
    print(f"  Credit Score: {applicant.credit_score} | Income: ${applicant.annual_income:,.2f}")
    print(f"  DTI: {applicant.debt_to_income:.1f}% | Employment: {applicant.employment_years} yrs")
    print(f"  FINAL DECISION: [{result['decision']}]")
    print(f"  Rules Fired:    {', '.join(result['rules_fired'])}")
    print(f"  Audit Rationale:")
    for r in result['reasons']:
        print(f"    - {r}")
    print(f"=======================================================")


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 6")
    print("   Rule-Based Decision Making System (Expert Engine)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    engine = RuleBasedDecisionEngine()

    sample_applicants = [
        ApplicantProfile("Aarav Sharma", credit_score=780, annual_income=85000, debt_to_income=24.0, employment_years=4),
        ApplicantProfile("Neha Patel", credit_score=695, annual_income=52000, debt_to_income=35.5, employment_years=3),
        ApplicantProfile("Rohan Gupta", credit_score=640, annual_income=38000, debt_to_income=42.0, employment_years=1),
        ApplicantProfile("Vikram Singh", credit_score=520, annual_income=60000, debt_to_income=25.0, employment_years=5),
    ]

    print("\n--- Evaluating Automated Test Profiles ---")
    for app in sample_applicants:
        res = engine.evaluate(app)
        display_decision(app, res)


if __name__ == "__main__":
    main()

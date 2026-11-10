"""
=============================================================================
  Lab 4 - Experiment 5 : Logical Inference Engine (Forward Chaining)
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D  (Artificial Intelligence)
  Topic    : Forward-Chaining Inference Engine - Medical Diagnosis Domain
=============================================================================
"""


# ---------------------------------------------------------------------------
# KNOWLEDGE BASE  - Facts
# ---------------------------------------------------------------------------
# Facts are plain strings following the pattern "predicate(arg1, arg2, ...)"

INITIAL_FACTS = {
    "has_symptom(patient1, fever)",
    "has_symptom(patient1, cough)",
    "has_symptom(patient1, sore_throat)",
    "has_symptom(patient2, fever)",
    "has_symptom(patient2, headache)",
    "has_symptom(patient2, body_ache)",
    "has_symptom(patient3, sneezing)",
    "has_symptom(patient3, runny_nose)",
    "has_symptom(patient3, mild_fever)",
    "has_symptom(patient4, chest_pain)",
    "has_symptom(patient4, shortness_of_breath)",
    "has_symptom(patient4, fatigue)",
    "vaccinated(patient1)",
}


# ---------------------------------------------------------------------------
# KNOWLEDGE BASE  - Rules
# ---------------------------------------------------------------------------
# Each rule is a dict:
#   "name"       : human-readable label
#   "conditions" : list of fact strings that must ALL be in the fact base
#   "conclusion" : fact string to add when conditions are met

RULES = [
    {
        "name": "R01 - Flu (fever + cough + sore_throat)",
        "conditions": [
            "has_symptom(patient1, fever)",
            "has_symptom(patient1, cough)",
            "has_symptom(patient1, sore_throat)",
        ],
        "conclusion": "diagnosed(patient1, flu)",
    },
    {
        "name": "R02 - Viral Fever (fever + headache + body_ache)",
        "conditions": [
            "has_symptom(patient2, fever)",
            "has_symptom(patient2, headache)",
            "has_symptom(patient2, body_ache)",
        ],
        "conclusion": "diagnosed(patient2, viral_fever)",
    },
    {
        "name": "R03 - Common Cold (sneezing + runny_nose + mild_fever)",
        "conditions": [
            "has_symptom(patient3, sneezing)",
            "has_symptom(patient3, runny_nose)",
            "has_symptom(patient3, mild_fever)",
        ],
        "conclusion": "diagnosed(patient3, common_cold)",
    },
    {
        "name": "R04 - Cardiac Risk (chest_pain + shortness_of_breath + fatigue)",
        "conditions": [
            "has_symptom(patient4, chest_pain)",
            "has_symptom(patient4, shortness_of_breath)",
            "has_symptom(patient4, fatigue)",
        ],
        "conclusion": "diagnosed(patient4, cardiac_risk)",
    },
    {
        "name": "R05 - Mild Flu (flu + vaccinated -> mild_flu)",
        "conditions": [
            "diagnosed(patient1, flu)",
            "vaccinated(patient1)",
        ],
        "conclusion": "classified_as(patient1, mild_flu)",
    },
    {
        "name": "R06 - Recommend rest for flu",
        "conditions": ["diagnosed(patient1, flu)"],
        "conclusion": "treatment(patient1, rest_and_fluids)",
    },
    {
        "name": "R07 - Recommend antivirals for viral_fever",
        "conditions": ["diagnosed(patient2, viral_fever)"],
        "conclusion": "treatment(patient2, antiviral_medication)",
    },
    {
        "name": "R08 - Recommend decongestant for common_cold",
        "conditions": ["diagnosed(patient3, common_cold)"],
        "conclusion": "treatment(patient3, decongestant)",
    },
    {
        "name": "R09 - Urgent care for cardiac_risk",
        "conditions": ["diagnosed(patient4, cardiac_risk)"],
        "conclusion": "treatment(patient4, emergency_care)",
    },
    {
        "name": "R10 - High priority for cardiac_risk",
        "conditions": ["treatment(patient4, emergency_care)"],
        "conclusion": "priority(patient4, high)",
    },
]


# ---------------------------------------------------------------------------
# FORWARD CHAINING ENGINE
# ---------------------------------------------------------------------------

class ForwardChainingEngine:
    """
    A generic forward-chaining inference engine.

    Algorithm:
        Repeat until no new fact is derived:
            For each rule whose ALL conditions are satisfied by current facts:
                If the conclusion is NOT already a fact:
                    Add the conclusion to the fact base  (rule fires)
    """

    def __init__(self, facts, rules):
        self.facts = set(facts)          # working memory
        self.rules = rules               # production rules
        self.fired_log = []              # ordered log of (rule_name, conclusion)

    # ------------------------------------------------------------------
    def conditions_met(self, rule):
        """Return True if every condition string is in the current fact base."""
        return all(cond in self.facts for cond in rule["conditions"])

    # ------------------------------------------------------------------
    def run(self):
        """Execute the forward-chaining loop."""
        iteration = 0

        print("\n[FORWARD CHAINING - starting inference loop]")

        while True:
            iteration += 1
            new_fact_added = False

            for rule in self.rules:
                if self.conditions_met(rule):
                    conclusion = rule["conclusion"]
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        self.fired_log.append((rule["name"], conclusion))
                        print(f"  Iter {iteration}: [{rule['name']}] fires  ->  {conclusion}")
                        new_fact_added = True

            if not new_fact_added:
                print(f"  Iter {iteration}: No new facts derived - inference complete.")
                break

        return self.facts

    # ------------------------------------------------------------------
    def print_report(self):
        """Print a structured summary of the inference session."""
        print("\n" + "=" * 70)
        print("  INFERENCE REPORT")
        print("=" * 70)

        print("\n  Rules fired (in order):")
        for i, (rule_name, conclusion) in enumerate(self.fired_log, 1):
            print(f"  {i:>2}. {rule_name}")
            print(f"       Conclusion: {conclusion}")

        print("\n  Final Fact Base:")
        for fact in sorted(self.facts):
            marker = " [derived]" if fact not in INITIAL_FACTS else ""
            print(f"    * {fact}{marker}")

        # Diagnostics summary
        print("\n  Diagnoses:")
        for fact in sorted(self.facts):
            if fact.startswith("diagnosed("):
                print(f"    - {fact}")

        print("\n  Treatments:")
        for fact in sorted(self.facts):
            if fact.startswith("treatment("):
                print(f"    - {fact}")

        print("=" * 70)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  LOGICAL FORWARD-CHAINING INFERENCE ENGINE")
    print("  Domain : Medical Diagnosis")
    print("=" * 70)

    print("\n  Initial Facts:")
    for fact in sorted(INITIAL_FACTS):
        print(f"    * {fact}")

    print(f"\n  Loaded {len(RULES)} rules.")

    engine = ForwardChainingEngine(INITIAL_FACTS, RULES)
    engine.run()
    engine.print_report()

    print("\n  Inference Engine demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()

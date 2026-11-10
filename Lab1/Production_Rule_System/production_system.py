"""
Production Rule System Implementation
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

A classical rule-based production system comprising:
1. Working Memory (Fact Base / Current State)
2. Knowledge Base (Set of IF-THEN production rules)
3. Inference Engine (Forward chaining Match-Resolve-Act cycle)
"""

from typing import List, Dict, Callable, Any, Set


class Rule:
    """Represents an individual production rule: IF condition THEN action."""

    def __init__(
        self,
        name: str,
        condition: Callable[[Set[str]], bool],
        action: Callable[[Set[str]], str],
        priority: int = 1,
    ):
        self.name = name
        self.condition = condition
        self.action = action
        self.priority = priority

    def can_fire(self, facts: Set[str]) -> bool:
        """Evaluates whether the rule's premise is satisfied by current facts."""
        return self.condition(facts)

    def fire(self, facts: Set[str]) -> str:
        """Executes the rule's action to deduce a new fact."""
        return self.action(facts)


class ProductionSystem:
    """Production rule engine utilizing forward chaining inference."""

    def __init__(self):
        self.rules: List[Rule] = []
        self.working_memory: Set[str] = set()
        self.execution_log: List[str] = []

    def add_rule(self, rule: Rule) -> None:
        """Adds a production rule to the knowledge base."""
        self.rules.append(rule)

    def add_fact(self, fact: str) -> None:
        """Adds a verified initial fact to working memory."""
        clean_fact = fact.strip().lower()
        if clean_fact:
            self.working_memory.add(clean_fact)

    def run(self, max_cycles: int = 100) -> Dict[str, Any]:
        """
        Executes the Forward-Chaining Inference Engine cycle:
        1. Match: Identify all rules whose conditions are met.
        2. Conflict Resolution: Select highest-priority unfired rule.
        3. Act: Fire the selected rule and update working memory.
        """
        cycles = 0
        fired_rules: Set[str] = set()
        self.execution_log.clear()

        while cycles < max_cycles:
            cycles += 1
            # 1. Match phase
            conflict_set: List[Rule] = [
                r for r in self.rules
                if r.name not in fired_rules and r.can_fire(self.working_memory)
            ]

            if not conflict_set:
                self.execution_log.append(f"Cycle {cycles}: No more applicable rules. Inference halted.")
                break

            # 2. Conflict Resolution phase: highest priority first
            conflict_set.sort(key=lambda r: r.priority, reverse=True)
            chosen_rule = conflict_set[0]

            # 3. Act phase
            new_fact = chosen_rule.fire(self.working_memory)
            fired_rules.add(chosen_rule.name)

            if new_fact and new_fact.lower() not in self.working_memory:
                self.working_memory.add(new_fact.lower())
                self.execution_log.append(
                    f"Cycle {cycles}: Fired [{chosen_rule.name}] (Priority {chosen_rule.priority}) -> Deduced: '{new_fact}'"
                )
            else:
                self.execution_log.append(
                    f"Cycle {cycles}: Fired [{chosen_rule.name}] (Priority {chosen_rule.priority}) -> Fact already known or no new fact."
                )

        return {
            "cycles": cycles,
            "final_facts": sorted(list(self.working_memory)),
            "log": self.execution_log,
        }


def build_sample_traffic_system() -> ProductionSystem:
    """Builds a classic autonomous vehicle rule-based decision system."""
    ps = ProductionSystem()

    # Rule 1: Emergency vehicle detected
    ps.add_rule(Rule(
        name="Emergency_Vehicle_Preemption",
        condition=lambda f: "siren_heard" in f or "emergency_vehicle_approaching" in f,
        action=lambda f: "pull_over_to_shoulder",
        priority=100
    ))

    # Rule 2: Red signal detection
    ps.add_rule(Rule(
        name="Traffic_Signal_Red",
        condition=lambda f: "traffic_light_red" in f and "pull_over_to_shoulder" not in f,
        action=lambda f: "apply_brakes_and_stop",
        priority=80
    ))

    # Rule 3: Obstacle on road
    ps.add_rule(Rule(
        name="Obstacle_Ahead",
        condition=lambda f: "obstacle_detected_within_10m" in f and "apply_brakes_and_stop" not in f,
        action=lambda f: "apply_emergency_brakes",
        priority=90
    ))

    # Rule 4: Green light with clear path
    ps.add_rule(Rule(
        name="Traffic_Signal_Green_Clear",
        condition=lambda f: "traffic_light_green" in f and "path_clear" in f and "apply_brakes_and_stop" not in f,
        action=lambda f: "accelerate_and_proceed",
        priority=50
    ))

    # Rule 5: Speed limit adherence
    ps.add_rule(Rule(
        name="Speed_Limit_Advisory",
        condition=lambda f: "accelerate_and_proceed" in f and "speed_limit_40" in f,
        action=lambda f: "maintain_speed_under_40",
        priority=40
    ))

    return ps


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 1")
    print("   Production Rule System (Inference Engine)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    system = build_sample_traffic_system()

    print("\n[Default Test Scenario]: Autonomous Vehicle Sensor Data")
    initial_facts = ["traffic_light_green", "path_clear", "speed_limit_40"]
    for fact in initial_facts:
        system.add_fact(fact)

    print(f"Initial Working Memory: {sorted(list(system.working_memory))}\n")
    print("Running Forward-Chaining Inference Engine...")
    result = system.run()

    print("\n--- Inference Execution Trace ---")
    for log_entry in result["log"]:
        print(f"  {log_entry}")

    print("\n--- Final Working Memory State ---")
    for fact in result["final_facts"]:
        print(f"  * {fact}")

    print("\n[Interactive Mode]")
    user_choice = input("Would you like to test a custom scenario? (y/n): ").strip().lower()
    if user_choice == "y":
        custom_system = build_sample_traffic_system()
        print("\nEnter facts separated by commas.")
        print("Available triggers: siren_heard, traffic_light_red, traffic_light_green,")
        print("                   path_clear, obstacle_detected_within_10m, speed_limit_40")
        raw = input("Facts: ")
        for f in raw.split(","):
            if f.strip():
                custom_system.add_fact(f.strip())
        res = custom_system.run()
        print("\n--- Custom Scenario Execution ---")
        for line in res["log"]:
            print(f"  {line}")
        print(f"\nFinal Facts: {res['final_facts']}")


if __name__ == "__main__":
    main()

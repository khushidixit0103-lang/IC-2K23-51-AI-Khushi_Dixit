"""
=============================================================================
  Lab 4 - Experiment 1 : Rule-Based Knowledge Representation
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D  (Artificial Intelligence)
  Topic    : Knowledge Representation using IF-THEN Production Rules
=============================================================================
"""


# ---------------------------------------------------------------------------
# KNOWLEDGE BASE  - Facts about animals
# ---------------------------------------------------------------------------
FACTS = {
    "tweety": {"has_feathers": True,  "can_fly": True,  "lays_eggs": True,
               "has_fur": False, "has_gills": False, "warm_blooded": True},
    "nemo":   {"has_feathers": False, "can_fly": False, "lays_eggs": True,
               "has_fur": False, "has_gills": True,  "warm_blooded": False},
    "rex":    {"has_feathers": False, "can_fly": False, "lays_eggs": False,
               "has_fur": True,  "has_gills": False, "warm_blooded": True},
    "leo":    {"has_feathers": False, "can_fly": False, "lays_eggs": False,
               "has_fur": True,  "has_gills": False, "warm_blooded": True},
    "dory":   {"has_feathers": False, "can_fly": False, "lays_eggs": True,
               "has_fur": False, "has_gills": True,  "warm_blooded": False},
}

# Derived-fact store - filled by rule engine
DERIVED = {}


# ---------------------------------------------------------------------------
# PRODUCTION RULES  - each rule is a (name, condition, conclusion) tuple
# ---------------------------------------------------------------------------

def rule_bird(name, facts):
    """IF has_feathers AND can_fly THEN is_bird."""
    if facts.get("has_feathers") and facts.get("can_fly"):
        return "is_bird"
    return None


def rule_fish(name, facts):
    """IF has_gills AND lays_eggs AND NOT has_feathers THEN is_fish."""
    if facts.get("has_gills") and facts.get("lays_eggs") and not facts.get("has_feathers"):
        return "is_fish"
    return None


def rule_mammal(name, facts):
    """IF has_fur AND warm_blooded THEN is_mammal."""
    if facts.get("has_fur") and facts.get("warm_blooded"):
        return "is_mammal"
    return None


def rule_can_swim(name, facts):
    """IF is_fish OR has_gills THEN can_swim."""
    derived = DERIVED.get(name, set())
    if "is_fish" in derived or facts.get("has_gills"):
        return "can_swim"
    return None


def rule_warm_vertebrate(name, facts):
    """IF is_mammal OR is_bird THEN is_warm_blooded_vertebrate."""
    derived = DERIVED.get(name, set())
    if "is_mammal" in derived or "is_bird" in derived:
        return "is_warm_blooded_vertebrate"
    return None


# Ordered rule list - order matters for chaining
RULES = [
    ("R1: Bird Classifier",            rule_bird),
    ("R2: Fish Classifier",            rule_fish),
    ("R3: Mammal Classifier",          rule_mammal),
    ("R4: Can-Swim Deduction",         rule_can_swim),
    ("R5: Warm-Vertebrate Deduction",  rule_warm_vertebrate),
]


# ---------------------------------------------------------------------------
# INFERENCE ENGINE  - forward chaining
# ---------------------------------------------------------------------------

def apply_rules(entity_name, facts):
    """Apply all production rules to a single entity, allowing chaining."""
    DERIVED[entity_name] = set()
    changed = True

    while changed:
        changed = False
        for rule_name, rule_fn in RULES:
            conclusion = rule_fn(entity_name, facts)
            if conclusion and conclusion not in DERIVED[entity_name]:
                DERIVED[entity_name].add(conclusion)
                print(f"    [RULE FIRED] {rule_name}  ->  {entity_name} : {conclusion}")
                changed = True  # A new fact was added; re-run rules

    return DERIVED[entity_name]


def run_knowledge_base():
    """Main driver: iterate over all entities and apply the rule engine."""
    print("=" * 70)
    print("  RULE-BASED KNOWLEDGE REPRESENTATION SYSTEM")
    print("  Domain : Animal Classification")
    print("=" * 70)

    for entity, facts in FACTS.items():
        print(f"\n--- Processing entity: '{entity.upper()}' ---")
        print(f"    Known facts : {facts}")
        derived = apply_rules(entity, facts)
        if derived:
            print(f"    Conclusions : {derived}")
        else:
            print("    Conclusions : (none derived)")

    # Summary table
    print("\n" + "=" * 70)
    print("  SUMMARY OF DERIVED KNOWLEDGE")
    print("=" * 70)
    for entity, conclusions in DERIVED.items():
        print(f"  {entity:<10} ->  {', '.join(conclusions) if conclusions else 'No conclusion'}")
    print("=" * 70)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run_knowledge_base()

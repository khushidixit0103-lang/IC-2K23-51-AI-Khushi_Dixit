"""
=============================================================================
  Lab 4 - Experiment 2 : Predicate Logic Representation
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D  (Artificial Intelligence)
  Topic    : Predicate Logic with Forward Chaining (no external libraries)
=============================================================================
"""

# ---------------------------------------------------------------------------
# ATOMIC FACTS  - represented as (predicate, arg1, arg2?) tuples
# ---------------------------------------------------------------------------
# Format: ("predicate_name", subject, object_or_None)
FACTS = [
    ("parent", "tom",   "bob"),
    ("parent", "tom",   "liz"),
    ("parent", "bob",   "ann"),
    ("parent", "bob",   "pat"),
    ("parent", "pat",   "jim"),
    ("male",   "tom",   None),
    ("male",   "bob",   None),
    ("male",   "pat",   None),
    ("male",   "jim",   None),
    ("female", "liz",   None),
    ("female", "ann",   None),
]


# ---------------------------------------------------------------------------
# HELPER  - query the current fact base
# ---------------------------------------------------------------------------

def query(predicate, arg1=None, arg2=None):
    """Return True if the fact (predicate, arg1, arg2) exists in FACTS."""
    for fact in FACTS:
        if fact[0] != predicate:
            continue
        if arg1 is not None and fact[1] != arg1:
            continue
        if arg2 is not None and fact[2] != arg2:
            continue
        return True
    return False


def all_values(predicate, position=1):
    """Return a list of unique values for the given argument position of a predicate."""
    results = []
    for fact in FACTS:
        if fact[0] == predicate:
            val = fact[position]
            if val is not None and val not in results:
                results.append(val)
    return results


def pairs(predicate):
    """Return all (arg1, arg2) pairs for a binary predicate."""
    return [(f[1], f[2]) for f in FACTS if f[0] == predicate and f[2] is not None]


# ---------------------------------------------------------------------------
# PREDICATE FUNCTIONS  (return True/False for a given instantiation)
# ---------------------------------------------------------------------------

def is_parent(x, y):
    """parent(X, Y) - X is a direct parent of Y."""
    return query("parent", x, y)


def is_male(x):
    """male(X) - X is male."""
    return query("male", x)


def is_female(x):
    """female(X) - X is female."""
    return query("female", x)


def is_father(x, y):
    """father(X, Y) - parent(X, Y) - male(X)."""
    return is_parent(x, y) and is_male(x)


def is_mother(x, y):
    """mother(X, Y) - parent(X, Y) - female(X)."""
    return is_parent(x, y) and is_female(x)


def is_grandparent(x, z):
    """grandparent(X, Z) - -Y [ parent(X, Y) - parent(Y, Z) ]."""
    all_people = all_values("parent", 1) + all_values("parent", 2)
    for y in set(all_people):
        if is_parent(x, y) and is_parent(y, z):
            return True
    return False


def is_sibling(x, y):
    """sibling(X, Y) - -P [ parent(P, X) - parent(P, Y) - X - Y ]."""
    if x == y:
        return False
    all_people = all_values("parent", 1)
    for p in all_people:
        if is_parent(p, x) and is_parent(p, y):
            return True
    return False


def is_ancestor(x, y):
    """ancestor(X, Y) - parent(X, Y)  OR  -Z [ parent(X, Z) - ancestor(Z, Y) ].
    Iterative (BFS) implementation to avoid recursion depth issues.
    """
    visited = set()
    queue = [x]
    while queue:
        current = queue.pop(0)
        for _, child in pairs("parent"):
            pass  # re-use pairs below
        # Collect children of current
        children = [f[2] for f in FACTS if f[0] == "parent" and f[1] == current]
        for child in children:
            if child == y:
                return True
            if child not in visited:
                visited.add(child)
                queue.append(child)
    return False


# ---------------------------------------------------------------------------
# FORWARD CHAINING  - derive new facts from existing ones
# ---------------------------------------------------------------------------

def forward_chain():
    """Derive father, mother, grandparent, sibling, ancestor facts."""
    new_facts = []
    all_people = list(set(all_values("parent", 1) + all_values("parent", 2)))

    print("\n[FORWARD CHAINING] Deriving new facts...")

    # Derive father / mother
    for x, y in pairs("parent"):
        if is_male(x) and ("father", x, y) not in [(f[0], f[1], f[2]) for f in FACTS + new_facts]:
            new_facts.append(("father", x, y))
            print(f"  Derived: father({x}, {y})")
        if is_female(x) and ("mother", x, y) not in [(f[0], f[1], f[2]) for f in FACTS + new_facts]:
            new_facts.append(("mother", x, y))
            print(f"  Derived: mother({x}, {y})")

    # Derive grandparent
    for x in all_people:
        for z in all_people:
            if x != z and is_grandparent(x, z):
                entry = ("grandparent", x, z)
                if entry not in [(f[0], f[1], f[2]) for f in FACTS + new_facts]:
                    new_facts.append(entry)
                    print(f"  Derived: grandparent({x}, {z})")

    # Derive sibling
    for x in all_people:
        for y in all_people:
            if x < y and is_sibling(x, y):   # x < y avoids duplicate pairs
                for entry in [("sibling", x, y), ("sibling", y, x)]:
                    if entry not in [(f[0], f[1], f[2]) for f in FACTS + new_facts]:
                        new_facts.append(entry)
                        print(f"  Derived: sibling({x}, {y})")

    # Derive ancestor
    for x in all_people:
        for y in all_people:
            if x != y and is_ancestor(x, y):
                entry = ("ancestor", x, y)
                if entry not in [(f[0], f[1], f[2]) for f in FACTS + new_facts]:
                    new_facts.append(entry)
                    print(f"  Derived: ancestor({x}, {y})")

    FACTS.extend(new_facts)
    return new_facts


# ---------------------------------------------------------------------------
# QUANTIFICATION DEMONSTRATIONS
# ---------------------------------------------------------------------------

def demo_universal():
    """FOR ALL X [ parent(X, ann) -> ancestor(X, ann) ] - check for all X."""
    print("\n[UNIVERSAL] For all X: parent(X, ann) -> ancestor(X, ann)")
    all_people = list(set(all_values("parent", 1) + all_values("parent", 2)))
    holds = True
    for x in all_people:
        if is_parent(x, "ann"):
            result = is_ancestor(x, "ann")
            print(f"  parent({x}, ann) is True  ->  ancestor({x}, ann) = {result}")
            if not result:
                holds = False
    print(f"  Universal statement holds: {holds}")


def demo_existential():
    """EXISTS X [ father(X, bob) ] - is there someone who is bob's father?"""
    print("\n[EXISTENTIAL] EXISTS X: father(X, bob)?")
    all_people = list(set(all_values("parent", 1) + all_values("parent", 2)))
    witness = None
    for x in all_people:
        if is_father(x, "bob"):
            witness = x
            break
    if witness:
        print(f"  Yes - father({witness}, bob) is True")
    else:
        print("  No witness found.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  PREDICATE LOGIC REPRESENTATION SYSTEM")
    print("  Domain : Family Relationships")
    print("=" * 70)

    print("\n[INITIAL FACTS]")
    for fact in FACTS:
        args = ", ".join(a for a in fact[1:] if a is not None)
        print(f"  {fact[0]}({args})")

    forward_chain()

    print("\n[ALL DERIVED FACTS - FINAL KNOWLEDGE BASE]")
    derived_preds = {"father", "mother", "grandparent", "sibling", "ancestor"}
    for fact in FACTS:
        if fact[0] in derived_preds:
            args = ", ".join(a for a in fact[1:] if a is not None)
            print(f"  {fact[0]}({args})")

    demo_universal()
    demo_existential()

    print("\n" + "=" * 70)
    print("  Predicate Logic demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()

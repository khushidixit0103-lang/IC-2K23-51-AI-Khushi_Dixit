"""
=============================================================================
  Lab 4 - Experiment 3 : Semantic Network
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D  (Artificial Intelligence)
  Topic    : Knowledge Representation using a Semantic Network (directed graph)
=============================================================================
"""


# ---------------------------------------------------------------------------
# SEMANTIC NETWORK CLASS
# ---------------------------------------------------------------------------

class SemanticNetwork:
    """
    A semantic network represented as a directed, labelled graph.

    Internal structure:
        graph[node] = list of (relation_label, target_node) tuples

    Standard relation labels used:
        IS-A     - subtype / instance relationship
        HAS-A    - possession / composition
        CAN      - capability
        PART-OF  - component relationship
    """

    def __init__(self):
        self.graph = {}   # node -> [(relation, target), ...]

    # ------------------------------------------------------------------
    # Mutators
    # ------------------------------------------------------------------

    def add_node(self, node):
        """Add a node (concept) to the network if it does not already exist."""
        if node not in self.graph:
            self.graph[node] = []
            print(f"  [Node added] '{node}'")

    def add_relation(self, source, relation, target):
        """
        Add a directed, labelled edge: source -[relation]-> target.
        Both nodes are created automatically if they do not exist.
        """
        self.add_node(source)
        self.add_node(target)
        edge = (relation, target)
        if edge not in self.graph[source]:
            self.graph[source].append(edge)
            print(f"  [Relation added] '{source}' -[{relation}]-> '{target}'")

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_relations(self, node):
        """Return all (relation, target) pairs for a given node."""
        return self.graph.get(node, [])

    def get_targets(self, node, relation):
        """Return all targets reachable from node via a specific relation."""
        return [t for (r, t) in self.get_relations(node) if r == relation]

    # ------------------------------------------------------------------
    # IS-A hierarchy traversal
    # ------------------------------------------------------------------

    def find_ancestors(self, node):
        """
        Walk up the IS-A chain and collect all ancestor concepts.
        Returns a list of (depth, ancestor) pairs.
        """
        ancestors = []
        visited = set()
        queue = [(node, 0)]

        while queue:
            current, depth = queue.pop(0)
            for target in self.get_targets(current, "IS-A"):
                if target not in visited:
                    visited.add(target)
                    ancestors.append((depth + 1, target))
                    queue.append((target, depth + 1))

        return ancestors

    def inherit_properties(self, node):
        """
        Collect all HAS-A and CAN properties inherited through IS-A links.
        Returns a dict mapping property relation to a list of values.
        """
        inherited = {"HAS-A": [], "CAN": [], "PART-OF": []}
        # Start with the node itself
        nodes_to_check = [node] + [anc for (_, anc) in self.find_ancestors(node)]

        for n in nodes_to_check:
            for relation in ("HAS-A", "CAN", "PART-OF"):
                for target in self.get_targets(n, relation):
                    if target not in inherited[relation]:
                        inherited[relation].append(target)

        return inherited

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def print_network(self):
        """Pretty-print the entire semantic network."""
        print("\n  -- SEMANTIC NETWORK ------------------------------------------")
        for node in sorted(self.graph.keys()):
            relations = self.graph[node]
            if relations:
                for rel, tgt in relations:
                    print(f"  -  {node:<20} --[{rel}]---  {tgt}")
            else:
                print(f"  -  {node:<20} (no outgoing edges)")
        print("  --------------------------------------------------------------")


# ---------------------------------------------------------------------------
# BUILD THE NETWORK - Animal domain
# ---------------------------------------------------------------------------

def build_animal_network():
    """Populate the semantic network with animal-domain knowledge."""
    net = SemanticNetwork()

    print("\n[BUILDING SEMANTIC NETWORK - Animal Domain]")

    # ---- IS-A hierarchy ----
    net.add_relation("Animal",   "HAS-A",   "Life")
    net.add_relation("Animal",   "CAN",     "Breathe")
    net.add_relation("Animal",   "CAN",     "Move")

    net.add_relation("Vertebrate",  "IS-A",  "Animal")
    net.add_relation("Vertebrate",  "HAS-A", "Backbone")

    net.add_relation("Mammal",   "IS-A",    "Vertebrate")
    net.add_relation("Mammal",   "HAS-A",   "Fur")
    net.add_relation("Mammal",   "CAN",     "RegulateBodyTemp")

    net.add_relation("Bird",     "IS-A",    "Vertebrate")
    net.add_relation("Bird",     "HAS-A",   "Feathers")
    net.add_relation("Bird",     "CAN",     "LayEggs")

    net.add_relation("Fish",     "IS-A",    "Vertebrate")
    net.add_relation("Fish",     "HAS-A",   "Gills")
    net.add_relation("Fish",     "CAN",     "Swim")

    net.add_relation("Dog",      "IS-A",    "Mammal")
    net.add_relation("Dog",      "HAS-A",   "Tail")
    net.add_relation("Dog",      "CAN",     "Bark")

    net.add_relation("Eagle",    "IS-A",    "Bird")
    net.add_relation("Eagle",    "CAN",     "Fly")
    net.add_relation("Eagle",    "HAS-A",   "SharpTalons")

    net.add_relation("Salmon",   "IS-A",    "Fish")
    net.add_relation("Salmon",   "CAN",     "Migrate")

    # ---- PART-OF ----
    net.add_relation("Wing",     "PART-OF", "Bird")
    net.add_relation("Fin",      "PART-OF", "Fish")
    net.add_relation("Paw",      "PART-OF", "Dog")

    return net


# ---------------------------------------------------------------------------
# DEMONSTRATIONS
# ---------------------------------------------------------------------------

def demo_traversal(net):
    """Show ancestors and inherited properties for selected nodes."""
    nodes_of_interest = ["Dog", "Eagle", "Salmon"]

    for node in nodes_of_interest:
        print(f"\n--- Node: '{node}' ---")

        # Ancestors
        ancestors = net.find_ancestors(node)
        if ancestors:
            print(f"  IS-A ancestors:")
            for depth, anc in ancestors:
                indent = "    " + "  " * (depth - 1) + "-- "
                print(f"{indent}{anc}  (depth {depth})")
        else:
            print("  IS-A ancestors: (none)")

        # Inherited properties
        props = net.inherit_properties(node)
        print(f"  Inherited HAS-A : {props['HAS-A']}")
        print(f"  Inherited CAN   : {props['CAN']}")
        print(f"  Inherited PART-OF usage: {props['PART-OF']}")

    # Direct relations of a single node
    print("\n--- Direct relations of 'Mammal' ---")
    for rel, tgt in net.get_relations("Mammal"):
        print(f"  Mammal -[{rel}]-> {tgt}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  SEMANTIC NETWORK KNOWLEDGE REPRESENTATION")
    print("  Domain : Animal Kingdom")
    print("=" * 70)

    net = build_animal_network()
    net.print_network()
    demo_traversal(net)

    print("\n" + "=" * 70)
    print("  Semantic Network demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()

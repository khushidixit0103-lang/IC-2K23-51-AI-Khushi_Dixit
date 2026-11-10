"""
Depth-First Search (DFS) Implementation
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Uninformed Search Algorithm:
- Strategy: LIFO Stack (Last-In-First-Out)
- Completeness: Complete on finite graphs with cycle avoidance (visited set)
- Optimality: Non-optimal (does not guarantee shortest path)
- Time Complexity: O(b^m) where m is maximum search depth
- Space Complexity: O(b * m) (linear memory footprint)
"""

from typing import Dict, List, Optional, Set


ROMANIA_MAP: Dict[str, List[str]] = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"],
}


class DepthFirstSearch:
    """Implements graph-traversal DFS with LIFO frontier stack."""

    def __init__(self, graph: Dict[str, List[str]]):
        self.graph = graph

    def search(self, start: str, goal: str) -> Optional[Dict]:
        if start not in self.graph or goal not in self.graph:
            return None

        # Stack contains: (current_node, path_taken)
        stack = [(start, [start])]
        visited: Set[str] = set()
        expansion_order: List[str] = []
        max_frontier_size = 1

        while stack:
            max_frontier_size = max(max_frontier_size, len(stack))
            current, path = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            expansion_order.append(current)

            if current == goal:
                return {
                    "path": path,
                    "cost_in_steps": len(path) - 1,
                    "nodes_expanded": len(expansion_order),
                    "expansion_order": expansion_order,
                    "max_frontier_size": max_frontier_size,
                }

            # Reverse alphabetical order to expand alphabetical first on pop
            for neighbor in sorted(self.graph.get(current, []), reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 3)")
    print("   Depth-First Search (DFS) Traversal")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    dfs = DepthFirstSearch(ROMANIA_MAP)
    start_city = "Arad"
    goal_city = "Bucharest"

    print(f"\nSearching path from '{start_city}' to '{goal_city}' using DFS...")
    result = dfs.search(start_city, goal_city)

    if result:
        print("\n--- Search Results ---")
        print(f"Discovered Path:     {' -> '.join(result['path'])}")
        print(f"Path Length (hops):  {result['cost_in_steps']}")
        print(f"Total Nodes Expanded: {result['nodes_expanded']}")
        print(f"Max Frontier Size:   {result['max_frontier_size']}")
        print("\nNode Expansion Order:")
        print(" -> ".join(result["expansion_order"]))
    else:
        print("Goal unreachable.")


if __name__ == "__main__":
    main()

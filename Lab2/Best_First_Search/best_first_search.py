"""
Greedy Best-First Search Implementation
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Informed Heuristic Search:
- Evaluation Function: f(n) = h(n) [Estimated cost from node n to goal]
- Frontier: Priority Queue ordered by minimum h(n)
- Benchmark: Romania Road Network with straight-line distance heuristic to Bucharest
"""

import heapq
from typing import Dict, List, Optional, Tuple, Set


ROMANIA_GRAPH: Dict[str, List[Tuple[str, int]]] = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
    "Giurgiu": [("Bucharest", 90)],
    "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
    "Eforie": [("Hirsova", 86)],
    "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
    "Iasi": [("Vaslui", 92), ("Neamt", 87)],
    "Neamt": [("Iasi", 87)],
}

# Straight-Line Distance heuristic to Bucharest (h_SLD)
STRAIGHT_LINE_HEURISTIC: Dict[str, int] = {
    "Arad": 366,
    "Bucharest": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}


class GreedyBestFirstSearch:
    """Implements Greedy Best-First Search using straight-line distance heuristic."""

    def __init__(self, graph: Dict[str, List[Tuple[str, int]]], heuristic: Dict[str, int]):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start: str, goal: str) -> Optional[Dict]:
        if start not in self.graph or goal not in self.graph:
            return None

        # Priority queue entry: (heuristic_val, current_node, path, actual_g_cost)
        frontier = [(self.heuristic[start], start, [start], 0)]
        visited: Set[str] = set()
        expansion_order: List[str] = []

        while frontier:
            h_val, curr, path, g_cost = heapq.heappop(frontier)

            if curr in visited:
                continue

            visited.add(curr)
            expansion_order.append(curr)

            if curr == goal:
                return {
                    "path": path,
                    "total_distance": g_cost,
                    "nodes_expanded": len(expansion_order),
                    "expansion_order": expansion_order,
                }

            for neighbor, step_cost in self.graph.get(curr, []):
                if neighbor not in visited:
                    heapq.heappush(
                        frontier,
                        (self.heuristic[neighbor], neighbor, path + [neighbor], g_cost + step_cost)
                    )

        return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 5)")
    print("   Greedy Best-First Search (GBFS)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    gbfs = GreedyBestFirstSearch(ROMANIA_GRAPH, STRAIGHT_LINE_HEURISTIC)
    start_city = "Arad"
    goal_city = "Bucharest"

    print(f"\nSearching path from '{start_city}' to '{goal_city}' using Greedy Best-First Search...")
    res = gbfs.search(start_city, goal_city)

    if res:
        print("\n--- Search Results ---")
        print(f"Discovered Path:        {' -> '.join(res['path'])}")
        print(f"Total Path Cost (km):   {res['total_distance']}")
        print(f"Total Nodes Expanded:   {res['nodes_expanded']}")
        print(f"\nNode Expansion Order:")
        print(" -> ".join(res["expansion_order"]))
    else:
        print("No path found.")


if __name__ == "__main__":
    main()

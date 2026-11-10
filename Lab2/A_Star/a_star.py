"""
A* Search Algorithm Implementation
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Informed Heuristic Search:
- Evaluation Function: f(n) = g(n) + h(n)
  * g(n) = Exact accumulated path cost from start node to n
  * h(n) = Admissible heuristic estimate from n to goal
- Optimality: Guaranteed optimal when h(n) is admissible and consistent
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


class AStarSearch:
    """Implements graph-search A* with priority queue on f(n) = g(n) + h(n)."""

    def __init__(self, graph: Dict[str, List[Tuple[str, int]]], heuristic: Dict[str, int]):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start: str, goal: str) -> Optional[Dict]:
        if start not in self.graph or goal not in self.graph:
            return None

        # Priority queue stores tuples: (f_cost, g_cost, current_node, path)
        f_start = self.heuristic[start]
        frontier = [(f_start, 0, start, [start])]
        best_g_costs: Dict[str, int] = {start: 0}
        expansion_order: List[Tuple[str, int, int, int]] = []

        while frontier:
            f_val, g_cost, curr, path = heapq.heappop(frontier)

            # Prune obsolete frontier entries
            if g_cost > best_g_costs.get(curr, float('inf')):
                continue

            h_val = self.heuristic[curr]
            expansion_order.append((curr, g_cost, h_val, f_val))

            if curr == goal:
                return {
                    "path": path,
                    "total_distance": g_cost,
                    "nodes_expanded": len(expansion_order),
                    "expansion_log": expansion_order,
                }

            for neighbor, step_cost in self.graph.get(curr, []):
                new_g = g_cost + step_cost
                if new_g < best_g_costs.get(neighbor, float('inf')):
                    best_g_costs[neighbor] = new_g
                    new_f = new_g + self.heuristic[neighbor]
                    heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

        return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 6)")
    print("   A* Search Algorithm (Optimal Heuristic Pathfinding)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    astar = AStarSearch(ROMANIA_GRAPH, STRAIGHT_LINE_HEURISTIC)
    start_city = "Arad"
    goal_city = "Bucharest"

    print(f"\nSearching optimal path from '{start_city}' to '{goal_city}' via A*...")
    res = astar.search(start_city, goal_city)

    if res:
        print("\n--- Search Results ---")
        print(f"Optimal Path:           {' -> '.join(res['path'])}")
        print(f"Optimal Path Cost (km): {res['total_distance']}")
        print(f"Total Nodes Expanded:   {res['nodes_expanded']}")

        print("\nDetailed Node Expansion Log (f = g + h):")
        print(f"{'Node':<16} | {'g(n)':<8} | {'h(n)':<8} | {'f(n)':<8}")
        print("-" * 46)
        for node, g, h, f in res["expansion_log"]:
            print(f"{node:<16} | {g:<8} | {h:<8} | {f:<8}")
    else:
        print("No path found.")


if __name__ == "__main__":
    main()

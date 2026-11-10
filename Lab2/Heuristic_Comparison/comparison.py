"""
Heuristic Search Algorithms Comparative Analysis
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Mandatory Analysis:
Compares Breadth-First Search (BFS), Depth-First Search (DFS),
Greedy Best-First Search (GBFS), and A* Search on a uniform benchmark
(Romania Road Network: Arad to Bucharest).

Evaluation Metrics:
1. Solution Quality (Total Path Cost in km)
2. Search Efficiency (Nodes Expanded)
3. Memory Consumption (Maximum Frontier Size)
4. Empirical Execution Time (Microseconds)
"""

import time
import heapq
from collections import deque
from typing import Dict, List, Tuple, Optional, Set, Any


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


def compute_path_cost(path: List[str]) -> int:
    cost = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        for neighbor, edge_cost in ROMANIA_GRAPH.get(u, []):
            if neighbor == v:
                cost += edge_cost
                break
    return cost


def run_bfs(start: str, goal: str) -> Dict[str, Any]:
    t0 = time.perf_counter()
    queue = deque([(start, [start])])
    visited = {start}
    nodes_expanded = 0
    max_frontier = 1

    while queue:
        max_frontier = max(max_frontier, len(queue))
        curr, path = queue.popleft()
        nodes_expanded += 1

        if curr == goal:
            elapsed = (time.perf_counter() - t0) * 1_000_000
            return {
                "algorithm": "BFS",
                "path": path,
                "cost": compute_path_cost(path),
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier,
                "time_us": round(elapsed, 2)
            }

        for neighbor, _ in sorted(ROMANIA_GRAPH.get(curr, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return {}


def run_dfs(start: str, goal: str) -> Dict[str, Any]:
    t0 = time.perf_counter()
    stack = [(start, [start])]
    visited: Set[str] = set()
    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        curr, path = stack.pop()

        if curr in visited:
            continue
        visited.add(curr)
        nodes_expanded += 1

        if curr == goal:
            elapsed = (time.perf_counter() - t0) * 1_000_000
            return {
                "algorithm": "DFS",
                "path": path,
                "cost": compute_path_cost(path),
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier,
                "time_us": round(elapsed, 2)
            }

        for neighbor, _ in sorted(ROMANIA_GRAPH.get(curr, []), reverse=True):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return {}


def run_gbfs(start: str, goal: str) -> Dict[str, Any]:
    t0 = time.perf_counter()
    frontier = [(STRAIGHT_LINE_HEURISTIC[start], start, [start], 0)]
    visited: Set[str] = set()
    nodes_expanded = 0
    max_frontier = 1

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        h, curr, path, g = heapq.heappop(frontier)

        if curr in visited:
            continue
        visited.add(curr)
        nodes_expanded += 1

        if curr == goal:
            elapsed = (time.perf_counter() - t0) * 1_000_000
            return {
                "algorithm": "Greedy Best-First",
                "path": path,
                "cost": g,
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier,
                "time_us": round(elapsed, 2)
            }

        for neighbor, step_cost in ROMANIA_GRAPH.get(curr, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (STRAIGHT_LINE_HEURISTIC[neighbor], neighbor, path + [neighbor], g + step_cost))

    return {}


def run_astar(start: str, goal: str) -> Dict[str, Any]:
    t0 = time.perf_counter()
    frontier = [(STRAIGHT_LINE_HEURISTIC[start], 0, start, [start])]
    best_g: Dict[str, int] = {start: 0}
    nodes_expanded = 0
    max_frontier = 1

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        f, g, curr, path = heapq.heappop(frontier)

        if g > best_g.get(curr, float('inf')):
            continue

        nodes_expanded += 1

        if curr == goal:
            elapsed = (time.perf_counter() - t0) * 1_000_000
            return {
                "algorithm": "A* Search",
                "path": path,
                "cost": g,
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier,
                "time_us": round(elapsed, 2)
            }

        for neighbor, step_cost in ROMANIA_GRAPH.get(curr, []):
            new_g = g + step_cost
            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                new_f = new_g + STRAIGHT_LINE_HEURISTIC[neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return {}


def main():
    print("=" * 75)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (ANALYSIS ACTIVITY)")
    print("   Comparative Evaluation of Heuristic & Uninformed Search")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 75)

    start = "Arad"
    goal = "Bucharest"
    print(f"\nBenchmark Problem: Standardized Romania Road Network ({start} -> {goal})\n")

    results = [
        run_bfs(start, goal),
        run_dfs(start, goal),
        run_gbfs(start, goal),
        run_astar(start, goal),
    ]

    print(f"{'Algorithm':<20} | {'Cost (km)':<10} | {'Nodes Expanded':<15} | {'Max Frontier':<12} | {'Time (us)'}")
    print("-" * 75)
    for r in results:
        print(f"{r['algorithm']:<20} | {r['cost']:<10} | {r['nodes_expanded']:<15} | {r['max_frontier']:<12} | {r['time_us']:<10}")
    print("-" * 75)

    print("\nDetailed Solution Paths Discovered:")
    for r in results:
        print(f"  * {r['algorithm']:<18}: {' -> '.join(r['path'])} (Cost: {r['cost']} km)")

    print("\n--- Analytical Observations ---")
    print("1. Optimality:")
    print("   - A* achieves the lowest, truly optimal road distance of 418 km via Rimnicu Vilcea & Pitesti.")
    print("   - Greedy Best-First took the Fagaras detour (450 km) due to myopic reliance on h(n).")
    print("   - BFS finds the shortest path in terms of edge hops (3 hops), but higher road distance (450 km).")
    print("2. Search Efficiency & Frontiers:")
    print("   - A* and GBFS expand significantly fewer nodes (4-6 nodes) compared to uninformed BFS (9 nodes).")
    print("   - A* expands fewer nodes than BFS while guaranteeing absolute cost optimality.")


if __name__ == "__main__":
    main()

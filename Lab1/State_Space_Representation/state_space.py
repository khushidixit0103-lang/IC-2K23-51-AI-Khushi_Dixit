"""
State Space Representation Framework
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Formulation:
Formal definition of an AI problem in State Space:
1. Initial State [s0]
2. Action Space [A(s)]
3. Transition Model / Successor Function [Result(s, a)]
4. Goal Test [Goal(s)]
5. Path Cost [c(s, a, s')]
Includes state-space expansion tree, branching factor analysis, and traversal.
"""

from typing import List, Tuple, Dict, Any, Optional, Set
from collections import deque


class StateSpaceProblem:
    """Abstract base class for formal AI State-Space problems."""

    def initial_state(self) -> Any:
        raise NotImplementedError

    def is_goal(self, state: Any) -> bool:
        raise NotImplementedError

    def actions(self, state: Any) -> List[str]:
        raise NotImplementedError

    def result(self, state: Any, action: str) -> Any:
        raise NotImplementedError

    def step_cost(self, state: Any, action: str, next_state: Any) -> float:
        return 1.0


class GridWorldProblem(StateSpaceProblem):
    """
    State space navigation problem on an N x M grid with obstacles.
    State: (x, y) coordinates.
    Actions: Up, Down, Left, Right.
    """

    def __init__(self, rows: int = 4, cols: int = 4, start: Tuple[int, int] = (0, 0),
                 goal: Tuple[int, int] = (3, 3), obstacles: Optional[Set[Tuple[int, int]]] = None):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.obstacles = obstacles or {(1, 1), (1, 2), (2, 2)}

    def initial_state(self) -> Tuple[int, int]:
        return self.start

    def is_goal(self, state: Tuple[int, int]) -> bool:
        return state == self.goal

    def actions(self, state: Tuple[int, int]) -> List[str]:
        r, c = state
        possible = []
        moves = {
            "Up": (r - 1, c),
            "Down": (r + 1, c),
            "Left": (r, c - 1),
            "Right": (r, c + 1),
        }
        for act, (nr, nc) in moves.items():
            if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.obstacles:
                possible.append(act)
        return possible

    def result(self, state: Tuple[int, int], action: str) -> Tuple[int, int]:
        r, c = state
        deltas = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
        dr, dc = deltas[action]
        return (r + dr, c + dc)

    def print_grid(self, path: Optional[List[Tuple[int, int]]] = None):
        path_set = set(path) if path else set()
        print("\nGrid World State Space Visualization:")
        for r in range(self.rows):
            row_str = []
            for c in range(self.cols):
                pt = (r, c)
                if pt == self.start:
                    row_str.append("[S]")
                elif pt == self.goal:
                    row_str.append("[G]")
                elif pt in self.obstacles:
                    row_str.append("[#]")
                elif pt in path_set:
                    row_str.append(" * ")
                else:
                    row_str.append(" . ")
            print(" ".join(row_str))
        print("Legend: [S]=Start, [G]=Goal, [#]=Obstacle, [*]=Solution Path, [.]=Open Cell\n")


def analyze_state_space(problem: StateSpaceProblem):
    """Explores the complete reachable state space and computes branching factor metrics."""
    start = problem.initial_state()
    visited: Set[Any] = {start}
    queue = deque([start])
    total_transitions = 0
    branching_factors = []

    while queue:
        curr = queue.popleft()
        acts = problem.actions(curr)
        branching_factors.append(len(acts))
        for act in acts:
            total_transitions += 1
            nxt = problem.result(curr, act)
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

    avg_branching = sum(branching_factors) / len(branching_factors) if branching_factors else 0
    return {
        "reachable_states": len(visited),
        "total_transitions": total_transitions,
        "max_branching_factor": max(branching_factors) if branching_factors else 0,
        "min_branching_factor": min(branching_factors) if branching_factors else 0,
        "avg_branching_factor": round(avg_branching, 2),
    }


def find_path_bfs(problem: StateSpaceProblem) -> Optional[List[Tuple[Any, str]]]:
    """Finds path from initial state to goal via state-space BFS."""
    start = problem.initial_state()
    queue = deque([(start, [(start, "START")])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if problem.is_goal(state):
            return path

        for act in problem.actions(state):
            nxt = problem.result(state, act)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [(nxt, act)]))

    return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 5")
    print("   Formal State-Space Representation & Analysis")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    grid = GridWorldProblem(rows=4, cols=4, start=(0, 0), goal=(3, 3))
    grid.print_grid()

    metrics = analyze_state_space(grid)
    print("--- State-Space Graph Metrics ---")
    print(f"  Reachable States (Vertices):     {metrics['reachable_states']}")
    print(f"  Total Directed Transitions (Edges): {metrics['total_transitions']}")
    print(f"  Maximum Branching Factor (b_max):   {metrics['max_branching_factor']}")
    print(f"  Minimum Branching Factor (b_min):   {metrics['min_branching_factor']}")
    print(f"  Average Branching Factor (b_avg):   {metrics['avg_branching_factor']}")

    path = find_path_bfs(grid)
    if path:
        print(f"\nOptimal Path to Goal Found in {len(path) - 1} steps:")
        coords = [s for s, _ in path]
        for step, (st, act) in enumerate(path):
            print(f"  Step {step}: Action = {act:<6} -> State = {st}")
        grid.print_grid(coords)


if __name__ == "__main__":
    main()

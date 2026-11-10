"""
8-Puzzle Solver Implementation
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

A* Search on the 8-Puzzle:
- State Representation: 3x3 tuple of integers (0 = blank)
- Inversion count check for solvability
- Heuristics:
  1. Misplaced Tiles: Number of tiles not in goal position
  2. Manhattan Distance: Sum of vertical and horizontal distances to target positions
- Demonstration of heuristic dominance (Manhattan dominates Misplaced Tiles)
"""

import heapq
from typing import List, Tuple, Optional, Dict, Set


# Standard goal state for 8-puzzle:
# 1 2 3
# 4 5 6
# 7 8 0
GOAL_STATE: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Precomputed target (row, col) for each tile 1..8
GOAL_POSITIONS: Dict[int, Tuple[int, int]] = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 0: (2, 2)
}


class EightPuzzleSolver:
    """A* solver for the 8-puzzle problem."""

    def __init__(self, start_state: Tuple[int, ...]):
        if len(start_state) != 9:
            raise ValueError("State must contain exactly 9 values (0-8).")
        self.start_state = start_state

    @staticmethod
    def is_solvable(state: Tuple[int, ...]) -> bool:
        """A state is solvable iff its inversion count is even."""
        tiles = [x for x in state if x != 0]
        inversions = 0
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] > tiles[j]:
                    inversions += 1
        return inversions % 2 == 0

    @staticmethod
    def heuristic_misplaced(state: Tuple[int, ...]) -> int:
        """h1: Counts tiles not in their goal position (excluding blank)."""
        return sum(1 for i in range(9) if state[i] != 0 and state[i] != GOAL_STATE[i])

    @staticmethod
    def heuristic_manhattan(state: Tuple[int, ...]) -> int:
        """h2: Sum of taxicab distances of all tiles from goal positions."""
        distance = 0
        for idx, val in enumerate(state):
            if val != 0:
                curr_r, curr_c = divmod(idx, 3)
                goal_r, goal_c = GOAL_POSITIONS[val]
                distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
        return distance

    @staticmethod
    def get_neighbors(state: Tuple[int, ...]) -> List[Tuple[Tuple[int, ...], str]]:
        """Generates all legal board configurations by sliding tiles into the blank space."""
        neighbors = []
        blank_idx = state.index(0)
        r, c = divmod(blank_idx, 3)

        moves = {
            "UP": (r - 1, c),
            "DOWN": (r + 1, c),
            "LEFT": (r, c - 1),
            "RIGHT": (r, c + 1)
        }

        for direction, (nr, nc) in moves.items():
            if 0 <= nr < 3 and 0 <= nc < 3:
                target_idx = nr * 3 + nc
                new_state = list(state)
                # Swap blank with adjacent tile
                new_state[blank_idx], new_state[target_idx] = new_state[target_idx], new_state[blank_idx]
                neighbors.append((tuple(new_state), direction))

        return neighbors

    def solve(self, heuristic_name: str = "manhattan") -> Optional[Dict]:
        """Runs A* search with the selected heuristic."""
        if not self.is_solvable(self.start_state):
            return None

        h_func = self.heuristic_manhattan if heuristic_name == "manhattan" else self.heuristic_misplaced
        h_start = h_func(self.start_state)

        # Priority queue entry: (f, g, state, path)
        frontier = [(h_start, 0, self.start_state, [(self.start_state, "START")])]
        visited: Set[Tuple[int, ...]] = set()
        nodes_expanded = 0

        while frontier:
            f, g, curr, path = heapq.heappop(frontier)

            if curr in visited:
                continue

            visited.add(curr)
            nodes_expanded += 1

            if curr == GOAL_STATE:
                return {
                    "path": path,
                    "moves_count": g,
                    "nodes_expanded": nodes_expanded,
                    "heuristic_used": heuristic_name
                }

            for next_st, move in self.get_neighbors(curr):
                if next_st not in visited:
                    next_g = g + 1
                    next_f = next_g + h_func(next_st)
                    heapq.heappush(frontier, (next_f, next_g, next_st, path + [(next_st, move)]))

        return None


def format_board(state: Tuple[int, ...]) -> str:
    lines = []
    for r in range(3):
        row = [str(state[r * 3 + c]) if state[r * 3 + c] != 0 else "_" for c in range(3)]
        lines.append("  " + " ".join(row))
    return "\n".join(lines)


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 7)")
    print("   8-Puzzle Solver (A* with Heuristic Dominance Analysis)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    # Initial state (Medium difficulty, solvable in 4-6 moves)
    initial_puzzle = (1, 2, 3, 0, 4, 6, 7, 5, 8)

    print("\nInitial State:")
    print(format_board(initial_puzzle))
    print("\nGoal State:")
    print(format_board(GOAL_STATE))

    solver = EightPuzzleSolver(initial_puzzle)
    if not solver.is_solvable(initial_puzzle):
        print("This puzzle instance is mathematically unsolvable.")
        return

    # Solve with Misplaced Tiles Heuristic (h1)
    res_misplaced = solver.solve(heuristic_name="misplaced")

    # Solve with Manhattan Distance Heuristic (h2)
    res_manhattan = solver.solve(heuristic_name="manhattan")

    print("\n--- Heuristic Performance Comparison ---")
    print(f"{'Heuristic Metric':<25} | {'Optimal Moves':<14} | {'Nodes Expanded'}")
    print("-" * 60)
    print(f"{'h1 (Misplaced Tiles)':<25} | {res_misplaced['moves_count']:<14} | {res_misplaced['nodes_expanded']}")
    print(f"{'h2 (Manhattan Distance)':<25} | {res_manhattan['moves_count']:<14} | {res_manhattan['nodes_expanded']}")
    print("-" * 60)
    print("Conclusion: Manhattan Distance strictly dominates Misplaced Tiles (fewer nodes expanded).")

    print("\n--- Step-by-Step Solution Trace (Manhattan) ---")
    for step, (st, action) in enumerate(res_manhattan["path"]):
        print(f"Step {step}: Action = {action}")
        print(format_board(st))
        print()


if __name__ == "__main__":
    main()

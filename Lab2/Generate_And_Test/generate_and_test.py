"""
Generate and Test Search Algorithm
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Concept:
Generate and Test is the most fundamental heuristic search paradigm:
1. Generator: Systematically generates candidate configurations in the state space.
2. Tester: Evaluates candidate against problem constraints / goal conditions.
Demonstrated on the classic N-Queens formulation with heuristic conflict scoring.
"""

from typing import List, Optional, Tuple
import time


class NQueensGenerateAndTest:
    """Solves the N-Queens problem using Generate-and-Test with heuristic conflict testing."""

    def __init__(self, n: int = 4):
        self.n = n
        self.nodes_generated = 0
        self.nodes_tested = 0

    def compute_heuristic_conflicts(self, state: List[int]) -> int:
        """
        Calculates the number of mutually attacking queen pairs (heuristic h).
        state[i] = row of queen in column i.
        h = 0 represents a valid goal state.
        """
        conflicts = 0
        k = len(state)
        for i in range(k):
            for j in range(i + 1, k):
                # Same row conflict
                if state[i] == state[j]:
                    conflicts += 1
                # Diagonal conflict
                if abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def test(self, state: List[int]) -> bool:
        """Tester function: returns True if state has N queens and 0 conflicts."""
        self.nodes_tested += 1
        if len(state) != self.n:
            return False
        return self.compute_heuristic_conflicts(state) == 0

    def solve(self) -> Optional[List[int]]:
        """
        Systematic generator: recursively builds permutations and tests candidates.
        """
        self.nodes_generated = 0
        self.nodes_tested = 0

        solution = []

        def backtrack_generate(current_state: List[int]) -> bool:
            if len(current_state) == self.n:
                self.nodes_generated += 1
                if self.test(current_state):
                    solution.extend(current_state)
                    return True
                return False

            for row in range(self.n):
                self.nodes_generated += 1
                current_state.append(row)
                if backtrack_generate(current_state):
                    return True
                current_state.pop()
            return False

        backtrack_generate([])
        return solution if solution else None

    def print_board(self, state: List[int]):
        """Visualizes the queen placements on an N x N chessboard."""
        print(f"\nChessboard Visualization ({self.n}x{self.n}):")
        for r in range(self.n):
            row_symbols = []
            for c in range(self.n):
                if state[c] == r:
                    row_symbols.append("[Q]")
                else:
                    row_symbols.append(" . ")
            print(" ".join(row_symbols))
        print()


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 1)")
    print("   Generate and Test Search Paradigm (N-Queens Solver)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    for n in [4, 5, 8]:
        solver = NQueensGenerateAndTest(n=n)
        start_t = time.perf_counter()
        solution = solver.solve()
        elapsed_ms = (time.perf_counter() - start_t) * 1000

        print(f"\n--- Solving {n}-Queens Problem ---")
        if solution is not None:
            print(f"Goal State Found: {solution} (Column -> Row)")
            print(f"  Heuristic Conflicts h(s):  {solver.compute_heuristic_conflicts(solution)}")
            print(f"  Nodes Generated:          {solver.nodes_generated}")
            print(f"  Complete Boards Tested:   {solver.nodes_tested}")
            print(f"  Execution Time:           {elapsed_ms:.2f} ms")
            if n <= 5:
                solver.print_board(solution)
        else:
            print(f"No solution found for N={n}.")


if __name__ == "__main__":
    main()

"""
Hill Climbing Search Algorithm
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Local Heuristic Search:
- Evaluates states using objective/heuristic evaluation function
- Implements:
  1. Steepest-Ascent Hill Climbing
  2. Random-Restart Hill Climbing (overcomes local extrema and plateaus)
Demonstrated on the 8-Queens problem minimizing conflicting queen pairs h(s).
"""

import random
from typing import List, Tuple, Optional


class EightQueensHillClimbing:
    """Solves the 8-Queens optimization problem using Hill Climbing variations."""

    def __init__(self, n: int = 8):
        self.n = n

    def compute_heuristic_conflicts(self, state: List[int]) -> int:
        """Heuristic h(s): number of pairs of queens attacking each other."""
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if state[i] == state[j]:
                    conflicts += 1
                if abs(state[i] - state[j]) == abs(i - j):
                    conflicts += 1
        return conflicts

    def get_random_state(self) -> List[int]:
        """Generates a random state of length n where state[col] = row."""
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def steepest_ascent(self, initial_state: Optional[List[int]] = None) -> Tuple[List[int], int, int, bool]:
        """
        Steepest-Ascent Hill Climbing:
        Generates all successor single-queen movements and chooses the one
        with the maximum reduction in conflicts.
        Returns: (final_state, final_conflicts, steps_taken, is_global_optimum)
        """
        current = list(initial_state) if initial_state is not None else self.get_random_state()
        current_conflicts = self.compute_heuristic_conflicts(current)
        steps = 0

        while True:
            if current_conflicts == 0:
                return (current, 0, steps, True)

            best_neighbor = None
            best_conflicts = current_conflicts

            # Explore all possible single-queen row moves (8 * 7 = 56 neighbors)
            for col in range(self.n):
                for row in range(self.n):
                    if row != current[col]:
                        neighbor = list(current)
                        neighbor[col] = row
                        h_val = self.compute_heuristic_conflicts(neighbor)
                        if h_val < best_conflicts:
                            best_conflicts = h_val
                            best_neighbor = neighbor

            # If no neighbor is strictly better, we hit a local maximum/plateau
            if best_neighbor is None or best_conflicts >= current_conflicts:
                return (current, current_conflicts, steps, current_conflicts == 0)

            current = best_neighbor
            current_conflicts = best_conflicts
            steps += 1

    def random_restart(self, max_restarts: int = 50) -> Tuple[List[int], int, int]:
        """
        Random-Restart Hill Climbing:
        Conducts repeated steepest-ascent searches from newly randomized initial states
        until the global optimum h(s) = 0 is found or max restarts exhausted.
        """
        total_steps = 0
        for restart in range(max_restarts):
            init = self.get_random_state()
            state, conflicts, steps, solved = self.steepest_ascent(init)
            total_steps += steps
            if solved:
                return (state, restart, total_steps)

        return (state, max_restarts, total_steps)


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 4)")
    print("   Hill Climbing Search (Steepest-Ascent & Random-Restart)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    random.seed(42)  # For reproducible academic verification
    solver = EightQueensHillClimbing(n=8)

    print("\n--- Testing Single-Run Steepest-Ascent Hill Climbing ---")
    runs = 10
    successes = 0
    for r in range(1, runs + 1):
        _, final_h, steps, solved = solver.steepest_ascent()
        if solved:
            successes += 1
            print(f"Run {r:02d}: Success! Found global optimum h=0 in {steps} steps.")
        else:
            print(f"Run {r:02d}: Trapped in local minimum (h = {final_h}) after {steps} steps.")

    success_rate = (successes / runs) * 100
    print(f"\nSteepest-Ascent Success Rate: {success_rate:.1f}% ({successes}/{runs})")
    print("Observation: Pure hill climbing gets trapped in local minima/shoulders.")

    print("\n--- Testing Random-Restart Hill Climbing ---")
    sol, restarts, total_steps = solver.random_restart()
    print(f"Global Optimum Found: {sol}")
    print(f"  Heuristic Conflicts h(s): {solver.compute_heuristic_conflicts(sol)}")
    print(f"  Restarts Required:        {restarts}")
    print(f"  Total Steps Taken:        {total_steps}")


if __name__ == "__main__":
    main()

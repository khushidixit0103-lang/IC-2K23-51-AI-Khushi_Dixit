"""
Water Jug Problem Implementation
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

State Space Representation and Production Rules for the Water Jug Problem:
- Capacities: Jug 1 = X liters, Jug 2 = Y liters
- Goal: Measure exactly Z liters in either jug
- Search Strategy: Breadth-First Search (BFS) to guarantee optimal (shortest) solution
"""

import math
from collections import deque
from typing import List, Tuple, Optional, Set


class WaterJugSolver:
    """Solves the generalized Water Jug problem using production rules and BFS."""

    def __init__(self, capacity_x: int, capacity_y: int, target: int):
        if capacity_x <= 0 or capacity_y <= 0 or target <= 0:
            raise ValueError("Capacities and target must be positive integers.")
        self.cap_x = capacity_x
        self.cap_y = capacity_y
        self.target = target

    def is_solvable(self) -> bool:
        """Determines solvability based on Bézout's identity and GCD condition."""
        if self.target > max(self.cap_x, self.cap_y):
            return False
        return self.target % math.gcd(self.cap_x, self.cap_y) == 0

    def get_successors(self, x: int, y: int) -> List[Tuple[Tuple[int, int], str]]:
        """
        Applies production rules to generate all valid next states from (x, y):
        Rules:
        1. Fill Jug 1
        2. Fill Jug 2
        3. Empty Jug 1
        4. Empty Jug 2
        5. Pour Jug 1 into Jug 2
        6. Pour Jug 2 into Jug 1
        """
        transitions = []

        # Rule 1: Fill Jug 1
        if x < self.cap_x:
            transitions.append(((self.cap_x, y), f"Fill Jug 1 ({self.cap_x}L)"))

        # Rule 2: Fill Jug 2
        if y < self.cap_y:
            transitions.append(((x, self.cap_y), f"Fill Jug 2 ({self.cap_y}L)"))

        # Rule 3: Empty Jug 1
        if x > 0:
            transitions.append(((0, y), "Empty Jug 1"))

        # Rule 4: Empty Jug 2
        if y > 0:
            transitions.append(((x, 0), "Empty Jug 2"))

        # Rule 5: Pour Jug 1 into Jug 2
        if x > 0 and y < self.cap_y:
            pour = min(x, self.cap_y - y)
            transitions.append(((x - pour, y + pour), f"Pour {pour}L from Jug 1 to Jug 2"))

        # Rule 6: Pour Jug 2 into Jug 1
        if y > 0 and x < self.cap_x:
            pour = min(y, self.cap_x - x)
            transitions.append(((x + pour, y - pour), f"Pour {pour}L from Jug 2 to Jug 1"))

        return transitions

    def solve(self) -> Optional[List[Tuple[Tuple[int, int], str]]]:
        """Performs BFS on state space to locate shortest path from (0, 0) to goal."""
        if not self.is_solvable():
            return None

        # Queue stores: (current_state, path_of_transitions)
        start_state = (0, 0)
        queue = deque([(start_state, [(start_state, "Initial state (both jugs empty)")])])
        visited: Set[Tuple[int, int]] = {start_state}

        while queue:
            (curr_x, curr_y), path = queue.popleft()

            # Goal check
            if curr_x == self.target or curr_y == self.target:
                return path

            for next_state, rule_desc in self.get_successors(curr_x, curr_y):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [(next_state, rule_desc)]))

        return None


def print_solution(path: List[Tuple[Tuple[int, int], str]], cap_x: int, cap_y: int, target: int):
    print(f"\nOptimal Solution Found in {len(path) - 1} steps:")
    print(f"{'Step':<6} | {'Jug 1 (' + str(cap_x) + 'L)':<12} | {'Jug 2 (' + str(cap_y) + 'L)':<12} | {'Rule / Action Applied'}")
    print("-" * 65)
    for idx, (state, action) in enumerate(path):
        print(f"{idx:<6} | {str(state[0]) + ' L':<12} | {str(state[1]) + ' L':<12} | {action}")
    print("-" * 65)


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 2")
    print("   Water Jug Problem (State-Space Search)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    # Standard default textbook demonstration: Jug 1 = 4L, Jug 2 = 3L, Target = 2L
    default_x, default_y, default_z = 4, 3, 2
    print(f"\n[Default Scenario]: Jug 1 = {default_x}L, Jug 2 = {default_y}L, Target = {default_z}L")

    solver = WaterJugSolver(default_x, default_y, default_z)
    sol = solver.solve()
    if sol:
        print_solution(sol, default_x, default_y, default_z)
    else:
        print("No solution exists for the default configuration.")

    print("\n[Interactive Mode]")
    choice = input("Would you like to solve with custom jug capacities? (y/n): ").strip().lower()
    if choice == "y":
        try:
            x = int(input("Enter capacity of Jug 1 (e.g. 5): ").strip())
            y = int(input("Enter capacity of Jug 2 (e.g. 7): ").strip())
            z = int(input("Enter target amount (e.g. 4): ").strip())
            custom_solver = WaterJugSolver(x, y, z)
            if not custom_solver.is_solvable():
                print(f"\n[Result]: Target {z}L is mathematically impossible with jugs {x}L and {y}L (GCD constraint).")
            else:
                cust_sol = custom_solver.solve()
                if cust_sol:
                    print_solution(cust_sol, x, y, z)
        except ValueError as err:
            print(f"Invalid input: {err}")


if __name__ == "__main__":
    main()

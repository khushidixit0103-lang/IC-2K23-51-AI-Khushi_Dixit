"""
Missionaries and Cannibals Problem Implementation
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Formulation:
- State: (M_left, C_left, Boat_left)
- Constraints: Cannibals must never outnumber Missionaries on either bank (if M > 0)
- Capacity: Boat holds up to 2 people, at least 1 person to row
- Strategy: Breadth-First Search (BFS) for minimal crossing steps
"""

from collections import deque
from typing import List, Tuple, Optional, Set


class State:
    """Represents the state of both banks and boat position."""

    def __init__(self, m_left: int, c_left: int, boat_left: int, total_m: int = 3, total_c: int = 3):
        self.m_left = m_left
        self.c_left = c_left
        self.boat_left = boat_left  # 1 if Left, 0 if Right
        self.total_m = total_m
        self.total_c = total_c

    @property
    def m_right(self) -> int:
        return self.total_m - self.m_left

    @property
    def c_right(self) -> int:
        return self.total_c - self.c_left

    def is_valid(self) -> bool:
        """Verifies boundary and safety constraints on both banks."""
        # Boundary constraints
        if not (0 <= self.m_left <= self.total_m and 0 <= self.c_left <= self.total_c):
            return False

        # Left bank safety: cannibals cannot outnumber missionaries if missionaries > 0
        if self.m_left > 0 and self.c_left > self.m_left:
            return False

        # Right bank safety
        if self.m_right > 0 and self.c_right > self.m_right:
            return False

        return True

    def is_goal(self) -> bool:
        """Goal is all missionaries, cannibals, and boat on the right bank."""
        return self.m_left == 0 and self.c_left == 0 and self.boat_left == 0

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, State)
            and self.m_left == other.m_left
            and self.c_left == other.c_left
            and self.boat_left == other.boat_left
        )

    def __hash__(self) -> int:
        return hash((self.m_left, self.c_left, self.boat_left))

    def __str__(self) -> str:
        b_left = "[BOAT]" if self.boat_left == 1 else "      "
        b_right = "[BOAT]" if self.boat_left == 0 else "      "
        l_str = f"{'M'*self.m_left}{'C'*self.c_left}".ljust(6)
        r_str = f"{'M'*self.m_right}{'C'*self.c_right}".ljust(6)
        return f"Left: {l_str} {b_left} ~~~ River ~~~ {b_right} Right: {r_str}"


def get_possible_moves() -> List[Tuple[int, int]]:
    """Possible boat passengers (m, c) for a boat of capacity 2."""
    return [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


def solve_missionaries_cannibals(total_m: int = 3, total_c: int = 3) -> Optional[List[Tuple[State, str]]]:
    """Finds the shortest sequence of valid crossings using BFS."""
    start_state = State(total_m, total_c, boat_left=1, total_m=total_m, total_c=total_c)
    if not start_state.is_valid():
        return None

    queue = deque([(start_state, [(start_state, "Initial state (everyone on Left bank)")])])
    visited: Set[State] = {start_state}
    moves = get_possible_moves()

    while queue:
        current, path = queue.popleft()

        if current.is_goal():
            return path

        for m, c in moves:
            if current.boat_left == 1:
                # Moving Left -> Right
                next_state = State(
                    current.m_left - m,
                    current.c_left - c,
                    boat_left=0,
                    total_m=total_m,
                    total_c=total_c,
                )
                action = f"Cross -> {m} Missionary(ies), {c} Cannibal(s) to Right bank"
            else:
                # Moving Right -> Left
                next_state = State(
                    current.m_left + m,
                    current.c_left + c,
                    boat_left=1,
                    total_m=total_m,
                    total_c=total_c,
                )
                action = f"Return <- {m} Missionary(ies), {c} Cannibal(s) to Left bank"

            if next_state.is_valid() and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(next_state, action)]))

    return None


def main():
    print("=" * 70)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 3")
    print("   Missionaries and Cannibals Problem (State-Space Search)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 70)

    solution = solve_missionaries_cannibals(3, 3)

    if not solution:
        print("No valid crossing sequence found.")
        return

    print(f"\nSolution Found in {len(solution) - 1} crossings:")
    print("-" * 70)
    for step, (state, action) in enumerate(solution):
        print(f"Step {step:02d}: {action}")
        print(f"         {state}")
        print("-" * 70)


if __name__ == "__main__":
    main()

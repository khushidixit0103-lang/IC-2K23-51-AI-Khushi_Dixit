"""
Intelligent Maze Solver & Robot Navigation
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Robot Navigation in a 2D Obstacle Grid:
- Environment: 2D Grid with walls ('#'), open passages ('.'), Start ('S'), and Goal ('G')
- Algorithms:
  1. Breadth-First Search (Uninformed)
  2. A* Search with Manhattan Distance Heuristic (Informed)
- Metrics: Solution path length, nodes expanded, execution time
"""

import heapq
from collections import deque
from typing import List, Tuple, Optional, Dict, Set


class Maze:
    """Represents a 2D grid maze environment."""

    def __init__(self, grid: List[str]):
        self.grid = [list(row) for row in grid]
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = self._find_char('S')
        self.goal = self._find_char('G')

        if not self.start or not self.goal:
            raise ValueError("Maze must contain both Start ('S') and Goal ('G').")

    def _find_char(self, char: str) -> Optional[Tuple[int, int]]:
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == char:
                    return (r, c)
        return None

    def get_valid_neighbors(self, r: int, c: int) -> List[Tuple[int, int]]:
        """Returns reachable adjacent (Up, Down, Left, Right) coordinates."""
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] != '#':
                neighbors.append((nr, nc))
        return neighbors

    def print_solution(self, path: List[Tuple[int, int]]):
        """Prints maze overlaying the discovered path with '*' characters."""
        path_set = set(path)
        print("\nMaze Navigation Visualization:")
        for r in range(self.rows):
            line = []
            for c in range(self.cols):
                pt = (r, c)
                if pt == self.start:
                    line.append("S")
                elif pt == self.goal:
                    line.append("G")
                elif pt in path_set:
                    line.append("*")
                else:
                    line.append(self.grid[r][c])
            print(" ".join(line))
        print()


def solve_maze_bfs(maze: Maze) -> Optional[Dict]:
    """Solves maze using Breadth-First Search."""
    queue = deque([(maze.start, [maze.start])])
    visited: Set[Tuple[int, int]] = {maze.start}
    nodes_expanded = 0

    while queue:
        curr, path = queue.popleft()
        nodes_expanded += 1

        if curr == maze.goal:
            return {
                "algorithm": "BFS",
                "path": path,
                "path_length": len(path) - 1,
                "nodes_expanded": nodes_expanded,
            }

        for neighbor in maze.get_valid_neighbors(*curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def solve_maze_astar(maze: Maze) -> Optional[Dict]:
    """Solves maze using A* Search with Manhattan Distance."""
    def manhattan(pt: Tuple[int, int]) -> int:
        return abs(pt[0] - maze.goal[0]) + abs(pt[1] - maze.goal[1])

    frontier = [(manhattan(maze.start), 0, maze.start, [maze.start])]
    best_g: Dict[Tuple[int, int], int] = {maze.start: 0}
    nodes_expanded = 0

    while frontier:
        f, g, curr, path = heapq.heappop(frontier)

        if g > best_g.get(curr, float('inf')):
            continue

        nodes_expanded += 1

        if curr == maze.goal:
            return {
                "algorithm": "A*",
                "path": path,
                "path_length": len(path) - 1,
                "nodes_expanded": nodes_expanded,
            }

        for neighbor in maze.get_valid_neighbors(*curr):
            new_g = g + 1
            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                new_f = new_g + manhattan(neighbor)
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 8)")
    print("   Intelligent Maze Solver & Robot Navigation")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    sample_maze = [
        "S . . # . . . .",
        "# # . # . # # .",
        ". . . . . . # .",
        ". # # # # . # .",
        ". . . # . . # .",
        "# # . # . # # .",
        ". . . . . . . G",
    ]
    sample_maze_clean = [row.replace(" ", "") for row in sample_maze]

    maze = Maze(sample_maze_clean)
    print("Initial Maze Layout:")
    maze.print_solution([])

    res_bfs = solve_maze_bfs(maze)
    res_astar = solve_maze_astar(maze)

    print("--- Algorithm Comparison on Maze ---")
    print(f"{'Algorithm':<10} | {'Optimal Path Steps':<20} | {'Nodes Expanded'}")
    print("-" * 50)
    print(f"{res_bfs['algorithm']:<10} | {res_bfs['path_length']:<20} | {res_bfs['nodes_expanded']}")
    print(f"{res_astar['algorithm']:<10} | {res_astar['path_length']:<20} | {res_astar['nodes_expanded']}")
    print("-" * 50)

    print("\nOptimal Robot Navigation Trajectory (A* Path):")
    maze.print_solution(res_astar["path"])


if __name__ == "__main__":
    main()

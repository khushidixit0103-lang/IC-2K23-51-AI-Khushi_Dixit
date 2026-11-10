"""
Vacuum Cleaner Problem Implementation
Lab 1 - AI Problem Formulation & Intelligent Problem Solving
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Russell & Norvig Vacuum World:
- Environment: 2 Rooms (A, B) or N-rooms, each Dirty or Clean
- Actuators: Move Left, Move Right, Suck (Clean)
- Sensors: Current location, Current room cleanliness status
- Agents implemented:
  1. Simple Reflex Agent
  2. Model-Based Agent (with internal memory)
"""

from typing import Dict, List, Tuple


class VacuumEnvironment:
    """Simulates the physical environment with discrete rooms."""

    def __init__(self, rooms: Dict[str, str], initial_agent_loc: str):
        # rooms: {'A': 'Dirty', 'B': 'Dirty'}
        self.rooms = rooms.copy()
        self.agent_loc = initial_agent_loc
        self.performance_score = 0
        self.action_history: List[Tuple[str, str, int]] = []

    def get_percept(self) -> Tuple[str, str]:
        """Returns (location, status) perceptible by the agent."""
        return (self.agent_loc, self.rooms[self.agent_loc])

    def execute_action(self, action: str) -> None:
        """Applies agent action, modifies environment state, and updates score."""
        cost = 0
        if action == "Suck":
            if self.rooms[self.agent_loc] == "Dirty":
                self.rooms[self.agent_loc] = "Clean"
                cost = -2
                reward = 10
            else:
                cost = -2
                reward = 0
        elif action == "Right":
            if self.agent_loc == "A":
                self.agent_loc = "B"
            cost = -1
            reward = 0
        elif action == "Left":
            if self.agent_loc == "B":
                self.agent_loc = "A"
            cost = -1
            reward = 0
        elif action == "NoOp":
            cost = 0
            reward = 0
        else:
            raise ValueError(f"Unknown action: {action}")

        # Passive reward for clean rooms
        clean_count = sum(1 for s in self.rooms.values() if s == "Clean")
        step_score = reward + cost + (clean_count * 5)
        self.performance_score += step_score
        self.action_history.append((self.agent_loc, action, self.performance_score))

    def is_all_clean(self) -> bool:
        return all(status == "Clean" for status in self.rooms.values())


class SimpleReflexAgent:
    """Selects actions based solely on current percept without history."""

    def decide(self, percept: Tuple[str, str]) -> str:
        loc, status = percept
        if status == "Dirty":
            return "Suck"
        elif loc == "A":
            return "Right"
        elif loc == "B":
            return "Left"
        return "NoOp"


class ModelBasedReflexAgent:
    """Maintains an internal model of the world to avoid redundant actions."""

    def __init__(self, known_rooms: List[str]):
        self.model: Dict[str, str] = {r: "Unknown" for r in known_rooms}

    def decide(self, percept: Tuple[str, str]) -> str:
        loc, status = percept
        self.model[loc] = status

        # If all rooms known to be clean, stop
        if all(self.model[r] == "Clean" for r in self.model):
            return "NoOp"

        if status == "Dirty":
            return "Suck"

        # Explore uncleaned rooms
        if loc == "A" and self.model.get("B") != "Clean":
            return "Right"
        elif loc == "B" and self.model.get("A") != "Clean":
            return "Left"

        return "NoOp"


def run_simulation(agent_type: str, initial_rooms: Dict[str, str], start_loc: str, steps: int = 10):
    env = VacuumEnvironment(initial_rooms, start_loc)
    agent = SimpleReflexAgent() if agent_type == "Simple Reflex" else ModelBasedReflexAgent(list(initial_rooms.keys()))

    print(f"\n--- Running {agent_type} Agent Simulation ---")
    print(f"Initial State: Location={start_loc}, Rooms={initial_rooms}")
    print(f"{'Step':<5} | {'Location':<10} | {'Percept':<10} | {'Action':<10} | {'Performance'}")
    print("-" * 55)

    for step in range(1, steps + 1):
        percept = env.get_percept()
        action = agent.decide(percept)
        env.execute_action(action)
        print(f"{step:<5} | {env.agent_loc:<10} | {percept[1]:<10} | {action:<10} | {env.performance_score:<10}")
        if action == "NoOp" and env.is_all_clean():
            print(f"Goal Reached: All rooms cleaned in {step} steps!")
            break

    print(f"Final Room States: {env.rooms}")
    print(f"Total Cumulative Score: {env.performance_score}\n")


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - EXPERIMENT 4")
    print("   Vacuum Cleaner Problem (Reflex & Model-Based Agents)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    test_scenarios = [
        {"A": "Dirty", "B": "Dirty"},
        {"A": "Clean", "B": "Dirty"},
        {"A": "Dirty", "B": "Clean"},
    ]

    for idx, scen in enumerate(test_scenarios, 1):
        print(f"\n================ Scenario {idx} ================")
        run_simulation("Simple Reflex", scen, start_loc="A", steps=5)
        run_simulation("Model-Based Reflex", scen, start_loc="A", steps=5)


if __name__ == "__main__":
    main()

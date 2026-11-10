"""
GPS Route Planning System
Lab 2 - Heuristic Search Algorithms
Student: Khushi Dixit (Roll No: IC-2K23-51)
Course: IC-709D / IC-703 C

Application: Intelligent GPS Route Planner
- Real geographic coordinates (Latitude, Longitude) for major Indian cities
- Haversine formula heuristic to estimate great-circle distance
- A* algorithm to compute the shortest road path
"""

import math
import heapq
from typing import Dict, List, Tuple, Optional


# Indian Cities with GPS coordinates (Lat, Lon)
CITY_COORDINATES: Dict[str, Tuple[float, float]] = {
    "Indore": (22.7196, 75.8577),
    "Bhopal": (23.2599, 77.4126),
    "Ujjain": (23.1765, 75.7885),
    "Nagpur": (21.1458, 79.0882),
    "Jabalpur": (23.1815, 79.9864),
    "Gwalior": (26.2183, 78.1828),
    "Jaipur": (26.9124, 75.7873),
    "Kota": (25.2138, 75.8648),
    "Ahmedabad": (23.0225, 72.5714),
    "Mumbai": (19.0760, 72.8777),
}

# Highway road distances (in km)
ROAD_NETWORK: Dict[str, List[Tuple[str, float]]] = {
    "Indore": [("Ujjain", 55.0), ("Bhopal", 192.0), ("Ahmedabad", 390.0), ("Mumbai", 585.0)],
    "Ujjain": [("Indore", 55.0), ("Kota", 260.0), ("Bhopal", 188.0)],
    "Bhopal": [("Indore", 192.0), ("Ujjain", 188.0), ("Jabalpur", 310.0), ("Nagpur", 350.0), ("Gwalior", 420.0)],
    "Kota": [("Ujjain", 260.0), ("Jaipur", 250.0), ("Gwalior", 310.0)],
    "Jaipur": [("Kota", 250.0), ("Gwalior", 330.0), ("Ahmedabad", 660.0)],
    "Gwalior": [("Bhopal", 420.0), ("Kota", 310.0), ("Jaipur", 330.0), ("Jabalpur", 500.0)],
    "Jabalpur": [("Bhopal", 310.0), ("Nagpur", 275.0), ("Gwalior", 500.0)],
    "Nagpur": [("Bhopal", 350.0), ("Jabalpur", 275.0), ("Mumbai", 815.0)],
    "Ahmedabad": [("Indore", 390.0), ("Jaipur", 660.0), ("Mumbai", 525.0)],
    "Mumbai": [("Indore", 585.0), ("Ahmedabad", 525.0), ("Nagpur", 815.0)],
}


def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Computes great-circle distance between two GPS coordinates using the Haversine formula.
    Provides an admissible lower-bound heuristic for routing on Earth's surface.
    """
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    earth_radius_km = 6371.0
    return earth_radius_km * c


class GPSRoutePlanner:
    """A* GPS Route Planner using Haversine heuristic."""

    def __init__(self, road_network: Dict[str, List[Tuple[str, float]]], coords: Dict[str, Tuple[float, float]]):
        self.roads = road_network
        self.coords = coords

    def plan_route(self, origin: str, destination: str) -> Optional[Dict]:
        if origin not in self.roads or destination not in self.roads:
            return None

        goal_coord = self.coords[destination]

        def h(city: str) -> float:
            return haversine_distance(self.coords[city], goal_coord)

        frontier = [(h(origin), 0.0, origin, [origin])]
        best_g: Dict[str, float] = {origin: 0.0}
        nodes_expanded = 0

        while frontier:
            f, g, curr, path = heapq.heappop(frontier)

            if g > best_g.get(curr, float('inf')):
                continue

            nodes_expanded += 1

            if curr == destination:
                return {
                    "origin": origin,
                    "destination": destination,
                    "path": path,
                    "total_distance_km": round(g, 1),
                    "nodes_expanded": nodes_expanded,
                }

            for neighbor, distance in self.roads.get(curr, []):
                new_g = g + distance
                if new_g < best_g.get(neighbor, float('inf')):
                    best_g[neighbor] = new_g
                    new_f = new_g + h(neighbor)
                    heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

        return None


def main():
    print("=" * 65)
    print("   ARTIFICIAL INTELLIGENCE LAB - LAB 2 (EXPERIMENT 9)")
    print("   Intelligent GPS Route Planner (A* with Haversine Heuristic)")
    print("   Student: Khushi Dixit | Roll No: IC-2K23-51")
    print("=" * 65)

    planner = GPSRoutePlanner(ROAD_NETWORK, CITY_COORDINATES)

    test_routes = [
        ("Indore", "Jaipur"),
        ("Indore", "Nagpur"),
        ("Ahmedabad", "Gwalior"),
    ]

    for origin, destination in test_routes:
        print(f"\nPlanning optimal highway itinerary from {origin} to {destination}...")
        route = planner.plan_route(origin, destination)
        if route:
            print(f"  Optimal Route:     {' -> '.join(route['path'])}")
            print(f"  Highway Distance:  {route['total_distance_km']} km")
            print(f"  Cities Evaluated:  {route['nodes_expanded']}")
        else:
            print("  Route not found.")


if __name__ == "__main__":
    main()

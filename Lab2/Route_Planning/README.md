# Experiment 9: GPS Route Planner (A* & Haversine Heuristic)

**Student Name:** Khushi Dixit  
**Roll Number:** IC-2K23-51  
**Course Code:** IC-709D / IC-703 C  
**Lab Unit:** Unit 2 — Heuristic Search Algorithms (CO2)  

---

## 🎯 Aim
To develop a real-world **GPS Route Planning System** using genuine geographic coordinates (latitude and longitude) of central and western Indian highway networks, applying the **Haversine formula** as an admissible heuristic to guide A* shortest-path itinerary optimization.

---

## 🧠 Formulation & The Haversine Distance Heuristic

When routing on a spherical terrestrial globe, straight-line distance must account for Earth's curvature. The Haversine formula calculates the great-circle distance between two GPS coordinates $(\phi_1, \lambda_1)$ and $(\phi_2, \lambda_2)$:

$$a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)$$
$$c = 2 \cdot \text{atan2}\left(\sqrt{a}, \sqrt{1 - a}\right)$$
$$d = R \cdot c \quad (\text{where } R = 6,371 \text{ km})$$

Because great-circle distance represents the absolute shortest possible physical trajectory on Earth's surface, $h_{\text{haversine}}$ is guaranteed to be **admissible** ($h(n) \le h^*(n)$), ensuring A* finds the provably optimal highway route.

---

## 🚀 Execution Command
```bash
# Navigate to experiment directory
cd Lab2/Route_Planning

# Run script
python route_planner.py
```

---

## 📊 Sample Input & Genuine Output

### Highway Navigation Scenarios
```text
Planning optimal highway itinerary from Indore to Jaipur...
  Optimal Route:     Indore -> Ujjain -> Kota -> Jaipur
  Highway Distance:  565.0 km
  Cities Evaluated:  4

Planning optimal highway itinerary from Indore to Nagpur...
  Optimal Route:     Indore -> Bhopal -> Nagpur
  Highway Distance:  542.0 km
  Cities Evaluated:  4

Planning optimal highway itinerary from Ahmedabad to Gwalior...
  Optimal Route:     Ahmedabad -> Jaipur -> Gwalior
  Highway Distance:  990.0 km
  Cities Evaluated:  7
```

---

## 💡 Learning Outcomes
1. Modeled geographic spatial routing using spherical trigonometry and real GPS coordinates.
2. Formulated the Haversine great-circle distance as a physically admissible heuristic.
3. Implemented realistic multi-city GPS navigation with genuine highway network distances.

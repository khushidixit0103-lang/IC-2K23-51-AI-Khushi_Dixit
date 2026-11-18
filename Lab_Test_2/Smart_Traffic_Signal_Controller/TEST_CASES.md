# AI Lab Test 2: Test Cases and Execution Results

**Student Name:** Khushi Dixit  
**Roll Number:** 51 (IC-2K23-51)  
**Subject:** Artificial Intelligence (Lab Test 2)  
**Problem:** Set 1 – Smart Traffic Signal Controller  

---

## 📌 Overview of Test Scenarios

To thoroughly validate the logical reasoning, rule integrity, safety constraints, and tie-breaking policies of the **Smart Traffic Signal Controller**, five comprehensive test scenarios were evaluated:

1. **Sample Benchmark Scenario:** Benchmark scenario provided in the official assignment specification.
2. **Test Case 1 (Emergency Priority):** Single emergency vehicle present on Road B with lower normal density.
3. **Test Case 2 (Normal Peak Traffic):** No emergency vehicles; right-of-way determined purely by weighted traffic volume.
4. **Test Case 3 (Blocked Road Safety Exclusion):** The road with the highest traffic volume (Road C) is blocked due to an accident.
5. **Test Case 4 (Equal Priority & Tie-Breaking):** Two roads (Road A and Road D) have identical priority scores, waiting times, and vehicle counts.
6. **Test Case 5 (Fail-Safe Defense):** All four intersection roads are blocked.

---

## 📐 Priority Scoring Mathematical Formulation

$$\text{Priority Score}(R) = 
\begin{cases} 
-1, & \text{if } \text{Blocked} = \text{yes} \quad (\text{Strict Exclusion}) \\
10000 + (10 \times \text{Wait}) + \text{Vehicles}, & \text{if } \text{Emergency} = \text{yes and Blocked} = \text{no} \\
W_{\text{density}} + (2 \times \text{Vehicles}) + (3 \times \text{Wait}), & \text{otherwise}
\end{cases}$$

Where density weights ($W_{\text{density}}$) are:
- `high` = 50
- `medium` = 30
- `low` = 10

---

## 🧪 Detailed Test Case Specifications

---

### 🔹 Test Case 1: Emergency Vehicle on Road B (Assignment Benchmark)

#### Objective
Verify that an emergency vehicle (e.g., ambulance, fire brigade) immediately preempts standard traffic, overriding roads with higher vehicle volumes and higher densities.

#### Input Data
| Road | Waiting Vehicles | Waiting Time | Traffic Density | Emergency? | Blocked? |
|---|---|---|---|---|---|
| **Road A** | 15 | 5 min | Medium | No | No |
| **Road B** | 8 | 12 min | Medium | **Yes** | No |
| **Road C** | 25 | 3 min | High | No | No |
| **Road D** | 5 | 7 min | Low | No | No |

#### Priority Score Calculations
- **Road A:** $30 + (15 \times 2) + (5 \times 3) = 30 + 30 + 15 = 75$
- **Road B:** $10000 + (12 \times 10) + 8 = 10000 + 120 + 8 = \mathbf{10128}$ *(Emergency Rule 1 Triggered)*
- **Road C:** $50 + (25 \times 2) + (3 \times 3) = 50 + 50 + 9 = 109$
- **Road D:** $10 + (5 \times 2) + (7 \times 3) = 10 + 10 + 21 = 41$

#### Execution Output
```text
------------------ CURRENT INTERSECTION STATUS ------------------
Road A | Veh: 15 | Wait: 5m | Density: medium | Emerg: no | Blocked: no | Score: 75
Road B | Veh: 8 | Wait: 12m | Density: medium | Emerg: yes | Blocked: no | Score: 10128
Road C | Veh: 25 | Wait: 3m | Density: high | Emerg: no | Blocked: no | Score: 109
Road D | Veh: 5 | Wait: 7m | Density: low | Emerg: no | Blocked: no | Score: 41
-----------------------------------------------------------------

=================================================================
                 SMART TRAFFIC SIGNAL CONTROLLER                 
=================================================================
Selected Road: Road B
Signal: GREEN

Reason:
An emergency vehicle is waiting on Road B. The system gives emergency vehicles the highest priority.

Decision Metrics:
  - Calculated Priority Score : 10128
  - Waiting Time              : 12 minutes
  - Waiting Vehicles          : 8
=================================================================
```

#### Outcome & Verification
- **Expected Winner:** Road B (GREEN)
- **Actual Winner:** Road B (GREEN)
- **Status:** **PASSED (100% Match)**

---

### 🔹 Test Case 2: Normal Peak Traffic (No Emergency Vehicles)

#### Objective
Verify that in the absence of emergency vehicles, the system optimizes throughput by awarding the GREEN signal to the road with the highest composite traffic priority score.

#### Input Data
| Road | Waiting Vehicles | Waiting Time | Traffic Density | Emergency? | Blocked? |
|---|---|---|---|---|---|
| **Road A** | 15 | 5 min | Medium | No | No |
| **Road B** | 8 | 12 min | Medium | No | No |
| **Road C** | 25 | 3 min | High | No | No |
| **Road D** | 5 | 7 min | Low | No | No |

#### Priority Score Calculations
- **Road A:** $30 + (15 \times 2) + (5 \times 3) = 30 + 30 + 15 = 75$
- **Road B:** $30 + (8 \times 2) + (12 \times 3) = 30 + 16 + 36 = 82$
- **Road C:** $50 + (25 \times 2) + (3 \times 3) = 50 + 50 + 9 = \mathbf{109}$ *(High Density + Volume Leader)*
- **Road D:** $10 + (5 \times 2) + (7 \times 3) = 10 + 10 + 21 = 41$

#### Execution Output
```text
------------------ CURRENT INTERSECTION STATUS ------------------
Road A | Veh: 15 | Wait: 5m | Density: medium | Emerg: no | Blocked: no | Score: 75
Road B | Veh: 8 | Wait: 12m | Density: medium | Emerg: no | Blocked: no | Score: 82
Road C | Veh: 25 | Wait: 3m | Density: high | Emerg: no | Blocked: no | Score: 109
Road D | Veh: 5 | Wait: 7m | Density: low | Emerg: no | Blocked: no | Score: 41
-----------------------------------------------------------------

=================================================================
                 SMART TRAFFIC SIGNAL CONTROLLER                 
=================================================================
Selected Road: Road C
Signal: GREEN

Reason:
Road C selected based on highest combined traffic priority (density weight + vehicle count + wait time).

Decision Metrics:
  - Calculated Priority Score : 109
  - Waiting Time              : 3 minutes
  - Waiting Vehicles          : 25
=================================================================
```

#### Outcome & Verification
- **Expected Winner:** Road C (GREEN)
- **Actual Winner:** Road C (GREEN)
- **Status:** **PASSED (100% Match)**

---

### 🔹 Test Case 3: Blocked Road Handling (Accident on Road C)

#### Objective
Ensure safety constraint enforcement: when Road C has the heaviest traffic but is blocked due to an accident, the controller strictly excludes Road C and safely grants GREEN to the next best eligible road (Road B).

#### Input Data
| Road | Waiting Vehicles | Waiting Time | Traffic Density | Emergency? | Blocked? |
|---|---|---|---|---|---|
| **Road A** | 15 | 5 min | Medium | No | No |
| **Road B** | 8 | 12 min | Medium | No | No |
| **Road C** | 25 | 3 min | High | No | **Yes (Accident)** |
| **Road D** | 5 | 7 min | Low | No | No |

#### Priority Score Calculations
- **Road A:** $30 + (15 \times 2) + (5 \times 3) = 75$
- **Road B:** $30 + (8 \times 2) + (12 \times 3) = \mathbf{82}$ *(Highest among eligible roads)*
- **Road C:** $\mathbf{-1}$ *(Rule 2 Triggered: Blocked Road Excluded)*
- **Road D:** $10 + (5 \times 2) + (7 \times 3) = 41$

#### Execution Output
```text
------------------ CURRENT INTERSECTION STATUS ------------------
Road A | Veh: 15 | Wait: 5m | Density: medium | Emerg: no | Blocked: no | Score: 75
Road B | Veh: 8 | Wait: 12m | Density: medium | Emerg: no | Blocked: no | Score: 82
Road C | Veh: 25 | Wait: 3m | Density: high | Emerg: no | Blocked: yes | Score: -1
Road D | Veh: 5 | Wait: 7m | Density: low | Emerg: no | Blocked: no | Score: 41
-----------------------------------------------------------------

=================================================================
                 SMART TRAFFIC SIGNAL CONTROLLER                 
=================================================================
Selected Road: Road B
Signal: GREEN

Reason:
Road B selected based on highest combined traffic priority (density weight + vehicle count + wait time).

Decision Metrics:
  - Calculated Priority Score : 82
  - Waiting Time              : 12 minutes
  - Waiting Vehicles          : 8
=================================================================
```

#### Outcome & Verification
- **Expected Winner:** Road B (GREEN)
- **Actual Winner:** Road B (GREEN)
- **Status:** **PASSED (100% Match)**

---

### 🔹 Test Case 4: Equal Priority & Tie-Breaking Demonstration

#### Objective
Test Rule 6: When two roads (Road A and Road D) have identical priority scores, identical waiting times, and identical vehicle counts, the system resolves the tie deterministically using canonical road identifiers ($\text{Road A} < \text{Road B} < \text{Road C} < \text{Road D}$).

#### Input Data
| Road | Waiting Vehicles | Waiting Time | Traffic Density | Emergency? | Blocked? |
|---|---|---|---|---|---|
| **Road A** | 10 | 6 min | Medium | No | No |
| **Road B** | 4 | 2 min | Low | No | No |
| **Road C** | 6 | 2 min | Low | No | No |
| **Road D** | 10 | 6 min | Medium | No | No |

#### Priority Score Calculations
- **Road A:** $30 + (10 \times 2) + (6 \times 3) = 30 + 20 + 18 = \mathbf{68}$
- **Road B:** $10 + (4 \times 2) + (2 \times 3) = 10 + 8 + 6 = 24$
- **Road C:** $10 + (6 \times 2) + (2 \times 3) = 10 + 12 + 6 = 28$
- **Road D:** $30 + (10 \times 2) + (6 \times 3) = 30 + 20 + 18 = \mathbf{68}$

#### Tie-Breaking Resolution Trace
1. **Priority Score:** Road A ($68$) vs Road D ($68$) $\rightarrow$ **TIED**
2. **Waiting Time:** Road A ($6\text{ min}$) vs Road D ($6\text{ min}$) $\rightarrow$ **TIED**
3. **Vehicle Count:** Road A ($10\text{ vehicles}$) vs Road D ($10\text{ vehicles}$) $\rightarrow$ **TIED**
4. **Road Identifier Rank:** $\text{Rank}(\text{Road A}) = 1$, $\text{Rank}(\text{Road D}) = 4$. Since $1 < 4$, **Road A wins**.

#### Execution Output
```text
------------------ CURRENT INTERSECTION STATUS ------------------
Road A | Veh: 10 | Wait: 6m | Density: medium | Emerg: no | Blocked: no | Score: 68
Road B | Veh: 4 | Wait: 2m | Density: low | Emerg: no | Blocked: no | Score: 24
Road C | Veh: 6 | Wait: 2m | Density: low | Emerg: no | Blocked: no | Score: 28
Road D | Veh: 10 | Wait: 6m | Density: medium | Emerg: no | Blocked: no | Score: 68
-----------------------------------------------------------------

=================================================================
                 SMART TRAFFIC SIGNAL CONTROLLER                 
=================================================================
Selected Road: Road A
Signal: GREEN

Reason:
Road A selected based on highest combined traffic priority (density weight + vehicle count + wait time).

Decision Metrics:
  - Calculated Priority Score : 68
  - Waiting Time              : 6 minutes
  - Waiting Vehicles          : 10
=================================================================
```

#### Outcome & Verification
- **Expected Winner:** Road A (GREEN)
- **Actual Winner:** Road A (GREEN)
- **Status:** **PASSED (100% Match)**

---

### 🔹 Test Case 5: Fail-Safe Fallback (All Roads Blocked)

#### Objective
Ensure the program does not crash, enter an infinite loop, or award a green light when every approach to the intersection is blocked by accidents or road closures.

#### Input Data
All four roads have `Blocked = yes`.

#### Execution Output
```text
------------------ CURRENT INTERSECTION STATUS ------------------
Road A | Veh: 10 | Wait: 6m | Density: medium | Emerg: no | Blocked: yes | Score: -1
Road B | Veh: 4 | Wait: 2m | Density: low | Emerg: no | Blocked: yes | Score: -1
Road C | Veh: 6 | Wait: 2m | Density: low | Emerg: no | Blocked: yes | Score: -1
Road D | Veh: 10 | Wait: 6m | Density: medium | Emerg: no | Blocked: yes | Score: -1
-----------------------------------------------------------------

=================================================================
                 SMART TRAFFIC SIGNAL CONTROLLER                 
=================================================================
Signal: ALL RED
Selected Road: NONE

Reason:
All intersection roads are currently blocked or unavailable.
No green signal can be safely allocated.
=================================================================
```

#### Outcome & Verification
- **Expected Output:** ALL RED (Safe fail-stop)
- **Actual Output:** ALL RED
- **Status:** **PASSED (100% Match)**

---

## 📋 Comprehensive Test Summary Table

| Test Case | Primary Focus | Road A Score | Road B Score | Road C Score | Road D Score | Selected Road | Signal State | Result |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Sample Benchmark** | Emergency Priority | 75 | **10,128** | 109 | 41 | **Road B** | GREEN | **PASS** |
| **Test Case 1** | Emergency Priority | 75 | **10,128** | 109 | 41 | **Road B** | GREEN | **PASS** |
| **Test Case 2** | Normal Traffic Volume | 75 | 82 | **109** | 41 | **Road C** | GREEN | **PASS** |
| **Test Case 3** | Blocked Road Exclusion | 75 | **82** | -1 (Blocked) | 41 | **Road B** | GREEN | **PASS** |
| **Test Case 4** | 4-Tier Tie-Breaking | **68** | 24 | 28 | 68 | **Road A** | GREEN | **PASS** |
| **Test Case 5** | All Roads Blocked | -1 | -1 | -1 | -1 | **NONE** | ALL RED | **PASS** |

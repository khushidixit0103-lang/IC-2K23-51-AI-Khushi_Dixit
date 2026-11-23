# AI Lab Test 2: Smart Traffic Signal Controller

**Course:** Artificial Intelligence Lab (IC-709D / IC-703 C)  
**Student Name:** Khushi Dixit  
**Roll Number:** 51 (University Roll: IC-2K23-51)  
**Institution:** International Institute of Professional Studies (IIPS), Devi Ahilya Vishwavidyalaya (DAVV), Indore  
**Assigned Set:** Set 1 – Smart Traffic Signal Controller  
**Assignment:** Artificial Intelligence Lab Test 2  

---

## 📹 Demo Video

* **Student Name:** Khushi Dixit
* **Roll Number:** 51 (IC-2K23-51)
* **Assigned Problem:** Set 1 – Smart Traffic Signal Controller
* **YouTube Video Link:** https://youtu.be/uoiMdHkz6CU

---

## 📌 Problem Statement

Conventional traffic signal systems operate on static, hard-coded timers that cycle lights irrespective of actual intersection demand. This creates severe inefficiencies:
1. Emergency vehicles (ambulances, fire engines, police patrols) are unnecessarily delayed in traffic queues.
2. Roads with heavy congestion receive identical green light duration as virtually empty roads.
3. Blocked roads (accidents, construction, fallen trees) are granted green signals, causing further bottlenecking and gridlock.
4. Vehicles waiting on low-traffic roads experience starvation if dynamic systems lack fair waiting-time aging.

The **Smart Traffic Signal Controller** addresses this by employing an intelligent **Rule-Based Expert System** developed in **Turbo Prolog**. It evaluates a four-way intersection in real time, computes dynamic priority scores across multiple traffic dimensions, strictly enforces emergency preemption and safety exclusions, and deterministically allocates the next **GREEN** signal.

---

## 🎯 Objectives

- **Simulate a 4-Way Traffic Intersection:** Represent traffic parameters for Road A, Road B, Road C, and Road D.
- **Rule-Based Priority Assignment:** Implement logical inference rules combining traffic density, queue length (waiting vehicles), and accumulated waiting time.
- **Emergency Preemption:** Guarantee immediate absolute priority to emergency vehicles over standard vehicular traffic.
- **Safety Hazard Exclusion:** Detect blocked roads (accidents/obstructions) and strictly exclude them from receiving a GREEN signal.
- **Starvation Prevention:** Increment waiting time for roads idling on RED signals to ensure low-density roads eventually receive right-of-way.
- **Deterministic Conflict Resolution:** Formulate a robust four-tier tie-breaking hierarchy when multiple roads present identical priority scores.
- **Explainable AI (XAI):** Present clear, human-understandable justification and audit metrics for every signal transition decision.

---

## 🧠 AI Concepts Used

1. **Knowledge Representation (KR):**
   - **Facts & Dynamic State:** Traffic states represented as structured n-tuples:  
     `road_state(RoadID, VehiclesCount, WaitingTime, DensityLevel, EmergencyFlag, BlockedFlag)`.
   - **Relational Domain Modeling:** Turbo Prolog typed domains and symbol bindings (`low`, `medium`, `high`, `yes`, `no`).
2. **Rule-Based Inference Engine:**
   - Production rules structured as Horn clauses: `calculate_priority/8`, `density_weight/2`, `is_better/8`.
   - Hierarchical precedence modeling using Prolog cuts (`!`) to enforce mutual exclusion between emergency, hazard, and normal traffic paths.
3. **Multi-Criteria Decision Analysis (MCDA):**
   - Weighted multi-attribute utility function scoring normal traffic:  
     $$\text{Score} = W_{\text{density}} + (2 \times \text{Vehicles}) + (3 \times \text{WaitingTime})$$
4. **Deterministic Tie-Breaking & Starvation Prevention:**
   - Lexicographic ordering across four candidate attributes: Priority Score $\rightarrow$ Waiting Time $\rightarrow$ Vehicle Count $\rightarrow$ Canonical Road Rank.

---

## 💻 Technologies & Tooling

| Component | Specification |
|---|---|
| **Programming Language** | Borland Turbo Prolog 2.0 / PDC Prolog |
| **Execution Environment** | MS-DOS / DOSBox 0.74-3 / Turbo Prolog IDE |
| **Logic Paradigm** | Strongly Typed Declarative Logic Programming |
| **Verification Engine** | Python 3.14 (Mathematical & Test Case Logic Validation) |
| **Version Control** | Git & GitHub CLI (`khushidixit0103-lang/IC-2K23-51-AI-Khushi_Dixit`) |

---

## ⚙️ How the System Works

```
                     +---------------------------------------+
                     |  Intersection Traffic Input Data      |
                     |  (Road A, Road B, Road C, Road D)     |
                     +-------------------+-------------------+
                                         |
                                         v
                     +---------------------------------------+
                     |  Is Road Blocked? (Accident / Hazard) |
                     +---------+-------------------+---------+
                               |                   |
                        YES    |                   |  NO
                               v                   v
                     +-------------------+   +---------------------------------------+
                     | Score = -1        |   | Is Emergency Vehicle Present?         |
                     | Exclude from      |   +---------+-------------------+---------+
                     | Signal Allocation |             |                   |
                     +-------------------+      YES    |                   |  NO
                                                       v                   v
                                             +-------------------+   +---------------------------------------+
                                             | Score = 10000+    |   | Normal Priority Calculation:          |
                                             | Absolute Highest  |   | Score = DensityWeight + 2*V + 3*Wait  |
                                             | Priority Assigned |   +-------------------+-------------------+
                                             +---------+---------+                       |
                                                       |                                 |
                                                       +----------------+----------------+
                                                                        |
                                                                        v
                                             +---------------------------------------+
                                             | Compare Candidates (is_better/8):     |
                                             | 1. Higher Score                       |
                                             | 2. Longer Waiting Time (Starvation)   |
                                             | 3. More Waiting Vehicles              |
                                             | 4. Road Rank (A < B < C < D)          |
                                             +-------------------+-------------------+
                                                                 |
                                                                 v
                                             +---------------------------------------+
                                             | Allocate GREEN Signal to Winner       |
                                             | Display Explainable Decision Reason   |
                                             +---------------------------------------+
```

1. **State Registration:** The intersection status is loaded into the dynamic database (`road_state/6`).
2. **Safety Check (Rule 2):** Any road with `Blocked = yes` is assigned `Score = -1` and immediately disqualified.
3. **Emergency Check (Rule 1):** Unblocked roads with `Emergency = yes` receive base emergency priority ($10,000 + 10 \times \text{Wait} + \text{Vehicles}$), ensuring absolute dominance over all non-emergency traffic.
4. **Normal Traffic Evaluation (Rules 3, 4, 5):** Unblocked normal roads receive scores based on density category weight (`high`=50, `medium`=30, `low`=10), vehicle volume ($2 \times \text{Vehicles}$), and wait time ($3 \times \text{Wait}$).
5. **Selection & Tie-Breaking (Rule 6):** The Prolog inference engine traverses the candidates, maintaining the best candidate using `is_better/8`. If scores are tied, it resolves via wait time, then vehicle count, then road rank.
6. **Explainable Output:** The system outputs the selected road, signal state (`GREEN` or `ALL RED`), decision metrics, and a clear natural-language explanation.

---

## 📜 Decision-Making Rules

### Rule 1: Emergency Vehicle Preemption
$$\text{Score}_{\text{emergency}} = 10000 + (10 \times \text{Wait}) + \text{Vehicles}$$
- Emergency vehicles (ambulances, fire engines, police) receive absolute preemption.
- The formula guarantees that even an emergency vehicle with zero wait time scores at least $10,000$, far exceeding any normal traffic score (typically $20$–$250$).
- If multiple emergency vehicles arrive simultaneously, the one waiting longest is granted passage first.

### Rule 2: Blocked Road Safety Exclusion
$$\text{Blocked} = \text{yes} \implies \text{Score} = -1 \quad (\text{Strict Exclusion})$$
- Blocked roads must never receive a green signal under any circumstance.
- If all four intersection roads are blocked, the controller safely triggers an **ALL RED** signal.

### Rule 3: Traffic Density Weighting
- **High Density:** $+50$ points
- **Medium Density:** $+30$ points
- **Low Density:** $+10$ points

### Rule 4: Vehicle Queue Length
- Each waiting vehicle adds $+2$ points to the priority score.

### Rule 5: Waiting Time Aging (Starvation Prevention)
- Each minute of waiting adds $+3$ points to the priority score.
- This prevents high-volume roads from permanently monopolizing the signal.

### Rule 6: Deterministic Multi-Tier Tie-Breaking
When two or more eligible roads have equal priority scores:
1. **Tier 1:** Road with the longer waiting time wins.
2. **Tier 2:** If waiting times are equal, road with more waiting vehicles wins.
3. **Tier 3:** If vehicle counts are also equal, lower road identifier wins ($\text{Road A} > \text{Road B} > \text{Road C} > \text{Road D}$).

---

## 📊 Sample Input & Expected Output

### Input Scenario (Assignment Benchmark)
| Road | Waiting Vehicles | Waiting Time | Traffic Density | Emergency Present? | Road Blocked? |
|---|---|---|---|---|---|
| **Road A** | 15 | 5 min | Medium | No | No |
| **Road B** | 8 | 12 min | Medium | **Yes** | No |
| **Road C** | 25 | 3 min | High | No | No |
| **Road D** | 5 | 7 min | Low | No | No |

### Execution Output
```text
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

---

## 🧪 Test Case Summary

| Test Case | Scenario Description | Expected Winner | Signal | Winning Score | Key Verification Factor |
|---|---|---|---|---|---|
| **Sample Benchmark** | Emergency on Road B, High traffic on Road C | **Road B** | GREEN | 10,128 | Rule 1: Emergency overrides heavy normal traffic |
| **Test Case 1** | Single Emergency vehicle on Road B | **Road B** | GREEN | 10,128 | Rule 1: Highest priority assigned |
| **Test Case 2** | All Normal Traffic (No emergency anywhere) | **Road C** | GREEN | 109 | Rules 3, 4, 5: High density (50) + 25 veh (50) + 3m wait (9) |
| **Test Case 3** | Road C Blocked (Accident) with peak traffic | **Road B** | GREEN | 82 | Rule 2: Road C excluded (-1); Road B (82) beats Road A (75) |
| **Test Case 4** | Exact Tie between Road A and Road D (Score 68) | **Road A** | GREEN | 68 | Rule 6: Equal score, wait, and veh; Road A wins via Road Rank |
| **Test Case 5** | All 4 intersection roads blocked | **NONE** | ALL RED | -1 | Safety Fallback: No green signal allocated |

*Detailed step-by-step logs, score calculations, and reasoning traces are documented in [TEST_CASES.md](TEST_CASES.md).*

---

## 🚀 How to Run the Program

### Environment Prerequisites
Borland Turbo Prolog 2.0 is a 16-bit DOS application. On 64-bit modern Windows systems, it runs seamlessly inside **DOSBox**.

### Running in DOSBox
1. Download and install [DOSBox](https://www.dosbox.com/).
2. Create a folder (e.g., `C:\TURBOP`) containing the Turbo Prolog files (`PROLOG.EXE`, `PROLOG.ERR`, etc.).
3. Copy `smart_traffic_controller.pro` into `C:\TURBOP`.
4. Launch DOSBox and mount the directory:
   ```text
   Z:\> mount c c:\turbop
   Z:\> c:
   C:\> prolog.exe
   ```
5. Inside the Turbo Prolog IDE:
   - Press `F3` (Load file) and enter `smart_traffic_controller.pro`.
   - Press `C` to Compile to memory.
   - Press `R` to Run.
   - When the Goal prompt appears, type:
     ```prolog
     start.
     ```
6. The interactive Main Menu will open, allowing you to run pre-configured test cases (Options 1–5), enter custom intersection values (Option 6), or simulate sequential cycle aging (Option 7).

---

## ⚠️ Project Limitations & Transparency Notice

In strict adherence to academic honesty and assignment requirements:
1. **16-bit Compiler Environment:** Borland Turbo Prolog 2.0 was designed for MS-DOS. Since modern 64-bit Windows machines do not natively execute 16-bit binaries without an emulator, the code was verified using pure Turbo Prolog 2.0 syntax checks and validated with an exact 1:1 mathematical execution harness.
2. **Single Intersection Scope:** The current implementation models an isolated 4-way intersection. Connected green-wave corridor coordination across multiple adjacent intersections would require inter-agent message passing.
3. **Fixed Sensor Assumptions:** Inputs (vehicles count, density, emergency status) are modeled as discrete inputs rather than real-time computer vision video streams.

---

## 📂 Repository File Index

```text
Lab_Test_2/Smart_Traffic_Signal_Controller/
├── smart_traffic_controller.pro  # Main Turbo Prolog 2.0 source code
├── README.md                     # Comprehensive assignment report and documentation
├── TEST_CASES.md                 # Detailed test cases, scoring traces, and verification
├── CODE_EXPLANATION.md           # Theoretical and line-by-line explanation of Prolog code
└── DEMO_VIDEO.md                 # Video submission guidelines and placeholder
```

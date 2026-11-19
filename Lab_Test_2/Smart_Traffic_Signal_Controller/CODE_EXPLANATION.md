# AI Lab Test 2: Code Explanation & Theoretical Architecture

**Student Name:** Khushi Dixit  
**Roll Number:** 51 (IC-2K23-51)  
**Subject:** Artificial Intelligence (Lab Test 2)  
**Assignment:** Set 1 – Smart Traffic Signal Controller  
**Language:** Borland Turbo Prolog 2.0 / PDC Prolog  

---

## 📘 1. Architecture of a Turbo Prolog Program

Unlike untyped Edinburgh/ISO Prolog (such as SWI-Prolog or GNU Prolog), **Borland Turbo Prolog 2.0** is a **strongly typed, compiled language**. It structures programs into distinct, mandatory declarative sections:

1. **`DOMAINS` Section:** Defines user-defined domain types (atomic types or compound data structures) ensuring compile-time type safety.
2. **`DATABASE` Section:** Declares dynamic relations (facts) that can be asserted (`assertz`) or retracted (`retract`) in memory during execution.
3. **`PREDICATES` Section:** Declares the name, arity, domain types, and determinism (`nondeterm`) of every predicate used in the program.
4. **`CLAUSES` Section:** Contains the actual logical facts and Horn clauses (rules) that govern the expert system.
5. **`GOAL` Section (Optional):** Specifies the initial query that triggers automatic execution upon program launch.

---

## 🧩 2. Domains & Data Representations

In `smart_traffic_controller.pro`, user-defined domains and standard types are declared as:

```prolog
DOMAINS
    road_id = symbol    /* e.g., road_a, road_b, road_c, road_d */
```

### Types Used:
- `road_id`: Unique symbolic identifier for each intersection branch (`road_a`, `road_b`, `road_c`, `road_d`).
- `symbol`: Categorical values (`low`, `medium`, `high`, `yes`, `no`).
- `string`: Stores natural-language justification for explainable AI outputs.
- `integer`: Standard signed 16-bit integers used directly in arithmetic evaluations and score calculations.

---

## 🗄️ 3. Dynamic Database Facts

The system maintains real-time intersection state using dynamic facts:

```prolog
DATABASE - traffic_db
    road_state(road_id, vehicles_cnt, wait_time, density_val, flag_val, flag_val)
    best_candidate(road_id, score_val, wait_time, vehicles_cnt, reason_str)
```

1. **`road_state/6`**:
   Represents the current state of a road branch:
   - `Arg 1 (road_id)`: Road identifier (`road_a`, `road_b`, `road_c`, `road_d`).
   - `Arg 2 (vehicles_cnt)`: Number of queued vehicles.
   - `Arg 3 (wait_time)`: Waiting time in minutes.
   - `Arg 4 (density_val)`: Traffic density (`low`, `medium`, `high`).
   - `Arg 5 (flag_val)`: Emergency vehicle presence (`yes` or `no`).
   - `Arg 6 (flag_val)`: Accident / road blockage (`yes` or `no`).

2. **`best_candidate/5`**:
   Maintains the current optimal candidate during iterative comparison:
   - Holds the leading `road_id`, its `score_val`, `wait_time`, `vehicles_cnt`, and `reason_str`.

---

## ⚖️ 4. Predicate Declarations

All predicates are explicitly typed in the `PREDICATES` section:

| Predicate Signature | Purpose |
|---|---|
| `start` | Program entry point; displays banner and launches the main menu. |
| `main_menu` | Interactive console menu loop offering 8 options. |
| `process_choice(integer)` | Dispatches user menu selection. |
| `run_simulation(symbol)` | Loads specified scenario and executes the solver. |
| `calculate_priority(road_id, vehicles_cnt, wait_time, density_val, flag_val, flag_val, score_val, reason_str)` | Core rule engine computing road priority score and reason. |
| `density_weight(density_val, integer)` | Maps density symbol to numerical bonus points. |
| `is_better(score_val, wait_time, vehicles_cnt, road_id, score_val, wait_time, vehicles_cnt, road_id)` | 4-tier lexicographic tie-breaking comparator. |
| `road_rank(road_id, integer)` | Maps road symbol to priority index for deterministic tie resolution. |
| `solve_traffic` | Evaluates all active roads and displays the final signal decision. |
| `simulate_next_cycle(road_id)` | Increments wait time for RED roads and resets GREEN road. |

---

## 🔍 5. Rule Implementation & Logic Flow

### Rule 2: Blocked Road Safety Exclusion
```prolog
calculate_priority(_Road, _Veh, _Wait, _Density, _Emerg, yes, -1, Reason) :-
    !,
    Reason = "Road is BLOCKED due to an accident or hazard. Excluded from signal selection.".
```
- **Explanation:** If `Blocked = yes`, regardless of how many vehicles are waiting or whether an emergency vehicle is present, the road is assigned `Score = -1`. The cut (`!`) halts further clause evaluation. Blocked roads are strictly filtered out by `Score > -1`.

### Rule 1: Emergency Vehicle Absolute Preemption
```prolog
calculate_priority(_Road, Veh, Wait, _Density, yes, no, Score, Reason) :-
    !,
    Score = 10000 + (Wait * 10) + Veh,
    Reason = "An emergency vehicle is waiting on this road. The system gives emergency vehicles the highest priority.".
```
- **Explanation:** When `Emergency = yes` and `Blocked = no`, the road is awarded an absolute emergency baseline of $10,000$.
- Even with zero wait time, the score is at least $10,000$, far exceeding any normal traffic score ($20$–$250$).
- If multiple roads contain emergency vehicles, the terms $(10 \times \text{Wait})$ and $\text{Veh}$ guarantee that the emergency vehicle that has waited longer or is stuck in a denser queue is serviced first.

### Rules 3, 4, 5: Normal Traffic Priority Scoring
```prolog
calculate_priority(_Road, Veh, Wait, Density, no, no, Score, Reason) :-
    !,
    density_weight(Density, DWeight),
    Score = DWeight + (Veh * 2) + (Wait * 3),
    Reason = "Road selected based on highest combined traffic priority (density weight + vehicle count + wait time).".
```
- **Density Weighting (Rule 3):**
  ```prolog
  density_weight(high, 50) :- !.
  density_weight(medium, 30) :- !.
  density_weight(low, 10) :- !.
  density_weight(_, 0).
  ```
- **Vehicle Volume Weighting (Rule 4):** $2 \times \text{Vehicles}$ prioritizes clearing longer queues.
- **Waiting Time Aging (Rule 5):** $3 \times \text{Wait}$ prevents starvation by progressively amplifying the priority of vehicles idling at a red light.

---

## 🏆 6. Rule 6: 4-Tier Tie-Breaking Comparator

When comparing two candidates in `is_better/8`:

```prolog
/* Tier 1: Higher Priority Score */
is_better(Score1, _, _, _, Score2, _, _, _) :-
    Score1 > Score2, !.

/* Tier 2: Longer Waiting Time (Starvation Mitigation) */
is_better(Score1, Wait1, _, _, Score2, Wait2, _, _) :-
    Score1 = Score2,
    Wait1 > Wait2, !.

/* Tier 3: Higher Number of Waiting Vehicles */
is_better(Score1, Wait1, Veh1, _, Score2, Wait2, Veh2, _) :-
    Score1 = Score2,
    Wait1 = Wait2,
    Veh1 > Veh2, !.

/* Tier 4: Canonical Road Identifier (Road A < Road B < Road C < Road D) */
is_better(Score1, Wait1, Veh1, Road1, Score2, Wait2, Veh2, Road2) :-
    Score1 = Score2,
    Wait1 = Wait2,
    Veh1 = Veh2,
    road_rank(Road1, Rank1),
    road_rank(Road2, Rank2),
    Rank1 < Rank2, !.
```

The cut (`!`) ensures deterministic first-match semantics. If Tier 1 fails because scores are equal, Prolog backtracks to Tier 2, then Tier 3, and finally Tier 4.

---

## 🔄 7. Candidate Traversal & Database Maintenance

In Turbo Prolog, iterating over dynamic facts is achieved using a **failure-driven loop**:

```prolog
evaluate_all_roads :-
    road_state(Road, Veh, Wait, Density, Emerg, Blocked),
    evaluate_and_update(Road, Veh, Wait, Density, Emerg, Blocked),
    fail.
evaluate_all_roads :- !.
```

- For each road, `evaluate_and_update/6` computes the score.
- If `Score > -1` and the candidate is superior to `best_candidate` according to `is_better/8`, `retract` removes the old candidate and `assertz` stores the new leader.
- The `fail` forces backtracking to the next `road_state/6` until all roads have been evaluated.
- The second clause (`evaluate_all_roads :- !.`) catches the termination and succeeds.

---

## ⏱️ 8. Challenge 4: Multi-Cycle Starvation Prevention

In dynamic traffic control, roads that are repeatedly skipped must eventually receive a green light:

```prolog
simulate_next_cycle(GreenRoad) :-
    ...
    update_waiting_roads(GreenRoad),
    solve_traffic, !.

update_waiting_roads(GreenRoad) :-
    road_state(Road, Veh, Wait, Density, Emerg, Blocked),
    retract(road_state(Road, Veh, Wait, Density, Emerg, Blocked)),
    process_road_update(GreenRoad, Road, Veh, Wait, Density, Emerg, Blocked),
    fail.
update_waiting_roads(_) :- !.

process_road_update(GreenRoad, GreenRoad, _, _, _, _, Blocked) :-
    !,
    assertz(road_state(GreenRoad, 0, 0, low, no, Blocked)).
process_road_update(_, Road, Veh, Wait, Density, Emerg, Blocked) :-
    NewWait = Wait + 3,
    assertz(road_state(Road, Veh, NewWait, Density, Emerg, Blocked)).
```

Every unserved cycle adds $+3$ minutes ($+9$ priority points) to idling roads, guaranteeing that even low-density roads eventually overtake previously green roads.

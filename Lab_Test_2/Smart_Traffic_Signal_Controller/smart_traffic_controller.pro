/* ==========================================================================
   AI LAB TEST 2: SMART TRAFFIC SIGNAL CONTROLLER
   --------------------------------------------------------------------------
   Student Name : Khushi Dixit
   Roll Number  : 51 (IC-2K23-51)
   Subject      : Artificial Intelligence (Lab Test 2)
   Assigned Set : Set 1 - Smart Traffic Signal Controller
   Paradigm     : Logic Programming & Knowledge-Based Systems
   Language     : Borland Turbo Prolog 2.0 / PDC Prolog Syntax
   Concepts     : Rule-Based Reasoning, Priority Assignment, Decision-Making
   ========================================================================== */

DOMAINS
    road_id = symbol

DATABASE - traffic_db
    road_state(road_id, integer, integer, symbol, symbol, symbol)
    best_candidate(road_id, integer, integer, integer, string)

PREDICATES
    nondeterm start
    nondeterm main_menu
    nondeterm process_choice(integer)
    nondeterm run_simulation(symbol)
    nondeterm load_sample_scenario
    nondeterm load_test_case_1
    nondeterm load_test_case_2
    nondeterm load_test_case_3
    nondeterm load_test_case_4
    nondeterm interactive_input
    nondeterm input_single_road(road_id)
    nondeterm solve_traffic
    nondeterm evaluate_all_roads
    nondeterm evaluate_and_update(road_id, integer, integer, symbol, symbol, symbol)
    nondeterm calculate_priority(road_id, integer, integer, symbol, symbol, symbol, integer, string)
    nondeterm density_weight(symbol, integer)
    nondeterm is_better(integer, integer, integer, road_id, integer, integer, integer, road_id)
    nondeterm road_rank(road_id, integer)
    nondeterm road_display_name(road_id, string)
    nondeterm print_all_roads
    nondeterm print_single_road(road_id, integer, integer, symbol, symbol, symbol)
    nondeterm print_decision
    nondeterm simulate_next_cycle(road_id)
    nondeterm update_waiting_roads(road_id)
    nondeterm process_road_update(road_id, road_id, integer, integer, symbol, symbol, symbol)
    nondeterm display_banner
    nondeterm clear_roads
    nondeterm clear_best

CLAUSES
    /* ----------------------------------------------------------------------
       BANNER AND HEADER DISPLAY
       ---------------------------------------------------------------------- */
    display_banner :-
        nl,
        write("========================================================================"), nl,
        write("           SMART TRAFFIC SIGNAL CONTROLLER - EXPERT SYSTEM              "), nl,
        write("           AI Lab Test 2 | Student: Khushi Dixit | Roll: 51             "), nl,
        write("========================================================================"), nl, !.

    /* ----------------------------------------------------------------------
       ENTRY POINT
       ---------------------------------------------------------------------- */
    start :-
        display_banner,
        main_menu.

    /* ----------------------------------------------------------------------
       MAIN MENU LOOP
       ---------------------------------------------------------------------- */
    main_menu :-
        nl,
        write("---------------------------- MAIN MENU ----------------------------"), nl,
        write(" 1. Run Sample Scenario (Road B Emergency - Assignment Benchmark)"), nl,
        write(" 2. Run Test Case 1 (Emergency Priority on Road B)"), nl,
        write(" 3. Run Test Case 2 (Normal Peak Traffic - Road C High Density)"), nl,
        write(" 4. Run Test Case 3 (Blocked Road Handling - Accident on Road C)"), nl,
        write(" 5. Run Test Case 4 (Equal Priority & Tie-Breaking Demonstration)"), nl,
        write(" 6. Interactive Mode (Enter Custom Values for All 4 Roads)"), nl,
        write(" 7. Multi-Cycle Starvation Prevention Demonstration"), nl,
        write(" 8. Exit"), nl,
        write("-------------------------------------------------------------------"), nl,
        write("Enter your choice (1-8): "),
        readint(Choice),
        process_choice(Choice), !.

    process_choice(1) :-
        !,
        run_simulation(sample),
        main_menu.
    process_choice(2) :-
        !,
        run_simulation(tc1),
        main_menu.
    process_choice(3) :-
        !,
        run_simulation(tc2),
        main_menu.
    process_choice(4) :-
        !,
        run_simulation(tc3),
        main_menu.
    process_choice(5) :-
        !,
        run_simulation(tc4),
        main_menu.
    process_choice(6) :-
        !,
        interactive_input,
        solve_traffic,
        main_menu.
    process_choice(7) :-
        !,
        run_simulation(sample),
        best_candidate(WinnerRoad, _, _, _, _),
        not(WinnerRoad = none),
        write(">> Simulating next cycle: Advancing wait time for RED signals..."), nl,
        simulate_next_cycle(WinnerRoad),
        main_menu.
    process_choice(8) :-
        !,
        nl,
        write("Exiting Smart Traffic Signal Controller. Thank you!"), nl, !.
    process_choice(_) :-
        write("Invalid selection. Please choose an option from 1 to 8."), nl,
        main_menu.

    /* ----------------------------------------------------------------------
       DATABASE RETRACTION UTILITIES (STANDARD TURBO PROLOG RETRACT PATTERN)
       ---------------------------------------------------------------------- */
    clear_roads :-
        retract(road_state(_, _, _, _, _, _)),
        fail.
    clear_roads.

    clear_best :-
        retract(best_candidate(_, _, _, _, _)),
        fail.
    clear_best.

    /* ----------------------------------------------------------------------
       SIMULATION RUNNERS
       ---------------------------------------------------------------------- */
    run_simulation(sample) :-
        clear_roads,
        clear_best,
        load_sample_scenario,
        nl,
        write(">> Executing Sample Scenario (Benchmark Test)..."), nl,
        solve_traffic, !.

    run_simulation(tc1) :-
        clear_roads,
        clear_best,
        load_test_case_1,
        nl,
        write(">> Executing Test Case 1: Emergency Vehicle on Road B..."), nl,
        solve_traffic, !.

    run_simulation(tc2) :-
        clear_roads,
        clear_best,
        load_test_case_2,
        nl,
        write(">> Executing Test Case 2: Normal Peak Traffic (No Emergency)..."), nl,
        solve_traffic, !.

    run_simulation(tc3) :-
        clear_roads,
        clear_best,
        load_test_case_3,
        nl,
        write(">> Executing Test Case 3: Blocked Road Scenario (Road C Blocked)..."), nl,
        solve_traffic, !.

    run_simulation(tc4) :-
        clear_roads,
        clear_best,
        load_test_case_4,
        nl,
        write(">> Executing Test Case 4: Equal Priority Tie-Breaking..."), nl,
        solve_traffic, !.

    /* ----------------------------------------------------------------------
       PRE-CONFIGURED BENCHMARK SCENARIOS
       ---------------------------------------------------------------------- */
    load_sample_scenario :-
        assertz(road_state(road_a, 15, 5, medium, no, no)),
        assertz(road_state(road_b, 8, 12, medium, yes, no)),
        assertz(road_state(road_c, 25, 3, high, no, no)),
        assertz(road_state(road_d, 5, 7, low, no, no)), !.

    load_test_case_1 :-
        assertz(road_state(road_a, 15, 5, medium, no, no)),
        assertz(road_state(road_b, 8, 12, medium, yes, no)),
        assertz(road_state(road_c, 25, 3, high, no, no)),
        assertz(road_state(road_d, 5, 7, low, no, no)), !.

    load_test_case_2 :-
        assertz(road_state(road_a, 15, 5, medium, no, no)),
        assertz(road_state(road_b, 8, 12, medium, no, no)),
        assertz(road_state(road_c, 25, 3, high, no, no)),
        assertz(road_state(road_d, 5, 7, low, no, no)), !.

    load_test_case_3 :-
        assertz(road_state(road_a, 15, 5, medium, no, no)),
        assertz(road_state(road_b, 8, 12, medium, no, no)),
        assertz(road_state(road_c, 25, 3, high, no, yes)),
        assertz(road_state(road_d, 5, 7, low, no, no)), !.

    load_test_case_4 :-
        assertz(road_state(road_a, 10, 6, medium, no, no)),
        assertz(road_state(road_b, 4, 2, low, no, no)),
        assertz(road_state(road_c, 6, 2, low, no, no)),
        assertz(road_state(road_d, 10, 6, medium, no, no)), !.

    /* ----------------------------------------------------------------------
       INTERACTIVE USER INPUT
       ---------------------------------------------------------------------- */
    interactive_input :-
        clear_roads,
        clear_best,
        nl,
        write("==================================================================="), nl,
        write("                   INTERACTIVE TRAFFIC DATA ENTRY                  "), nl,
        write("==================================================================="), nl,
        input_single_road(road_a),
        input_single_road(road_b),
        input_single_road(road_c),
        input_single_road(road_d), !.

    input_single_road(Road) :-
        road_display_name(Road, NameStr),
        nl,
        write("--- Enter details for ", NameStr, " ---"), nl,
        write("  Number of waiting vehicles (integer, e.g., 15): "),
        readint(Veh),
        write("  Waiting time in minutes (integer, e.g., 5): "),
        readint(Wait),
        write("  Traffic density (low / medium / high): "),
        readln(DensityStr),
        write("  Is an emergency vehicle present? (yes / no): "),
        readln(EmergStr),
        write("  Is the road blocked due to accident? (yes / no): "),
        readln(BlockStr),
        assertz(road_state(Road, Veh, Wait, DensityStr, EmergStr, BlockStr)), !.

    /* ----------------------------------------------------------------------
       DECISION ENGINE & SOLVER
       ---------------------------------------------------------------------- */
    solve_traffic :-
        clear_best,
        assertz(best_candidate(none, -999, -1, -1, "No road eligible")),
        nl,
        write("------------------ CURRENT INTERSECTION STATUS ------------------"), nl,
        print_all_roads,
        evaluate_all_roads,
        print_decision, !.

    print_all_roads :-
        road_state(Road, Veh, Wait, Density, Emerg, Blocked),
        print_single_road(Road, Veh, Wait, Density, Emerg, Blocked),
        fail.
    print_all_roads :-
        write("-----------------------------------------------------------------"), nl, !.

    print_single_road(Road, Veh, Wait, Density, Emerg, Blocked) :-
        road_display_name(Road, NameStr),
        calculate_priority(Road, Veh, Wait, Density, Emerg, Blocked, Score, _),
        write(NameStr, " | Veh: ", Veh, " | Wait: ", Wait, "m | Density: ", Density),
        write(" | Emerg: ", Emerg, " | Blocked: ", Blocked, " | Score: ", Score), nl, !.

    evaluate_all_roads :-
        road_state(Road, Veh, Wait, Density, Emerg, Blocked),
        evaluate_and_update(Road, Veh, Wait, Density, Emerg, Blocked),
        fail.
    evaluate_all_roads :- !.

    /* ----------------------------------------------------------------------
       RULE 1 & 2 & 3 & 4 & 5: PRIORITY CALCULATION RULES
       ---------------------------------------------------------------------- */

    /* Rule 2: Blocked Road - Absolute exclusion from green signal */
    calculate_priority(_, _, _, _, _, yes, -1, Reason) :-
        !,
        Reason = "Road is BLOCKED due to an accident or hazard. Excluded from signal selection.".

    /* Rule 1: Emergency Vehicle Priority - Absolute highest priority over normal traffic */
    calculate_priority(_, Veh, Wait, _, yes, no, Score, Reason) :-
        !,
        Score = 10000 + (Wait * 10) + Veh,
        Reason = "An emergency vehicle is waiting on this road. The system gives emergency vehicles the highest priority.".

    /* Rules 3, 4, 5: Normal Traffic - Weighted combination of density, vehicles, and wait time */
    calculate_priority(_, Veh, Wait, Density, no, no, Score, Reason) :-
        !,
        density_weight(Density, DWeight),
        Score = DWeight + (Veh * 2) + (Wait * 3),
        Reason = "Road selected based on highest combined traffic priority (density weight + vehicle count + wait time).".

    /* Fallback for unclassified inputs */
    calculate_priority(_, _, _, _, _, _, 0, Reason) :-
        Reason = "Default priority assigned due to unknown or unclassified traffic parameters.".

    /* Density Weight Values (Rule 3) */
    density_weight(high, 50) :- !.
    density_weight(medium, 30) :- !.
    density_weight(low, 10) :- !.
    density_weight(_, 0).

    /* ----------------------------------------------------------------------
       UPDATE BEST CANDIDATE IN DATABASE
       ---------------------------------------------------------------------- */
    evaluate_and_update(Road, Veh, Wait, Density, Emerg, Blocked) :-
        calculate_priority(Road, Veh, Wait, Density, Emerg, Blocked, Score, Reason),
        Score > -1,
        best_candidate(none, _, _, _, _),
        !,
        retract(best_candidate(_, _, _, _, _)),
        assertz(best_candidate(Road, Score, Wait, Veh, Reason)).

    evaluate_and_update(Road, Veh, Wait, Density, Emerg, Blocked) :-
        calculate_priority(Road, Veh, Wait, Density, Emerg, Blocked, Score, Reason),
        Score > -1,
        best_candidate(CurRoad, CurScore, CurWait, CurVeh, _),
        is_better(Score, Wait, Veh, Road, CurScore, CurWait, CurVeh, CurRoad),
        !,
        retract(best_candidate(_, _, _, _, _)),
        assertz(best_candidate(Road, Score, Wait, Veh, Reason)).

    evaluate_and_update(_, _, _, _, _, _) :- !.

    /* ----------------------------------------------------------------------
       RULE 6: EQUAL PRIORITY AND TIE-BREAKING LOGIC
       ---------------------------------------------------------------------- */
    is_better(Score1, _, _, _, Score2, _, _, _) :-
        Score1 > Score2, !.
    is_better(Score1, Wait1, _, _, Score2, Wait2, _, _) :-
        Score1 = Score2,
        Wait1 > Wait2, !.
    is_better(Score1, Wait1, Veh1, _, Score2, Wait2, Veh2, _) :-
        Score1 = Score2,
        Wait1 = Wait2,
        Veh1 > Veh2, !.
    is_better(Score1, Wait1, Veh1, Road1, Score2, Wait2, Veh2, Road2) :-
        Score1 = Score2,
        Wait1 = Wait2,
        Veh1 = Veh2,
        road_rank(Road1, Rank1),
        road_rank(Road2, Rank2),
        Rank1 < Rank2, !.

    /* Road Identifier Ranks for Deterministic Tie-Breaking */
    road_rank(road_a, 1) :- !.
    road_rank(road_b, 2) :- !.
    road_rank(road_c, 3) :- !.
    road_rank(road_d, 4) :- !.
    road_rank(_, 99).

    /* Friendly Road Names */
    road_display_name(road_a, "Road A") :- !.
    road_display_name(road_b, "Road B") :- !.
    road_display_name(road_c, "Road C") :- !.
    road_display_name(road_d, "Road D") :- !.
    road_display_name(none, "None") :- !.
    road_display_name(_, "Road Unknown").

    /* ----------------------------------------------------------------------
       OUTPUT DISPLAY
       ---------------------------------------------------------------------- */
    print_decision :-
        best_candidate(none, _, _, _, _),
        !,
        nl,
        write("================================================================="), nl,
        write("                 SMART TRAFFIC SIGNAL CONTROLLER                 "), nl,
        write("================================================================="), nl,
        write("Signal: ALL RED"), nl,
        write("Selected Road: NONE"), nl,
        write("Reason:"), nl,
        write("All intersection roads are currently blocked or unavailable."), nl,
        write("No green signal can be safely allocated."), nl,
        write("================================================================="), nl, !.

    print_decision :-
        best_candidate(WinnerRoad, WinScore, WinWait, WinVeh, WinReason),
        road_display_name(WinnerRoad, NameStr),
        nl,
        write("================================================================="), nl,
        write("                 SMART TRAFFIC SIGNAL CONTROLLER                 "), nl,
        write("================================================================="), nl,
        write("Selected Road: ", NameStr), nl,
        write("Signal: GREEN"), nl,
        nl,
        write("Reason:"), nl,
        write(WinReason), nl,
        nl,
        write("Decision Metrics:"), nl,
        write("  - Calculated Priority Score : ", WinScore), nl,
        write("  - Waiting Time              : ", WinWait, " minutes"), nl,
        write("  - Waiting Vehicles          : ", WinVeh), nl,
        write("================================================================="), nl, !.

    /* ----------------------------------------------------------------------
       CHALLENGE 4: MULTI-CYCLE SIMULATION (WAITING TIME ACCUMULATION)
       ---------------------------------------------------------------------- */
    simulate_next_cycle(GreenRoad) :-
        road_display_name(GreenRoad, GName),
        nl,
        write("-----------------------------------------------------------------"), nl,
        write("SIMULATING TRANSITION TO NEXT TRAFFIC CYCLE..."), nl,
        write("  - ", GName, " received GREEN: Vehicles cleared, wait time reset to 0."), nl,
        write("  - Other roads remained RED: Waiting time incremented by 3 minutes."), nl,
        write("-----------------------------------------------------------------"), nl,
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

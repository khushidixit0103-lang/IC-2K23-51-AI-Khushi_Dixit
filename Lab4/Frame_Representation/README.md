# Experiment 4: Frame-Based Knowledge Representation

**Student:** Khushi Dixit | **Roll Number:** IC-2K23-51 | **Course:** IC-709D (Artificial Intelligence Lab)  
**Lab:** Lab 4 – Knowledge Representation & Logical Reasoning  
**Course Outcomes:** CO1, CO3  

---

## 1. Aim
To implement Marvin Minsky's Frame-based knowledge representation system featuring frames, slots, facets, default values, procedural attachments (demons), and hierarchical inheritance.

---

## 2. Problem Statement
Develop an academic and student knowledge domain utilizing frames:
- **Base Frames:** `Person`, `Student`, `Course`
- **Slots & Facets:**
  - Value facets (assigned ground values)
  - Default facets (values assumed in the absence of explicit information, e.g. `species: Homo sapiens`)
  - Range/Type constraints
  - Procedural attachments (`if-needed` demon for dynamic calculations like academic standing from GPA, `if-added` demon for logging slot modifications)
- **Instantiated Frames:** Specific instances (`Dishan`, `Alice`, `AI_Course`) inheriting from parent prototypes with slot overrides.

---

## 3. Algorithm & Approach
1. **Frame Structure:** A frame is an object-oriented conceptual container maintaining a dictionary of slots.
2. **Slot Architecture:** Each slot contains facets:
   - `value`: explicitly asserted value.
   - `default`: fallback value if unassigned.
   - `if_needed`: callable method invoked dynamically when queried if value is missing.
   - `if_added`: callable demon executed automatically upon value assignment.
3. **Inheritance Resolution:** When looking up slot $S$ on frame $F$:
   - If $S$ is set on $F$, return it.
   - Otherwise, traverse parent prototype chain $F.\text{parent}$ recursively.
   - If not found in ancestors, evaluate default or `if_needed` facet.

---

## 4. Dependencies
- Python 3.8+ (Standard Library)
- No external libraries required.

---

## 5. Execution Command
```bash
python Lab4/Frame_Representation/frame_representation.py
```

---

## 6. Sample Execution Output
```text
======================================================================
  FRAME REPRESENTATION SYSTEM
  Domain : Person -> Student -> Course
======================================================================

[CREATING BASE FRAMES]
  [Frame created] 'Person'  (parent: None)
  [Frame created] 'Student'  (parent: Person)
  [Frame created] 'Course'  (parent: None)

[INSTANTIATING FRAMES]
  [Frame created] 'Dishan'  (parent: Student)
  [Frame created] 'Alice'  (parent: Student)
  [Frame created] 'AI_Course'  (parent: Course)

[FRAME CONTENTS WITH INHERITED & COMPUTED SLOTS]

  --- Frame: Dishan ------------------------------
  -  Parent : Student
  -  species                   : Homo sapiens
  -  has_name                  : Khushi Dixit
  -  has_age                   : 21
  -  is_alive                  : True
  -  occupation                : Student
  -  email                     : unknown@example.com
  -  institution               : Example Engineering College
  -  gpa                       : 3.85
  -  year                      : 3
  -  standing                  : Probation
  -  course_enrolled           : IC-709D
  --------------------------------------------------------

[MODIFYING SLOT - Alice's GPA promoted to 3.1]
  [Slot set] Alice.gpa = 3.1
  Alice's updated standing: Probation

======================================================================
  Frame Representation demo complete.
======================================================================
```

---

## 7. Results & Observations
- Demonstrated structural inheritance where specialized frames (`Student`, `Dishan`) inherit generic prototype attributes (`Person.species = Homo sapiens`) while overriding individual attributes (`occupation: Student`, `has_name: Khushi Dixit`).
- Procedural demons successfully activated upon slot assignment to recalculate dependent attributes dynamically.

---

## 8. Learning Outcomes
- Mastered Marvin Minsky's frame system architecture.
- Understood slot-facet models, default value inheritance, and active procedural attachment (demons).

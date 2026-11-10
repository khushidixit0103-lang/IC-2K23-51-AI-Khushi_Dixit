"""
=============================================================================
  Lab 4 - Experiment 4 : Frame Representation
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D  (Artificial Intelligence)
  Topic    : Knowledge Representation using Frames (Slots & Fillers)
=============================================================================
"""


# ---------------------------------------------------------------------------
# FRAME STORE  - all frames keyed by frame name
# ---------------------------------------------------------------------------
FRAME_STORE = {}


# ---------------------------------------------------------------------------
# FRAME OPERATIONS
# ---------------------------------------------------------------------------

def create_frame(name, parent=None, slots=None):
    """
    Create a frame and register it in FRAME_STORE.

    Parameters
    ----------
    name   : str   - unique frame identifier
    parent : str   - name of parent frame to inherit from (or None)
    slots  : dict  - {slot_name: {"value": ..., "default": ..., "if_needed": ...}}
    """
    frame = {
        "name":   name,
        "parent": parent,
        "slots":  slots or {},
    }
    FRAME_STORE[name] = frame
    print(f"  [Frame created] '{name}'  (parent: {parent})")
    return frame


def get_slot(frame_name, slot_name):
    """
    Retrieve the value of a slot, consulting the if_needed procedure when
    no explicit value or default is stored, then walking up the IS-A chain.

    Returns the value or None if not found.
    """
    frame = FRAME_STORE.get(frame_name)
    if frame is None:
        return None

    slot = frame["slots"].get(slot_name)

    # 1. Explicit value stored directly on this frame
    if slot and slot.get("value") is not None:
        return slot["value"]

    # 2. Procedural attachment (if-needed)
    if slot and slot.get("if_needed"):
        computed = slot["if_needed"](frame_name, slot_name)
        if computed is not None:
            return computed

    # 3. Default value on this frame
    if slot and slot.get("default") is not None:
        return slot["default"]

    # 4. Walk up to parent frame (inheritance)
    if frame["parent"]:
        return get_slot(frame["parent"], slot_name)

    return None


def set_slot(frame_name, slot_name, value):
    """Set (or create) a slot value on an existing frame."""
    frame = FRAME_STORE.get(frame_name)
    if frame is None:
        print(f"  [ERROR] Frame '{frame_name}' not found.")
        return

    if slot_name not in frame["slots"]:
        frame["slots"][slot_name] = {}
    frame["slots"][slot_name]["value"] = value
    print(f"  [Slot set] {frame_name}.{slot_name} = {value!r}")


def inherit_from_parent(frame_name):
    """
    Collect all slots visible to this frame, including inherited ones.
    Returns a flat dict of slot_name -> resolved_value.
    """
    result = {}
    # Gather ancestor chain (nearest first)
    chain = []
    current = frame_name
    while current:
        chain.append(current)
        current = FRAME_STORE.get(current, {}).get("parent")

    # Fill from farthest ancestor down so closer values override
    for ancestor in reversed(chain):
        frame = FRAME_STORE.get(ancestor, {})
        for slot_name in frame.get("slots", {}):
            val = get_slot(frame_name, slot_name)  # resolved for frame_name
            if val is not None:
                result[slot_name] = val

    return result


def print_frame(frame_name):
    """Pretty-print a single frame with all resolved slot values."""
    resolved = inherit_from_parent(frame_name)
    frame = FRAME_STORE[frame_name]
    print(f"\n  --- Frame: {frame_name} ------------------------------")
    print(f"  -  Parent : {frame['parent']}")
    for slot, value in resolved.items():
        print(f"  -  {slot:<25} : {value}")
    print(f"  -{'-' * 55}")


# ---------------------------------------------------------------------------
# BUILD FRAMES
# ---------------------------------------------------------------------------

def build_frames():
    """Define the three base frames and two concrete instances."""

    # ---- 1. Person (root frame) ----
    create_frame(
        name="Person",
        parent=None,
        slots={
            "species":    {"default": "Homo sapiens"},
            "has_name":   {"default": "Unknown"},
            "has_age":    {"default": 0},
            "is_alive":   {"default": True},
            "occupation": {"default": "Unemployed"},
            # Procedural attachment: derive email from name
            "email": {
                "if_needed": lambda frame_name, _: (
                    get_slot(frame_name, "has_name").lower().replace(" ", ".") + "@example.com"
                    if get_slot(frame_name, "has_name") else None
                )
            },
        },
    )

    # ---- 2. Student (inherits from Person) ----
    create_frame(
        name="Student",
        parent="Person",
        slots={
            "occupation":  {"default": "Student"},
            "institution": {"default": "Unknown University"},
            "gpa":         {"default": 0.0},
            "year":        {"default": 1},
            # Procedural attachment: academic standing from GPA
            "standing": {
                "if_needed": lambda frame_name, _: (
                    "Excellent" if (get_slot(frame_name, "gpa") or 0) >= 3.7 else
                    "Good"      if (get_slot(frame_name, "gpa") or 0) >= 3.0 else
                    "Average"   if (get_slot(frame_name, "gpa") or 0) >= 2.0 else
                    "Probation"
                )
            },
        },
    )

    # ---- 3. Course (independent frame) ----
    create_frame(
        name="Course",
        parent=None,
        slots={
            "course_id":   {"default": "XXX-000"},
            "title":       {"default": "Untitled"},
            "credits":     {"default": 3},
            "department":  {"default": "General"},
            "max_seats":   {"default": 60},
            # Procedural attachment: remaining seats derived from enrolled count
            "remaining_seats": {
                "if_needed": lambda frame_name, _: (
                    (get_slot(frame_name, "max_seats") or 0)
                    - (get_slot(frame_name, "enrolled") or 0)
                )
            },
        },
    )


def instantiate_frames():
    """Create concrete instance frames."""

    print("\n[INSTANTIATING FRAMES]")

    # ---- Instance 1: Dishan (a specific student) ----
    create_frame(
        name="Dishan",
        parent="Student",
        slots={
            "has_name":   {"value": "Khushi Dixit"},
            "has_age":    {"value": 21},
            "institution": {"value": "Example Engineering College"},
            "gpa":        {"value": 3.85},
            "year":       {"value": 3},
            "course_enrolled": {"value": "IC-709D"},
        },
    )

    # ---- Instance 2: Alice (another student) ----
    create_frame(
        name="Alice",
        parent="Student",
        slots={
            "has_name":   {"value": "Alice Sharma"},
            "has_age":    {"value": 20},
            "institution": {"value": "Example Engineering College"},
            "gpa":        {"value": 2.4},
            "year":       {"value": 2},
        },
    )

    # ---- Instance 3: AI Course ----
    create_frame(
        name="AI_Course",
        parent="Course",
        slots={
            "course_id":  {"value": "IC-709D"},
            "title":      {"value": "Artificial Intelligence"},
            "credits":    {"value": 4},
            "department": {"value": "Information Technology"},
            "max_seats":  {"value": 50},
            "enrolled":   {"value": 45},
        },
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  FRAME REPRESENTATION SYSTEM")
    print("  Domain : Person -> Student -> Course")
    print("=" * 70)

    print("\n[CREATING BASE FRAMES]")
    build_frames()

    instantiate_frames()

    print("\n[FRAME CONTENTS WITH INHERITED & COMPUTED SLOTS]")
    for name in ["Person", "Student", "Course", "Dishan", "Alice", "AI_Course"]:
        print_frame(name)

    # Demonstrate set_slot
    print("\n[MODIFYING SLOT - Alice's GPA promoted to 3.1]")
    set_slot("Alice", "gpa", 3.1)
    print("  Alice's updated standing:", get_slot("Alice", "standing"))

    print("\n" + "=" * 70)
    print("  Frame Representation demo complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()

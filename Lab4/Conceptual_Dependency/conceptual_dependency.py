"""
=============================================================================
  Lab 4 - Experiment 6 : Conceptual Dependency (CD) Representation
  Student  : Khushi Dixit
  Roll No  : IC-2K23-51
  Course   : IC-709D (Artificial Intelligence Lab)
  Topic    : Knowledge Representation using Roger Schank's Conceptual Dependency
=============================================================================
"""

from typing import Dict, Any, List, Optional


class ConceptualDependencyStructure:
    """
    Represents a statement in Roger Schank's Conceptual Dependency (CD) Theory.
    
    Primitive ACTs:
      - ATRANS : Transfer of an abstract relationship (e.g., give, transfer ownership)
      - PTRANS : Transfer of physical location of an object (e.g., go, drive, move)
      - PROPEL : Application of physical force to an object (e.g., push, throw)
      - MOVE   : Movement of a body part by its owner (e.g., kick, reach)
      - GRASP  : Grasping an object by an actor (e.g., grab, hold)
      - INGEST : Taking an object to the inside of an animal (e.g., eat, drink)
      - EXPEL  : Expulsion of something from the body (e.g., spit, cry)
      - MTRANS : Transfer of mental information between minds (e.g., tell, teach)
      - MBUILD : Construction of new information from existing thoughts (e.g., decide, conclude)
      - SPEAK  : Producing sounds from a vocal organ
      - ATTEND : Focusing a sensory organ on a stimulus (e.g., listen, observe)
    """

    def __init__(
        self,
        sentence: str,
        actor: str,
        act: str,
        obj: str,
        recipient_to: Optional[str] = None,
        recipient_from: Optional[str] = None,
        direction_to: Optional[str] = None,
        direction_from: Optional[str] = None,
        instrument: Optional['ConceptualDependencyStructure'] = None,
        tense: str = "PAST"
    ):
        self.sentence = sentence
        self.actor = actor
        self.act = act
        self.obj = obj
        self.recipient_to = recipient_to
        self.recipient_from = recipient_from
        self.direction_to = direction_to
        self.direction_from = direction_from
        self.instrument = instrument
        self.tense = tense

    def to_dict(self) -> Dict[str, Any]:
        data = {
            "Sentence": self.sentence,
            "Tense": self.tense,
            "Actor (PP)": self.actor,
            "Primitive ACT": self.act,
            "Object (PP)": self.obj,
        }
        if self.recipient_to or self.recipient_from:
            data["Recipient Case (R)"] = {
                "FROM": self.recipient_from,
                "TO": self.recipient_to
            }
        if self.direction_to or self.direction_from:
            data["Direction Case (D)"] = {
                "FROM": self.direction_from,
                "TO": self.direction_to
            }
        if self.instrument:
            data["Instrumental ACT (I)"] = self.instrument.to_dict()
        return data

    def display(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}Surface Sentence : \"{self.sentence}\"")
        print(f"{prefix}Tense            : {self.tense}")
        print(f"{prefix}Actor (PP)       : {self.actor}")
        print(f"{prefix}<===> ACT       : {self.act}")
        print(f"{prefix}  <-o (Object)   : {self.obj}")
        if self.recipient_to or self.recipient_from:
            print(f"{prefix}  <-R (Recipient): [FROM: {self.recipient_from}] -> [TO: {self.recipient_to}]")
        if self.direction_to or self.direction_from:
            print(f"{prefix}  <-D (Direction): [FROM: {self.direction_from}] -> [TO: {self.direction_to}]")
        if self.instrument:
            print(f"{prefix}  <-I (Instrument):")
            self.instrument.display(indent=indent + 2)


def build_cd_knowledge_base() -> List[ConceptualDependencyStructure]:
    kb = []

    # 1. "John gave Mary a book" -> ATRANS (Transfer of ownership)
    cd1 = ConceptualDependencyStructure(
        sentence="John gave Mary a book.",
        actor="John",
        act="ATRANS",
        obj="Book",
        recipient_from="John",
        recipient_to="Mary",
        tense="PAST"
    )
    kb.append(cd1)

    # 2. "Dishan drove from Campus to Library" -> PTRANS with instrument
    inst2 = ConceptualDependencyStructure(
        sentence="Dishan operated the car controls.",
        actor="Dishan",
        act="MOVE",
        obj="Hands/Feet",
        direction_from="Neutral",
        direction_to="Car Controls",
        tense="PAST"
    )
    cd2 = ConceptualDependencyStructure(
        sentence="Dishan drove from Campus to Library.",
        actor="Dishan",
        act="PTRANS",
        obj="Dishan",
        direction_from="Campus",
        direction_to="Library",
        instrument=inst2,
        tense="PAST"
    )
    kb.append(cd2)

    # 3. "The professor told students the exam date" -> MTRANS (Mental transfer)
    cd3 = ConceptualDependencyStructure(
        sentence="The professor told the students the exam date.",
        actor="Professor",
        act="MTRANS",
        obj="Exam Date Fact",
        recipient_from="Professor's Memory (CP)",
        recipient_to="Students' Memory (CP)",
        tense="PAST"
    )
    kb.append(cd3)

    # 4. "Alice ate an apple using a spoon" -> INGEST
    inst4 = ConceptualDependencyStructure(
        sentence="Alice grasped the spoon.",
        actor="Alice",
        act="GRASP",
        obj="Spoon",
        tense="PAST"
    )
    cd4 = ConceptualDependencyStructure(
        sentence="Alice ate an apple.",
        actor="Alice",
        act="INGEST",
        obj="Apple",
        direction_from="Outside Body",
        direction_to="Alice's Stomach",
        instrument=inst4,
        tense="PAST"
    )
    kb.append(cd4)

    # 5. "Bob decided to study AI" -> MBUILD (Mental creation)
    cd5 = ConceptualDependencyStructure(
        sentence="Bob decided to study AI.",
        actor="Bob",
        act="MBUILD",
        obj="Decision: Study AI Course",
        recipient_from="Bob's Thoughts",
        recipient_to="Bob's Long-Term Memory (LTM)",
        tense="PAST"
    )
    kb.append(cd5)

    return kb


def main():
    print("=" * 70)
    print("  CONCEPTUAL DEPENDENCY (CD) KNOWLEDGE REPRESENTATION")
    print("  Framework : Roger Schank Primitive ACT Representation")
    print("  Student   : Khushi Dixit | Roll No: IC-2K23-51 | Course: IC-709D")
    print("=" * 70)

    kb = build_cd_knowledge_base()
    print(f"\n[DEMONSTRATING {len(kb)} CONCEPTUAL DEPENDENCY STRUCTURES]\n")

    for idx, cd in enumerate(kb, start=1):
        print(f"--- Case {idx} ---")
        cd.display(indent=1)
        print("-" * 50)

    print("\n[INFERENCE FROM CD PRIMITIVES]")
    print("  Rule: If ACT == ATRANS and recipient_to != None:")
    print("    Deduce: New owner of object is recipient_to.")
    for cd in kb:
        if cd.act == "ATRANS":
            print(f"  > Statement: \"{cd.sentence}\"")
            print(f"    Inference: {cd.recipient_to} now possesses {cd.obj}.")

    print("  Rule: If ACT == PTRANS and direction_to != None:")
    print("    Deduce: Current location of actor/object is direction_to.")
    for cd in kb:
        if cd.act == "PTRANS":
            print(f"  > Statement: \"{cd.sentence}\"")
            print(f"    Inference: {cd.actor} is now at {cd.direction_to}.")

    print("\n" + "=" * 70)
    print("  Conceptual Dependency Representation complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()

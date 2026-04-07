from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self) -> 'SpaceMission':

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_cmd_or_capt = any(m.rank in (Rank.commander,
                                         Rank.captain) for m in self.crew)

        if not has_cmd_or_capt:
            raise ValueError("Mission must have at least one Commander \
or Captain")

        if self.duration_days > 365:

            experienced_crew = sum(1 for m in self.crew
                                   if m.years_experience >= 5)

            if experienced_crew < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need at least \
50% experienced crew (5+ years)")

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():

    print("Space Mission Crew Validation")
    print("=========================================")

    sarah = CrewMember(
        member_id="CM001", name="Sarah Connor", rank=Rank.commander,
        age=45, specialization="Mission Command", years_experience=20
    )
    john = CrewMember(
        member_id="CM002", name="John Smith", rank=Rank.lieutenant,
        age=35, specialization="Navigation", years_experience=10
    )
    alice = CrewMember(
        member_id="CM003", name="Alice Johnson", rank=Rank.officer,
        age=28, specialization="Engineering", years_experience=3
    )

    try:

        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-01-01T08:00:00",
            duration_days=900,
            crew=[sarah, john, alice],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")

        for m in valid_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:

        print("Expected validation error:")

        for error in e.errors():
            print(f"{error['msg'].split(',')[1].strip()}")

    print("=========================================")

    try:

        invalid_mission = SpaceMission(
            mission_id="M2024_LUNA",
            mission_name="Lunar Backup",
            destination="Moon",
            launch_date="2025-02-01T08:00:00",
            duration_days=30,
            crew=[john, alice],
            budget_millions=500.0
        )
        print(invalid_mission)

    except ValidationError as e:

        print("Expected validation error:")

        for error in e.errors():
            print(f"{error['msg'].split(',')[1].strip()}")


if __name__ == "__main__":
    main()

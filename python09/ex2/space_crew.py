from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum
import json


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


def load_missions(path: str) -> list[SpaceMission]:

    with open(path, "r") as f:
        raw_data = json.load(f)

    missions = []

    for item in raw_data:
        try:
            missions.append(item)
        except Exception as e:
            print(e)

    return missions


def main():

    print("Space Mission Crew Validation")
    print("=========================================")

    missions = load_missions("space_missions.json")

    working_missions = missions[0]

    sarah = CrewMember(
        member_id=working_missions['crew'][0]['member_id'],
        name=working_missions['crew'][0]['name'],
        rank=working_missions['crew'][0]['rank'],
        age=working_missions['crew'][0]['age'],
        specialization=working_missions['crew'][0]['specialization'],
        years_experience=working_missions['crew'][0]['years_experience']
    )

    james = CrewMember(
        member_id=working_missions['crew'][1]['member_id'],
        name=working_missions['crew'][1]['name'],
        rank=working_missions['crew'][1]['rank'],
        age=working_missions['crew'][1]['age'],
        specialization=working_missions['crew'][1]['specialization'],
        years_experience=working_missions['crew'][1]['years_experience']
    )

    anna = CrewMember(
        member_id=working_missions['crew'][2]['member_id'],
        name=working_missions['crew'][2]['name'],
        rank=working_missions['crew'][2]['rank'],
        age=working_missions['crew'][2]['age'],
        specialization=working_missions['crew'][2]['specialization'],
        years_experience=working_missions['crew'][2]['years_experience']
    )

    try:

        valid_mission = SpaceMission(
            mission_id=working_missions['mission_id'],
            mission_name=working_missions['mission_name'],
            destination=working_missions['destination'],
            launch_date=working_missions['launch_date'],
            duration_days=working_missions['duration_days'],
            crew=[sarah, james, anna],
            budget_millions=working_missions['budget_millions']
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

    print("\n=========================================")

    try:

        invalid_mission = SpaceMission(
            mission_id=working_missions['mission_id'],
            mission_name=working_missions['mission_name'],
            destination=working_missions['destination'],
            launch_date=working_missions['launch_date'],
            duration_days=working_missions['duration_days'],
            crew=[anna],
            budget_millions=working_missions['budget_millions']
        )

        print("Valid mission created:")
        print(f"Mission: {invalid_mission.mission_name}")
        print(f"ID: {invalid_mission.mission_id}")
        print(f"Destination: {invalid_mission.destination}")
        print(f"Duration: {invalid_mission.duration_days} days")
        print(f"Budget: ${invalid_mission.budget_millions}M")
        print(f"Crew size: {len(invalid_mission.crew)}")
        print("Crew members:")

        for m in invalid_mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:

        print("Expected validation error:")

        for error in e.errors():
            print(f"{error['msg'].split(',')[1].strip()}")


if __name__ == "__main__":
    main()

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional
import json


class SpaceStation(BaseModel):

    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def load_stations(path: str) -> list[dict]:

    with open(path, "r") as f:
        raw_data = json.load(f)

    stations = []

    for item in raw_data:
        try:
            stations.append(item)
        except Exception as e:
            print(e)

    return stations


def main() -> None:

    print("Space Station Data Validation")
    print("========================================")

    try:

        stations = load_stations("space_stations.json")

        working_stations: dict = stations[0]

        valid_station = SpaceStation(
            station_id=working_stations['station_id'],
            name=working_stations['name'],
            crew_size=working_stations['crew_size'],
            power_level=working_stations['power_level'],
            oxygen_level=working_stations['oxygen_level'],
            last_maintenance=working_stations['last_maintenance'],
            is_operational=working_stations['is_operational']
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        status = ("Operational" if valid_station.is_operational
                  else "Non-operational")
        print(f"Status: {status}")

    except ValidationError as e:

        print("Expected validation error:")

        for err in e.errors():
            print(err["msg"])

    print("========================================")

    try:

        stations = load_stations("invalid_stations.json")

        working_stations = stations[0]

        invalid_station = SpaceStation(
            station_id=working_stations['station_id'],
            name=working_stations['name'],
            crew_size=working_stations['crew_size'],
            power_level=working_stations['power_level'],
            oxygen_level=working_stations['oxygen_level'],
            last_maintenance=working_stations['last_maintenance'],
            is_operational=working_stations['is_operational']
        )
        print(invalid_station)

    except ValidationError as e:

        print("Expected validation error:")

        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()

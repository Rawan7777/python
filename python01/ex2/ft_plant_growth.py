#!/usr/bin/env python3

class Plant:
    """Represents a growing plant."""

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.plant_age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":

    name = "Rose"
    intial_height = 25
    intial_plant_age = 30

    rose = Plant(name, intial_height, intial_plant_age)

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(6):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - intial_height}cm")

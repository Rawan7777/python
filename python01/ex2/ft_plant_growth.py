#!/usr/bin/env python3

class Plant:

    """Represents a growing plant."""

    def __init__(self, name: str, height: int, plant_age: int) -> None:
        """
        Initialize a Plant instance.

        :param name: Name of the plant
        :param height: Height in centimeters
        :param plant_age: Age in days
        """
        self.name = name.capitalize()
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        """Increase the plant's height by 1 cm."""
        self.height += 1

    def age(self) -> None:
        """Increase the plant's age by 1 day."""
        self.plant_age += 1

    def get_info(self) -> str:
        """Return a formatted string with plant information."""
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"


if __name__ == "__main__":

    name = "rose"
    initial_height = 25
    initial_plant_age = 30

    rose = Plant(name, initial_height, initial_plant_age)

    print("=== Day 1 ===")
    print(rose.get_info())

    for day in range(1, 7):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")

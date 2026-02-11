#!/usr/bin/env python3

class Plant:

    """Represent a plant in the garden."""

    def __init__(self, name: str, height: int, age: int):

        """Initialize a Plant instance.
        :param name: Name of the plant
        :param height: Height in centimeters
        :param age: Age in days"""

        self.name = name.capitalize()
        self.height = height
        self.age = age

    def display_data(self) -> str:

        """Return formatted plant information."""

        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":

    print("=== Garden Plant Registry ===")

    rose = Plant("rose", 25, 30)
    print(rose.display_data())

    sunflower = Plant("sunflower", 80, 45)
    print(sunflower.display_data())

    cactus = Plant("cactus", 15, 120)
    print(cactus.display_data())

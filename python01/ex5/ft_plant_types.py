#!/usr/bin/env python3

class Plant:

    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        :param name: Name of the plant
        :param height: Height in centimeters
        :param age: Age in days
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):

    """Represents a flower plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Simulate blooming of the flower."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """Return formatted information about the flower."""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):

    """Represents a tree plant."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int
                 ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Simulate shade production of the tree."""
        print(f"{self.name} provides {self.trunk_diameter + 28} m² of shade")

    def get_info(self) -> str:
        """Return formatted information about the tree."""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):

    """Represents a vegetable plant."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """Return formatted information about the vegetable."""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season}. "
                f"Rich in {self.nutritional_value}")


if __name__ == "__main__":

    print("=== Garden Plant Types ===\n")

    rose = Flower("rose", 25, 30, "red")
    print(rose.get_info())
    rose.bloom()
    print()

    oak = Tree("oak", 500, 1825, 50)
    print(oak.get_info())
    oak.produce_shade()
    print()

    tomato = Vegetable("tomato", 80, 90, "summer harvest", "vitamin C")
    print(tomato.get_info())

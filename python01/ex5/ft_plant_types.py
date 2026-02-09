#!/usr/bin/env python3

class Plant:

    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:

        """Initialize a Plant instance.
        :param name: Name of the plant
        :param height: Height in centimeters
        :param age: Age in days"""

        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):

    """Represents a flower plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:

        """Initialize a Flower instance.
        Calls the parent Plant constructor using super() to initialize
        the common plant attributes (name, height, and age), then sets
        the flower-specific color attribute.
        :param color: Color of the flower"""

        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Simulate blooming of the flower."""
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self) -> str:
        """Return formatted information about the flower."""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")


class Tree(Plant):

    """Represents a tree plant."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int
                 ) -> None:

        """Initialize a Tree instance
        Calls the parent Plant constructor using super() to initialize
        the common plant attributes (name, height, and age), then sets
        the tree-specific trunk diameter attribute.
        :param trunk_diameter: Diameter of the trunk in centimeters"""

        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Simulate shade production of the tree."""
        print(f"{self.name} provides {self.trunk_diameter * 1.56:.0f}"
              f" square meters of shade\n")

    def get_info(self) -> str:
        """Return formatted information about the tree."""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):

    """Represents a vegetable plant."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:

        """Initialize a Vegetable instance
        Calls the parent Plant constructor using super() to initialize
        the common plant attributes (name, height, and age), then sets
        the vegetable-specific harvest season and nutritional value
        attributes.
        :param harvest_season: Harvest season of the vegetable
        :param nutritional_value: Main nutritional value of the vegetable"""

        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """Return formatted information about the vegetable."""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season}.\n"
                f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":

    print("=== Garden Plant Types ===\n")

    rose = Flower("rose", 25, 30, "red")
    print(rose.get_info())
    rose.bloom()

    oak = Tree("oak", 500, 1825, 50)
    print(oak.get_info())
    oak.produce_shade()

    tomato = Vegetable("tomato", 80, 90, "summer harvest", "vitamin C")
    print(tomato.get_info())

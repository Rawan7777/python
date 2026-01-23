#!/usr/bin/env python3

class Plant:

    """Represents a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

if __name__ == "__main__":
    
    print("=== Garden Plant Registry ===")

    rose = Plant("rose", 25, 30)
    print(rose.get_info())

    sunflower = Plant("sunflower", 80, 45)
    print(sunflower.get_info())
    
    cactus = Plant("Cactus", 15, 120)
    print(cactus.get_info())

#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age
    
    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color"

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points


class GardenManager:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_garden_network(cls):
        ...

    class GardenStats:
        ...

if __name__ == "__main__":

    alice = GardenManager("Alice")

    alice.create_garden_network("Oak Tree")
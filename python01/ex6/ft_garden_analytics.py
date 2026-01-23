#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, prize_points):
        super().__init__(name, height, age)
        self.prize_points = prize_points


class GardenManager:

    def create_garden_network():
        ...

    class GardenStats:
        ...
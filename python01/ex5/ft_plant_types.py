#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter + 28} square meters of shade")

    def get_info(self) -> str:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
    
    def get_info(self, rich_of) -> str:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season}")
        print(f"{self.name} is rich in {rich_of}")

if __name__ == "__main__":

    print("=== Garden Plant Types ===\n")

    rose = Flower("rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()
    print()
    oak = Tree("oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()
    print()
    tomato = Vegetable("tomato", 80, 90, "summer harvest")
    tomato.get_info("vitamin C")
    
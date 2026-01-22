class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter + 28} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = "vitamin C"
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season}")
        print(f"{self.name} is rich in {self.nutritional_value}")

print("=== Garden Plant Types ===")

rose = Flower("rose", 25, 30, "red")
rose.bloom()
print()
Oak = Tree("Oak", 500, 1825, 50)
Oak.produce_shade()
print()
Tomato = Vegetable("Tomato", 80, 90, "summer harvest")
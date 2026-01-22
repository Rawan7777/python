class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

print("=== Garden Plant Registry ===")
Plant("rose", 25, 30)
Plant("sunflower", 80, 45)
Plant("Cactus", 15, 120)

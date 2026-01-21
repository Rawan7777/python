class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"{name.capitalize()}: {height}cm, {age} days old")

print("=== Garden Plant Registry ===")
Plant("rose", 25, 30)
Plant("sunflower", 80, 45)
Plant("Cactus", 15, 120)

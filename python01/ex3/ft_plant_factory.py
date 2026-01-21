class Plant:
    total = 0
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.total += 1
        print(f"Created: {name.capitalize()} ({height}cm, {age} days)")

    def show_total():
        print(f"Total plants created: {Plant.total}")

print("=== Plant Factory Output ===")

rose = Plant("rose", 25, 30)
Oak = Plant("Oak", 200, 365)
Cactus = Plant("Cactus", 5, 90)
Sunflower = Plant("Sunflower", 80, 45)
Fern = Plant("Fern", 15, 120)

Plant.show_total()

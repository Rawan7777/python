class Plant:
    def __init__(self, name, height, plant_age):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self, day):
        return self.height + day - 1

    def age(self, day):
        return self.plant_age + day - 1

    def get_info(self, day):
        print(f"=== Day {day} ===")
        print(f"{self.name}: {self.grow(day)}cm, {self.age(day)} days old")
        if day > 1:
            print(f"Growth this week: +{day - 1}cm")
            

rose = Plant("rose", 25, 30)

rose.get_info(1)
rose.get_info(7)
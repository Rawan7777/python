#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass

class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 10

    def add_plant(self, name):
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[name] = {"water": 5, "sun": 8}
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            if self.water_tank <= 0:
                raise WaterError("Not enough water in tank")

            for plant in self.plants:
                self.plants[plant]["water"] += 1
                self.water_tank -= 1
                print(f"Watering {plant} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name):
       
        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]
        
        if water > 10:
            raise HealthError(
                f"Error checking {name}: Water level {water} is too high (max 10)"
            )

        if water < 1:
            raise HealthError(
                f"Error checking {name}: Water level {water} is too low (min 1)"
            )

        if sun > 12:
            raise HealthError(
                f"Error checking {name}: Sunlight hours {sun} is too high (max 12)"
            )

        if sun < 2:
            raise HealthError(
                f"Error checking {name}: Sunlight hours {sun} is too low (min 2)"
            )

        print(f"{name}: healthy (water: {water}, sun: {sun})")


def main():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")  # error
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        manager.water_plants()
    except WaterError as e:
        print(f"Watering error: {e}")

    print("Checking plant health...")
    try:
        manager.check_health("tomato")
        manager.plants["lettuce"]["water"] = 15  # force error
        manager.check_health("lettuce")
    except HealthError as e:
        print(e)

    print("Testing error recovery...")
    try:
        manager.water_tank = 0
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    main()

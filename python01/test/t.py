#!/usr/bin/env python3

class Plant:
    """Base class for all plants."""
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.type = "Plant"  # manual type tracking

    def grow(self):
        """Increase height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    """Plant with flowers that can bloom."""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True
        self.type = "FloweringPlant"


class PrizeFlower(FloweringPlant):
    """Flower that gives prize points."""
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.prize_points = points
        self.type = "PrizeFlower"


class GardenManager:
    """Manages plants and multiple gardens."""
    total_gardens = 0
    garden_scores = {}

    class GardenStats:
        """Manual helper class to calculate garden statistics."""

        @staticmethod
        def total_plants(plants):
            count = 0
            for _ in plants:
                count += 1
            return count

        @staticmethod
        def total_growth(plants):
            growth = 0
            for _ in plants:
                growth += 1
            return growth

        @staticmethod
        def plant_types_count(plants):
            plant_count = 0
            flowering_count = 0
            prize_count = 0
            for p in plants:
                # manual type checking using the 'type' attribute
                if p.type == "PrizeFlower":
                    prize_count += 1
                elif p.type == "FloweringPlant":
                    flowering_count += 1
                else:
                    plant_count += 1
            return {"Plant": plant_count, "FloweringPlant": flowering_count, "PrizeFlower": prize_count}

        @staticmethod
        def validate_height(plants):
            valid = True
            for p in plants:
                if p.height < 0:
                    valid = False
            return valid

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1
        GardenManager.garden_scores[self.owner] = 0

    def add_plant(self, plant):
        """Add a plant to the garden."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        """Grow all plants in the garden and update garden score."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            # manual score update
            score = plant.height
            if plant.type == "PrizeFlower":
                score += plant.prize_points
            GardenManager.garden_scores[self.owner] = GardenManager.garden_scores[self.owner] + score

    def report(self):
        """Generate a garden report using GardenStats."""
        stats = self.GardenStats
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if p.type == "PrizeFlower":
                print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming), Prize points: {p.prize_points}")
            elif p.type == "FloweringPlant":
                print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming)")
            else:
                print(f"- {p.name}: {p.height}cm")

        total_growth = stats.total_growth(self.plants)
        total_count = stats.total_plants(self.plants)
        type_counts = stats.plant_types_count(self.plants)
        height_valid = stats.validate_height(self.plants)

        print(f"Plants added: {total_count}, Total growth: {total_growth}cm")
        print(f"Plant types: {type_counts['Plant']} regular, {type_counts['FloweringPlant']} flowering, {type_counts['PrizeFlower']} prize flowers")
        print(f"Height validation test: {height_valid}")

    @classmethod
    def create_garden_network(cls, owner):
        """Create a single garden for an owner."""
        return cls(owner)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # Create gardens
    alice = GardenManager.create_garden_network("Alice")
    bob = GardenManager.create_garden_network("Bob")

    # Create exactly 3 plants to match desired output
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Add plants to Alice's garden
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    # Grow plants
    alice.grow_all()

    # Report
    alice.report()

    # Garden scores summary
    print(f"Garden scores - Alice: {GardenManager.garden_scores['Alice']}, Bob: {GardenManager.garden_scores['Bob']}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")

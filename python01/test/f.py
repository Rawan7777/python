#!/usr/bin/env python3

class Plant:
    """Base class for all plants."""
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

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


class PrizeFlower(FloweringPlant):
    """Flower that gives prize points."""
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.prize_points = points


class GardenManager:
    """Manages plants and multiple gardens."""
    total_gardens = 0
    garden_scores = {}

    class GardenStats:
        """Helper class to calculate garden statistics."""
        @staticmethod
        def total_plants(plants: list) -> int:
            return len(plants)

        @staticmethod
        def total_growth(plants: list) -> int:
            # Growth = sum of growth in this turn
            return sum(1 for _ in plants)

        @staticmethod
        def plant_types_count(plants: list) -> dict:
            counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for p in plants:
                if isinstance(p, PrizeFlower):
                    counts["PrizeFlower"] += 1
                elif isinstance(p, FloweringPlant):
                    counts["FloweringPlant"] += 1
                else:
                    counts["Plant"] += 1
            return counts

        @staticmethod
        def validate_height(plants: list) -> bool:
            return all(p.height >= 0 for p in plants)

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
        """Grow all plants in the garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            # Increase garden score
            score = plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
            GardenManager.garden_scores[self.owner] += score

    def report(self):
        """Generate a garden report using GardenStats."""
        stats = self.GardenStats
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if isinstance(p, PrizeFlower):
                print(f"- {p.name}: {p.height}cm, {p.color} flowers (blooming), Prize points: {p.prize_points}")
            elif isinstance(p, FloweringPlant):
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
    def create_garden_network(cls, owners):
        """Create multiple gardens for different owners."""
        return cls(owners)


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

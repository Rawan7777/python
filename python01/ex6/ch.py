#!/usr/bin/env python3

class Plant:

    """Represents a basic plant with a name, height, and type"""

    def __init__(self, name: str, height: int, plant_type: str) -> None:

        """Initialize a Plant object.
            name (str): Plant name.
            height (int): Initial plant height in cm.
            plant_type (str): Type of the plant."""

        self.name = name.capitalize()
        self.height = height
        self.plant_type = plant_type
        self.bloom = "not_blooming"

    def grow(self, height: int) -> None:

        """Increase plant height.
            height (int): Growth amount in cm."""

        self.height += height
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:

        """Return plant information.:
            str: Formatted plant information."""

        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):

    """Represents a flowering plant."""

    def __init__(self, name: str, height: int, plant_type: str,
                 color: str) -> None:

        """Initialize a FloweringPlant.
            name (str): Plant name.
            height (int): Initial height.
            plant_type (str): Type of plant.
            color (str): Flower color."""

        super().__init__(name, height, plant_type)
        self.color = color
        self.bloom = "blooming"

    def get_info(self) -> str:

        """Return flowering plant information.
            str: Formatted plant information."""

        return (f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers ({self.bloom})")


class PrizeFlower(FloweringPlant):

    """Represents a flowering plant that gives prize points."""

    def __init__(self, name: str, height: int, plant_type: str, color: str,
                 prize_points: int) -> None:

        """Initialize a PrizeFlower.
            name (str): Plant name.
            height (int): Initial height.
            plant_type (str): Plant type.
            color (str): Flower color.
            prize_points (int): Prize points."""

        super().__init__(name, height, plant_type, color)
        self.prize_points = prize_points
        self.bloom = "blooming"

    def get_info(self) -> str:

        """Return prize flower information.
            str: Formatted plant information."""

        return (f"- {self.name}: {self.height}cm, {self.color} "
                f"flowers ({self.bloom}), Prize points: {self.prize_points}")


class GardenManager:

    """Manages gardens, owners, and statistics."""

    owners: list[str] = []
    owners_score: dict[str, int] = {}
    total_gardens: int = 0

    def __init__(self, owner: str) -> None:

        """Initialize a GardenManager.
            owner (str): Owner name."""

        self.owner = owner
        self.owner_garden: list[Plant] = []
        GardenManager.owners.append(self.owner)
        GardenManager.owners_score[self.owner] = 0
        GardenManager.total_gardens += 1
        self.gowth_times: int = 0

    def add_plant(self, plant: Plant) -> None:

        """Add a plant to the garden.
            plant (Plant): Plant instance."""

        self.owner_garden.append(plant)
        GardenManager.owners_score[self.owner] += plant.height
        if plant.bloom == "blooming":
            GardenManager.owners_score[self.owner] += 15
        if plant.plant_type == "PrizeFlower":
            GardenManager.owners_score[self.owner] += plant.prize_points
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self) -> None:

        """Grow all plants by 1 cm."""

        print(f"\n{self.owner} is helping all plants grow...")

        for plant in self.owner_garden:
            plant.grow(1)
            GardenManager.owners_score[self.owner] += 1
        self.gowth_times += 1

    class GardenStats:

        """Provides garden statistics."""

        plant_added: int = 0

        @classmethod
        def added_growth(cls, owner_garden: list[Plant],
                         gowth_times: int) -> None:

            """Print total plants added and growth.
                owner_garden (list[Plant]): List of plants.
                gowth_times (int): Growth cycles count."""
            old_count = cls.plant_added
            for _ in owner_garden:
                cls.plant_added += 1
            print(f"Plants added: {cls.plant_added - old_count},"
                  f" Total growth: {cls.plant_added * gowth_times}cm")

        @staticmethod
        def plant_types(owner_garden: list[Plant]) -> dict[str, int]:

            """Count plant types.
            owner_garden (list[Plant]): List of plants.
            Returns dict[str, int]: Count of each plant type."""

            counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}

            for plant in owner_garden:
                if plant.plant_type == "Plant":
                    counts["Plant"] += 1
                elif plant.plant_type == "FloweringPlant":
                    counts["FloweringPlant"] += 1
                elif plant.plant_type == "PrizeFlower":
                    counts["PrizeFlower"] += 1
            return counts

        @staticmethod
        def height_validation_test(owner_garden: list[Plant]) -> bool:

            """Validate that no plant has negative height.
            owner_garden (list[Plant]): List of plants.
            Returns bool: Validation result."""

            for plant in owner_garden:
                if plant.height < 0:
                    return False
            return True

    def garden_report(self) -> None:

        """Display full garden report."""

        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.owner_garden:
            if plant.plant_type == "Plant":
                print(plant.get_info())
            elif plant.plant_type == "FloweringPlant":
                print(plant.get_info())
            elif plant.plant_type == "PrizeFlower":
                print(plant.get_info())
        print()
        self.GardenStats.added_growth(self.owner_garden, self.gowth_times)
        self.gowth_times = 0
        my_dict = self.GardenStats.plant_types(self.owner_garden)
        print(f"Plant types: {my_dict["Plant"]} regular", end=", ")
        print(f"{my_dict["FloweringPlant"]} flowering", end=", ")
        print(f"{my_dict["PrizeFlower"]} prize flowers")
        print(f"\nHeight validation test: "
              f"{self.GardenStats.height_validation_test(self.owner_garden)}")
        print("Garden scores -", end=" ")
        counter = 0
        for key, value in GardenManager.owners_score.items():
            print(f"{key}: {value}", end="")
            counter += 1
            if counter < GardenManager.total_gardens:
                print(",", end=" ")
        print(f"\nTotal gardens managed: {GardenManager.total_gardens}")

    @classmethod
    def create_garden_network(cls, owner: str):

        """Create a GardenManager instance.
        owner (str): Owner name.
        Returns GardenManager: New instance."""

        return cls(owner.capitalize())


if __name__ == "__main__":

    print("=== Garden Management System Demo ===\n")

    alice = GardenManager.create_garden_network("alice")
    bob = GardenManager.create_garden_network("bob")

    zayi = Plant("Sakura", 92, "Plant")
    bob.owner_garden.append(zayi)
    GardenManager.owners_score["Bob"] += zayi.height

    oak = Plant("Oak Tree", 100, "Plant")
    rose = FloweringPlant("Rose", 25, "FloweringPlant", "red")
    sunflower = PrizeFlower("Sunflower", 50, "PrizeFlower", "red", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all_plants()
    alice.grow_all_plants()

    alice.garden_report()

    ssunflower = PrizeFlower("Ssunflower", 50, "PrizeFlower", "red", 10)

    alice.add_plant(ssunflower)
    alice.garden_report()


class Plant:

    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, type_of_plant: str) -> None:
        """
        Initialize a Plant instance.

        :param name: Name of the plant
        :param height: Height in centimeters
        :param age: Age in days
        """
        self.name = name.capitalize()
        self.height = height
        self.type_of_plant = type_of_plant.capitalize()

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def show_info(self):
        print(f"- {self.name}: {self.height}cm")



class FloweringPlant(Plant):

    """Represents a flower plant."""

    def __init__(self, name: str, height: int, type_of_plant: str, color: str) -> None:
        super().__init__(name, height, type_of_plant)
        self.color = color
        self.bloom = "blooming"

    def show_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom})")

class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, type_of_plant: str, color: str, prize_point: int
                 ) -> None:
        super().__init__(name, height, type_of_plant, color)
        self.prize_point = prize_point

    def show_info(self):
        print(f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom}), Prize points: {self.prize_point}")


class GardenManager:

    num_of_gardens = 0
    num_of_plants = 0
    total_growth = 0
    regular_count = 0
    flowering_count = 0
    prizeflower_count = 0
    owners_score = {}

    def __init__(self, owner: str):
        self.owner = owner
        self.owner_plants = []
        GardenManager.owners_score[self.owner] = 0;
        GardenManager.num_of_gardens += 1
    
    class GardenStats:
        ...

    @classmethod
    def create_garden_network(cls, garden_owner):
        return cls (garden_owner)
    
    def add_plant(self, plant):
        self.owner_plants.append(plant)
        GardenManager.num_of_plants += 1
        if plant.type_of_plant == "Plant":
            GardenManager.regular_count += 1
        elif plant.type_of_plant == "FloweringPlant":
            GardenManager.flowering_count += 1
        elif plant.type_of_plant == "PrizeFlower":
            GardenManager.prizeflower_count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")


    def grow_all_plants(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.owner_plants:
            plant.grow()
            GardenManager.total_growth += 1

    def get_report(self):

        print("Plants in garden:")
        for plant in self.owner_plants:
            plant.show_info()
        print(f"Plants added: {GardenManager.num_of_plants}, Total growth: {GardenManager.total_growth}cm")
        print(f"Plant types: {GardenManager.regular_count} regular, {GardenManager.flowering_count} flowering, {GardenManager.prizeflower_count} prize flowers")
        self.height_validation_test()

    @staticmethod
    def checker(height):
        if height < 0:
            return 1
        return 0;

    def height_validation_test(self):
        for plant in self.owner_plants:
            if self.checker(plant.height):
                print("Height validation test: False")
                return
        print("Height validation test: True")

print("=== Garden Management System Demo ===\n")

alice = GardenManager.create_garden_network("Alice")
bob = GardenManager.create_garden_network("bob")

oak_Tree = Plant("Oak Tree", 100, "plant")
rose = FloweringPlant("rose", 12, "FloweringPlant", "red")
sunflower = PrizeFlower("Sunflower", 10, "PrizeFlower", "pink", 100)

alice.add_plant(oak_Tree)
alice.add_plant(rose)
alice.add_plant(sunflower)

alice.grow_all_plants()

print("\n=== Alice's Garden Report ===")

alice.get_report()

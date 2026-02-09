
class Plant:

    def __init__(self, name: str, height: int, plant_type: str) -> None:

        self.name = name.capitalize()
        self.height = height
        self.plant_type = plant_type
        self.bloom = "not_blooming"

    def grow(self, height: int) -> None:
        self.height += height
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, plant_type: str, color: str) -> None:

        super().__init__(name, height, plant_type)
        self.color = color
        self.bloom = "blooming"

    def get_info(self) -> str:
        return (f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers ({self.bloom})")


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, plant_type: str, color: str, prize_points: int
                 ) -> None:
        super().__init__(name, height, plant_type, color)
        self.prize_points = prize_points
        self.bloom = "blooming"


    def get_info(self) -> str:
        return (f"- {self.name}: {self.height}cm, "
                f"{self.color} flowers ({self.bloom}), Prize points: {self.prize_points}")




class GardenManager:

    owners = []
    owners_score = {}
    total_gardens = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.owner_garden = []
        GardenManager.owners.append(self.owner)
        GardenManager.owners_score[self.owner] = 0
        GardenManager.total_gardens += 1
        self.gowth_times = 0

    def add_plant(self, plant):
        self.owner_garden.append(plant)
        GardenManager.owners_score[self.owner] += plant.height
        if plant.bloom == "blooming":
            GardenManager.owners_score[self.owner] += 15
        if plant.plant_type == "PrizeFlower":
            GardenManager.owners_score[self.owner] += plant.prize_points
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all_plants(self):
        print(f"\n{self.owner} is helping all plants grow...")

        for plant in self.owner_garden:
            plant.grow(1)
            GardenManager.owners_score[self.owner] += 1
        self.gowth_times += 1

    class GardenStats:
        
        plant_added = 0;

        @classmethod
        def added_plants_and_growth(cls, owner_garden: list, gowth_times: int) -> None:
            for _ in owner_garden:
                cls.plant_added += 1
            print(f"Plants added: {cls.plant_added}, Total growth: {cls.plant_added * gowth_times}cm")

        @classmethod
        def plant_types(cls, owner_garden: list) -> dict:

            counts = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}

            for plant in owner_garden:
                if plant.plant_type == "Plant":
                    counts["Plant"] += 1
                elif plant.plant_type == "FloweringPlant":
                    counts["FloweringPlant"] += 1
                elif plant.plant_type == "PrizeFlower":
                    counts["PrizeFlower"] += 1
            return counts

        @classmethod
        def height_validation_test(cls, owner_garden: list):
            for plant in owner_garden:
                if plant.height < 0:
                    return False
            return True


    def garden_report(self):
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
        self.GardenStats.added_plants_and_growth(self.owner_garden, self.gowth_times)
        my_dict = self.GardenStats.plant_types(self.owner_garden)
        print(f"Plant types: {my_dict["Plant"]} regular, {my_dict["FloweringPlant"]} flowering, {my_dict["PrizeFlower"]} prize flowers")
        print(f"\nHeight validation test: {self.GardenStats.height_validation_test(self.owner_garden)}")
        print("Garden scores -", end=" ")
        counter = 0
        for key, value in GardenManager.owners_score.items():
            print(f"{key}: {value}", end="")
            counter += 1
            if counter < GardenManager.total_gardens:
                print(",", end=" ")
        print(f"\nTotal gardens managed: {GardenManager.total_gardens}")


    @classmethod
    def create_garden_network(cls, owner):
        return cls(owner.capitalize())

    @staticmethod
    def utility():
        ...

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

    alice.garden_report()
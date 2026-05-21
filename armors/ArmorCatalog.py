from armors.Armor import Armor

class ArmorCatalog:

    def __init__(self):
        self.armors = {
            "example_armor": {"name": "armor_name", "block_reduction": 0.1},
            "leather_armor": {"name": "leather_armor", "block_reduction": 0.2},
            "iron_armor": {"name": "iron_armor", "block_reduction": 0.4},
            "heavy_armor": {"name": "heavy_armor", "block_reduction": 0.5}
        }


    def create_armor(self, armor_name: str):
        data = self.armors[armor_name]
        return Armor(data["name"], data["damage"])
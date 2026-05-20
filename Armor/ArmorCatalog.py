
from abc import ABC, abstractmethod
from weapons.Weapon import Weapon


class WeaponCatalog(ABC):

    @abstractmethod
    def __init__(self):
        self.weapons = {
            "example_weapon": {"name": "weapon_name", "damage": 10},
        }


    def create_weapon(self, weapon_type: str):
        data = self.weapons[weapon_type]
        return Weapon(data["name"], data["damage"])


# leather_armor = Armor("Leather Armor", 10, 20)
# iron_armor = Armor("Iron Armor", 25, 35)
# heavy_armor = Armor("Heavy Armor", 35, 45)
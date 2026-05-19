from weapons import WeaponCatalog
from weapons.Weapon import Weapon

class SwordCatalog(WeaponCatalog):

    #Override
    def __init__(self):
        self.weapons = {
            "wood_sword": {"name": "wood sword", "damage": 10},
            "iron_sword": {"name": "iron sword", "damage": 20},
            "death_sword": {"name": "death sword", "damage": 50},
        }
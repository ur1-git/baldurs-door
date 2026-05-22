from equipment.EquipmentCatalog import EquipmentCatalog

class SwordCatalog(EquipmentCatalog):
    #Override
    def __init__(self):
        self.weapons = {
            "wood_sword": {"name": "wood sword", "damage": 10},
            "iron_sword": {"name": "iron sword", "damage": 20},
            "death_sword": {"name": "death sword", "damage": 50},
        }

    def create_equipment(self, equipment_type: str):
        data = self.equipments[equipment_type]
        return Sword(data["name"], data["damage"])
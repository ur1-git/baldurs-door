
from abc import ABC, abstractmethod
from equipment.Equipment import Equipment


class EquipmentCatalog(ABC):

    @abstractmethod
    def __init__(self):
        self.equipments = {
            "example_weapon": {"name": "weapon_name", "damage": 10},
        }


    def create_equipment(self, equipment_type: str):
        data = self.equipments[equipment_type]
        return Equipment(data["name"], data["damage"])
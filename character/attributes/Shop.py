from character.Character import Character
from equipment.armors.ArmorCatalog import ArmorCatalog
from equipment.weapons.SwordCatalog import SwordCatalog


class Shop:
    def __init__(self):
        self.swords = SwordCatalog()
        self.armors = ArmorCatalog()

    def buy_equipment(self, name: str, character: Character):
        pass

    def buy_weapon(self, name: str, character: Character):
        weapon = self.swords.create_equipment(name)
        if weapon is None:
            print("Weapon",  name, "not found")
            return
        character.change_weapon(weapon)

    def buy_armor(self, name: str, character: Character):
        armor = self.armors.create_equipment(name)
        if armor is None:
            print("Armor", name, "not found")
            return
        character.change_armor(armor)
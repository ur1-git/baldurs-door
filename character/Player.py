from character.Character import Character
from character.attributes.Strength import Strength
from character.attributes.Constitution import Constitution
from character.attributes.Dexterity import Dexterity
from character.attributes.Mind import Mind
from equipment.weapons.Weapon import Weapon
from equipment.armors.Armor import Armor

class Player(Character):
    def __init__(self, name: str):
        super().__init__(name,
                         weapon = Weapon("stick", 1),
                         armor = Armor("clothes", 0),
                         constitution = Constitution(10),
                         strength = Strength(5),
                         dexterity = Dexterity(5),
                         mind = Mind(5))
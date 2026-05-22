from character.Character import Character
from character.attributes.Strength import Strength
from character.attributes.Constitution import Constitution
from character.attributes.Dexterity import Dexterity
from character.attributes.Mind import Mind
from equipment.weapons.Weapon import Weapon
from equipment.armors.Armor import Armor

class Enemy(Character):
    def __init__(self, name, weapon: Weapon, armor: Armor, constitution: Constitution, strength: Strength, dexterity: Dexterity, mind: Mind):
        super().__init__(name, weapon, armor, constitution, strength, dexterity, mind)

    def should_heal(self):
        if self.constitution.life < (0.5 * self.constitution.stat):
           self.inventory.use_item("health_potion")
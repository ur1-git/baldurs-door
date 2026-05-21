
from character.attributes.Strength import Strength
from character.attributes.Constitution import Constitution
from character.attributes.Dexterity import Dexterity
from character.attributes.Mind import Mind
from weapons.Weapon import Weapon
from armors.Armor import Armor

class Character:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon("stick", 1)
        self.armor = Armor("clothes", 0)
        self.dead = False


        # stats
        self.constitution = Constitution(1)
        self.strength = Strength(1)
        self.dexterity = Dexterity(1)
        self.mind = Mind(1)


    def physic_attacked(self, damage: int):
        if self.dexterity.is_evading():
            print(self.name, ": Attack evaded!")
            return
        self.constitution.block_physic(damage, self.armor) # it already changes life

    def mind_attacked(self):
        self.constitution.receive_damage(self.mind.mind_attacked())
from RollDice import RollDice
from character.attributes import Strength
from character.attributes import Dexterity
from character.attributes import Constitution
from weapons import Weapon


class Character:
    def __init__(self, name, life: int, weapon: Weapon, constitution: Constitution, strength: Strength, dexterity: Dexterity):
        self.name = name
        self.weapon = weapon
        self.dead = False

        # stats
        self.constitution = constitution
        self.strength = strength
        self.dexterity = dexterity
        # magic

    def get_life(self):
        return self._life

    def set_life(self, new_life: int):
        if new_life <= 0:
            self._life = 0
            print(self.name, " just died!")
            self.dead = True
        else:
            self._life = new_life
            self.dead = False
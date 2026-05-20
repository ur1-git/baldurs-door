import RollDice
from Armor.Armor import Armor
from character.attributes.Attribute import Attribute


class Constitution (Attribute):
    def __init__(self, stat):
        super().__init__(stat)
        self.life = stat
        self.dead = False

    def set_life(self, new_life):
        if self.stat > new_life:
            self.life = new_life
        else:
            self.life = self.stat

        if self.life <= 0:
            self.dead = True

    def receive_healing(self, healing):
        if self.dead:
            print("You can't heal someone who is dead!")
            return




    def blocked_damage(self, armor: Armor) -> int:
        if RollDice.roll100double() <
        block_chance = armor.block_chance * (1 + self.stat / 200)
        block_reduction = armor.block_reduction * (1 + self.stat / 100)
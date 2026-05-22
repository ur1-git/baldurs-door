import RollDice
from equipment.armors.Armor import Armor
from character.attributes.Attribute import Attribute


class Constitution (Attribute):
    def __init__(self, stat):
        super().__init__(stat)
        self.life = stat
        self.dead = False
        self.block_chance = stat * 0.5

    def improve_stat(self, amount: int = 1):
        self.stat += amount
        self.block_chance = self.stat * 0.5


    def receive_damage(self, damage):
        new_life = self.life - damage
        if new_life <= 0:
            self.life = 0
            self.dead = True
            print("Have died")
        else:
            self.life = new_life
            print("Have received ", damage)


    def receive_healing(self, healing):
        if self.dead:
            print("Can't be healed because is dead!")
            return

        old_life = self.life
        self.life = min(self.life + healing, self.stat)
        total_healed = self.life - old_life

        print("Have been healed ", total_healed, "hp")


    def block_reduction(self, armor: Armor):
        return 1 - armor.value / 100


    def block_physic(self, damage: int, armor: Armor):
        if RollDice.roll100double() <= self.block_chance:
            print("Attack blocked!")
            self.receive_damage(damage * self.block_reduction(armor))
        else:
            self.receive_damage(damage)
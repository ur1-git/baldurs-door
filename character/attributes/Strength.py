from character.attributes.Attribute import Attribute
from equipment.weapons.Weapon import Weapon


class Strength(Attribute):
    def __init__(self, stat):
        super().__init__(stat)

    def physic_attack(self, weapon: Weapon):
        """
        Returns damage as: weapon damage + strength points
        :return: int
        """
        return weapon.normal_attack() + self.stat
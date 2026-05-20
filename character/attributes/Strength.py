from character.Character import Character
from weapons.Weapon import Weapon


class Strength:
    def __init__(self, strength: int):
        self._strength = strength

    def physic_attack(self, weapon: Weapon):
        """
        Returns damage as an int.
        :return: int
        """
        return weapon.normal_attack() + self._strength * 0.35
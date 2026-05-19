from weapons import SwordCatalog
from weapons.Weapon import Weapon


class Character:
    def __init__(self, name, damage: int, life: int, weapon: Weapon):
        self.name = name
        self._damage = damage
        self._life = life
        self._weapon = weapon
        self.dead = False

    def get_damage(self):
        return self._damage

    def get_life(self):
        return self._life

    def set_life(self, new_life: int):
        if new_life <= 0:
            self._life = 0
            print(self.name, " just died!")
        else:
            self._life = new_life

    def attack(self, enemy: Character, damage: int):
        enemy.set_life(enemy.get_life() - damage)
        print(enemy.name(), " received ", damage, " damage from ", self.name)
from abc import ABC

from character.Inventory import Inventory
from character.attributes.Strength import Strength
from character.attributes.Constitution import Constitution
from character.attributes.Dexterity import Dexterity
from character.attributes.Mind import Mind
from equipment.weapons.Weapon import Weapon
from equipment.armors.Armor import Armor

class Character(ABC):
    def __init__(self, name, weapon: Weapon, armor: Armor, constitution: Constitution, strength: Strength, dexterity: Dexterity, mind: Mind):
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.inventory = Inventory()
        self.dead = False


        # stats
        self.constitution = constitution
        self.strength = strength
        self.dexterity = dexterity
        self.mind = mind

    def status(self):
        print("===== ", self.name, " ======")
        print("Weapon: ", self.weapon.name, ", damage: ", self.weapon.value)
        print("Armor: ", self.armor.name, ", protection: ", self.armor.value * 100, "%")
        print("--- Attributes ---")
        print("HP: ", self.constitution.life, "/", self.constitution.stat)
        print("Mana: ", self.mind.mana, "/", self.mind.stat)

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def change_armor(self, new_armor: Armor):
        self.armor = new_armor

    def weapon_attack(self, enemy: Character):
        enemy.physic_attacked(self.strength.physic_attack(self.weapon))

    def physic_attacked(self, damage: int):
        if self.dexterity.is_evading():
            print(self.name, ": Attack evaded!")
            return
        self.constitution.block_physic(damage, self.armor) # it already changes life

    def mind_attacked(self):
        self.constitution.receive_damage(self.mind.mind_attacked())

    def use_inventory_item(self, item_name: str, target=None):
        if target is None: target = self
        self.inventory.use_item(item_name, target)
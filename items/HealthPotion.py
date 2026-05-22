from character.Character import Character
from items.Item import Item


class HealthPotion(Item):
    def __init__(self, name: str, healing_points: int):
        super().__init__(name)
        self.healing_points = healing_points

    def use(self, character: Character):
        character.constitution.receive_healing(self.healing_points)
        self.uses_left -= 1
        if self.uses_left <= 0: self.destroy = True
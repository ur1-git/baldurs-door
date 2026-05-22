from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character.Character import Character

class Item(ABC):
    def __init__(self, name: str):
        self.name = name
        self.uses_left = 1
        self.destroy = False

    def add_one(self):
        self.uses_left += 1
        self.destroy = False

    @abstractmethod
    def use(self, character: Character):
        self.uses_left -= 1
        if self.uses_left <= 0: self.destroy = True
import math

import RollDice


class Dexterity:

    def __init__(self, dexterity: int):
        self._dexterity = dexterity

    def _critical_chance(self) -> float:
        base_chance = 2
        max_chance = 90
        scale = 0.005

        return base_chance + (max_chance - base_chance) * math.log(1 + scale * self._dexterity) / math.log(1 + scale * 100)

    def critical(self) -> int:
        """
        Returns an integer 1 if not or 2 if yes.
        The chance depends on the character's dexterity.
        :return: int
        """
        return RollDice.roll100double() <= self._critical_chance()

    def is_evading(self) -> bool:
        evasion_chance = 2 + (35 - 2) * self._dexterity / 100
        return RollDice.roll100double() <= evasion_chance
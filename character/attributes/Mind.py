from character.attributes.Attribute import Attribute


class Mind(Attribute):
    def __init__(self, stat):
        super().__init__(stat)
        self.mana = stat

    def use_mana(self, required_mana) -> bool:
        if required_mana > self.mana:
            return False
        else:
            self.mana -= required_mana
            return True

    def regen_mana(self, add_mana):
        if (self.mana + add_mana) > self.stat:
            self.mana = self.stat
        else:
            self.mana += add_mana

    def mind_attacked(self):
        # TODO
        pass
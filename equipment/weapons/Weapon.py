from equipment.Equipment import Equipment


class Weapon(Equipment):
    def __init__(self, name: str, damage: int):
        super().__init__(name, damage)
        self.drawn = True

    def draw(self):
        self.drawn = True

    def undraw(self):
        self.drawn = False

    def normal_attack(self):
        if self.drawn:
            return self.value
        else:
            print("Draw your weapon first!")
            return 0
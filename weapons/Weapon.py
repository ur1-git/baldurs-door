class Weapon:
    def __init__(self, name: str, damage: int):
        self.name = name
        self._damage = damage
        self.drawn = False

    def draw(self):
        self.drawn = True

    def undraw(self):
        self.drawn = False

    def normal_attack(self):
        if self.drawn:
            return self._damage
        else:
            print("Draw your weapon first!")
            return 0
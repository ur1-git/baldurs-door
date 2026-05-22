class Attribute:
    def __init__(self, stat):
        self.stat = stat

    def improve_stat(self, amount: int = 1):
        self.stat += amount
class Armor:
    def __init__(self, name: str, block_reduction: float):
        """
        :param name:
        :param block_reduction: should be a float between 0 and 1 as 0.35, 0.6...
        """
        self.name = name
        self.block_reduction = block_reduction
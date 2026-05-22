
from items.Item import Item


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        for each_item in self.items:
            if each_item.name == item.name:
                each_item.add_one()
        self.items.append(item)

    def use_item(self, item_name: str, character: Character):
        for item in self.items:
            if item_name == item.name:
                item.use(character)
                self.items = [item1 for item1 in self.items if not item1.destroy]
                return
        print("You dont have any ", item_name)

    def look(self):
        for item in self.items:
            print(item.name, ": ", item.quantity)
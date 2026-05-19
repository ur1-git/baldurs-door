from Character import Character
from weapons.SwordCatalog import SwordCatalog

if __name__ == '__main__':
    sword_catalog = SwordCatalog()
    player = Character("Thyrion", 100, sword_catalog.create_weapon("iron_sword"))
    enemies = []
    enemies.append(Character("Orc", 20, sword_catalog.create_weapon("wood_sword")))
    enemies.append(Character("Bandit", 10, sword_catalog.create_weapon("iron_sword")))

    player.attack(enemies[1])


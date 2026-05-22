
from character.Player import Player
from character.attributes.Shop import Shop
from items.HealthPotion import HealthPotion
from equipment.weapons.SwordCatalog import SwordCatalog

if __name__ == '__main__':
    sword_catalog = SwordCatalog()
    player = Player("Thyrion")
    enemies = []
    enemies.append(Player("Orc"))
    enemies.append(Player("Bandit"))

    shop = Shop()

    player.status()
    player.constitution.improve_stat(30)

    player.weapon_attack(enemies[1])
    player.inventory.add_item(HealthPotion("health_potion_III", 50))

    player.status()

    player.use_inventory_item("health_potion_III")
    shop.buy_armor("leather_armor", player)

    player.status()
from inventory import Inventory


class Square:

    def __init__(self, message=None):
        self.loot = Inventory()
        self.message = message

    def can_move(self, game, player, direction):
        return None

    def event(self, game, player, event):
        if event == "arrive":
            if self.loot:
                game.log(player, "Найдены предметы: {}".format(self.loot))
                player.inventory.update(self.loot)
                self.loot = Inventory()
            if self.message:
                game.log(self.message)

class Minotaur(Square):
    def arrive(self, game, player):
        game.log("Вы попались МИНОТАВРУ. Жуткий конец.")
        player.die(game)

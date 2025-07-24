from inventory import Inventory
from exceptions import GameEnded


class Square:

    def __init__(self, message=None, objects=None):
        if objects:
            self.loot = Inventory(objects)
        else:
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

    def __str__(self):
        return type(self).__name__


class Minotaur(Square):
    def event(self, game, player, event):
        if event == "arrive":
            game.log("Вы попались МИНОТАВРУ. Жуткий конец.")
            die_for_real = player.die(game)
            if die_for_real and 'сокровище' in self.loot:
                game.log("Сокровищем завладел МИНОТАВР. Игра окончена.")
                raise GameEnded()

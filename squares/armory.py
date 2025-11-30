from .square import Square
from events import PlayerArrive

class Armory(Square):
    obj = "патрон"
    count = 3

    def event(self, game, player, event):
        super(Armory, self).event(game, player, event)
        if isinstance(event, PlayerArrive):
            while player.inventory.count(self.obj) < self.count:
                player.inventory.add(self.obj)
            game.log(
                player, "Вы попали на склад - теперь у вас есть {} x{}".format(self.obj, self.count))

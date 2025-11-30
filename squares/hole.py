from .square import Square
from events import PlayerArrive

class Hole(Square):

    def __init__(self, target, **kwargs):
        super(Hole, self).__init__(**kwargs)
        self.target = target

    def event(self, game, player, event):
        super(Hole, self).event(game, player, event)
        if isinstance(event, PlayerArrive):
            game.log(player, "Вы попали в ДЫРУ.")
            player.position = self.target

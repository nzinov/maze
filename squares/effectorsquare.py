from .square import Square
from events import PlayerArrive

class EffectorSquare(Square):

    def __init__(self, effect_class, **kwargs):
        super(EffectorSquare, self).__init__(**kwargs)
        self.effect_class = effect_class

    def event(self, game, player, event):
        super(EffectorSquare, self).event(game, player, event)
        if isinstance(event, PlayerArrive):
            player.add_effect(game, self.effect_class())

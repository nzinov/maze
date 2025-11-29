from .effect import ExpiringEffect
from events import AfterChose, AfterMove
from constants import DIRECTIONS


class Confusion(ExpiringEffect):
    INVERSE_DIRECTIONS = {'в': 'н', 'н': 'в', 'л': 'п', 'п': 'л'}

    def __init__(self, time):
        self.time = time

    def expire(self, game, player):
        game.log(player, "Стоп, куда это Вы только что сходили?")

    def event(self, game, player, event):
        if isinstance(event, AfterChose):
            if event.action in DIRECTIONS:
                event.action = self.INVERSE_DIRECTIONS[event.action]
                return True
        elif isinstance(event, AfterMove):
            event.direction = tuple(d * -1 for d in event.direction)
            return True
        else:
            super().event(game, player, event)

    def __str__(self):
        return 'Confusion({})'.format(self.time)

from .effect import ExpiringEffect
from events import AfterChoice, AfterItemChoice, AfterMove
from constants import DIRECTIONS


class Confusion(ExpiringEffect):
    INVERSE_DIRECTIONS = {'в': 'н', 'н': 'в', 'л': 'п', 'п': 'л'}

    def __init__(self, time):
        self.time = time
        self.initial_time = time
        self.move_count = 0
        self.item_count = 0

    def expire(self, game, player):
        if self.move_count + self.item_count > 0:
            mes = 'Вы оглядываетесь назад, чешете затылок и думаете: "'
            if self.move_count > 0:
                mes += 'Куда это я ходил последние раунды? '
            if self.item_count > 0:
                mes += 'И в каком направлении предметы применял? '
            mes += 'Вроде хотел в другую сторону..."'
            game.log(player, mes)

    def event(self, game, player, event):
        if isinstance(event, AfterChoice) or isinstance(event, AfterItemChoice):
            if event.action in DIRECTIONS:
                if isinstance(event, AfterChoice):
                    self.move_count += 1
                elif isinstance(event, AfterItemChoice):
                    self.item_count += 1
                event.action = self.INVERSE_DIRECTIONS[event.action]
                return True
        elif isinstance(event, AfterMove):
            if self.initial_time != self.time:
                event.direction = tuple(d * -1 for d in event.direction)
                return True
        else:
            return super().event(game, player, event)

    def __str__(self):
        return 'Confusion({})'.format(self.time)

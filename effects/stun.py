from .effect import ExpiringEffect
from events import PlayerStartTurn, EffectStart, PlayerMove


class Stun(ExpiringEffect):

    def __init__(self, time, damage=-10):
        self.time = time + 1
        self.damage = damage
        assert damage < 0

    def event(self, game, player, event):
        if isinstance(event, PlayerStartTurn):
            game.log(player, "Вы пропускаете ход")
            player.event(game, PlayerMove())
            game.next_move()
        elif isinstance(event, EffectStart):
            player.change_health(game, self.damage)
        else:
            super().event(game, player, event)

    def __str__(self):
        return 'Stun({})'.format(self.time)

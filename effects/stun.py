from .effect import Effect


class Stun(Effect):

    def __init__(self, time, damage=-10):
        self.time = time
        self.damage = damage
        assert damage < 0

    def event(self, game, player, event):
        if event == "before_move":
            game.log("Вы пропускаете ход")
            self.time -= 1
            if self.time == 0:
                self._expire(player)
            game.next_move()
        elif event == "start":
            player.change_health(game, self.damage)
        else:
            super(Stun, self).event(game, player, event)

    def __str__(self):
        return 'Stun({})'.format(self.time)

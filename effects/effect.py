class Effect:

    def __init__(self):
        pass

    def event(self, game, player, event):
        pass

    def _expire(self, player):
        try:
            player.effects.remove(self)
        except ValueError:
            pass


class ExpiringEffect(Effect):
    time = 1

    def __init__(self):
        self.time = type(self).time

    def expire(self, game, player):
        pass

    def event(self, game, player, event):
        if event == "move":
            self.time -= 1
            if self.time <= 0:
                self.expire(game, player)
                self._expire(player)

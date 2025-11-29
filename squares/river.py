from .square import Square


class River(Square):

    def __init__(self, direction, **kwargs):
        super(River, self).__init__(**kwargs)
        self.direction = direction

    def event(self, game, player, event):
        super(River, self).event(game, player, event)
        if event == "start_round":
            player.position += self.direction
            player.event(game, "arrive")

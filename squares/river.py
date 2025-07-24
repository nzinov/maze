from .square import Square


class River(Square):

    def __init__(self, destination, **kwargs):
        super(River, self).__init__(**kwargs)
        self.destination = destination

    def event(self, game, player, event):
        super(River, self).event(game, player, event)
        if event == "start_turn":
            player.position = self.destination
            player.event(game, "arrive")

from .square import Square


class Exit(Square):

    def __init__(self, direction, **kwargs):
        super(Exit, self).__init__(**kwargs)
        self.direction = direction

    def can_move(self, game, player, direction):
        if direction == self.direction:
            if "сокровище" in player.inventory:
                game.log("Вы вышли из лабиринта. Победа!")
                game.win(player)
            else:
                game.log("Вы уперлись в закрытую дверь")
        return None

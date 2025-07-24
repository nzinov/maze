from .square import Square


class PoisonCloud(Square):

    def __init__(self, damage=-20, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage
        assert damage < 0

    def event(self, game, player, event):
        super().event(game, player, event)
        if event == "arrive":
            game.log("Вы вошли в комнату, заполненную ядовито-зеленым газом")
        if event == "before_move":
            game.log("*Кхе-кхе*, чертов газ!")
            player.change_health(game, self.damage)

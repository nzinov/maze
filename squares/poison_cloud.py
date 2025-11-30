from .square import Square
from events import PlayerArrive, PlayerStartTurn

class PoisonCloud(Square):

    def __init__(self, damage=-20, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage
        assert damage < 0

    def event(self, game, player, event):
        super().event(game, player, event)
        if isinstance(event, PlayerArrive):
            game.log("Вы вошли в комнату, заполненную ядовито-зеленым газом")
        if isinstance(event, PlayerStartTurn):
            game.log("*Кхе-кхе*, чертов газ!")
            player.change_health(game, self.damage)

from .common_object import Object, register_object
from squares import River


@register_object("скакалка")
class JumpingRope(Object):
    "прыгать - проверить: земля ли под вами?"
    @staticmethod
    def action(game, player, action):
        if action == "прыгать":
            if isinstance(game.field[player.position], River):
                game.log(player, "Вы прыгаете и слышите плеск воды")
            else:
                game.log(player, "Вы попрыгали. Кажется, под вами и правда земля")
            return False

from constants import DIRECTIONS
from .common_object import Object, register_object


@register_object("патрон")
class Bullet(Object):
    "в/н/л/п - выстрелить в заданую сторону"
    @staticmethod
    def action(game, player, action):
        if action in DIRECTIONS:
            position = player.position
            direction = DIRECTIONS[action]
            while True:
                hit = False
                for other in game.players:
                    if other.position == position and player.name != other.name:
                        hit = True
                        game.log("Вы попали в игрока {}".format(other.name))
                        other.change_health(game, -40)
                if hit:
                    return True
                if game.field.can_move(position, direction):
                    position += direction
                else:
                    game.log("Вы промазали")
                    return True

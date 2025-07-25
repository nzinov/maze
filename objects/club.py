from .common_object import Object, register_object
from constants import DIRECTIONS


@register_object("дубина")
class Club(Object):
    "Такой суковатой дубиной кого угодно с места сшибешь. в/н/л/п - ударить в заданую сторону"
    @staticmethod
    def action(game, player, action):
        if action in DIRECTIONS:
            hit = False
            direction = DIRECTIONS[action]
            for other in game.players:
                if player.name != other.name and (other.position == player.position
                                                  or other.position == player.position + direction):
                    game.log("Вы попали игроку {} прямо по голове".format(other.name))
                    hit = True
                    if game.field.can_move(other.position, direction):
                        other.position += direction
                        other.event(game, "arrive")
                        other.change_health(game, -20)
            if not hit:
                game.log("Дубина со свистом рассекла воздух")
            return False

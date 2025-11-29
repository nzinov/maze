from constants import DIRECTIONS
from .common_object import Object, register_object


@register_object("рейлган")
class Railgun(Object):
    "Похоже, мощная пушка. Хм, индикатор мигает красным, заряда осталось мало? в/н/л/п - выстрелить в заданую сторону"
    @staticmethod
    def action(game, player, action):
        if action in DIRECTIONS:
            position = player.position
            direction = DIRECTIONS[action]
            while True:
                for other in game.players:
                    if other.position == position and player.name != other.name:
                        game.log("Вы попали в игрока {}".format(other.name))
                        other.die(game)
                if not game.field.is_legal(position + direction):
                    game.log("Вот это да, эту стену даже рейлган не берет!")
                    return True
                elif game.field.can_move(position, direction):
                    position += direction
                else:
                    game.log("Вay, стены как не бывало!")
                    game.field.destroy_wall(position, direction)

from .common_object import Object, register_object
from position import Position


@register_object("компас")
class Compass(Object):
    "Похоже на компас, только указатель стрелки золотой. Может 'проверить', куда показывает?"
    @staticmethod
    def get_direction(player, treasure_position):
        y_dir = ""
        if treasure_position.y() > player.position.y():
            y_dir = "восток"
        elif treasure_position.y() < player.position.y():
            y_dir = "запад"
        x_dir = ""
        if treasure_position.x() > player.position.x():
            x_dir = "юг"
        elif treasure_position.x() < player.position.x():
            x_dir = "север"
        return 'о-'.join([d for d in [x_dir, y_dir] if d])

    @classmethod
    def action(cls, game, player, action):
        if action == 'проверить':
            if "сокровище" in player.inventory:
                game.log("Компас указывает на вашу сумку. А, ну да.")
                return False
            treasure_position = None
            for other in game.players:
                if other.position.field == player.position.field and "сокровище" in other.inventory:
                    treasure_position = other.position
                    break
            for x, row in enumerate(game.field.fields[player.position.field].squares):
                for y, square in enumerate(row):
                    if "сокровище" in square.loot:
                        treasure_position = Position(player.position.field, x, y)
                        break
            if treasure_position is None:
                game.log("Стрелка крутится по кругу, странно...")
                return False
            else:
                direction = cls.get_direction(player, treasure_position)
                if direction:
                    game.log("Стрелка указывает на " + direction)
                else:
                    game.log("Оно совсем рядом, прямо перед вами!")
                return False

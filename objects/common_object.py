class Object:
    "это обычный предмет"
    pass

OBJECTS = {}


def register_object(name, cls=None):
    def helper(cls):
        OBJECTS[name] = cls
        return cls
    if cls is None:
        return helper
    else:
        return helper(cls)

register_object("сокровище", Object)

@register_object("посох")
class Bullet(Object):
    "Это древний артефакт - Посох Несчастного Лурьехи. Кажется, если им 'махнуть', что-то произойдет"
    @staticmethod
    def action(game, player, action):
        if action == "махнуть":
            if not hasattr(player, 'cock'):
                game.log("Вы взмахнули посохом - и стены лабиринта огласил дурацкий смех.")
                player.name = "Петух {}".format(player.name)
                player.cock = True
            else:
                game.log('"Петух! Петух!" - раздается голос из ниоткуда, и опять звучит странный смех.')
            return False

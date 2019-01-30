FIELD = """
3
8
 : | :V: |W:R:M
.+.+.+.+.+.+.+.
 :^: : : : :R:R
.+.+.+.+.+=+.+=
 | :B| : |G: : 
.+.+=+.+=+.+.+.
 : : : : : | : 
.+.+.+.+=+.+.+=
W: : : :<: :V: 
=+.+=+.+=+.+.+.
G: : : |T| | :W
=+=+.+=+.+.+.+=
>:Z: : | : |A: 
.+.+.+.+=+=+.+.
@: :E: : : : : 
4
 :G: : 
.+.+.+.
 :O:D: 
.+=+.+.
>: :<: 
.+.+.+.
 |^| : 
3
T:M:T
.+.+.
T:O:T
.+.+.
T:E:T
T Stuff({"сокровище": 1})
E Exit(DOWN)
M Minotaur()
R Square("Вы слышите РЫК МИНОТАВРА!")
W Stuff({"посох": 1})
A Hole((2, 2))
B Hole((6, 6))
G Armory()
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
V RubberRoom(DOWN)
Z EffectorSquare(lambda: Sleep(7, 1, (1, 1)))
D EffectorSquare(lambda: Sleep(4, 2, (1, 1)))
@ EffectorSquare(lambda: Stun(3), "Вы попали в ловушку!")
"""
from squares import Square
from objects import register_object, Object
class Minotaur(Square):
    def arrive(self, game, player):
        game.log("Вы попались МИНОТАВРУ. Жуткий конец.")
        player.die(game)

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

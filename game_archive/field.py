"""3
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
T Square(objects={"сокровище": 1})
E Exit(DOWN)
M Minotaur()
R Square(messages={"end_turn": "Вы слышите РЫК МИНОТАВРА!"})
W Square(objects={"посох": 1})
A Hole(Position(0, 2, 2))
B Hole(Position(0, 6, 6))
G Armory()
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
V RubberRoom(DOWN)
Z EffectorSquare(lambda: Sleep(7, Position(1, 1, 1)))
D EffectorSquare(lambda: Sleep(4, Position(2, 1, 1)))
@ EffectorSquare(lambda: Stun(3), messages={"arrive": "Вы попали в ловушку!"})
"""

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

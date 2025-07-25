"""3
5
S.T.P.<|X
.+=+.+=+.
Q.R.Z..|A
=+.+=+.+.
M.R.W....
.+.+.+=+.
R.R|..>..
.+=+.+.+.
L.<|C|^.D
5
S.E.P.<|N
.+=+.+=+.
I.R.Z..|A
=+.+=+.+.
M.R......
.+.+.+=+.
R.R|..<..
.+=+.+.+.
Y.<|C|^.D
5
..T.....H
.+=+.+=+.
R.R....|A
=+.+=+.+.
M.R.W....
.+.+.+=+.
R.R|..<..
.+=+.+.+.
K.<|C|^.D
T Square(objects={"сокровище": 1})
E Exit(UP)
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
Q RubberRoom(RIGHT, message="Вы слышите РЫК МИНОТАВРА!")
I RubberRoom(UP, message="Вы слышите РЫК МИНОТАВРА!")
X Hole(Position(1, 4, 0))
Y Hole(Position(0, 0, 4))
L Hole(Position(1, 0, 4))
N Hole(Position(0, 4, 0))
H Hole(Position(2, 4, 0))
K Hole(Position(2, 0, 4))
M Minotaur()
R Square("Вы слышите РЫК МИНОТАВРА!")
P PoisonCloud()
Z EffectorSquare(lambda: Sleep(5, Position(2, 1, 2)))
S EffectorSquare(lambda: Stun(3, -25), message="Вы попали в ловушку!")
W Square(objects={"посох": 1})
D Square(objects={"дубина": 1})
C Square(objects={"компас": 1})
A Armory()
"""

"""5
4
 . .>.E
.+.+=+.
 | .<|V
.+.+.+.
 .>. .W
.+=+.+.
1. . |A
4
3. |Z.2
.+.+.+.
J| . |.
.+.+=+.
S. . ..
=+=+.+=
R. .S.A
4
K| . .5
.+.+=+.
 | . |J
.+.+.+=
 .C| .C
=+.+.+.
A.C. .4
4
0.9.<.T
.+.+.+.
9.8. .8
.+.+.+.
9. . |7
.+.+.+.
6.J| .7
6
 . . . . ..
.+.+.+.+.+.
 . . . . ..
.+.+.+.+.+.
 . .D. .V..
.+.+.+.+.+.
 | | . . .I
.+.+=+.+.+.
 . . . .^..
.+.+.+.+.+.
 . . . . ..
T Square(objects={"сокровище": 1})
E Exit(UP, objects={"компас": 1})
I Exit(RIGHT)
1 Hole(Position(1, 0, 3))
2 Hole(Position(0, 3, 0))
3 Hole(Position(2, 3, 3))
4 Hole(Position(1, 0, 0))
5 Hole(Position(3, 3, 0))
6 Hole(Position(2, 0, 3))
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
V RubberRoom(DOWN)
A Armory()
W Square(objects={"посох": 1})
K Square(objects={"компас": 1})
J Square(objects={"скакалка": 1})
Z EffectorSquare(lambda: Sleep(6, Position(4, 2, 4)))
S EffectorSquare(lambda: Sleep(6, Position(4, 4, 4)))
C EffectorSquare(lambda: Confusion(4), messages={"player_arrive": "Вы чувствуете себя... как-то странно"})
7 River(UP)
8 River(LEFT)
9 River(DOWN)
0 River(RIGHT, objects={"бутылка": 1})
R Square(objects={"рейлган": 2})
D EffectorSquare(lambda: Stun(1, -300))
"""

"""2
8
a: : |B| : :X:d
=+=+.+ +.+.+.+.
E: | : :D: | :V
=+.+.+.+ +.+.+.
A:X|>: :<|B: :C
.+.+.+=+=+=+=+.
 |R|3: :Z:R:X: 
.+.+.+=+.+.+.+.
V: :2|T| : | : 
.+.+.+=+.+=+.+.
X: |1: : |B: :X
.+.+=+=+.+.+=+ 
B| : :C| : | :A
=+.+.+.+.+=+ +=
b: :<:X:  B: :c
4
 : :>:<
.+.+.+.
 : : : 
.+=+.+.
 :B:T: 
=+.+.+.
E: : :^
B Square(objects={"бутылка": 1})
E Exit(LEFT)
T Square(objects={"сокровище": 1})
A Armory()
X Square(objects={"зачарованная_бутылка": 1})
C Square(objects={"дубина": 1})
R Square(objects={"скакалка": 1})
Z EffectorSquare(lambda: Sleep(7, Position(1, 3, 2)))
D EffectorSquare(lambda: Sleep(4, Position(1, 0, 3)))
a Hole(Position(0, 7, 7))
b Hole(Position(0, 0, 7))
c Hole(Position(0, 0, 0))
d Hole(Position(0, 7, 0))
1 River(Position(0, 4, 2))
2 River(Position(0, 3, 2))
3 River(Position(0, 2, 2))
V RubberRoom(DOWN)
^ RubberRoom(UP)
> RubberRoom(RIGHT)
< RubberRoom(LEFT)
"""

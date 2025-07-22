class Position:

    def __init__(self, field, x, y=None):
        pos = x
        if y is not None:
            pos = (x, y)
        self.field = field
        self.pos = pos

    def __eq__(self, other):
        if not isinstance(other, Position):
            raise TypeError()
        return self.field == other.field and \
            self.pos == other.pos

    def __add__(self, other):
        if not isinstance(other, tuple):
            raise TypeError()
        return Position(self.field,
                        self.pos[0] + other[0],
                        self.pos[1] + other[1])

    def x(self):
        return self.pos[0]

    def y(self):
        return self.pos[1]

    def __str__(self):
        return str((self.field,) + self.pos)

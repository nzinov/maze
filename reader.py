from collections import defaultdict
from squares import *
from effects import *
from objects import *
from custom import *
from game import Subfield, Field
from position import Position
import io
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)


def read_field(fname):
    # solution from http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    import importlib.util
    print(fname)
    spec = importlib.util.spec_from_file_location("custom", fname)
    custom = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom)
    for name, obj in custom.__dict__.items():
        globals()[name] = obj
    f = io.StringIO(custom.__doc__)
    subfield_number = int(f.readline())
    field = Field([])
    keys = defaultdict(lambda: [])
    for i in range(subfield_number):
        size = int(f.readline())
        squares = [[None for i in range(size)] for j in range(size)]
        hwalls = [[None for i in range(size)] for j in range(size - 1)]
        vwalls = [[None for i in range(size - 1)] for j in range(size)]
        for x in range(size):
            row = f.readline()
            for y in range(size):
                symbol = row[2 * y]
                if symbol in [".", " ", "O"]:
                    squares[x][y] = Square()
                else:
                    keys[symbol].append(Position(i, x, y))
                if y != size - 1:
                    vwalls[x][y] = row[2 * y + 1] == "|"
            if x != size - 1:
                row = f.readline()
                for y in range(size):
                    hwalls[x][y] = row[2 * y] == "="
        field.fields.append(
            Subfield(size, squares, vwalls=vwalls, hwalls=hwalls))
    while True:
        row = f.readline()
        if not row:
            break
        symbol = row[0]
        if not keys[symbol]:
            print("Warning: '{}' is never used".format(symbol))
        for pos in keys[symbol]:
            square = eval(row[1:])
            if not isinstance(square, Square):
                print("Warning: got {} not Square for symbol '{}'".format(type(square), symbol))
            field.fields[pos.field].squares[pos.x()][pos.y()] = square
        del keys[symbol]
    if keys:
        print("Warning, undefined symbols: ", ", ".join(keys.keys()))
    descr = f.readline()
    if descr == "":
        descr = None
    else:
        descr = descr[:-1]
    field.description = descr
    return field

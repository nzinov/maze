"""
Generates a template for a field.
Usage: generate.py [size1 size2 ...]

size: int - size of the corresponding field
"""
from sys import argv
VWALL = ":"
HWALL = "."
ROOM = " "
CROSS = "+"
print('"""', end="")
n = list(map(int, argv[1:]))
print(len(n))
for el in n:
    print(el)
    for i in range(el - 1):
        print((ROOM + VWALL) * (el - 1) + ROOM)
        print((HWALL + CROSS) * (el - 1) + HWALL)
    print((ROOM + VWALL) * (el - 1) + ROOM)
print('"""')

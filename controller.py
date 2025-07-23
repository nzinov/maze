from game import Game, Field, GameEnded
from player import Player
from reader import read_field
from position import Position


class Controller:

    def __init__(self):
        print("Введите имя файла с полем: ", end="")
        fname = input()
        field = read_field(fname)
        print("Поле имеет размеры {0}x{0}".format(field.fields[0].size))
        print("Введите имена игроков через пробел: ", end="")
        players = input().split()
        while True:
            print("Введите позиции игроков в формате x:y через пробел: ", end="")
            positions = list(
                map(lambda x: tuple(map(int, x.split(":"))), input().split()))
            if len(positions) == len(players) and all([field.fields[0].is_legal(Position(0, el)) for el in positions]):
                break
            else:
                print("Недопустимые стартовые позиции!")
        players = [Player(name, Position(0, pos, ind))
                   for ind, (name, pos) in enumerate(zip(players, positions))]
        self.game = Game(self, field, players)

    def loop(self):
        try:
            while True:
                print("Введите команду: ", end="")
                action = input()
                self.game.action(action)
        except GameEnded:
            pass

    def log(self, message):
        print(message)

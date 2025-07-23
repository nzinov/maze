#!/usr/bin/python3
"""
Launch the game and create a test file based on it
Usage: generate_test.py field_file test_file [field x y...]
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game import Game, Field, GameEnded
from player import Player
from reader import read_field
from position import Position
from sys import argv, exit


class Controller:

    def __init__(self, field_file, test_file, positions):
        self.test_file = open(test_file, "w")
        print(field_file, file=self.test_file)
        print(len(positions), file=self.test_file)
        for el in positions:
            print(el.field, el.x(), el.y(), file=self.test_file)
        field = read_field(field_file)
        players = [Player(str(player_ind), pos, player_ind)
                   for player_ind, pos in enumerate(positions)]
        self.game = Game(self, field, players)

    def loop(self):
        try:
            while True:
                print("Введите команду: ", end="")
                action = input()
                print(">>>{}".format(action), file=self.test_file)
                self.game.action(action)
        except GameEnded:
            pass
        self.test_file.close()

    def log(self, message):
        print(message)
        print(message, file=self.test_file)


if __name__ == "__main__":
    if len(argv) < 3 or (len(argv) - 3) % 3 != 0:
        print("Invalid number of arguments.")
        exit(1)
    field_file = argv[1]
    test_file = argv[2]
    positions = []
    for i in range((len(argv) - 3) // 3):
        positions.append(Position(*map(int, argv[3 * i + 3: 3 * i + 6])))
    Controller(field_file, test_file, positions).loop()

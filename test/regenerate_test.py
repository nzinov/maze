#!/usr/bin/python3
"""
Regenerate test after protocol change
Usage: regenerate_test.py test_file
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

    def __init__(self, test_file):
        self.test_file = open(test_file, "r")
        self.output = open("{}.new".format(test_file), "w")
        field_file = self.test_file.readline()[:-1]
        print(field_file, file=self.output)
        field = read_field(field_file)
        player_number = int(self.test_file.readline())
        print(player_number, file=self.output)
        players = []
        for i in range(player_number):
            line = self.test_file.readline()[:-1]
            players.append(Player(str(i), Position(*map(int, line.split())), i))
            print(line, file=self.output)
        self.game = Game(self, field, players)

    def loop(self):
        try:
            for line in self.test_file:
                action = line.strip()
                if not action:
                    break
                if action[:3] == ">>>":
                    print(action, file=self.output)
                    action = action[3:]
                    self.game.action(action)
            while True:
                print("Введите команду: ", end="")
                action = input()
                print(">>>{}".format(action), file=self.output)
                self.game.action(action)
        except GameEnded:
            print("Successfuly regenerated!")
        self.output.close()

    def log(self, message):
        print(message)
        print(message, file=self.output)


if __name__ == "__main__":
    if len(argv) < 1:
        print("Invalid number of arguments.")
        exit(1)
    test_file = argv[1]
    Controller(test_file).loop()

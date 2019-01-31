#!/usr/bin/python3
"""
Launch recorder test
Usage: test.py test_file
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from game import Game, Field, GameEnded
from player import Player
from reader import read_field
from position import Position
from sys import argv, exit


class TestFailed(Exception):
    pass


class Controller:

    def __init__(self, test_file):
        self.test_file = open(test_file, "r")
        field_file = self.test_file.readline()[:-1]
        field = read_field(field_file)
        player_number = int(self.test_file.readline())
        players = []
        for i in range(player_number):
            players.append(Player(str(i), Position(
                *map(int, self.test_file.readline().split()))))
        self.game = Game(self, field, players)

    def test(self):
        try:
            while True:
                action = self.test_file.readline()[:-1]
                if not action:
                    break
                if action[:3] != ">>>":
                    print("Expected action got {}".format(action))
                    return False
                action = action[3:]
                self.game.action(action)
        except GameEnded:
            pass
        except TestFailed:
            return False
        print("OK!")
        return True

    def log(self, message):
        answer = self.test_file.readline()[:-1]
        if answer != message:
            print("{} != {}".format(answer, message))
            raise TestFailed()


def run_test(test_file):
    return Controller(test_file).test()

if __name__ == "__main__":
    if len(argv) < 1:
        print("Invalid number of arguments.")
        exit(1)
    test_file = argv[1]
    run_test(test_file)

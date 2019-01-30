#!/bin/python3
from test.test import run_test
from reader import read_field
from sys import exit
import os
failed = 0
run = 0
os.chdir("test/")
for test_file in os.listdir(path='.'):
    if test_file.endswith(".test"):
        print("Running {}".format(test_file))
        run += 1
        if not run_test(test_file):
            failed += 1
os.chdir("..")
for field in os.listdir(path='game_archive/'):
    if field.endswith(".py"):
        print("Loading {}".format(field))
        read_field(field)
print("Run {}, failed {}".format(run, failed))
if failed > 0:
    exit(1)

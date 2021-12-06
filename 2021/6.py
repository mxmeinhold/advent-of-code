#! /bin/python3

import sys
from functools import lru_cache

with open(sys.argv[1], 'r') as in_file:
    # a lanternfish in this list is represented by it's timer
    lanternfish = list(map(int, next(in_file).split(',')))

### Part 1 ###

def handle():
    """ Apply a day to the list """
    new_lanternfish = []
    for i in range(len(lanternfish)):
        lanternfish[i] -= 1
        if lanternfish[i] == -1:
            lanternfish[i] = 6
            new_lanternfish.append(8)
    lanternfish.extend(new_lanternfish)

for i in range(80):
    handle()

print(f'Part 1: {len(lanternfish)}')

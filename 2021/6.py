#! /bin/python3

import sys
from functools import lru_cache

with open(sys.argv[1], 'r') as in_file:
    # a lanternfish in this list is represented by it's timer
    lanternfish = list(map(int, next(in_file).split(',')))

@lru_cache
def predict(timer: int, days: int) -> int:
    """
    Get the number of lanternfish there will be after days days if this is the
    only lantern fish, and it's timer is timer.

    Since there's only 9 possible timer values for each possible day, we gain a
    lot by doing memoization as we recurse and the tree expands.
    """
    if days == 0:
        return 1

    if timer == 0:
        return predict(6, days-1) + predict(8, days-1)

    return predict(timer-1, days-1)

print('Part 1: ', sum(map(lambda timer: predict(timer, 80), lanternfish)))
print('Part 2: ', sum(map(lambda timer: predict(timer, 256), lanternfish)))

#!/bin/python3

# Day 5
# take a string. If a letter is adjacent to it's uppercase, remove both.
# Done when no such pairs remain

def verify(polymer):
    i = len(polymer) - 1
    while i > 0:
        if polymer[i] != polymer[i - 1] and polymer[i].upper() == polymer[i - 1].upper():
            return False
        i -= 1
    return True

def collapse(polymer):
    while not verify(polymer):
        i = len(polymer) - 1
        while i > 0:
            if polymer[i] != polymer[i - 1] and polymer[i].upper() == polymer[i - 1].upper():
                polymer = polymer[:i - 1] + polymer[i + 1:]
                i -= 1
            i -= 1
    return polymer

import sys
polymer = next(open(sys.argv[1], 'r')).strip()

## Part 1 ##
# Collapse the polymer
part_1_polymer = polymer
print(len(collapse(part_1_polymer)))

## Part 2 ##
# Remove 1 type of unit (aA, bB, cC, etc.). Find the shortest polymer. 
import string
print(min(map(lambda c: len(collapse(polymer.replace(c, '').replace(c.upper(), ''))), string.ascii_lowercase)))

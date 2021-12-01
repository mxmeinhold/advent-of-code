#!/bin/python3

import sys

### Part 1 ###
# Given an ordered list of sea floor depths, count the number of relative increases

with open(sys.argv[1], 'r') as in_file:
    depths = list(map(int, in_file))

increased = 0
for i in range(1, len(depths)-1):
    if depths[i-1] < depths[i]:
        increased += 1

print(f'Part 1: {increased}')

### Part 2 ###
# Instead of looking at each depth, consider a sliding window of 3 measurements.
# Take the sum of each window, and count the number of relative increases

increased = 0
last = sum(depths[0:3])
for i in range(1, len(depths)-2):
    new = sum(depths[i:i+3])
    if last < new:
        increased += 1
    last = new

print(f'Part 2: {increased}')

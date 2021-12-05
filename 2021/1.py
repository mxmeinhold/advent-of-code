#!/bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    depths = list(map(int, in_file))

### Part 1 ###
# Given an ordered list of sea floor depths, count the number of relative increases

print(f'Part 1: {sum(map(lambda i: depths[i-1] < depths[i], range(1, len(depths))))}')

### Part 2 ###
# Instead of looking at each depth, consider a sliding window of 3 measurements.
# Take the sum of each window, and count the number of relative increases
# Since A+B+C < B+C+D is equivalent to A < D, we can skip the whole sum thing

print(f'Part 2: {sum(map(lambda i: depths[i] < depths[i+3], range(len(depths)-3)))}')


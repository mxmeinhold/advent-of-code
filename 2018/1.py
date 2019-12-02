#!/bin/python3

import sys

### Part 1 ###
# initial frequency is 0. Find final frequency if input is a string of changes

in_file = open(sys.argv[1], 'r')

change_list = list(map(int, in_file))

print(sum(change_list))


### Part 2 ###
# The change list loops. Find the first frequency that is repeated.

from itertools import accumulate, cycle

# accumulate [a, b, c] = a, a+b, a+b+c...
# cycle [a, b, c] = a, b, c, a, b, c....
freq_iter = accumulate(cycle(change_list))

seen = set()
print(next(freq
    for freq in freq_iter
    if freq in seen or seen.add(freq)))

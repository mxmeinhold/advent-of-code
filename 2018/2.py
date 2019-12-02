#!/bin/python3

def check(i):
    lets = dict()
    for let in i:
        if let not in lets:
            lets[let] = 0
        lets[let] += 1

    return (1 if 2 in lets.values() else 0, 1 if 3 in lets.values() else 0)

import sys

ids = list(map(lambda s: s.strip(), open(sys.argv[1], 'r')))

## Part 1 ##
# find a checksum by multiplying the number of ids with 2 of any letter and the number of ids with 3 of any letter
two = 0
three = 0
for i in ids:
    t2, t3 = check(i)
    two += t2
    three += t3
print(two*three)


## Part 2 ##
# find letters in common between 2 ids that differ by one charachter at the same index.
for index, i in enumerate(ids[:-1]):
    for j in ids[index + 1:]:
        diffs = 0
        for c_index, char in enumerate(i):
            if char != j[c_index]:
                diffs += 1
        if diffs == 1:
            print(i, j)

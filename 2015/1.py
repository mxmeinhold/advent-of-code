#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    data = list(in_file)

### Part 1 ###

part1 = 0

def handle(c) -> int:
    if c == '(':
        return 1
    if c == ')':
        return -1

print(f'Part 1: {sum(map(handle, data[0]))}')

### Part 2 ###

part2 = 0
c_num =0

for c in data[0]:
    c_num += 1
    part2 += handle(c)
    if part2 == -1:
        print(c_num)

print(f'Part 2: {part2}')

#! /bin/python3

import sys
from itertools import accumulate, chain

with open(sys.argv[1], 'r') as in_file:
    instrs = next(in_file).strip()

class point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # I'm gonna presume other is a point
        return point(self.x+other.x, self.y+other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return (self.x, self.y).__hash__()

    def __repr__(self):
        return f'point({self.x}, {self.y})'

dirs = {
    '^': point(0, 1),
    'v': point(0, -1),
    '<': point(-1, 0),
    '>': point(1, 0),
}

p = point(0,0)
houses = {p: 1}
for diff in map(dirs.get, instrs):
    p += diff
    houses[p] = houses.get(p, 0) + 1

print('Part 1:', len(houses))

dirs = {
    '^': point(0, 1),
    'v': point(0, -1),
    '<': point(-1, 0),
    '>': point(1, 0),
}

sp = point(0,0)
rp = point(0,0)
houses = {point(0,0): 2}
for i in range(0, len(instrs), 2):
    diff = dirs[instrs[i]]
    sp += diff
    diff = dirs[instrs[i+1]]
    rp += diff
    houses[sp] = houses.get(sp, 0) + 1
    houses[rp] = houses.get(rp, 0) + 1

print('Part 2:', len(houses))

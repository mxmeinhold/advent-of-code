#! /bin/python3

import sys

def filter_to_range(seq):
    for n in seq:
        if n <= 50 and n >= -50:
            yield n

with open(sys.argv[1], 'r') as in_file:
    cubes = dict()
    for line in in_file:
        mode, coords = tuple(line.strip().split(' '))
        xs, ys, zs = tuple(map(lambda l: list(range(int(l[0]), int(l[1])+1)), map(lambda c: c.split('=')[1].split('..'), coords.split(','))))
        for x in filter_to_range(xs):
            for y in filter_to_range(ys):
                for z in filter_to_range(zs):
                    cubes[(x, y, z)] = 1 if mode == 'on' else 0

print('Part 1:', sum(cubes.values()))

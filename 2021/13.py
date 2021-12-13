#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    a = ''.join(in_file).split('\n\n')
    coords = set(map(lambda l: tuple(map(int, l.strip().split(','))), a[0].splitlines()))
    instrs = list(map(str.strip, a[1].splitlines()))

for instr in instrs:
    line, num = tuple(instr.removeprefix('fold along ').split('='))
    num = int(num)

    new_coords = set()
    if line == 'x':
        for coord in coords:
            if coord[0] > num:
                new_coords.add( (num-(coord[0] - num), coord[1]))
            elif coord[0] != num:
                new_coords.add(coord)
    elif line == 'y':
        for coord in coords:
            if coord[1] > num:
                new_coords.add((coord[0], num - (coord[1]- num)))
            elif coord[1] != num:
                new_coords.add(coord)
    coords = new_coords
# I just commented these out to do part 2
    #break
#print(len(set(coords)))

x = max(map(lambda c: c[0], coords))
y = max(map(lambda c: c[1], coords))
out = [['.' for i in range(x+1)] for j in range(y+1)]

for c in coords:
    out[c[1]][c[0]] = '#'

print('\n'.join(map(''.join, out)))

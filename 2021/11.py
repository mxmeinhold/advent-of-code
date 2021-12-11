#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    src = map(int, ''.join(map(str.strip, in_file)))
    octopodes = {
        (r, c): next(src)
        for r in range(10)
        for c in range(10)
    }

part1 = 0

coords = lambda: {(r,c) for r in range(10) for c in range(10)}

def step():
    ''' Does a step. Returns False if all the octopodes flashed in sync '''
    flashed = set()
    not_flashed = coords()
    for c in not_flashed:
        octopodes[c] += 1

    while any(map(lambda c: octopodes[c] > 9, not_flashed)):
        for c in not_flashed:
            if octopodes[c] > 9:
                flashed.add(c)
                global part1
                part1 += 1

                for row in range(max(0, c[0]-1), min(9, c[0]+1)+1):
                    for col in range(max(0, c[1]-1), min(9, c[1]+1)+1):
                        octopodes[(row, col)] += 1

        not_flashed -= flashed

    for t in flashed:
        octopodes[t] = 0

    if len(flashed) == 100:
        return False

    return True


part2 = 1
while step():
    if part2 == 100:
        print('Part 1:', part1)
    part2 += 1

print('Part 2:', part2)

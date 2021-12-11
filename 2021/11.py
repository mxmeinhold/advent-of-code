#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    octopodes = list(map(lambda l: list(map(int, l.strip())), in_file))

part1 = 0

def step():
    ''' Does a step. Returns False if all the octopodes flashed in sync '''
    for r in range(10):
        for c in range(10):
            octopodes[r][c] +=1

    flashed = []
    while any(map(lambda l: any(map(lambda i: i>9, l)), octopodes)):
        for r in range(10):
            for c in range(10):
                if (r,c) in flashed:
                    octopodes[r][c] = 0
                    continue
                if octopodes[r][c] > 9:
                    flashed.append((r,c))
                    global part1
                    part1 += 1

                    for r2 in range(max(0, r-1), min(9, r+1)+1):
                        for c2 in range(max(0, c-1), min(9, c+1)+1):
                            octopodes[r2][c2] += 1
    for t in flashed:
        octopodes[t[0]][t[1]] = 0

    if len(flashed) == 100:
        return False

    return True


part2 = 1
while step():
    if part2 == 100:
        print('Part 1:', part1)
    part2 += 1

print('Part 2:', part2)

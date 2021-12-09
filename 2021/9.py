#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    heights = list(map(lambda l: list(map(int, l.strip())), in_file))

    low_heights = []
    for r in range(len(heights)):
        for c in range(len(heights[r])):
            if r != 0:
                if heights[r][c] >= heights[r-1][c]:
                    continue
            if r != len(heights)-1:
                if heights[r][c] >= heights[r+1][c]:
                    continue
            if c != 0:
                if heights[r][c] >= heights[r][c-1]:
                    continue
            if c != len(heights[0])-1:
                if heights[r][c] >= heights[r][c+1]:
                    continue
            low_heights.append(heights[r][c])

    basins = []
    r = 0
    c = 0

    def flood(r,c):
        if heights[r][c] != 9:
            neighs = []
            if r != 0:
                neighs.append((r-1,c))
            if r != len(heights)-1:
                neighs.append((r+1,c))
            if c != 0:
                neighs.append((r,c-1))
            if c != len(heights[0])-1:
                neighs.append((r,c+1))
            heights[r][c] = 9
            return sum(map(lambda t: flood(*t), neighs)) +1
        return 0

    basins = sorted(filter(lambda b: b!=0, (flood(r,c) for r in range(len(heights)) for c in range(len(heights[0])))))




print('Part 1:', sum(map(lambda h: h+1, low_heights)))

print('Part 2:', basins[-1] * basins[-2] * basins[-3])

#!/bin/python3

import sys, re

## Part 1 ##
# find the area of overlapping claims
# claim pattern: #123 @ 3,2: 5x4

# (id, (c,r), (w,h))
claims = [ (int(match.group(1)), (int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))) for match in
        re.finditer(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', "\n".join(map(lambda s: s.strip(), open(sys.argv[1])))) ]

from itertools import repeat

size = 1024
claims_grid = [ [ 0 for i in range(0, size) ] for j in range(0, size)]
overlap_grid = [ [ 0 for i in range(0, size) ] for j in range(0, size)]
overlapped = [ i + 1 for i in range(0, len(claims)) ]

for claim in claims:
    cid = claim[0]
    c,r = claim[1]
    w,h = claim[2]
    for row in range(r, r + h):
        for col in range(c, c + w):
            if claims_grid[row][col] == 0:
                claims_grid[row][col] = cid
            else:
                overlap_grid[row][col] = 1
                overlapped[cid - 1] = 0
                overlapped[claims_grid[row][col] - 1] = 0

print(sum(sum(l) for l in overlap_grid))

## Part 2 ##
# find the uninterrupted claim
print(list(filter(lambda x: x != 0, overlapped)))

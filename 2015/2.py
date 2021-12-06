#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    dims = list(map(lambda l: tuple(map(int, l.split('x'))), map(str.strip, in_file)))

def paper_area(l, w, h):
    sides = (l*w, w*h, h*l)
    return (
        2*sum(sides) # surface area
        + min(sides) # smallest side
    )

def ribbon_length(l, w, h):
    sides = (l+w, w+h, h+l)
    return 2*min(sides) + l*w*h

print('Part 1:', sum(map(lambda d: paper_area(*d), dims)), 'square feet')
print('Part 2:', sum(map(lambda d: ribbon_length(*d), dims)), 'feet')

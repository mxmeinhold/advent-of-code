#! /bin/python3

import sys

from typing import Iterable, Literal, Sequence, cast

Chr = Literal['#', '.']
Coord = tuple[int, int]
Image = dict[Coord, Chr]

with open(sys.argv[1], 'r') as in_file:
    algo: Sequence[Chr] = cast(Sequence[Chr], next(in_file).strip())
    next(in_file) # blank

    result = cast(Image, {
        (r, c): char
        for r, line in enumerate(map(str.strip, in_file))
        for c, char in enumerate(line)
    })

def adj(coord: Coord) -> Iterable[Coord]:
    """
    Get the coords adjacent to coord
    (8-connected, including coord, in the order needed for int conversion)
    """
    r, c = coord
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            yield (row, col)

def enhance_c(coord: Coord, image: dict[Coord, Chr], step: int) -> Chr:
    """ get the enhanced pixel for a given coord """
    return algo[int(''.join(
        map(
            lambda c: '1' if c == '#' else '0',
            map(
                lambda c: image.get(c, algo[0] if step % 2 == 0 else '.'),
                adj(coord)
            )
        )
    ), 2)]

def enhance(data: Image, step: int) -> Image:
    """ Enhance an image """
    out = {}
    coords = set()
    for d in data:
        coords |= set(adj(d))
    for d in coords:
        out[d] = enhance_c(d, data, step)
    return out

def debug(image: Image) -> None:
    """ Print an image for debugging purposes """
    maxc = max(map(lambda t: t[1], image.keys()))

    out = '\n'
    for coord in sorted(image.keys()):
        out += image[coord]
        if coord[1] == maxc:
            out += '\n'
    print(out)

#debug(result)

for i in range(2):
    result = enhance(result, i+1)
print('Part 1:', sum((1 if c == '#' else 0 for c in result.values())))
#debug(result)

for i in range(2, 50):
    result = enhance(result, i+1)
print('Part 2:', sum((1 if c == '#' else 0 for c in result.values())))

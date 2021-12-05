#! /bin/python3

# Needed to enable type annotations on class functions that use the enclosing type
from __future__ import annotations

import sys
from collections.abc import Iterable
from itertools import chain
from typing import Any, Optional

class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Coord):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def __str__(self) -> str:
        return f'Coord({self.x}, {self.y})'

    def __repr__(self) -> str:
        return str(self)

class VentLine:

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f'VentLine({self.left}, {self.right})'

    def __init__(self, line: str):
        left, right = tuple(line.split(' -> '))
        self.left = Coord(*map(int, left.split(',')))
        self.right = Coord(*map(int, right.split(',')))

        self.coords = set()
        x_diff = 1 if self.left.x < self.right.x else (0 if self.left.x == self.right.x else -1)
        y_diff = 1 if self.left.y < self.right.y else (0 if self.left.y == self.right.y else -1)
        c = self.left
        while c != self.right:
            self.coords.add(c)
            c = Coord(c.x+x_diff, c.y+y_diff)
        self.coords.add(self.right)

    def is_vertical(self) -> bool:
        return self.left.x == self.right.x

    def is_horizantal(self) -> bool:
        return self.left.y == self.right.y

    def overlap(self, other: VentLine) -> set[Coord]:
        return self.coords & other.coords

class Map:

    def __init__(self, vents: Iterable):
        self.vents = list(vents)

        self.coords = list(chain.from_iterable(map(lambda v: v.coords, self.vents)))

        self._map_cache: Optional[dict[Coord, int]] = None

    def num_overlaps(self) -> int:
        return sum(map(lambda i: i>1, self.map().values()))

    def map(self) -> dict[Coord, int]:
        if self._map_cache:
            return self._map_cache
        m: dict[Coord, int] = {}
        for c in self.coords:
            m[c] = m.get(c, 0) + 1

        self._map_cache = m
        return m

    def __repr__(self) -> str:
        width = max(map(lambda c: c.x, self.map().keys()))+1
        height = max(map(lambda c: c.y, self.map().keys()))+1
        m = [[
                self.map().get(Coord(x, y), '.')
                for x in range(width)
            ]
            for y in range(height)
        ]

        return '\n'.join(map(lambda l: ''.join(map(str, l)), (m)))


with open(sys.argv[1], 'r') as in_file:
    vents = list(map(VentLine, map(str.strip, in_file)))

### Part 1 ###
# only vertical or horizantal lines
part1 = Map(filter(lambda v: v.is_vertical() or v.is_horizantal(), vents))
print(f'Part 1: {part1.num_overlaps()}')

### Part 2 ###
part2 = Map(vents)
print(f'Part 2: {part2.num_overlaps()}')

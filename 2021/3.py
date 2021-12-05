#!/bin/python3

import sys
from functools import reduce
from typing import Literal, Optional, cast, TypeVar
from collections.abc import Iterator

Bit = Literal['0', '1']


with open(sys.argv[1], 'r') as in_file:
    tups = cast(
        list[tuple[Bit, ...]],
        list(map(tuple, map(str.strip, in_file))),
    )

def to_int(t: tuple[Bit, ...]) -> int:
    """
    Take a tuple of '0's and '1's, and convert it to an int by interpreting it
    as a binary string
    """
    return int(''.join(t), base=2)

def count(col: tuple[Bit, ...], prefer: Optional[Bit] = None) -> tuple[Bit, Bit]:
    """
    Take a tuple of Bits, and return (<most common>, <least common>)

    if there are an equal number of ones and zeros:
        if prefer is set, returns (prefer, prefer)
        otherwise, raises Exception
    """
    def bump(l: list[int], n: Bit) -> list[int]:
        l[int(n)] += 1
        return l

    # count how many zeros and ones there are
    zeros, ones = reduce(bump, col, [0,0])

    # return most, least
    if zeros > ones:
        return '0', '1'
    if ones > zeros:
        return '1', '0'
    if prefer:
        return prefer, prefer
    raise Exception('equal 1s and 0s, and no prefer specified')

### Part 1

# The following line, explained from outside -> in
# reduce(int.__mul__): reduce the mapping to an integer by multiplication
# (tl;dr: this does the gamm_rate * epsilon_rate)
#  map(to_int): converts every row into a string of binary digits, then to an int
#   zip: gives us an iterator of rows
#    map(count): gets the most common digit of each column
#     zip: gets us an iterator of tuples
print(f'Part 1: {reduce(int.__mul__, map(to_int, zip(*map(count, zip(*tups)))))}')

### Part 2

ogr = tups.copy()
csr = tups.copy()
idx = 0

T = TypeVar('T')
def index_iter(it: Iterator[T], index: int) -> T:
    for _ in range(index):
        _ = next(it)
    return next(it)

def part2(ts: list[tuple[Bit, ...]], prefer: Bit) -> tuple[Bit, ...]:
    index = 0
    while len(ts) > 1:
        col = index_iter(zip(*ts), index)
        o = count(col, prefer=prefer)[~int(prefer)]
        ts = list(filter(lambda t: t[index] == o, ts))
        index += 1
    return ts[0]

oxygen = to_int(part2(ogr, '1'))
co2 = to_int(part2(csr, '0'))


print(f'Part 2: {oxygen * co2}')

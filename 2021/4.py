#!/bin/python3

import sys
from itertools import groupby, compress, chain, filterfalse
from collections.abc import Iterator, Iterable
from typing import Annotated, cast, Any, TypeVar, Generic

class Board:
    """
    A Board tracks a board's numbers, as well as what has been called on it,
    and provides functions for determining win states and score
    """

    rows: Annotated[list[list[int]], 'the grid in this board']
    selected: Annotated[list[list[bool]], 'selected[r][c] indicates if rows[r][c] has been marked']
    last_marked: Annotated[int, 'the last number marked on this board. Used in score calculation']

    def __init__(self, lines: Iterable[str]) -> None:
        self.rows = list(map(
            lambda l: list(map(
                int,
                l.split()
            )),
            lines
        ))
        self.selected = [
            [ False for i in range(len(self.rows)) ]
            for j in range(len(self.rows))
        ]

        self.last_marked = -1

    def rows_win(self) -> bool:
        """ Determine if this board is won by a completed row """
        for row in self.selected:
            if all(row):
                return True
        return False

    def cols_win(self) -> bool:
        """ Determine if this board is won by a completed column """
        for col in zip(*self.selected):
            if all(col):
                return True
        return False

    def won(self) -> bool:
        """ Determine if this board has been won """
        return self.rows_win() or self.cols_win()

    def mark(self, num: int) -> None:
        """ Mark that a number has been called on this board """
        for row in self.rows:
            if num in row:
                r = self.rows.index(row)
                c = row.index(num)
                self.selected[r][c] = True
                self.last_marked = num
                return

    def score(self) -> int:
        """
        Get this board's score

        Score is the product of the sum of all uncalled numbers in this board
        and the last number called on this board
        """
        return sum(compress(
            chain.from_iterable(self.rows),
            # score is based on the uncalled numbers
            map(lambda s: not s, chain.from_iterable(self.selected)),
        )) * self.last_marked


T = TypeVar('T')
class clumper(Iterable[Iterator[T]], Generic[T]):
    """
    Partition an interable into groups, each of which is an iterable that
    returns n elements from the original iterable

    If the length of the iterable % n != 0, the final group is be truncated
    (e.g. `list(map(list, clumper(range(3), n=2)))` returns `[[1,2], [3]]`)
    """

    it: Annotated[Iterator[T], 'this clumper\'s source iterator']
    n: Annotated[int, 'the size of clumps produced by this clumper']

    _i: Annotated[int, 'the internal state of this clumper']

    def __init__(self, it: Iterable[T], n: int = 1) -> None:
        """ it is the iterable to group, n is the number of items per group """
        self.it = iter(it)
        self.n = n

        # We add 1 before we return from key(), so we have to start at -1
        self._i = -1

    def _key(self, *_: Any) -> int:
        """
        the return value of this function changes after it has been called self.n times,
        """
        self._i += 1
        return self._i // self.n

    def __iter__(self) -> Iterator[Iterator[T]]:
        return map(lambda t: t[1], groupby(self.it, self._key))

with open(sys.argv[1], 'r') as in_file:
    # Strip the empty lines
    f = filter(lambda l: len(l.strip()) > 0, in_file)

    # Grab the draw numbers
    nums = list(map(int, next(f).split(',')))

    # Create the boards (each board is 5x5, so we need 5 lines per board)
    boards = list(map(Board, clumper(f, n=5)))

part1_winner = None
for number in nums:
    for board in boards:
        board.mark(number)

    ### Part 1 ###
    # Record the first board that gets won
    if not part1_winner and any(map(Board.won, boards)):
        part1_winner = next(filter(Board.won, boards))

    ### Part 2 ###
    # Remove all the boards that have already been won so we can find the last
    # board that gets one without wasting time on the others
    if len(boards) > 1:
        boards = list(filterfalse(Board.won, boards))
    else:
        break

# on valid puzzle input, we can be confident this isn't None, so cast to quiet mypy
part1_winner = cast(Board, part1_winner)

print(f'Part 1: {part1_winner.score()}')
print(f'Part 2: {boards[0].score()}')

#! /bin/python3

from ast import literal_eval
from itertools import permutations
from math import ceil
from math import floor
import sys

class Pair:
    def __init__(self, left, right, depth, parent):
        self.parent = parent
        self.depth = depth
        if not isinstance(left, int):
            self.left = Pair(left[0], left[1], depth+1, self)
        else:
            self.left = left
        if not isinstance(right, int):
            self.right = Pair(right[0], right[1], depth+1, self)
        else:
            self.right = right

    def __repr__(self):
        return f'[{self.left},{self.right}]'

    def __str__(self):
        return f'[{self.left},{self.right}]'

    def add_left(self, num):
        """ add num to the first regular number from the left in this pair """
        if isinstance(self.right, int):
            self.right += num
        else:
            self.right.add_left(num)

    def add_right(self, num):
        """ add num to the first regular number from the right in this pair """
        if isinstance(self.left, int):
            self.left += num
        else:
            self.left.add_right(num)

    def add_up_left(self, num):
        """ add num to the next regular number to the left of this pair """
        if not self.parent:
            return
        if self.parent.right is self:
            if isinstance(self.parent.left, int):
                self.parent.left += num
            else:
                self.parent.left.add_left(num)
        else:
            self.parent.add_up_left(num)

    def add_up_right(self, num):
        """ add num to the next regular number to the right of this pair """
        if not self.parent:
            return
        if self.parent.left is self:
            if isinstance(self.parent.right, int):
                self.parent.right += num
            else:
                self.parent.right.add_right(num)
        else:
            self.parent.add_up_right(num)

    def explode(self):
        """
        Check if there's anything to explode in this pair.
        Returns true if an explode was performed
        """

        if self.depth < 4:
            if not isinstance(self.left, int):
                if self.left.explode():
                    return True
            if not isinstance(self.right, int):
                if self.right.explode():
                    return True
        if self.depth == 4:
            self.add_up_left(self.left)
            self.add_up_right(self.right)
            if self.parent.left is self:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return True
        return False

    def total_reduce(self):
        """ Reduce this pair until there's nothing to reduce """
        while self.reduce():
            pass

    def reduce(self):
        """
        Reduce this pair. Returns true if a reduciton operation was performed
        """
        if self.explode():
            return True
        return self.split()

    def split(self):
        """
        Check if there's anything to split in this pair.
        Returns true if a split was performed
        """

        if not isinstance(self.left, int):
            if self.left.split():
                return True
        elif self.left >= 10:
            self.left = Pair(floor(self.left / 2), ceil(self.left / 2), self.depth+1, self)
            return True

        if not isinstance(self.right, int):
            if self.right.split():
                return True
        elif self.right >= 10:
            self.right = Pair(floor(self.right / 2), ceil(self.right / 2), self.depth+1, self)
            return True
        return False

    def magnitude(self):
        """ Return the magnitude of this pair """
        left = self.left.magnitude() if not isinstance(self.left, int) else self.left
        right = self.right.magnitude() if not isinstance(self.right, int) else self.right

        return 3*left + 2*right

with open(sys.argv[1], 'r') as in_file:
    lines = list(map(lambda l: Pair(l[0], l[1], 0, None), map(literal_eval, in_file)))
    for line in lines:
        line.total_reduce()

    top = lines[0]
    for line in lines[1:]:
        top = Pair(literal_eval(str(top)), literal_eval(str(line)), 0, None)
        top.total_reduce()

    print('Part 1:', top.magnitude())

    mags = set()
    for l, r in permutations(lines, 2):
        s = Pair(literal_eval(str(l)), literal_eval(str(r)), 0, None)
        s.total_reduce()
        mags.add(s.magnitude())

    print('Part 2:', max(mags))

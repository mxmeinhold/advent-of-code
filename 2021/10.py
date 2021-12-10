#! /bin/python3

import sys
from functools import reduce

# Points for part 1
part1 = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
} 

# Points for part 2
part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# A convenience function for swapping pairs
swap = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',
}.get

scores = []

with open(sys.argv[1], 'r') as in_file:
    lines = list(map(str.strip,in_file))

    corrupted = []
    for line in lines:
        stack = []
        for c in line:
            if c in '([{<':
                stack.append(c)
            elif c in '>]})':
                if stack[-1] == swap(c):
                    stack.pop()
                else:
                    corrupted.append(c)
                    break
        else:
            scores.append(reduce(
                lambda base, new: base * 5 + new,
                map(part2.get,
                    map(swap,
                        reversed(stack)
                    )
                )
            ))

fin = sorted(scores)
print('Part 1:', sum(map(part1.get, corrupted)))
print('Part 2:', fin[int(len(fin)/2)])


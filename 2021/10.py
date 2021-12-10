#! /bin/python3

import sys
from functools import reduce

# part1_score is updated by get_completion
part1_score = 0

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

# Simple filter predicate to check for non-zero/non-empty/non-None values
not_empty = lambda l: l

# Function for reducing the points for each charachter in a completion to the
# score for the line
to_part2_score = lambda base, new: base * 5 + new


def get_completion(line):
    """
    Return a list of the open side of the incomplete chunks from line

    If the line is complete, returns []
    If the line is corrupt, scores this line for part1, and returns []
    If the line is incomplete, returns the completion
    E.g:
    - '({[()({}{}' -> [ ')', ']', '}', ')' ]
    - '((()))' -> []
    - '(((}))' -> [], adds 3 to part1 score
    """
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c in '>]})':
            if stack[-1] == swap(c):
                stack.pop()
            else:
                global part1_score
                part1_score += part1[c]
                return []
    return list(map(swap, reversed(stack)))


def score_part2(completion):
    """
    Get the score for a completion

    ie: for the incomplete line
    `[({(<(())[]>[[{[]{<()<>>`
    you would pass this function `}}]])})]`
    and it would return the score for this line, 288957
    """
    return reduce(to_part2_score,
        map(part2.get,
            completion
        )
    )

with open(sys.argv[1], 'r') as in_file:
    part2_scores = sorted(
        map(score_part2,
            filter(not_empty,
                map(get_completion,
                    in_file
                )
            )
        )
    )

print('Part 1:', part1_score)
print('Part 2:', part2_scores[int(len(part2_scores)/2)])

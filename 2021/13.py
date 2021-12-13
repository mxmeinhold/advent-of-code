#! /bin/python3

from functools import reduce
import sys
import time

with open(sys.argv[1], 'r') as in_file:
    a = ''.join(in_file).split('\n\n')
    dots = set(map(lambda l: tuple(map(int, l.split(','))), a[0].splitlines()))
    instrs = map(lambda instr: instr.removeprefix('fold along '), a[1].splitlines())
    instrs = map(lambda instr: instr.split('='), instrs)
    instrs = map(lambda instr: (instr[0], int(instr[1])), instrs)

# Filter out the dots on the fold line, since they get destroyed
# axis is 'x' or 'y', the axis of the fold
# line is the line (e.g. 5 for x=5) that the fold is on
filt = lambda axis, line: lambda dot: dot[0 if axis == 'x' else 1] != line

# Compute the new dot position after the fold
# Doing this with abs means I can apply this function to every point, not just
# the ones past the fold
# axis is 'x' or 'y', the axis of the fold
# line is the line (e.g. 5 for x=5) that the fold is on
func = lambda axis, line: lambda dot: (line - abs(dot[0] - line), dot[1]) if axis == 'x' else (dot[0], line - abs(dot[1] - line))

# Apply the instruction to dots
apply = lambda dots, instr: set(map(func(*instr), filter(filt(*instr), dots)))


# We need the number of dots left after the first fold for part 1
start = time.time_ns()
dots = apply(dots, next(instrs))
end = time.time_ns()
print('Part 1:', len(dots), f'({end-start} nanoseconds, or {(end-start)/1000000}ms)')

# And process the rest of the instrs for part 2
start = time.time_ns()
dots = reduce(apply, instrs, dots)

# Humans are faster at parsing ascii art text than I can write code, so let's
# just print it. I'm using ' ' instead of '.' like in the input because it
# makes it so much easier to read.
print('\n'.join(map(''.join, ((
        '#' if (x,y) in dots else ' '
        for x in range(max(map(lambda d: d[0], dots))+1)
    )
    for y in range(max(map(lambda d: d[1], dots))+1)
))))
end = time.time_ns()
print(end-start, f'nanoseconds, or {(end-start)/1000000}ms')

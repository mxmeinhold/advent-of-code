#! /bin/python3

import sys

template = ""

with open(sys.argv[1], 'r') as in_file:
    template = next(in_file).strip()
    next(in_file) # blank
    rules = dict(map(lambda s: tuple(s.strip().split(' -> ')), in_file))

def step(pairs):
    out = dict()
    for pair, count in pairs.items():
        if pair in rules:
            out[pair[0] + rules[pair]] = out.get(pair[0] + rules[pair], 0) + count
            out[rules[pair] + pair[1]] = out.get(rules[pair] + pair[1], 0) + count
        else:
            out[pair] = count
    return out

def count(pairs):
    out = dict()
    out = {template[0]: 1, template[-1]: 1}
    for pair, count in pairs.items():
        out[pair[0]] = out.get(pair[0], 0) + count
        out[pair[1]] = out.get(pair[1], 0) + count

    # floordiv by 2 since we're double counting
    return max(out.values())//2 - min(out.values())//2

# The final string would be too long to fit in memory, so reduce to counts of
# pairs, which is a much smaller set. This has the benefit of making our
# iteration faster since we have a smaller set to iterate over
pairs = dict()
for i in range(len(template)-1):
    pairs[template[i:i+2]] = pairs.get(template[i:i+2], 0) + 1

for _ in range(10):
    pairs = step(pairs)

print('Part 1:', count(pairs))

for _ in range(30):
    pairs = step(pairs)

print('Part 2:', count(pairs))

#! /bin/python3

import sys

template = ""

with open(sys.argv[1], 'r') as in_file:
    template = next(in_file).strip()
    next(in_file) # blank
    rules = dict(map(lambda s: tuple(s.strip().split(' -> ')), in_file))

def step(templ):
    out = ""
    for i in range(len(templ)-1):
        pair = templ[i:i+2]
        if pair in rules:
            out += pair[0] + rules[pair]
        else:
            out += pair[0]
    # Make sure we include the last charachter
    out += templ[-1]
    return out

def count(string):
    counts = dict()
    for c in template:
        counts[c] = counts.get(c, 0) + 1
    return max(counts.values()) - min(counts.values())

for _ in range(10):
    template = step(template)

print('Part 1:', count(template))

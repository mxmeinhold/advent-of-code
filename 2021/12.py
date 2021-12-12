#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    caves = dict()
    for line in map(str.strip, in_file):
        d = line.split('-')
        caves[d[0]] = caves.get(d[0], list()) + [d[1]]
        if d[0] != 'start' and d[1] != 'end':
            caves[d[1]] = caves.get(d[1], list()) + [d[0]]

paths = []
def path(node, stack):
    if node == 'end':
        paths.append(stack + [node])
        return
    if node in stack and node.islower() :
        return
    for n in caves[node]:
        path(n, stack + [node])

    
path('start', [])
print('Part 1', len(paths))

paths = []
def path(node, stack):
    if node == 'start' and node in stack:
        return
    if node == 'end':
        paths.append(stack + [node])
        return
    if node in stack and node.islower() and max(map(stack.count, filter(str.islower, stack)), default=0) > 1:
        return
    for n in caves[node]:
        path(n, stack + [node])

    
path('start', [])
print('Part 2', len(paths))

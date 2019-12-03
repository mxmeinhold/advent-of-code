#!/bin/python3

import sys

file = open(sys.argv[1], 'r')
moves = list(map(lambda l: l.strip().split(','), file))

# Translate directions to a step in that direction
adj = {
        'U': {'x':0,'y':1},
        'R': {'x':1,'y':0},
        'D': {'x':0,'y':-1},
        'L': {'x':-1,'y':0},
        }

# Utiltiy functions
adj_point = lambda p, direct: {'x': p['x'] + adj[direct]['x'], 'y': p['y'] + adj[direct]['y']}
stringify = lambda m: f'{m["x"]},{m["y"]}'
manhat = lambda p1,p2: abs(abs(p1['x']) - abs(p2['x'])) + abs(abs(p1['y']) - abs(p2['y']))
dist_along_wire = lambda intersect, r: r.index(intersect) + 1


### Part 1 ###
# Find the point where the lines cross closest to the start, and return the manhattan distance
origin = {'x': 0, 'y':0}

def map_moves(moves):
    points = [origin]
    for move in moves:
        direction = move[0]
        dist = int(move[1:])
        
        while dist > 0:
            points.append(adj_point(points[-1], direction))
            dist = dist - 1
    return points[1:]
results = list(map(lambda move: set(map(stringify, move)), map(map_moves, moves)))

intersects = list(map(lambda res: {'x': res[0], 'y': res[1]}, map(lambda r: list(map(int, r.split(','))), results[0].intersection(results[1]))))

dists = map(lambda i: manhat(i, origin), intersects)

print(f'Part 1: {min(dists)}')

### Part 2 ###
# Find the intersection that can be reached in the fewest steps

results = list(map(lambda move: list(map(stringify, move)), map(map_moves, moves)))
s_intersects = map(stringify, intersects)


dists = map(lambda i: dist_along_wire(i, results[0]) + dist_along_wire(i, results[1]), s_intersects)

print(f'Part 2: {min(dists)}')

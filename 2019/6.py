#!/bin/python3

import sys

### Part 1 ###
# Count the number of direct (A orbits B) and indirect (A orbits B which orbits C) orbits

orbits = list(map(lambda o: list(map(lambda s: s.strip(),
                                     o.split(')'))),
                  open(sys.argv[1], 'r').readlines()))

mapp = dict()
for orbit in orbits:
    if orbit[0] in mapp:
        mapp[orbit[0]].append(orbit[1])
    else:
        mapp[orbit[0]] = [orbit[1]]

def orbit_count(key, depth):
    if key in mapp:
        return depth + sum(map(lambda o: orbit_count(o, depth + 1),
                               mapp[key]))
    return depth

roots = [o[0] for o in orbits]
children = [o[1] for o in orbits]
roots = list(filter(lambda r: all(map(lambda c: r not in c,
                                      children)),
                    roots))
num_orbits = sum(map(lambda r: orbit_count(r, 0), roots))
print(f'Part 1: {num_orbits}')

### Part 2 ###
# Count the number of transfers needed to get from 'YOU' to 'SAN'
parents = dict()
for parent in mapp:
    for kid in mapp[parent]:
        parents[kid] = parent

depth = 1
par = parents['YOU']
you_pars = dict()
while par not in roots:
    you_pars[parents[par]] = depth
    depth = depth + 1
    par = parents[par]

depth = 0
par = parents['SAN']
while par not in roots and par not in you_pars:
    depth = depth + 1
    par = parents[par]

print(f'Part 2: {depth + you_pars[par]}')

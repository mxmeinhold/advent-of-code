#!/bin/python3

import sys
import string

# parents = raw[*][5], children = raw[*][36]
raw = list(map(lambda s: s.strip(), open(sys.argv[1], 'r')))

deps = { key : [line[5] for line in raw if line[36] == key] for key in string.ascii_uppercase }

order = ''
while len(deps) > 0:
    free = [ key for key in deps if len(deps[key]) == 0 ]
    chosen = sorted(free)[0]
    order += chosen
    deps.pop(chosen)
    deps = { key : [value for value in deps[key] if value != chosen] for key in deps }

print(order)

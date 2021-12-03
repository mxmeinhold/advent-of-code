#!/bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    data = list(in_file)

### Part 1
tups = []
for line in data:
    tups.append(tuple(line.strip()))
print(tups[0])

def count(col):
    d = dict()
    for c in col:
        d[c] = 1 + d.get(c, 0)
    if max(d.values()) == min(d.values()):
        raise
    return max(d, key= d.get), min(d, key= d.get)

gamma_str = []
epsilon_str = []
cols = list(zip(*tups))
for col in cols:
    g, e = count(col)
    gamma_str.append(g)
    epsilon_str.append(e)
print(gamma_str)


gamma_rate = int(''.join(gamma_str), base=2)# bit 1 = mode of bits 1 in the other numbers, etc.
epsilon_rate = int(''.join(epsilon_str), base=2)# bit 1 = mode of bits 1 in the other numbers, etc.
print(gamma_rate)
print(epsilon_rate)

print(f'Part 1: {gamma_rate * epsilon_rate}')

### Part 2
ans = 0

ogr = list(tups)
csr = list(tups)
idx = 0
while len(ogr) > 1:
    o_col = list(zip(*ogr))[idx]
    try:
        o, _ = count(o_col)
    except:
        o = '1'
    ogr = list(filter(lambda t: t[idx] == o, ogr))
    idx += 1
idx = 0
while len(csr) > 1:
    c_col = list(zip(*csr))[idx]
    try:
        _, c = count(c_col)
    except:
        c = '0'
    csr = list(filter(lambda t: t[idx] == c, csr))
    idx += 1

ogr = int(''.join(*ogr), base=2)
csr = int(''.join(*csr), base=2)

print(f'Part 2: {ogr * csr}')

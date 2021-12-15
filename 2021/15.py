#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    data = [
        [
            int(c) for c in line.strip()
        ]
        for line in in_file
    ]


def neighbors(spot):
    return {
        (spot[0]-1, spot[1]),
        (spot[0]+1, spot[1]),
        (spot[0], spot[1]-1),
        (spot[0], spot[1]+1),
    }

def djikstras(risk):
    risks = {
        (r, c): risk[r][c]
        for r in range(len(risk))
        for c in range(len(risk[0]))
    }


    dists ={ (0,0): 0 }
    unvisited = set(risks.keys())
    seen = set()

    current = (0,0)
    end = (len(risk)-1, len(risk[0])-1)
    while current != end:
        unvisited -= {current}
        seen -= {current}
        for neigh in neighbors(current) & unvisited:
            seen.add(neigh)
            dists[neigh] = min(dists.get(neigh, dists[current] + risks[neigh]), dists[current] + risks[neigh])

        current = min(seen, key=dists.get,)

    return dists[end]

print('Part 1:', djikstras(data))

full_map = [[0 for _ in range(len(data[0]) * 5)] for _ in range(len(data) * 5)]

for r in range(len(data)):
    for c in range(len(data[0])):
        value = data[r][c]
        for right in range(5):
            dvalue = value
            for down in range(5):
                full_map[r + len(data)*down][c + len(data[0])*right] = dvalue
                dvalue = max(1, (dvalue+1) %10)
            value = max(1, (value+1)%10)

def debug(risks):
    print('\n'.join(map(lambda line: ''.join(map(str, line)), full_map)))
    print('\n'.join(map(lambda line: ''.join(map(str, line)), data)))

print('Part 2:', djikstras(full_map))

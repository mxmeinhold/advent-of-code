#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    crab_h = list(map(int, next(in_file).split(',')))

    crabs = [0] * (max(crab_h)+1)

    for crab in crab_h:
        crabs[crab] += 1


# Fuel cost in part 1 is 1/distance
agg_fuel = lambda dest, origin, num_crabs: abs(dest-origin) * num_crabs

fuel = map(lambda i: sum(map(lambda h: agg_fuel(i, h, crabs[h]), range(len(crabs)))), range(len(crabs)))

print('Part 1:', min(fuel))

# Fuel cost in part 2 is:
# the function f(n) = f(n-1) + n, f(0) = 0
# which describes the sequence 1, 3, 6, 10, 15, ...
# which is equivalent to f(n) = n(n+1)/2
agg_fuel = lambda dest, origin, num_crabs: int(abs(dest-origin) * (abs(dest-origin) + 1) /2 * num_crabs)

fuel = map(lambda i: sum(map(lambda h: agg_fuel(i, h, crabs[h]), range(len(crabs)))), range(len(crabs)))

print('Part 2:', min(fuel))


# The above, but as a one liner, because why not?
print('\n'.join((
    lambda crabs, parts: map(
        lambda part: 'Part {}: {}'.format(part[0], min(map(
            lambda dest: sum(map(
                lambda origin: part[1](abs(dest-origin), crabs[origin]),
                range(len(crabs)),
                )),
            range(len(crabs)),
            ))),
        parts,
        )
    )(
        (
            lambda dists: list(map(
                    dists.count,
                    range(max(dists) + 1),
                    ))
        )(list(map(int, next(open(sys.argv[1], 'r')).split(',')))),
        (
            (1, (lambda dist, num_crabs: dist * num_crabs)),
            (2, (lambda dist, num_crabs: int(dist * (dist + 1) / 2 * num_crabs))),
        ),
    )
))

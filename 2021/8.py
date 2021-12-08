#! /bin/python3

import sys

# Count the number of signals that are 1, 4, 7, or 8
# (the ones we know based on length alone)
part1 = 0

# Sum the outputs
part2 = 0

len_to_num = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

proper = {
    'abcefg'  : '0',
    'cf'      : '1',
    'acdeg'   : '2',
    'acdfg'   : '3',
    'bcdf'    : '4',
    'abdfg'   : '5',
    'abdefg'  : '6',
    'acf'     : '7',
    'abcdefg' : '8',
    'abcdfg'  : '9',
}

with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        signals, output = tuple(line.split('|'))

        # { number: signal }
        ans = {}
        
        # all signals of length 5
        fives = []

        # all signals of length 6
        sixes = []

        for pat in map(set, signals.strip().split()):
            if len(pat) == 5:
                fives.append(pat)
            elif len(pat) == 6:
                sixes.append(pat)
            else:
                ans[len_to_num[len(pat)]] = pat

        candidates = { c: set('abcdefg') for c in 'cef' }

        # we know 1, 7, 4, 8
        # a = 7-1
        candidates['a'] = ans[7] - ans[1]

        # b,d = 4-1
        candidates['b'] = ans[4] - ans[1]
        candidates['d'] = ans[4] - ans[1]

        # e,g = 8-7-4
        candidates['e'] = ans[8]-ans[7]-ans[4]
        candidates['g'] = ans[8]-ans[7]-ans[4]

        for c in 'cf':
            for oc in 'abdeg':
                candidates[c] -= candidates[oc]

        # {'g', 'd', 'a'} in all of fives
        fs = set.intersection(*fives)
        for c in {'g', 'd', 'a'}:
            candidates[c] &= fs

        # {'b', 'g', 'a', 'f'}  in all of sixes
        ss = set.intersection(*sixes)
        for c in {'b', 'g', 'a', 'f'}:
            candidates[c] &= ss

        # c,e = 8-5
        ans[5] = candidates['a'] | candidates['b'] | candidates['d'] | candidates['f'] | candidates['g']
        candidates['c'] &= ans[8]-ans[5]
        candidates['e'] &= ans[8]-ans[5]

        # Map signal chars to proper chars
        key = { next(iter(candidates[c])): c for c in candidates }

        # Decode the output
        out = ''
        for o in output.strip().split():
            real = proper[''.join(sorted(map(key.get, o)))]
            if real in ['1', '4', '7', '8']:
                part1 += 1
            out += real
        part2 += int(out)

print('Part 1:', part1)

print('Part 2:', part2)

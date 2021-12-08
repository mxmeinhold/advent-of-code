#! /bin/python3

import sys

with open(sys.argv[1], 'r') as in_file:
    lines = []
    for line in in_file:
        patterns, output = tuple(line.split('|'))
        patterns = patterns.strip().split()
        outputs = output.strip().split()
        lines.append((patterns, outputs))

nums = {
    2: 1,
    3: 7,
    4: 4,
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: 8,
}

proper = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg'),
}

proper_inv = {''.join(sorted(proper[n])): n for n in proper}

final_outs = []
full_outs =[]

for patterns, outputs in lines:
    ans = {}
    fives = []
    sixes = []
    for pat in patterns:
        if len(pat) == 5:
            fives.append(set(pat))
        elif len(pat) == 6:
            sixes.append(set(pat))
        else:
            ans[nums[len(pat)]] = set(pat)

    candidates = { chr(c): set(map(chr, range(ord('a'), ord('g') + 1))) for c in range(ord('a'), ord('g')+1) }

    #for num in ans:
        #for c in proper[num]:
            #candidates[c] &= set(ans[num])

    # we know 1, 7, 4, 8
    # a = 7-1
    candidates['a'] = ans[7] - ans[1]
    for c in set(candidates) - {'a'}:
        candidates[c] -= candidates['a']


    # b,d = 4-1
    candidates['b'] = ans[4] - ans[1]
    candidates['d'] = ans[4] - ans[1]
    for c in set(candidates) - {'b', 'd'}:
       candidates[c] -= candidates['b'] & candidates['d']

    # e,g = 8-7-4
    candidates['e'] = ans[8]-ans[7]-ans[4]
    candidates['g'] = ans[8]-ans[7]-ans[4]
    for c in set(candidates) - {'e', 'g'}:
       candidates[c] -= candidates['e'] & candidates['g']

    # {'g', 'd', 'a'} in all of fives
    # {'b', 'g', 'a', 'f'}  in all of sixes
    fs = set(map(chr, range(ord('a'), ord('g') + 1)))
    for f in fives:
        fs &= f
    for c in {'g', 'd', 'a'}:
        candidates[c] &= fs

    ss = set(map(chr, range(ord('a'), ord('g') + 1)))
    for s in sixes:
        ss &= s
    for c in {'b', 'g', 'a', 'f'}:
        candidates[c] &= ss

    candidates['e'] -= candidates['g']
    candidates['c'] -= candidates['f']

    rev_candidates = {candidates[c].pop(): c for c in candidates}

    out = []
    for o in outputs:
        real = set()
        for c in o:
            real.add(rev_candidates[c])
        final_outs.append(proper_inv[''.join(sorted(real))])
        out.append(proper_inv[''.join(sorted(real))])
    full_outs.append(int(''.join(map(str, out))))

print('Part 1:', len(list(filter(lambda n: n in [1,4,7,8], final_outs))))

print('Part 2:', sum(full_outs))

#! /bin/python3

import sys

scores = []
with open(sys.argv[1], 'r') as in_file:
    lines = list(map(str.strip,in_file))

    illegal = []
    for line in lines:
        stack = []
        good= True
        for c in line:
            if c in '([{<':
                stack.append(c)
            elif c in '>]})':
                if c == '>':
                    if stack[-1] == '<':
                        stack.pop()
                    else:
                        good=False
                        illegal.append(c)
                        break
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        good=False
                        illegal.append(c)
                        break
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        good=False
                        illegal.append(c)
                        break
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        good=False
                        illegal.append(c)
                        break
        if good:
            fix = ''.join(stack).replace('(',')').replace('{','}').replace('[',']').replace('<','>')
            lf = list(fix)
            lf.reverse()
            fix = ''.join(lf)
            score = 0
            p = {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
            }
            for c in fix:
                score *= 5
                score += p[c]
            scores.append(score)


points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
} 

fin = sorted(scores)
print('Part 1:', sum(map(points.get, illegal)))
print('Part 2:', fin[int(len(fin)/2)])


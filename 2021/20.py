#! /bin/python3

import sys

expand = 2
with open(sys.argv[1], 'r') as in_file:
    algo = next(in_file).strip()
    next(in_file) # blank
    lines = list(map(list, map(str.strip, in_file)))

def enhance(image):
    def get(r, c):
        if r >= len(image) or r < 0:
            return '.'
        if c >= len(image[r]) or c < 0:
            return '.'
        return image[r][c]

    out = [['.' for _ in range(len(image[0])+(2*expand))] for _ in range(len(image)+(2*expand))]

    for row in range(-expand, len(image)+expand):
        for col in range(-expand, len(image[0])+expand):
            string = ''.join((get(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2)))
            idx = int(string.replace('.', '0').replace('#', '1'), 2)
            out[row+expand][col+expand] = algo[idx]
    return out

def enhance2(image, step):
    def get(r, c):
        if r >= len(image) or r < 0 or c >= len(image[r]) or c < 0:
            return algo[0] if step % 2 == 1 else algo[int((algo[0]*9).replace('#', '1').replace('.', '0'), 2)]
        return image[r][c]

    out = [['.' for _ in range(len(image[0])+(2*expand))] for _ in range(len(image)+(2*expand))]

    for row in range(-expand, len(image)+expand):
        for col in range(-expand, len(image[0])+expand):
            string = ''.join((get(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2)))
            idx = int(string.replace('.', '0').replace('#', '1'), 2)
            out[row+expand][col+expand] = algo[idx]
    return out
def enhance3(image, step):
    def get(r, c):
        if r >= len(image) or r < 0 or c >= len(image[r]) or c < 0:
            return algo[0] if step % 2 == 1 else algo[int((algo[0]*9).replace('#', '1').replace('.', '0'), 2)]
        return image[r][c]

    out = [['.' for _ in range(len(image[0]))] for _ in range(len(image))]

    for row in range(len(image)):
        for col in range(len(image[0])):
            string = ''.join((get(r, c) for r in range(row-1, row+2) for c in range(col-1, col+2)))
            idx = int(string.replace('.', '0').replace('#', '1'), 2)
            out[row][col] = algo[idx]
    return out

def debug(image):
    print('\n'.join(map(lambda line: ''.join(line).replace('.', ' '), image)))

#debug(lines)
e1 = enhance(lines)
debug(e1)
e2 = enhance2(e1, 2)
debug(e2)
print('Part 1:', sum((1 if c == '#' else 0 for line in e2 for c in line )))
result = list(map(lambda line: line[expand:-expand], e2[expand:-expand]))
debug(result)
print(len(result), len(result[0]))
#for i in range(50-2):
for i in range(2):
    result = enhance3(result, i)
    #debug(result)
print('Part 2:', sum((1 if c == '#' else 0 for line in result for c in line )))




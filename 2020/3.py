import sys

class RoundList(list):
    def __getitem__(self, key):
        return super().__getitem__(key % (len(self)))

in_file = open(sys.argv[1], 'r')
# Make a 2D list (That's infinite in the X axis)
grid = list(map(RoundList, map(lambda s: s.strip(), in_file)))

def test_slope(r_step, c_step):
    ''' Count the number of trees encountered on a given slope '''
    c = c_step
    trees = 0
    for r in range(r_step, len(grid), r_step):
        if grid[r][c] == '#':
            trees += 1
        c += c_step
    return trees

### Part 1 ###
# Starting at the top-left corner, and following a slope of right 3 down 1,
# How many trees (`#`) do you encounter?

print(f'Part 1: {test_slope(1, 3)}')

### Part 2 ###
# Try several slopes, and multiply all the results together
from functools import reduce

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
value = reduce(lambda a, b: a*b, map(lambda s: test_slope(*s), slopes))
print(f'Part 2: {value}')

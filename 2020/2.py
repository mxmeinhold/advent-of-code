import sys

class Password:

    def __init__(self, line):
        entries = line.replace(':', '').replace('-', ' ').split()
        self.low = int(entries[0])
        self.high = int(entries[1])
        self.sub = entries[2]
        self.passwd = entries[3]

### Part 1 ###
# Given a password file in the following format (each line):
#   low-high sub: passwd
# Count the number of `passwd`s that have at least `low` instances of `sub`
# and at most `high`

    def is_valid1(self):
        count = self.passwd.count(self.sub)
        return self.low <= count and count <= self.high

### Part 2 ###
# Given a password file in the following format (each line):
#   low-high sub: passwd
# Count the number of passwords that have `sub at index `low` xor index `high` (one indexed)

    def is_valid2(self):
        return (self.passwd[self.low - 1] == self.sub) ^ \
               (self.passwd[self.high - 1] == self.sub)


passwords = list(map(Password, open(sys.argv[1], 'r')))
valids1 = sum(map(lambda p: p.is_valid1(), passwords))
valids2 = sum(map(lambda p: p.is_valid2(), passwords))
print(f'Part 1: {valids1}')
print(f'Part 2: {valids2}')

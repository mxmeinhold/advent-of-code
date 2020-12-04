import sys
import re

class Passport:
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    optional_fields = {'cid'}

    def __init__(self, entry):
        fields = re.split(r'\s+',  entry.strip())
        for field in fields:
            sp = field.split(':')
            setattr(self, sp[0], sp[1])

    def is_valid(self):
        return len(self.required_fields - self.optional_fields - set(self.__dict__.keys())) == 0


    ### Part 2 ###
    # Now we gotta do field validation
    def is_valid2(self):
        if not self.is_valid():
            return False

        try:
            # byr: int, 1920 <= byr <= 2002
            self.byr = int(self.byr)
            if not(1920 <= self.byr and self.byr <= 2002):
                return False
            # iyr: int, 2010 <= iyr <= 2020
            self.iyr = int(self.iyr)
            if not(2010 <= self.iyr and self.iyr <= 2020):
                return False
            # eyr: int, 2020 <= eyr <= 2030
            self.eyr = int(self.eyr)
            if not(2020 <= self.eyr and self.eyr <= 2030):
                return False
            # hgt: number followed by unit string
            #  - if cm: 150 <= number <= 193
            #  - if in: 59 <= number <= 76
            num = int(self.hgt[:-2])
            unit = self.hgt[-2:]
            if unit == 'cm':
                if not(150 <= num and num <= 193):
                    return False
            elif unit == 'in':
                if not(50 <= num and num <= 76):
                    return False
            else:
                return False
            # hcl: `#` followed by 6 hex digits
            if re.match(r'^#[0-9a-f]{6}$', self.hcl) is None:
                return False
            # ecl: one of `[amb, blu, brn, gry, grn, hzl, oth]`
            if self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
            # pid: 9 digit number, including leading zeros
            if re.match(r'^\d{9}$', self.pid) is None:
                return False
            # cid: ignored
        except:
            # If we errored, it was probably integer formatting
            return False
        return True

batch = list(map(Passport, ''.join(open(sys.argv[1], 'r').readlines()).split('\n\n')))

### Part 1 ###
# Get the number of valid passports in the batch
# Passports are in the form of `key:value`, with each field separated by
# whitespace and passport entries are separated by empty lines. A valid
# passport must have all required_fields, though it may be missing
# optional_fields

print(f'Part 1: {sum(map(lambda p: p.is_valid(), batch))}')
print(f'Part 2: {sum(map(lambda p: p.is_valid2(), batch))}')

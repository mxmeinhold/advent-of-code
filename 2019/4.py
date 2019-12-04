#!/bin/python3


mini = 353096
maxi = 843212

def verify(num):
    digits = [char for char in str(num)]

    two_in_a_row = False
    idx = 0
    while idx < len(digits) - 1:
        # Never decreasing
        if digits[idx] > digits[idx + 1]:
            return False
        # Two in a row
        if digits[idx] == digits[idx + 1]:
            two_in_a_row = True
        idx = idx + 1
    return two_in_a_row

def verify_part_2(num):
    digits = [char for char in str(num)]

    two_in_a_row = False
    idx = 0
    while idx < len(digits) - 1:
        # Never decreasing
        if digits[idx] > digits[idx + 1]:
            return False
        # Two in a row
        if digits[idx] == digits[idx + 1]:
            if idx >= 1:
                if digits[idx] != digits[idx - 1]:
                    if idx < len(digits) - 2: 
                        if digits[idx + 1] != digits[idx + 2]:
                            two_in_a_row = True
                    else:
                        two_in_a_row = True
            else:
                if idx < len(digits) - 2: 
                    if digits[idx + 1] != digits[idx + 2]:
                        two_in_a_row = True
                else:
                    two_in_a_row = True
        idx = idx + 1
    return two_in_a_row

### Part 1 ###
#However, they do remember a few key facts about the password:
#
#    It is a six-digit number.
#    The value is within the range given in your puzzle input.
#    Two adjacent digits are the same (like 22 in 122345).
#    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#    Other than the range rule, the following are true:
#
#        111111 meets these criteria (double 11, never decreases).
#        223450 does not meet these criteria (decreasing pair of digits 50).
#        123789 does not meet these criteria (no double).
#        How many different passwords within the range given in your puzzle input meet these criteria?

### Part 2 ###
# 3 in a row doesn't count as 2 in a row

print(f'Part 1: {len(list(filter(verify, range(mini, maxi + 1))))}')
print(f'Part 2: {len(list(filter(verify_part_2, range(mini, maxi + 1))))}')

### Part 2 ###

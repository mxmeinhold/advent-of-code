#!/bin/python3

import sys

init_mem = lambda: list(map(int, open(sys.argv[1], 'r').read().split(',')))

### Part 1 ###
# Opcode 1: 1,in1,in2,out - Adds values at in1 and in2 and places the result at out
# Opcode 2: 2,in1,in2,out - Multiplys values at in1 and in2 and places the result at out
# Opcode 3: 3,pos - takes an input, places it at pos
# Opcode 4: 4,pos - outputs the value at pos
# Opcode 99: Terminate

### Part 2 ###
# Opcode 5: jump if nonzero
# Opcode 6: jump if zero
# Opcode 7: Less than
# Opcode 8: Equals

# This day also adds immediate mode to the parameters

def compute(values):

    def op1(index, mode):
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        values[values[index + 3]] = value1 + value2
        return index + 4

    def op2(index, mode):
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        values[values[index + 3]] = value1 * value2
        return index + 4

    def op3(index, mode):
        values[values[index + 1]] = int(input('input:'))
        return index + 2

    def op4(index, mode):
        print(values[index + 1] if mode & 1 else values[values[index + 1]])
        return index + 2

    def op5(index, mode):
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        if value1 != 0:
            return value2
        return index + 3


    def op6(index, mode):
        # jump if 1 is zero
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        if value1 == 0:
            return value2
        return index + 3

    def op7(index, mode):
        # if 1 < 2, stow 1 else 0
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        values[values[index + 3]] = 1 if value1 < value2 else 0
        return index + 4

    def op8(index, mode):
        # if 1 == 2 stow 1 else 0
        value1 = values[index + 1] if mode & 1 else values[values[index + 1]]
        value2 = values[index + 2] if mode & 10 else values[values[index + 2]]
        values[values[index + 3]] = 1 if value1 == value2 else 0
        return index + 4


    ops = {1: op1, 2: op2, 3: op3, 4: op4, 5: op5, 6: op6, 7: op7, 8: op8, }

    instruction = 0
    while values[instruction] != 99:
        print(values[instruction:instruction+4])
        instruction = ops[values[instruction] % 100](instruction, int(values[instruction] / 100))


compute(init_mem())

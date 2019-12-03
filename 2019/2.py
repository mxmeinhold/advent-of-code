#!/bin/python3

import sys

init_mem = lambda: list(map(int, open(sys.argv[1], 'r').read().split(',')))

### Part 1 ###
# Opcode 1: 1,in1,in2,out - Adds values at in1 and in2 and places the result at out
# Opcode 2: 2,in1,in2,out - Multiplys values at in1 and in2 and places the result at out
# Opcode 99: Terminate

def compute(noun, verb, values):
    values[1] = noun
    values[2] = verb

    def op1(index):
        values[values[index + 3]] = values[values[index + 1]]  +  values[values[index + 2]]

    def op2(index):
        values[values[index + 3]] = values[values[index + 1]] * values[values[index + 2]]

    ops = {1: op1, 2: op2, }

    instruction = 0
    while values[instruction] != 99:
        ops[values[instruction]](instruction)
        instruction = instruction + 4 

    return values[0]

print(f'Part 1: {compute(12, 2, init_mem())}')

### Part 2 ###
# Find the noun and verb that produce the output 19690720

noun = -1
verb = -1
output = 0

while output != 19690720:
    noun = noun + 1
    if noun > 99:
        noun = 0
        verb = verb + 1
        if verb > 99:
            break
    try:
        output = compute(noun, verb, init_mem())
    except:
        continue

print(f'Part 2: {100 * noun + verb}')

import sys

### Part 1 ###
# Given a list of numbers, find the product of the two entries that sum to 2020

expense_report = list(map(int, open(sys.argv[1], 'r')))

def part1(expense_report):
    for idx, num1 in enumerate(expense_report[:-1]):
        for num2 in expense_report[idx + 1:]:
            if num1 + num2 == 2020:
                print(f'Part 1: {num1 * num2}')
                return num1 * num2

part1(expense_report)

### Part 2 ###
# This time, find the product of the three entries that sum to 2020
def part2(expense_report):
    for idx1, num1 in enumerate(expense_report[:-2]):
        for idx2, num2 in enumerate(expense_report[idx1 + 1:-1]):
            for num3 in expense_report[idx2 + 1:]:
                if num1 + num2 + num3 == 2020:
                    print(f'Part 2: {num1 * num2 * num3}')
                    return num1 * num2 * num3

part2(expense_report)

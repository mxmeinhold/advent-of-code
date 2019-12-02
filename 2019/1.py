#!/bin/python3

import sys

### Part 1 ###
# Given a list of masses, determine the total fuel requirement
# fuel = floor(mass / 3) - 2

calc_fuel = lambda mass: int(mass / 3) - 2

in_file = open(sys.argv[1], 'r')
masses = list(map(int, in_file))
fuel_required = sum(map(calc_fuel, masses))

print(f'Fuel required: {fuel_required}')

### Part two ###
# Also account for the mass of the fuel

def calc_fuel_with_fuel(mass):
    fuel = calc_fuel(mass)
    more_fuel = calc_fuel(fuel)
    while more_fuel > 0:
        fuel = fuel + more_fuel
        more_fuel = calc_fuel(more_fuel)
    return fuel

fuel_accounting_for_fuel = sum(map(calc_fuel_with_fuel, masses))

print(f'Fuel required accounting for the wieght of the fuel: {fuel_accounting_for_fuel}')

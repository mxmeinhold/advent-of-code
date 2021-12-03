#!/bin/python3

from abc import ABC, abstractmethod
import sys
from typing import Literal, NamedTuple, cast

Instruction = Literal['forward', 'up', 'down']

class Command(NamedTuple):
    """ A command from our planned course """
    instr: Instruction
    x: int

class Part(ABC):
    """
    This class defines common part functionality, such as output formatting and `apply()`
    """

    part: int
    horizantal: int
    depth: int

    def __init__(self) -> None:
        self.horizantal = 0
        self.depth = 0

    @abstractmethod
    def forward(self, x: int) -> None:
        pass

    @abstractmethod
    def up(self, x: int) -> None:
        pass

    @abstractmethod
    def down(self, x: int) -> None:
        pass

    def apply(self, instr: Instruction, x: int) -> None:
        """
        Apply an instruction this part's tracking of our position

        instr: the instruction to execute ('forward', 'down', 'up')
        x:     the value
        """
        getattr(self, instr)(x)

    def __int__(self) -> int:
        """ Get the answer of this part as an int """
        return self.horizantal * self.depth

    def __str__(self) -> str:
        """ Get the answer of this part as a formatted string """
        return f'Part {self.part}: {int(self)}'

class Part1(Part):
    """
    For part 1, each line of the planned course should be interpreded as follows:

    `forward x` increases horizantal by x
    `up x` decreases depth by x
    `down x` increases depth by x

    Our output is our final horizantal * our final depth
    Both horizantal and depth begin at 0
    """

    part = 1

    def forward(self, x: int) -> None:
        self.horizantal += x

    def up(self, x: int) -> None:
        self.depth -= x

    def down(self, x: int) -> None:
        self.depth += x

class Part2(Part):
    """
    For part 2, each line of the planned course should be interpreded as follows:

    `forward x` increases horizantal by x and depth by x * aim
    `up x` decreases aim by x
    `down x` increases aim by x

    Our output is our final horizantal * our final depth
    horizantal, aim, and depth begin at 0
    """

    part = 2
    aim: int

    def __init__(self) -> None:
        super().__init__()
        self.aim = 0

    def forward(self, x: int) -> None:
        self.horizantal += x
        self.depth += self.aim * x

    def up(self, x: int) -> None:
        self.aim -= x

    def down(self, x: int) -> None:
        self.aim += x

def parse_cmd(line: str) -> Command:
    """ Parse a command from each line in the course """
    instr, x = tuple(line.split())
    return Command(cast(Instruction, instr), int(x))


if __name__ == '__main__':
    part1 = Part1()
    part2 = Part2()

    with open(sys.argv[1], 'r') as course:
        for cmd in map(parse_cmd, course):
            part1.apply(*cmd)
            part2.apply(*cmd)

    print(part1)
    print(part2)

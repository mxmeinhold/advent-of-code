#! /bin/python3

import sys

class Packet:
    def __init__(self):
        pass

    def parse(bits):
        """ Parse a packet. Returns the packet and it's length """
        self = Packet()
        self.version = int(bits[0:3], 2)
        self.type_id = int(bits[3:6], 2)

        end = None
        
        if self.type_id == 4:
            self.sub, subend = Literal.parse(bits[6:])
            end = subend+6
        else:
            self.sub, subend = Operator.parse(bits[6:])
            end = subend+6

        self.sub.version = self.version
        self.sub.type_id = self.type_id
        return self.sub, end

from functools import reduce

ops = {
    0: sum,
    1: lambda subs: reduce(int.__mul__, subs, 1),
    2: min,
    3: max,
    5: lambda subs: 1 if subs[0] > subs[1] else 0,
    6: lambda subs: 1 if subs[0] < subs[1] else 0,
    7: lambda subs: 1 if subs[0] == subs[1] else 0,
}

class Operator(Packet):

    def part1(self):
        return self.version + sum(map(lambda s: s.part1(), self.subs))

    def part2(self):
        return ops[self.type_id](list(map(lambda s: s.part2(), self.subs)))

    def __repr__(self):
        return f'Operator(type={self.type_id}, subs={self.subs})'

    def parse(bits):
        """ Parse an Operator. Returns the Operator and the length """
        self = Operator()
        self.length_type_id = int(bits[0])
        if self.length_type_id == 0:
            self.sub_pkt_length = int(bits[1:16], 2)
            end = 16+self.sub_pkt_length
            subend = 16
            self.subs = []
            while subend < end:
                sub, newsubend = Packet.parse(bits[subend:])
                subend += newsubend
                self.subs.append(sub)

        else:
            self.num_sub_pkts = int(bits[1:12], 2)
            self.subs = []
            subend = 12
            while len(self.subs) < self.num_sub_pkts:
                sub, newsubend = Packet.parse(bits[subend:])
                self.subs.append(sub)
                subend += newsubend
        return self, subend

class Literal(Packet):

    def part2(self):
        return self.value

    def part1(self):
        return self.version

    def __str__(self):
        return f'Literal({self.value})'

    def __repr__(self):
        return f'Literal({self.value})'

    def parse(bits):
        """ Parse a Literal. Returns the literal and the length """
        self = Literal()
        end = 0
        accum = ''
        
        # groups of 4, each with a 1 bit prefix
        for i in range(0, len(bits), 5):
            accum += bits[i+1:i+5]
            # The last group has prefix '0'
            if bits[i] == '0':
                end = i+5
                break
        self.value = int(accum, 2)
        return self, end



    # numbers are msb first
    # 3: version (number)
    # 3: type id (number)
    #  - 4: literal value: encodes a single binary number, padded with leading zeros until it's a multiple of 4 bits, broken into groups of 4. all groups but the last group are prefixed by 1, the last bit is prefixed by 0

    #  - anything else: operator. Contians one or more packets
         # bit following the packet header: length type ID:
        # - 0: next 15 bits represent the length of sub packets in this packet
        # - 1: next 11 bits represent the number of sub packets in this packet
        # followed by the subpackets


# Hex digit to binary string function
replace = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}.get

with open(sys.argv[1], 'r') as in_file:
    p, last_idx = Packet.parse(''.join(map(replace, next(in_file).strip())))
    print('Part 1:', p.part1())
    print('Part 2:', p.part2())



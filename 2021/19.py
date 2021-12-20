#! /bin/python3

import sys
from copy import deepcopy

# find overlap of at least 12 beacons, can determine scanner relative position

from functools import lru_cache

class Point:
    def __init__(self, coords):
        self.x, self.y, self.z = tuple(coords)

    def __repr__(self):
        return str((self.x, self.y, self.z))
    def __str__(self):
        return str((self.x, self.y, self.z))

    def __add__(self, other):
        if isinstance(other, Point):
            return Point((self.x + other.x, self.y + other.y, self.z + other.z))
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point((self.x - other.x, self.y - other.y, self.z - other.z))
        else:
            raise NotImplemented

    def __eq__(self, other):
        return (self.x, self.y, self.z) == other
    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


class Scanner:

    def overlap(self, other):
        count = 0
        m = 0
        for orientation in scanner.orientations():
            for delta in {
                    point - opoint
                    for point in other.points
                    for opoint in orientation.points
                }:
                count += 1
                m = max(m, len(set(filter(other.points.__contains__, map(delta.__add__, orientation.points)))))
                if len(set(filter(other.points.__contains__, map(delta.__add__, orientation.points)))) >= 12:
                    #print(m, self.id, other.id)
                    return orientation.shifted(delta)
        #print(m, self.id, other.id)

    def __init__(self, *args):
        lines = args[0].strip().split('\n')
        self.id = int(lines[0].removeprefix('--- scanner ').removesuffix(' ---'))
        self.position = Point((0,0,0)) if self.id == 0 else None

        self.points = {
                Point(map(int, line.split(',')))
                for line in lines[1:]
                }
        self.orientations_cache = None
    
    def with_points(self, points):
        new = super().__new__(Scanner)
        new.id = self.id
        new.position = self.position
        new.points = points
        new.orientations_cache = None
        return new

    def orientations(self):
        if self.orientations_cache == None:
            self.orientations_cache = [
                self,
                self.with_points({ Point((point.y, point.z, point.x)) for point in self.points }),
                self.with_points({ Point((point.z, point.x, point.y)) for point in self.points }),
                self.with_points({ Point((point.z, point.y, point.x)) for point in self.points }),
                self.with_points({ Point((point.y, point.x, point.z)) for point in self.points }),
                self.with_points({ Point((point.x, point.z, point.y)) for point in self.points }),

                self.with_points({ Point((point.x, -point.y, -point.z)) for point in self.points }),
                self.with_points({ Point((point.y, -point.z, -point.x)) for point in self.points }),
                self.with_points({ Point((point.z, -point.x, -point.y)) for point in self.points }),
                self.with_points({ Point((point.z, -point.y, -point.x)) for point in self.points }),
                self.with_points({ Point((point.y, -point.x, -point.z)) for point in self.points }),
                self.with_points({ Point((point.x, -point.z, -point.y)) for point in self.points }),

                self.with_points({ Point((-point.x, point.y, -point.z)) for point in self.points }),
                self.with_points({ Point((-point.y, point.z, -point.x)) for point in self.points }),
                self.with_points({ Point((-point.z, point.x, -point.y)) for point in self.points }),
                self.with_points({ Point((-point.z, point.y, -point.x)) for point in self.points }),
                self.with_points({ Point((-point.y, point.x, -point.z)) for point in self.points }),
                self.with_points({ Point((-point.x, point.z, -point.y)) for point in self.points }),

                self.with_points({ Point((-point.x, -point.y, point.z)) for point in self.points }),
                self.with_points({ Point((-point.y, -point.z, point.x)) for point in self.points }),
                self.with_points({ Point((-point.z, -point.x, point.y)) for point in self.points }),
                self.with_points({ Point((-point.z, -point.y, point.x)) for point in self.points }),
                self.with_points({ Point((-point.y, -point.x, point.z)) for point in self.points }),
                self.with_points({ Point((-point.x, -point.z, point.y)) for point in self.points }),

                self.with_points({ Point((-point.x, point.y, point.z)) for point in self.points }),
                self.with_points({ Point((-point.y, point.z, point.x)) for point in self.points }),
                self.with_points({ Point((-point.z, point.x, point.y)) for point in self.points }),
                self.with_points({ Point((-point.z, point.y, point.x)) for point in self.points }),
                self.with_points({ Point((-point.y, point.x, point.z)) for point in self.points }),
                self.with_points({ Point((-point.x, point.z, point.y)) for point in self.points }),

                self.with_points({ Point((point.x, -point.y, point.z)) for point in self.points }),
                self.with_points({ Point((point.y, -point.z, point.x)) for point in self.points }),
                self.with_points({ Point((point.z, -point.x, point.y)) for point in self.points }),
                self.with_points({ Point((point.z, -point.y, point.x)) for point in self.points }),
                self.with_points({ Point((point.y, -point.x, point.z)) for point in self.points }),
                self.with_points({ Point((point.x, -point.z, point.y)) for point in self.points }),

                self.with_points({ Point((point.x, point.y, -point.z)) for point in self.points }),
                self.with_points({ Point((point.y, point.z, -point.x)) for point in self.points }),
                self.with_points({ Point((point.z, point.x, -point.y)) for point in self.points }),
                self.with_points({ Point((point.z, point.y, -point.x)) for point in self.points }),
                self.with_points({ Point((point.y, point.x, -point.z)) for point in self.points }),
                self.with_points({ Point((point.x, point.z, -point.y)) for point in self.points }),

                self.with_points({ Point((-point.x, -point.y, -point.z)) for point in self.points }),
                self.with_points({ Point((-point.y, -point.z, -point.x)) for point in self.points }),
                self.with_points({ Point((-point.z, -point.x, -point.y)) for point in self.points }),
                self.with_points({ Point((-point.z, -point.y, -point.x)) for point in self.points }),
                self.with_points({ Point((-point.y, -point.x, -point.z)) for point in self.points }),
                self.with_points({ Point((-point.x, -point.z, -point.y)) for point in self.points }),
            ]
        return self.orientations_cache

    @lru_cache
    def shifted(self, spot):
        new = super().__new__(Scanner)
        new.id = self.id
        new.position = spot
        new.points = {
            point + spot for point in self.points
        }
        return new

with open(sys.argv[1], 'r') as in_file:
    s = ''.join(in_file)
    scanners = list(map(Scanner, s.split('\n\n')))
    done = [scanners[0]]
    not_done = scanners[1:]

    checked = {}
    while len(not_done) > 0:
        #print(len(not_done), len(done))
        rems = []
        for i, scanner in enumerate(not_done):
            for d in done:
                if scanner.id in checked and d.id in checked[scanner.id]:
                    continue
                checked[scanner.id] = checked.get(scanner.id, set()) | {d.id}
                if (new := scanner.overlap(d)) != None:
                    done.append(new)
                    rems.append(i)
                    break
        #print(list(map(lambda s: s.position, done)))
        #print('looping')
        for rem in reversed(sorted(rems)):
            del not_done[rem]
    
    part1 = set()

    for d in done:
        part1 |= d.points

    print('Part 1:', len(part1))

    print('Part 2:', max((
        s1.position.dist(s2.position)
        for s1 in done
        for s2 in done
        )))
            



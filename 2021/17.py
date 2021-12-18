#! /bin/python3

import sys
from itertools import accumulate, count

with open(sys.argv[1], 'r') as in_file:
    line = next(in_file).strip()

    xs, ys = tuple(map(
        lambda s: sorted(map(int, s.split('=')[1].split('..'))),
        line.removeprefix('target area: ').split(', ')
    ))

    maxx = max(xs)
    minx = min(xs)
    maxy = max(ys)
    miny = min(ys)

    xs = list(range(minx, maxx+1))
    ys = list(range(miny, maxy+1))


    target = {
        (x, y)
        for x in range(minx, maxx+1)
        for y in range(miny, maxy+1)
    }


def check(x, y):
    """ convenience function for checking if x,y is within the target """
    return x in xs and y in ys

def test(xv, yv):
    """
    text the given initial velocities
    returns a tuple: (whether target was hit, maximum height attained)
    """
    xv_init = xv
    x, y = 0, 0

    ret = (False, 0)

    if xv <= 0 and x < minx:
        return ret
    if yv <= 0 and y < miny:
        return ret

    if check(x, y):
        ret = (True, 0)

    while (x <= maxx) if xv_init >= 0 else (x >= minx):
        x += xv
        y += yv

        xv -= xv//abs(xv) if xv != 0 else 0
        yv -= 1

        if xv == 0 and x not in xs:
            break

        if xv == 0 and y < miny:
            break

        ret = ret[0], max(ret[1], y)

        if check(x, y):
            ret = (True, max(ret[1], y))
    return ret

def plot_x(xv):
    """ Generator that yeilds x positions for a given initial xv """

    for x in accumulate(range(xv, 0, -1 if xv > 0 else 1), initial=0):
        yield x

def plot_y(yv):
    """
    Generator that yeilds y positions for a given initial yv
    Note that this is an infinite generator
    """
    return accumulate(count(yv, -1), initial=0)

def plot(xv, yv):
    """
    Return an iterable of the position the probe occupies at each step
    if these velocities hit the target, the last coordinate in the returned
    iterable will be the last coordinate in the probe's path that is within the
    target
    """
    yiter = plot_y(yv)
    for x, y in zip(plot_x(xv), yiter):
        yield (x, y)

    if x in xs:
        for y in yiter:
            if y >= miny:
                yield (x, y)
            else:
                return

def debug_plot(xv, yv):
    """ Prints a plot of the trajectory of the probe """
    coords = set(plot(xv, yv))
    x_dim = (
        min(minx, min(map(lambda t: t[0], coords))),
        max(maxx, max(map(lambda t: t[1], coords))),
    )
    y_dim = (
        min(miny, min(map(lambda t: t[0], coords))),
        max(maxy, max(map(lambda t: t[1], coords))),
    )
    for y in range(y_dim[1], y_dim[0] - 1, -1):
        print(''.join(
            '#' if (x, y) in coords else 'T' if x in xs and y in ys else '.'
            for x in range(x_dim[0], x_dim[1]+1)
            ))

def get_xvs():
    """ generate all x velocities that could hit the target """
    mx = 0 if minx > 0 else minx
    mxx = maxx if maxx > 0 else 0

    for xv in range(mx, mxx+1):
        if any(map(xs.__contains__, plot_x(xv))):
            yield xv

def get_yvs(xv):
    """ generate all y velocities that hit the target for a given xv """
    y_delta = 0

    for x in plot_x(xv):
        x += xv
        y_delta -= 1
        if x in xs:
            for y in range(miny-y_delta-1, max(abs(miny), abs(maxy))+1):
                yield y

valid_vs = set(filter(lambda t: t[0], (
    (*test(x_i, y_i), (x_i, y_i))
    for x_i in get_xvs()
    for y_i in set(get_yvs(x_i))
)))

print('Part 1:', max(map(lambda t: t[1], valid_vs)))
print('Part 2:', len(set(map(lambda t: t[2], valid_vs))))

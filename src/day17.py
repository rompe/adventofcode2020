#!/usr/bin/env python

import collections
import itertools
import math
import sys


cache = dict(timestamp=0)


def parse_input(input_file):
    """Parse input file and return the pocket dimension."""
    lines = open(input_file).read().splitlines()
    dimension = collections.defaultdict(bool)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            dimension[(x, y, 0)] = char == '#'
    return dimension


def get_neighbours(coord, dimension):
    """Return all 26 neigbours of coord."""
    values = []
    x, y, z = coord
    for xx in (x - 1, x, x + 1):
        for yy in (y - 1, y, y + 1):
            for zz in (z - 1, z, z + 1):
                if (xx, yy, zz) != coord:
                    values.append(dimension[(xx, yy, zz)])
    return values


def show_dimension(dimension):
    """Print dimension like it's shown in the example."""
    zs = set()
    ys = set()
    xs = set()
    for x, y, z in dimension:
        xs.add(x)
        ys.add(y)
        zs.add(z)
    for z in sorted(zs):
        print('z=%s' % z)
        for y in sorted(ys):
            row = ''
            for x in xs:
                row += '#' if dimension[(x, y, z)] else '.'
            print(row)
    print('')


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    # lines = open(input_file).read().splitlines()
    dimension = parse_input(input_file)
    print(dimension)
    show_dimension(dimension)
    for cycle in range(6):
        neighbours = {}
        for coord in dimension.copy():
            get_neighbours(coord, dimension)  # Just to extend the dimension
        for coord in dimension.copy():
            neighbours[coord] = get_neighbours(coord, dimension).count(True)
        for coord in neighbours:
            if dimension[coord]:
                if neighbours[coord] not in (2, 3):
                    dimension[coord] = False
            elif neighbours[coord] == 3:
                dimension[coord] = True
        print('After %s cycles:' % (cycle + 1))
        show_dimension(dimension)
    return list(dimension.values()).count(True)


def parse_input4(input_file):
    """Parse input file and return the pocket dimension."""
    lines = open(input_file).read().splitlines()
    dimension = collections.defaultdict(bool)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            dimension[(x, y, 0, 0)] = char == '#'
    return dimension


def get_neighbours4(coord, dimension):
    """Return all 80 neigbours of coord."""
    values = []
    x, y, z, w = coord
    for xx in (x - 1, x, x + 1):
        for yy in (y - 1, y, y + 1):
            for zz in (z - 1, z, z + 1):
                for ww in (w - 1, w, w + 1):
                    if (xx, yy, zz, ww) != coord:
                        values.append(dimension[(xx, yy, zz, ww)])
    return values


def show_dimension4(dimension):
    """Print dimension like it's shown in the example."""
    zs = set()
    ys = set()
    xs = set()
    ws = set()
    for x, y, z, w in dimension:
        xs.add(x)
        ys.add(y)
        zs.add(z)
        ws.add(w)
    for w in sorted(ws):
        for z in sorted(zs):
            print('z=%s, w=%s' % (z, w))
            for y in sorted(ys):
                row = ''
                for x in xs:
                    row += '#' if dimension[(x, y, z, w)] else '.'
                print(row)
    print('')


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    # lines = open(input_file).read().splitlines()
    dimension = parse_input4(input_file)
    print(dimension)
    show_dimension4(dimension)
    for cycle in range(6):
        print("Cycle %s" % (cycle - 1))
        neighbours = {}
        for coord in dimension.copy():
            get_neighbours4(coord, dimension)  # Just to extend the dimension
        for coord in dimension.copy():
            neighbours[coord] = get_neighbours4(coord, dimension).count(True)
        for coord in neighbours:
            if dimension[coord]:
                if neighbours[coord] not in (2, 3):
                    dimension[coord] = False
            elif neighbours[coord] == 3:
                dimension[coord] = True
        print('After %s cycles:' % (cycle + 1))
        # show_dimension4(dimension)
    return list(dimension.values()).count(True)


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

#!/usr/bin/env python

import sys


def rotate(current_direction, direction, degrees):
    """Rotate R or L."""
    directions = 'NESWNESW'
    if direction == 'R':
        new_direction = directions[int(directions.index(current_direction) + degrees / 90)]
    else:
        new_direction = directions[int(directions.rindex(current_direction) - degrees / 90)]
    return new_direction


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    coords = dict(N=0, E=0, S=0, W=0)
    current_direction = 'E'
    for line in lines:
        action = line[0]
        value = int(line[1:])
        if action in ('R', 'L'):
            current_direction = rotate(current_direction, action, value)
        elif action == 'F':
            coords[current_direction] += value
        else:
            coords[action] += value
    x = coords['E'] - coords['W']
    y = coords['N'] - coords['S']
    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1
    return x + y


def rotate2(coords, direction, degrees):
    """Rotate R or L."""
    for dummy in range(int(degrees / 90)):
        if direction == 'R':
            coords['E'], coords['S'], coords['W'], coords['N'] = \
                coords['N'], coords['E'], coords['S'], coords['W']
        else:
            coords['W'], coords['N'], coords['E'], coords['S'] = \
                coords['N'], coords['E'], coords['S'], coords['W']
    return coords


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    coords = dict(N=1, E=10, S=0, W=0)
    ship = dict(x=0, y=0)
    for line in lines:
        action = line[0]
        value = int(line[1:])
        if action in ('R', 'L'):
            coords = rotate2(coords, action, value)
        elif action == 'F':
            ship['x'] += (coords['E'] - coords['W']) * value
            ship['y'] += (coords['N'] - coords['S']) * value
        else:
            coords[action] += value
    x = ship['x']
    y = ship['y']
    if x < 0:
        x = x * -1
    if y < 0:
        y = y * -1
    # print(ship)
    return x + y


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

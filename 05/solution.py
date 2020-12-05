#!/usr/bin/env python

import re
import sys


def get_seat_id(binary_seat):
    """Return the seat ID for "binary_seat"."""
    line = binary_seat
    row = line[:-3].replace('B', '1').replace('F', '0')
    seat = line[-3:].replace('R', '1').replace('L', '0')
    row = int(row, base=2)
    seat = int(seat, base=2)
    id = 8 * row + seat
    return id


def solution(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    ids = []
    for line in lines:
        ids.append(get_seat_id(line))
    print(max(ids))


def solution2(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    ids = []
    for line in lines:
        ids.append(get_seat_id(line))
    previous = 0
    for id in sorted(ids):
        if previous + 2 == id:
            print(id - 1)
        previous = id


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

#!/usr/bin/env python

import itertools
import sys


def solution(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    valids = 0
    for line in lines:
        count, char, password = line.split()
        char = char[0]
        lowest, highest = count.split('-')
        if (password[int(lowest) - 1] == char) ^ (password[int(highest) - 1] == char):
            valids += 1
    print(valids)


if __name__ == "__main__":
    sys.exit(solution(sys.argv[1]))

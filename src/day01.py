#!/usr/bin/env python

import itertools
import operator
import sys


def pick_numbers(input_file):
    """Pick two numbers adding to 2020 and multiply them."""
    numbers = [int(num) for num in open(input_file).read().split()]
    for data in itertools.combinations(numbers, 3):
        if data[0] + data[1] + data[2] == 2020:
            print(data[0] * data[1] * data[2])


if __name__ == "__main__":
    sys.exit(pick_numbers(sys.argv[1]))

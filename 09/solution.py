#!/usr/bin/env python

import re
import sys
import itertools


def solution(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    numbers = [int(line) for line in lines]
    #print(lines)
    preamble = 25
    for row, value in enumerate(numbers):
        if row >= preamble:
            for combination in itertools.combinations(numbers[row - preamble:row], 2):
                if sum(combination) == value:
                    break
            else:
                return value


def solution2(input_file):
    """Solve today's riddle."""
    number = solution(input_file)
    lines = open(input_file).read().splitlines()
    numbers = [int(line) for line in lines]
    for row, value in enumerate(numbers):
        # print("%s..." % row)
        shift = 1
        summa = value
        while summa < number:
            stack = numbers[row:row + shift]
            summa = sum(stack)
            if summa == number:
                return max(stack) + min(stack)
            shift += 1


if __name__ == "__main__":
    print(solution(sys.argv[1]))
    print(solution2(sys.argv[1]))

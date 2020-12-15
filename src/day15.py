#!/usr/bin/env python

import collections
import sys


cache = dict(timestamp=0)


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    numbers = [int(number) for number in lines[0].split(',')]
    while True:
        last = numbers[-1]
        length = len(numbers)
        if length == 2020:
            return last
        if last in numbers[:-1]:
            # print('%s has been said before' % last)
            number = numbers[-2::-1].index(last) + 1
            # print('distance between the latest %s is %s in %s' % (last, number, numbers))
        else:
            # print('%s has not been said before' % last)
            number = 0
        numbers.append(number)


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    numbers = [int(number) for number in lines[0].split(',')]
    spoken_once = set()
    spoken_twice = set()
    while True:
        last = numbers[-1]
        length = len(numbers)
        if length % 10000 == 0:
            print(length)
        if length == 30000000:
            return last
        if last in spoken_twice:
            # print('%s has been said before' % last)
            number = numbers[-2::-1].index(last) + 1
            # print('distance between the latest %s is %s in %s' % (last, number, numbers))
        else:
            # print('%s has not been said before' % last)
            number = 0
        if number not in spoken_twice:
            if number in spoken_once:
                spoken_twice.add(number)
            else:
                spoken_once.add(number)
        numbers.append(number)


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

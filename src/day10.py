#!/usr/bin/env python

import collections
import sys


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    counts = collections.defaultdict(int)
    numbers = [int(line) for line in lines]
    numbers.sort()
    numbers.insert(0, 0)  # the outlet
    numbers.append(numbers[-1] + 3)  # my device

    for i, value in enumerate(numbers[1:]):
        counts[value - numbers[i]] += 1
    return counts[1] * counts [3]


chains_to_device = dict()


def get_chain_count(start, ups, device):
    """Return number of chains."""
    if start == device:
        print("bam!")
        return 1
    if start in chains_to_device:
        return chains_to_device[start]
    count = 0
    for i in ups[start]:
        count += get_chain_count(i, ups, device)
    chains_to_device[start] = count
    return count


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    numbers = [int(line) for line in lines]
    numbers.sort()
    numbers.insert(0, 0)  # the outlet
    device = numbers[-1] + 3
    numbers.append(device)  # my device

    ups = {}
    for number in numbers:
        ups[number] = [i for i in numbers if 1 <= (i - number) <= 3]
    return get_chain_count(0, ups, device)


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

#!/usr/bin/env python

import re
import sys


def solution(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().split('\n\n')
    print(lines)
    counts = []
    for line in lines:
        chars = set(line.replace('\n', ''))
        print(chars)
        counts.append(len(chars))
    print(sum(counts))

def solution2(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().split('\n\n')
    counts = []
    for lineset in lines:
        lines = lineset.splitlines()
        firstline = set(lines[0])
        for line in lines[1:]:
            firstline.intersection_update(line)
        counts.append(len(firstline))
    print(sum(counts))


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

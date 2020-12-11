#!/usr/bin/env python

import math
import sys


def solution(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    width = len(lines[0])
    hits = 0
    misses = 0
    pos = 0
    for line in lines[1:]:
        pos += 3
        pos %= width
        print("%s %s" % (line, pos))
        if line[pos] == '.':
            misses += 1
        else:
            hits += 1
    print("%d trees, %d misses" % (hits, misses))


def solution2(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    width = len(lines[0])
    all_hits = []
    for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        hits = 0
        misses = 0
        pos = 0
        for line in lines[down::down]:
            pos += right
            pos %= width
            # print("%s %s" % (line, pos))
            if line[pos] == '.':
                misses += 1
            else:
                hits += 1
        print("%d %d: %d trees, %d misses" % (right, down, hits, misses))
        all_hits.append(hits)
    print(math.prod(all_hits))


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

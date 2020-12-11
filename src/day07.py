#!/usr/bin/env python

import re
import sys
import collections


def get_outer_colors(rules, color):
    """Return a set of colors that may contain "color"."""
    outer_colors = set(mycolor for mycolor in rules if color in rules[mycolor])
    for outer_color in outer_colors.copy():
        outer_colors.update(get_outer_colors(rules, outer_color))
    return outer_colors


def solution(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    #print(lines)
    rules = collections.defaultdict(list)
    for line in lines:
        color, content = line.split(' bags contain ', 1)
        contents = content.rstrip('.').split(', ')
        for item in contents:
            item_count, remainder = item.split(' ', 1)
            item_color = remainder.rsplit(' ', 1)[0]
            if item_count != 'no':
                rules[color] += [item_color] * int(item_count)
            else:
                rules[color]
    print(len(get_outer_colors(rules, 'shiny gold')))


def get_inner_colors(rules, color):
    """Return a list of colors that "color" must contain."""
    inner_colors = rules[color][:]
    for inner_color in inner_colors[:]:
        inner_colors += get_inner_colors(rules, inner_color)
    return inner_colors


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    #print(lines)
    rules = collections.defaultdict(list)
    for line in lines:
        color, content = line.split(' bags contain ', 1)
        contents = content.rstrip('.').split(', ')
        for item in contents:
            item_count, remainder = item.split(' ', 1)
            item_color = remainder.rsplit(' ', 1)[0]
            if item_count != 'no':
                rules[color] += [item_color] * int(item_count)
            else:
                rules[color]
    print(len(get_inner_colors(rules, 'shiny gold')))


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

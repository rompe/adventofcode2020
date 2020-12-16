#!/usr/bin/env python

import collections
import itertools
import math
import sys


cache = dict(timestamp=0)


def parse_input(input_file):
    """Parse input file and return rules, my ticket, nearby tickets."""
    lines = open(input_file).read().split('\n\n')
    rules = {}
    for line in lines[0].splitlines():
        key, values = line.split(':')

        items = values.replace(' or ', ' ').split()
        rules[key] = items
    my_ticket = lines[1].splitlines()[1]
    tickets = lines[2].splitlines()[1:]
    return rules, my_ticket, tickets


def check_ranges(ranges, value):
    """Check if value is in any of the ranges."""
    for fromto in ranges:
        start, end = fromto.split('-')
        if int(value) in range(int(start), int(end) + 1):
            return True
        # else:
        #     print('%s is not between %s and %s' % (value, start, end))
    return False


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    # lines = open(input_file).read().splitlines()
    rules, my_ticket, tickets = parse_input(input_file)
    invalid_numbers = []
    invalid_tickets = set()
    for ticket in tickets:
        values = ticket.split(',')
        for value in values:
            for rule in rules:
                if check_ranges(rules[rule], value):
                    break
            else:
                invalid_tickets.add(ticket)
                invalid_numbers.append(int(value))
    return sum(invalid_numbers)


def check_column(rule, column):
    """Check if all values in column are covered by rule."""
    for value in column:
        if not check_ranges(rule, value):
            return False
    return True


def solution2(input_file):
    """Solve today's riddle."""
    # This is basically part 1...
    rules, my_ticket, tickets = parse_input(input_file)
    invalid_numbers = []
    invalid_tickets = set()
    for ticket in tickets:
        values = ticket.split(',')
        for value in values:
            for rule in rules:
                if check_ranges(rules[rule], value):
                    break
            else:
                invalid_tickets.add(ticket)
                invalid_numbers.append(int(value))
    for invalid_ticket in invalid_tickets:
        tickets.remove(invalid_ticket)
    # Part 2 follows...
    column_names = collections.defaultdict(list)
    columns = [[int(row.split(',')[column]) for row in tickets] for column in range(len(my_ticket.split(',')))]
    for index, column in enumerate(columns):
        for rule in rules:
            if check_column(rules[rule], column):
                print('%s ist %s' % (rule, index))
                column_names[rule].append(index)
                # break
        else:
            print("%s %s passt nicht" % (index, column))
    print(column_names)
    for dummy in range(len(columns) * len(columns)):
        for name in column_names.copy():
            if len(column_names[name]) == 1:
                for name2 in column_names:
                    if name != name2 and column_names[name][0] in column_names[name2]:
                        column_names[name2].remove(column_names[name][0])
    print(column_names)
    return math.prod(int(my_ticket.split(',')[column_names[name][0]]) for name in column_names if name.startswith('departure'))

if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

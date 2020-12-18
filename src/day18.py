#!/usr/bin/env python

import operator
import re
import sys


cache = dict(timestamp=0)


def parse_input(input_file):
    """Parse input file and return expressions."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    return lines


def calculate_expression(expression):
    """Calculate expression using nonsense rules."""
    if hasattr(expression, "group"):
        expression = expression.group(0).strip('()')
        # print("Converted expression:", expression)
    while '(' in expression:
        expression = re.sub(r'\([^)(]*\)', calculate_expression, expression)
        # print(expression)
    # print('Final expression:', expression)
    items = expression.split()
    previous = int(items[0])
    mode = operator.add
    for item in items[1:]:
        if item == '+':
            mode = operator.add
        elif item == '*':
            mode = operator.mul
        elif item.isdecimal():
            previous = int(mode(previous, int(item)))
        else:
            print("parsing error: %s" % item)
    return str(previous)


def solution1(input_file):
    """Solve today's riddle."""
    expressions = parse_input(input_file)
    result = 0
    for expression in expressions:
        result += int(calculate_expression(expression))
        # print('lap:', result)
    return result


def calculate_expression2(expression):
    """Calculate expression using nonsense rules."""
    if hasattr(expression, "group"):
        expression = expression.group(0).strip('()')
        # print("Converted expression:", expression)
    while '(' in expression:
        expression = re.sub(r'\([^)(]*\)', calculate_expression2, expression)
        # print(expression)
    while '+' in expression and '*' in expression:
        expression = re.sub(r'\d+\s*\+\s*\d+', calculate_expression2, expression)
        # print(expression)
    # print('Final expression:', expression)
    items = expression.split()
    previous = int(items[0])
    mode = operator.add
    for item in items[1:]:
        if item == '+':
            mode = operator.add
        elif item == '*':
            mode = operator.mul
        elif item.isdecimal():
            previous = int(mode(previous, int(item)))
        else:
            print("parsing error: %s" % item)
    return str(previous)


def solution2(input_file):
    """Solve today's riddle."""
    expressions = parse_input(input_file)
    result = 0
    for expression in expressions:
        result += int(calculate_expression2(expression))
        # print('lap:', result)
    return result


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

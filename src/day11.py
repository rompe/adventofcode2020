#!/usr/bin/env python

import collections
import sys


def get_surrounding(char, line, lines):
    """Return a list of seats surrounding this one."""
    # print("get_surrounding(%s, %s)" % (char, line))
    coords = ((char - 1, line - 1), (char, line - 1), (char + 1, line -1),
              (char - 1, line), (char + 1, line),
              (char - 1, line + 1), (char, line + 1), (char + 1, line + 1))
    result = []
    for char, line in coords:
        if 0 <= char < len(lines[0]) and 0 <= line < len(lines):
            # print(line, char, lines)
            result.append(lines[line][char])
    return result


def process_grid(lines):
    """Apply the rules to "lines" and return the result."""
    new_lines = []
    for lineno, line in enumerate(lines):
        new_line = ''
        for charno, char in enumerate(line):
            if char != '.':
                surrounding = get_surrounding(charno, lineno, lines)
                occupied = surrounding.count('#')
                if char == 'L' and occupied == 0:
                    char = '#'
                elif char == '#' and occupied >= 4:
                    char = 'L'
            new_line += char
        new_lines.append(new_line)
    # print('\n%s\n' % '\n'.join(new_lines))
    return new_lines


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    previous_lines = None
    while lines != previous_lines:
        previous_lines = lines
        lines = process_grid(lines)
    return ''.join(lines).count('#')


def get_next_in_sight(char, line, char_offset, line_offset, lines):
    """Return the next seat in sight."""
    new_char = char + char_offset
    new_line = line + line_offset
    if 0 <= new_char < len(lines[0]) and 0 <= new_line < len(lines):
        current = lines[new_line][new_char]
        # print("Line %d, char %d is %s" % (new_line, new_char, current))
        if current == '.':
            current = get_next_in_sight(new_char, new_line, char_offset, line_offset, lines)
        # print("Current is %s" % current)
        return current
    return ''


def get_surrounding2(char, line, lines):
    """Return a list of seats surrounding this one."""
    offsets = ((-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1))
    result = []
    for char_offset, line_offset in offsets:
        result.append(get_next_in_sight(char, line, char_offset, line_offset, lines))
    return result


def process_grid2(lines):
    """Apply the rules to "lines" and return the result."""
    new_lines = []
    for lineno, line in enumerate(lines):
        new_line = ''
        for charno, char in enumerate(line):
            if char != '.':
                surrounding = get_surrounding2(charno, lineno, lines)
                occupied = surrounding.count('#')
                if char == 'L' and occupied == 0:
                    char = '#'
                elif char == '#' and occupied >= 5:
                    char = 'L'
            new_line += char
        new_lines.append(new_line)
        # print('old line: %s' % line)
        # print('new line: %s' % new_line)
    # print('\n%s\n' % '\n'.join(new_lines))
    return new_lines


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    previous_lines = None
    while lines != previous_lines:
        previous_lines = lines
        lines = process_grid2(lines)
    # print('\n'.join(lines))
    return ''.join(lines).count('#')


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

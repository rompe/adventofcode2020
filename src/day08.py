#!/usr/bin/env python

import re
import sys
import collections


def solution(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    #print(lines)
    accu = 0
    visited = []
    lineno = 0
    while lineno not in visited:
        visited.append(lineno)
        line = lines[lineno]
        jmp = 1
        cmd, val = line.split()
        if cmd == "acc":
            accu += int(val)
        elif cmd == "jmp":
            jmp = int(val)
        lineno += jmp
    print(accu, visited)


def is_looping(lines):
    """Return True if the program in "lines" is an endless loop."""
    print(lines)
    accu = 0
    visited = []
    lineno = 0
    while lineno not in visited:
        visited.append(lineno)
        line = lines[lineno]
        jmp = 1
        cmd, val = line.split()
        if cmd == "acc":
            accu += int(val)
        elif cmd == "jmp":
            jmp = int(val)
        lineno += jmp
        if lineno >= len(lines):
            print("accu is %d" % accu)
            return False
    return True


def solution2(input_file):
    """Solve today's riddle."""
    lines = open(input_file).read().splitlines()
    for lineno, line in enumerate(lines):
        mylines = lines[:]
        if line.startswith("jmp"):
            mylines[lineno] = line.replace("jmp", "nop")
            if not is_looping(mylines):
                return str(lineno)
        elif line.startswith("nop"):
            mylines[lineno] = line.replace("nop", "jmp")
            if not is_looping(mylines):
                return str(lineno)
    return "Huh?"


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

#!/usr/bin/env python

import re
import sys


def solution(input_file):
    """Solve today's riddle."""
    docs = open(input_file).read().split('\n\n')
    needed = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    valids = 0
    for doc in docs:
        fields = [field.split(':')[0] for field in doc.split()]
        if needed.issubset(fields):
            valids += 1
    print(valids)


def solution2(input_file):
    """Solve today's riddle."""
    docs = open(input_file).read().split('\n\n')
    res = {"byr": "\d{4}", "iyr": "\d{4}", "eyr": "\d{4}",
           "hgt": "\d+(cm|in)", "hcl": "#[0-9a-f]{6}",
           "ecl": "(amb|blu|brn|gry|grn|hzl|oth)", "pid": "\d{9}"}
    needed = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    valids = 0
    for doc in docs:
        fields = dict(field.split(':') for field in doc.split())
        if needed.issubset(fields):
            toadd = 1
            for field in res:
                match = re.match(res[field] + '$', fields[field])
                if not match:
                    print("%s passt nicht" % field)
                    toadd = 0
                else:
                    if field == "byr" and not (1920 <= int(fields[field]) <= 2002):
                        toadd = 0
                    elif field == "iyr" and not (2010 <= int(fields[field]) <= 2020):
                        toadd = 0
                    elif field == "eyr" and not (2020 <= int(fields[field]) <= 2030):
                        toadd = 0
                    elif field == "hgt":
                        num = int(fields[field][:-2])
                        if fields[field].endswith("in") and not (59 <= num <= 76):
                            print("height %d in" % num)
                            toadd = 0
                        elif fields[field].endswith("cm") and not (150 <= num <= 193):
                            toadd = 0
                if not toadd:
                    print("%s: %s" % (field, fields[field]))
                    break
            valids += toadd
    print(valids)


if __name__ == "__main__":
    sys.exit(solution2(sys.argv[1]))

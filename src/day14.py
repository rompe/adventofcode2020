#!/usr/bin/env python

import collections
import sys


cache = dict(timestamp=0)


def int2bin(number):
    """Return number as a binary represented as a 36-byte string."""
    return "{0:036b}".format(number)


def bin2int(binstring):
    """Return 36 bit/byte binstring as an int."""
    return int(binstring, 2)


def modify_value(value, old_value, bitmask):
    """Return old_value modified with value and bitmask."""
    value = int2bin(int(value))
    new_value = ''
    for index, char in enumerate(value):
        if bitmask[index] == 'X':
            # print('set [{0}] to {1}'.format(index, char))
            new_value += char
        else:
            # print('set [{0}] to preset {1}'.format(index, bitmask[index]))
            new_value += bitmask[index]
    return new_value


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    memory = {}
    bitmask = 'X' * 36
    for line in lines:
        action, value = line.split(' = ')
        if action == 'mask':
            bitmask = value
        else:
            address = int(action.split('[')[1].split(']')[0])
            memory[address] = modify_value(value, memory.get(address, '0' * 36), bitmask)
        # print(memory)
    int_values = [bin2int(memory[key]) for key in memory]
    return sum(int_values)


def extrapolate_addresses(addresses):
    """Extrapolate addresses."""
    # print('extrapolate_addresses(%s)' % addresses)
    new_addresses = []
    for address in addresses:
        if 'X' in address:
            new_addresses += extrapolate_addresses([address.replace('X', '0', 1)])
            new_addresses += extrapolate_addresses([address.replace('X', '1', 1)])
        else:
            new_addresses.append(address)
    return new_addresses


def modify_address(address, bitmask):
    """Return a list of addresses."""
    value = int2bin(address)
    new_value = ''
    for index, char in enumerate(value):
        if bitmask[index] == '0':
            # print('set [{0}] to {1}'.format(index, char))
            new_value += char
        else:
            # print('set [{0}] to preset {1}'.format(index, bitmask[index]))
            new_value += bitmask[index]
    new_values = extrapolate_addresses([new_value])
    return [bin2int(new_value) for new_value in new_values]


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    memory = {}
    bitmask = 'X' * 36
    for line in lines:
        action, value = line.split(' = ')
        if action == 'mask':
            bitmask = value
        else:
            address = int(action.split('[')[1].split(']')[0])
            modified_value = modify_value(value, memory.get(address, '0' * 36), 'X' * 36)
            addresses = modify_address(address, bitmask)
            for address in addresses:
                memory[address] = modified_value
        # print(memory)
    int_values = [bin2int(memory[key]) for key in memory]
    return sum(int_values)


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

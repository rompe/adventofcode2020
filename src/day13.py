#!/usr/bin/env python

import sys


def solution1(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    timestamp, buses_line = lines
    buses = [int(bus) for bus in buses_line.split(',') if bus.isdecimal()]
    timestamp = int(timestamp)
    waiting_times = {bus - timestamp % bus: bus for bus in buses}
    min_time = min(waiting_times)
    return min_time * waiting_times[min_time]


def solution2(input_file):
    """Solve today's riddle."""
    # lines = open(input_file).read().split('\n\n')
    lines = open(input_file).read().splitlines()
    buses = [int(i) for i in lines[1].replace('x', '0').split(',')]
    max_bus = max(buses)
    max_bus_index = buses.index(max_bus)
    timestamp = max_bus - max_bus_index

    while True:
        timestamp += max_bus
        print(timestamp)
        for offset, bus in enumerate(buses):
            if bus != 0 and (timestamp + offset) % bus != 0:
                break
        else:
            return timestamp


if __name__ == "__main__":
    print(solution1(sys.argv[1]))
    print(solution2(sys.argv[1]))

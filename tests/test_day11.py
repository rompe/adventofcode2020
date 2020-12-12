#!/usr/bin/env python
"""Test for today."""

import unittest
import day11


result_after_seven_rounds = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""


class Day11Test(unittest.TestCase):
    """Test for today."""

    def setUp(self) -> None:
        self.input_file = __file__.replace("test_", "").replace(".py", ".txt")

    def test_process_grid(self):
        """Test process_grid()."""
        lines = open(self.input_file).read().splitlines()
        for dummy in range(8):
            lines = day11.process_grid(lines)
        self.assertEqual('\n'.join(lines), result_after_seven_rounds.strip())

    def test_solution1(self):
        """Test solution1()."""
        result = day11.solution1(self.input_file)
        self.assertEqual(result, 37)

    def test_get_surrounding2(self):
        """Test get_surrounding2()."""
        result = day11.get_surrounding2(7, 2, result_after_seven_rounds.splitlines())
        self.assertEqual(''.join(result), 'LLL##L')

    def test_solution2(self):
        """Test solution2()."""
        result = day11.solution2(self.input_file)
        self.assertEqual(result, 26)

#!/usr/bin/env python
"""Test for today."""

import unittest
import day14


class Day12Test(unittest.TestCase):
    """Test for today."""

    def setUp(self) -> None:
        self.input_file = __file__.replace("test_", "").replace(".py", ".txt")
        self.input_file2 = __file__.replace("test_", "").replace(".py", "-2.txt")

    def test_solution1(self):
        """Test solution1()."""
        result = day14.solution1(self.input_file)
        self.assertEqual(result, 165)

    def test_modify_address(self):
        """Test modify_address()."""
        address = 42
        bitmask = '000000000000000000000000000000X1001X'
        expected_result = [26, 27, 58, 59]
        result = day14.modify_address(address, bitmask)
        self.assertEqual(result, expected_result)

    def test_solution2(self):
        """Test solution2()."""
        result = day14.solution2(self.input_file2)
        self.assertEqual(result, 208)

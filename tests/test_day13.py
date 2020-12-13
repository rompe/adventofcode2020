#!/usr/bin/env python
"""Test for today."""

import unittest
import day13


class Day12Test(unittest.TestCase):
    """Test for today."""

    def setUp(self) -> None:
        self.input_file = __file__.replace("test_", "").replace(".py", ".txt")

    def test_solution1(self):
        """Test solution1()."""
        result = day13.solution1(self.input_file)
        self.assertEqual(result, 295)

    def test_solution2(self):
        """Test solution2()."""
        result = day13.solution2(self.input_file)
        self.assertEqual(result, 1068781)

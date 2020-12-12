#!/usr/bin/env python
"""Test for today."""

import unittest
import day10


class Day10Test(unittest.TestCase):
    """Test for today."""

    def setUp(self) -> None:
        self.input_file = __file__.replace("test_", "").replace(".py", ".txt")

    def test_solution1(self):
        """Test solution1()."""
        result = day10.solution1(self.input_file)
        self.assertEqual(result, 220)

    def test_solution2(self):
        """Test solution1()."""
        result = day10.solution2(self.input_file)
        self.assertEqual(result, 19208)

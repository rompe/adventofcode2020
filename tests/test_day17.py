#!/usr/bin/env python
"""Test for today."""

import unittest
import day17


class Day17Test(unittest.TestCase):
    """Test for today."""

    def setUp(self) -> None:
        self.input_file = __file__.replace("test_", "").replace(".py", ".txt")

    def test_solution1(self):
        """Test solution1()."""
        result = day17.solution1(self.input_file)
        self.assertEqual(result, 112)

    def test_solution2(self):
        """Test solution2()."""
        result = day17.solution2(self.input_file)
        self.assertEqual(result, 848)

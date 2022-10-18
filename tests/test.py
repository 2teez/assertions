#!/usr/bin/env python3
import unittest
import sys 
sys.path.append("..")
from assertions import assert_eq, asserts


class Tester(unittest.TestCase):
    def test_asserts(self):
        self.assertEqual(asserts([], True))

    def test_asserts(self):
        self.assertEqual(asserts("Lagos"), True)

    def test_assert_eq(self):
        self.assertEqual(assert_eq([0, 1, 2], list(range(5))), True)

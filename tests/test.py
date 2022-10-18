#!/usr/bin/env python3
import unittest
from ..assertions import assertions


class Tester(unittest.TestCase):
    def test_asserts(self):
        self.assertEqual(assertions.asserts([], True))

    def test_asserts(self):
        self.assertEqual(assertions.asserts("Lagos"), True)

    def test_assert_eq(self):
        self.assertEqual(assertions.assert_eq([0, 1, 2], list(range(5))))

#!/usr/bin/env python3
import unittest
import sys
sys.path.append("..")
from assertions import assert_eq, assert_eq_prnt, asserts

def product(lst: list[int]) -> int:
    result = 1
    for n in lst:
        result *= n
    return result

assert_eq_prnt(product([2,3,5,7]), 21, show=True)
        

class Tester(unittest.TestCase):
    def test_asserts(self):
        self.assertEqual(asserts([]), False)

    def test_asserts2(self):
        self.assertEqual(asserts("Lagos"), True)

    def test_assert_eq(self):
        self.assertEqual(assert_eq([0, 1, 2], list(range(5))), True)

    def test_assert_eq2(self):
        self.assertEqual(assert_eq([0,1,2,3,4], list(range(5))), True)

    def test_assert_eq_product(self):
        self.assertEqual(assert_eq(product([2,3,5,7]), 210), True)

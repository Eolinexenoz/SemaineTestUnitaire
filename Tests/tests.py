import unittest
import re

from Sample.parse import InputParser


class Tests(unittest.TestCase):

    def test_input(self):
        enteredstring = "4d6 5d20 4d3"
        ipp = InputParser()
        res = ipp.check(enteredstring)
        self.assertTrue(res)

unittest.main()
import unittest
import re

from Sample.parse import InputParser


class Tests(unittest.TestCase):

    def test_input(self):
        enteredstring = "4d6+99 100d2+100"
        ipp = InputParser()
        res = ipp.check(enteredstring)
        self.assertTrue(res)

unittest.main()
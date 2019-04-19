import unittest
from funcs import test

class FuncsTestCase(unittest.TestCase):
    def test1(self):
        res = test(1,2,3)
        self.assertEqual(res, 6)

unittest.main()
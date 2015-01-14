import unittest

from custommath import CustomMath
from unittest import TestCase

class TestCustomMath(TestCase):
    def setUp(self):
        self.instance = CustomMath(10, 2)

    def test_add(self):
        self.assertEqual(self.instance.add(), 12)

    def test_subtract(self):
        self.assertEqual(self.instance.subtract(), 8)

if __name__ == '__main__':
    unittest.main()

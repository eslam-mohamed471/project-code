from hello import rearrange
import unittest
"""print now"""
class Testrea(unittest.TestCase):
    def test_basic(self):
        testcase = "Eslam, mohamed"
        expected = ("mohamed Eslam")
        self.assertEqual(rearrange(testcase),expected)
    def test_empty(self):
        testcase = ""
        expected = ("")
        self.assertEqual(rearrange(testcase),expected)
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange(testcase),expected)
    def test_one_name(self):
        testcase = "Hopper"
        expected = "Hopper"
        self.assertEqual(rearrange(testcase),expected)
unittest.main()

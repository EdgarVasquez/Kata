import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_ContainRange(self):
        self.assertEqual(True, main.ContainsRange(7))  # add assertion here

    def test_ContainRange2(self):
        self.assertEqual(True, main.ContainsRange(10))

    def test_ContainRange3(self):
        self.assertEqual(True, main.ContainsRange2(2))


if __name__ == '__main__':
    unittest.main()

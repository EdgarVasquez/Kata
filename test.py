import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, main.RangeInteger1(2))  # add assertion here pasar

    def test_ContainRange(self):
        self.assertEqual(False, main.ContainsRange(7))  # add assertion here no va a pasar

    def test_ContainRange2(self):
        self.assertEqual(False, main.ContainsRange(10)) # no va a pasar

    def test_ContainRange3(self):
        self.assertEqual(False, main.ContainsRange2(2)) # no va pasar

    def test_ContainRange4(self):
        self.assertEqual(True, main.ContainsRange3(3)) #  va pasar

    def test_ContainRange5(self):
            self.assertEqual(True, main.ContainsRange3(5))  # va pasar

    def test_ContainRange6(self):
        self.assertEqual(False, main.ContainsRange3(11))  # no va pasar

    def test_ContainRange7(self):
        self.assertEqual(True, main.ContainsRange3(3))  # va pasar

    def test_ContainRange9(self):
            self.assertEqual(",2,3,4,5", main.GetAllPoints(2,6))  # va pasar


if __name__ == '__main__':
    unittest.main()

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(7, 5), 2)
        self.assertEqual(self.calc.subtract(-1, -3), 2)
        self.assertEqual(self.calc.subtract(-7, 5), -12)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(9, 9), 81)
        self.assertEqual(self.calc.multiply(-9, 9), -81)
        self.assertEqual(self.calc.multiply(-9, -9), 81)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(0, 1), 0)
import unittest
from app import app, perform_operation

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = perform_operation(5, 3, 'add')
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = perform_operation(10, 4, 'subtract')
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = perform_operation(3, 6, 'multiply')
        self.assertEqual(result, 18)

    def test_division(self):
        result = perform_operation(8, 2, 'divide')
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        result = perform_operation(8, 0, 'divide')
        self.assertEqual(result, 'Cannot divide by zero')

if __name__ == '__main__':
    unittest.main()

import unittest
from app import UnitConverterHandler

class TestConverterLogic(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        celsius = 0
        expected_fahrenheit = 32
        calculated = (celsius * 9/5) + 32
        self.assertEqual(calculated, expected_fahrenheit)

    def test_boiling_point(self):
        celsius = 100
        expected_fahrenheit = 212
        calculated = (celsius * 9/5) + 32
        self.assertEqual(calculated, expected_fahrenheit)

if __name__ == '__main__':
    unittest.main()
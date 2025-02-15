#Kypton Lantz
#February 14, 2025
#Module 7 - Assignment 2: Test Cases
#Write a program that produces the required results. Document those results, then add unit tests to test whether functions work as required.

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_country function."""
    def test_city_country(self):
        """Test that the function returns the correct string."""
        result = city_country('santiago', 'chile')
        expected = 'Santiago, Chile'
        print(f"\nExpected: {expected}")
        print(f"Actual Result: {result}")
        self.assertEqual(result, 'Santiago, Chile')
        print("Test Passed!\n")

if __name__ == '__main__':
    unittest.main()

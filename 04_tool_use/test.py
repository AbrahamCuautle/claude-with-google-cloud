import unittest
import math
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test suite for the calculate_pi function."""
    
    def test_pi_accuracy_5_digits(self):
        """Test that pi is calculated accurately to 5 decimal places."""
        calculated_pi = calculate_pi()
        actual_pi = math.pi
        
        # Round to 5 decimal places and compare
        calculated_rounded = round(calculated_pi, 5)
        actual_rounded = round(actual_pi, 5)
        
        self.assertEqual(calculated_rounded, actual_rounded,
                        f"Expected {actual_rounded}, but got {calculated_rounded}")
    
    def test_pi_starts_with_314159(self):
        """Test that pi starts with 3.14159..."""
        calculated_pi = calculate_pi()
        
        # Check first 6 significant figures (3.14159)
        pi_str = f"{calculated_pi:.5f}"
        self.assertTrue(pi_str.startswith("3.14159"),
                       f"Expected pi to start with 3.14159, but got {pi_str}")
    
    def test_pi_in_correct_range(self):
        """Test that calculated pi is within reasonable bounds."""
        calculated_pi = calculate_pi()
        
        # Pi should be between 3.14159 and 3.14160
        self.assertGreater(calculated_pi, 3.14159,
                          "Pi should be greater than 3.14159")
        self.assertLess(calculated_pi, 3.14160,
                       "Pi should be less than 3.14160")
    
    def test_pi_type(self):
        """Test that the function returns a float."""
        calculated_pi = calculate_pi()
        self.assertIsInstance(calculated_pi, float,
                            "calculate_pi should return a float")
    
    def test_pi_absolute_difference(self):
        """Test that the absolute difference from actual pi is minimal."""
        calculated_pi = calculate_pi()
        actual_pi = math.pi
        
        # Difference should be less than 0.000001 (6 decimal places)
        difference = abs(calculated_pi - actual_pi)
        self.assertLess(difference, 0.00001,
                       f"Difference {difference} is too large")
    
    def test_pi_compare_with_known_value(self):
        """Test against the known value of pi to 10 decimal places."""
        calculated_pi = calculate_pi()
        known_pi = 3.1415926536  # Pi to 10 decimal places
        
        # Check accuracy to 5 decimal places
        self.assertAlmostEqual(calculated_pi, known_pi, places=5,
                              msg="Pi not accurate to 5 decimal places")


if __name__ == '__main__':
    print("Running tests for calculate_pi function...")
    print(f"\nCalculated Pi: {calculate_pi()}")
    print(f"Actual Pi:     {math.pi}")
    print(f"Difference:    {abs(calculate_pi() - math.pi)}\n")
    
    unittest.main()

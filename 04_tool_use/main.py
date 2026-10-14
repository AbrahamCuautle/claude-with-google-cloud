def greeting():
    print("Hi there")


def calculate_pi():
    """
    Calculate pi to the 5th decimal digit using the Machin formula.
    
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: Pi calculated to at least 5 decimal places (3.14159...)
    """
    def arctan(x, num_terms=20):
        """
        Calculate arctan(x) using Taylor series expansion.
        arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
        """
        result = 0
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * (x ** (2 * n + 1)) / (2 * n + 1)
        return result
    
    # Machin's formula: pi = 4 * (4 * arctan(1/5) - arctan(1/239))
    pi_value = 4 * (4 * arctan(1/5, 30) - arctan(1/239, 30))
    
    return pi_value
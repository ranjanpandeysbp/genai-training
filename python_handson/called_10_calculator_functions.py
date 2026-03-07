"""
Calculator Functions - Basic arithmetic operations with error handling
"""

def add(a, b):
    """
    Add two numbers
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers with error handling for division by zero
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        Result of a divided by b
        
    Raises:
        ValueError: If b is zero
        TypeError: If inputs are not numbers
    """
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero. Divisor must be a non-zero number.")
        
        # Check if inputs are numbers
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers (int or float).")
        
        return a / b
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except TypeError as te:
        print(f"Error: {te}")
        return None


# Example usage and testing
if __name__ == "__main__":
    # Test addition
    print("=== Addition ===")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"3.5 + 2.5 = {add(3.5, 2.5)}")
    
    # Test subtraction
    print("\n=== Subtraction ===")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"3.5 - 2.5 = {subtract(3.5, 2.5)}")
    
    # Test multiplication
    print("\n=== Multiplication ===")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"3.5 * 2 = {multiply(3.5, 2)}")
    
    # Test division (normal case)
    print("\n=== Division ===")
    print(f"10 / 5 = {divide(10, 5)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"7 / 2 = {divide(7, 2)}")
    
    # Test division by zero (error handling)
    print("\n=== Division by Zero Error Handling ===")
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
    
    # Test with invalid input (error handling)
    print("\n=== Invalid Input Error Handling ===")
    result = divide(10, "five")
    print(f"10 / 'five' = {result}")

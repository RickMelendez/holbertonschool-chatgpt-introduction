#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input integer.
         If the input is negative, returns a message stating that factorial is not defined for negative numbers.
         If the input is 0, returns 1.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 filename.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: Input must be an integer")
    sys.exit(1)

result = factorial(n)
print(result)

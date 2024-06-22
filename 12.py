#!/usr/bin/env python3
"""
checks if a number is even or odd
"""

def check_even_odd():
    """
    takes an integer input
    checks if it is an even number or odd
    prints output to user
    """
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check_even_odd()

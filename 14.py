#!/usr/bin/env python3
"""
prompts user to enter an number until user inputs number greater than 100
"""

while True:
    """loops endlessly"""
    num = int(input("Enter an integer: "))

    if num > 100:
        break;



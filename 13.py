#!/usr/bin/env python3
"""
prints numbers between 0ne and 50 that are divisible by 3
"""

for x in range(1, 51):
    """iterates from 1 to 50"""
    if x % 3 == 0:
        # checks if current number is divisible by three and prints it
        print(x)

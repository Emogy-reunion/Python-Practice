#!/usr/bin/env python
"""
This program:
    asks user for a number
    prints a list of all divisors of that number range 2000
"""

a = list(range(2000))
divisor_list = []
num = int(input("Enter a number: "))

for x in a:
    if x % num == 0:
        divisor_list.append(x)

print(divisor_list)

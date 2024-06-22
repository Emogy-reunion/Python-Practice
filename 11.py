#!/usr/bin/env python3
"""
swaps two numbers without using a temporary variable
"""

a = 40
b = 60
print(f"a before swapping is {a}")
print(f"b before swapping is {b}")

a, b = b, a

print(f"a after swapping is {a}")
print(f"b after swapping is {b}")

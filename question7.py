#!/usr/bin/env python
"""
This program:
    List comprehension
    Takes a list a makes a new list with only even elements
"""
a = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 10]
new_list = [x for x in a if x % 2 == 0]
print(new_list)

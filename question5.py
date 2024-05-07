#!/usr/bin/env python
"""
This program:
    takes two lists
    returns a list containing all elements that are common in both lists
"""

a = [1, 2, 3, 4, 4, 5]
b = [4, 7, 8, 9, 20, 5, 2, 5, 1]
new_list = []
for x in a:
    if x in b and x not in new_list:
        new_list.append(x)

print(new_list)

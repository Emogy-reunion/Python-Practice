#!/usr/bin/env python
"""
This program:
    filters out elements that are less than 5 from a list
    adds them to a new list and prints them out
    asks a user for a number and returns a list that oy contains elements from original list smaller than the one given by user
"""

a = [1, 1, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for x in a:
    if x < 5:
        new_list.append(x)

print(new_list)

another_list = []
num = int(input("Enter a number: "))
for x in a:
    if x < num:
        another_list.append(x)

print(another_list)

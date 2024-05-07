#!/usr/bin/env python
from datetime import datetime

"""
this code does:
    allows user to enter a name and age
    prints a message telling them what year they will turn 100years old
    prompts user to enter another number
    print the above prompt that number of times
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))
years_rem = 100 - age
year = datetime.now().year + years_rem
print(f"{name} will turn 100 years old in the year {year} after {years_rem} years")
number = int(input("Enter a number: "))

x = 0
while x<number:
    print(f"{name} will turn 100 years old in the year {year} after {years_rem} years")
    x+=1

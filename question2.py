#!/usr/bin/env python

"""
This code:
    asks user for a number
    prints an appropriate message if no is even or ofd
    checks if a number is a multiple of 4
    asks user to enter two numbers number 1 and number 2
    checks if number1 divides number 2 evenly and prints an appropriate message
"""

number = int(input("Enter a number: "))
if number%2 == 0:
    print("This number is even")
else:
    print("This numbet is odd")

if number%4 == 0:
    print("This number is a multiple of 4")

num = int(input("Enter a number1: "))
check = int(input("Enter a number2: "))
if num%check == 0:
    print("Number1 evenly divides number2")
else:
    print("Number1 doesn't evenly divide number2")

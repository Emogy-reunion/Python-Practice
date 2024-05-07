#!/usr/bin/env python
"""
This program:
    asks user to enter a string
    checks if it's a palindrome
"""

# Ask the user for input
user_input = input("Enter a string: ")

# Remove whitespace and convert to lowercase
cleaned_input = user_input.lower().replace(" ", "")

# Check if the cleaned input is equal to its reverse
if cleaned_input == cleaned_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


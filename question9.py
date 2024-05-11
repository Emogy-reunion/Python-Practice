#!/usr/bin/env python
import random


"""
This program:
    generates a random number between 1 and 9
    asks user to guess number
    compares the input with the number
    """

rand_num = random.randint(1, 9)
guess = int(input("Guess a nymber between 1 ans 9: "))
if guess == rand_num:
    print("You guessed right!")
elif guess < rand_num:
    print("You guessed too low!")
else:
    print("You guessed too high!")

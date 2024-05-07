#!/usr/bin/env python
"""
A basic rock paper scissor game
"""
print("Options are: ")
print("R for rock")
print("S for scissors")
print("P for paper")

# Define winning conditions
winning_conditions = {
    'R': 'S',  # Rock beats Scissors
    'S': 'P',  # Scissors beats Paper
    'P': 'R'   # Paper beats Rock
}

while True:
    player1 = input("Player1: ").upper()
    player2 = input("Player2: ").upper()

    if player1 == player2:
        print("Draw!")
    elif winning_conditions[player1] == player2:
        print("Player1 wins!")
        print("Game Over!")
        break
    else:
        print("Player2 wins!")
        print("Game Over!")
        break

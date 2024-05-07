#!/usr/bin/env python
"""
A basic rock paper scissor game
"""
print("Options are: ")
print("R for rock")
print("S for scissors")
print("P for paper")

while True:
    player1 = input("Player1: ").upper()
    player2 = input("Player2: ").upper()

    if player1 == 'R' and player2 == 'S':
        print("Player1 wins!")
        print("Game Over!")
        break
    elif player1 == 'S' and player2 == 'R':
        print("Player2 wins!")
        print("Game Over!")
        break
    elif player1 == 'S' and player2 == 'P':
        print("Player1 wins!")
        print("Game Over!")
        break
    elif player1 == 'P' and player2 == 'S':
        print("Player2 wins!")
        print("Game Over!")
        break
    elif player1 == 'P' and player2 == 'R':
        print("Player1 wins!")
        print("Game Over!")
        break
    elif player1 == 'R' and player2 == 'P':
        print("Player2 wins!")
        print("Game Over!")
        break
    else:
        print("Draw!")

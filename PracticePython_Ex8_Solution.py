# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:56:51 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 8: List Rock Paper Scissors ###

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)
#   Remember the rules:
#       Rock beats scissors
#       Scissors beats paper
#       Paper beats rock


player1 = input("\nPlayer1, enter your play: ")
player2 = input("\nPlayer2, enter your play: ")

plays = ['rock', 'scissors', 'paper']

if player1 == player2:
    print("It's a tie! Play again?")
elif player1 == plays[0] and player2 == plays[1]:
    print("Player1 wins! Play again?")
elif player1 == plays[1] and player2 == plays[2]:
    print("Player1 wins! Play again?")
elif player1 == plays[2] and player2 == plays[0]:
    print("Player1 wins! Play again?")
elif player1 == plays[1] and player2 == plays[0]:
    print("Player2 wins! Play again?")
elif player1 == plays[2] and player2 == plays[1]:
    print("Player2 wins! Play again?")
elif player1 == plays[0] and player2 == plays[2]:
    print("Player2 wins! Play again?")
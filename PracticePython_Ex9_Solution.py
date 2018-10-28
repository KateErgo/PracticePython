# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 10:10:16 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 9: Guessing Game One ###

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

#   Extras:
#       1. Keep the game going until the user types “exit”
#       2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
number = random.randint(1,10)

guess = int(input("\nI have a number in my mind. Take a guess: "))

if guess == number:
    print("You guessed it! The number is: " + number)
elif guess < number:
    print("Too low!")
else:
    print("Too high!")
    
### Extras 1
import random
number = random.randint(1,10)

keepGoing = True

while keepGoing:
    guess = input("\nI have a number in my mind. Try to take a guess. (Press 'exit' to stop the game): ")

    if guess == 'exit':
        break
    elif int(guess) == number:
        print("You guessed it! The number is: " + str(number) + ".")
    elif int(guess) < number:
        print("Too low!")
    else:
        print("Too high!")
        
### Extras 2
import random
number = random.randint(1,10)

keepGoing = True
counter = 0

while keepGoing:
    guess = input("\nI have a number in my mind. Try to take a guess. (Press 'exit' to stop the game): ")
    counter = counter + 1
    
    if guess == 'exit':
        break
    elif int(guess) == number:
        print("You guessed it! The number is: " + str(number) + ".")
        print("\nIt took you " + str(counter) + " guess(es) to find the number.")
    elif int(guess) < number:
        print("Too low!")
    else:
        print("Too high!")

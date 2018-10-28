# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:14:47 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 1: Character Input ###

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

#   Extras:
#       Add on to the previous program by asking the user for another number and printing out that many copies of 
#       the previous message. (Hint: order of operations exists in Python)
#       Print out that many copies of the previous message on separate lines. 
#       (Hint: the string "\n is the same as pressing the ENTER button)


name = input("\nPlease enter you name: ")
age = int(input("\nPlease enter your age: "))
number = int(input("\nPlease enter a number of your liking: "))

year = (100 - age) + 2018

print(("\nYou will turn 100 years old in the year: " + str(year) + ".") * number)

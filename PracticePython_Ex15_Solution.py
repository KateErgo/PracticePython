# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:15:31 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 15: Reverse Word Order ###

# Write a program (using functions!) that asks the user for a long string containing multiple words. 
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#   My name is Michele
#   Then I would see the string:
#   Michele is name My
#   shown back to me.

string = input("\nPlease enter a string containing multiple words: ")

def reverse(string):
    
    words = string.split()
    reversed_string = words[::-1]
    
    return ' '.join(reversed_string)

reverse(string)
    
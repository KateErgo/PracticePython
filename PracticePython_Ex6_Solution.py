# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:03:05 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 6: String Lists ###

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("\nEnter a string: ")

if string == string[::-1]:
    print("Yes, " + "'" + string + "'" + " is a palindrome.")
else:
    print("No, " + "'" + string + "'" + " is not a palindrome.")
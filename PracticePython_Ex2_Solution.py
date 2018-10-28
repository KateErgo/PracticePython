# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:27:41 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 2: Odd Or Even ###

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#   Extras:
#       1. If the number is a multiple of 4, print out a different message.
#       2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#       If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


### Extras 1 
number = int(input("\nPlease enter a number of you liking: "))

if number % 4 == 0:
    print("Your number is a multiple of 4.")
elif number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
    
### Extras 2

num = int(input("\nPlease enter a number of you liking: "))
check = int(input("\nPlease enter another number of you liking: "))

if check % num == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
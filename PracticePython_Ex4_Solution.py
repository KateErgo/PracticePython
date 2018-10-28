# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:47:37 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 4: Divisors ###

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


number = int(input("\nChoose a number of your liking: "))
divisors = []

for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)
print(divisors)
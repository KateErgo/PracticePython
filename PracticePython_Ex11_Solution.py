# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 10:57:02 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 11: Check Primality Functions ###

# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def isPrime():
     
    number = int(input("\nEnter a number: "))
    
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                print("It's not a prime!")
                break
        else:
            print("It's a prime!")
    else:
        print("It's not a prime!")
        
isPrime()
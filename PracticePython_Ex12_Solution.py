# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:29:47 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 12: List Ends ###

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of 
# only the first and last elements of the given list. For practice, write this code inside a function.


a = [5, 10, 15, 20, 25]
b = []

def firstAndLast(a):
    
    b = []
    
    b.append(a[0])
    b.append(a[-1])
    
    return b
    
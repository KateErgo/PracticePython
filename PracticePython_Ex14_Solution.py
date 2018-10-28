# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:25:16 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 14: List Remove Duplicates ###

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list 
# minus all the duplicates.

#   Extras:
#       1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#       2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 2, 3, 5, 3, 2, 5, 1, 6, 7]

### Using loops
def rm_duplicates(a):
    
    b = []
    for element in a:
        if element not in b:
            b.append(element)
        
    return b

### Using sets
def rm_duplicates2(a):
   
    b = list(set(a))
    
    return b

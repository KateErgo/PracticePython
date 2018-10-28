# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 08:52:50 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 5: List Overlap ###

# Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#   Extras:
#       1. Randomly generate two lists to test this
#       2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

c = list(set(a).intersection(b))
print(c)

### Extras 1
import random
a = random.sample(range(30),10)
b = random.sample(range(30),15)

c = []

c = list(set(a).intersection(b))
print(a)
print(b)
print(c)

### Extras 2

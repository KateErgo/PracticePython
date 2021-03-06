# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 18:33:28 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 23: File Overlap ###

# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of 
# happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other number. 
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
# The explanation is easier with an example, which I will describe below.)

import os
os.chdir("C:/Users/kate/1620_PhD/Self study/Python/PracticePython3")

primes = set(open('primenumbers.txt').read().split())
happies = set(open('happynumbers.txt').read().split())
overlap = primes.intersection(happies)
 
print(overlap)
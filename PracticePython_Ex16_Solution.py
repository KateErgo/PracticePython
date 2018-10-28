# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:22:30 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 16: Password Generator ###

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of 
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password 
# every time the user asks for a new password. Include your run-time code in a main method.

#   Extra:
#       Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


import string
from random import *

min_char = 4
max_char = 8

all_char = string.ascii_letters + string.punctuation + string.digits

question = input("Would you like to generate a new password? [y/n]: ")

if question == 'y':
    generate_pass = ''.join(choice(all_char) for i in range(randint(min_char, max_char)))
else:
    exit
    
print ("Here you go, your password is: ", generate_pass)

# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:54:48 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 22: Read From File ###

# Given a .txt file that has a list of a bunch of names, count how many of each name there are 
# in the file, and print out the results to the screen. I have a .txt file for you, if you want 
# to use it!

#   Extra:
#       1. Instead of using the .txt file from above (or instead of, if you want the challenge), 
#           take this .txt file, and count how many of each “category” of each image there are. 
#           This text file is actually a list of files corresponding to the SUN database scene 
#           recognition database, and lists the file directory hierarchy for the images. 
#           Once you take a look at the first line or two of the file, it will be clear which 
#           part represents the scene category. To do this, you’re going to have to remember a bit 
#           about string parsing in Python 3. I talked a little bit about it in this post.

import os
os.chdir("C:/Users/kate/1620_PhD/Self study/Python/PracticePython3")

f = open('nameslist.txt', 'r')
if f.mode == 'r':
    contents = f.read()
    print(contents)
    
print("\nLuke: " + str(contents.count('Luke')))
print("\nLea: " + str(contents.count('Lea')))
print("\nDarth: " + str(contents.count('Darth')))


### Extras 1 
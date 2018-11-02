# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:30:22 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 20: Element Search ###

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest 
# to largest) and another number. The function decides whether or not the given number is inside the list and 
# returns (then prints) an appropriate boolean.

#   Extras:
#        1. Use binary search.

def element_search(list_num, number):
    
    list_num = sorted(list_num)
    
    if number in list_num:
        return True
    else:
        return False
    
def main():
    
    list_num = input("\nEnter a list of numbers: ")
    number = input("\nEnter a number: ")
    
    result = element_search(list_num, number)
    
    print(result)
    
main()


### Extras 1

def binary_search(list_num, number):
    
    list_num = sorted(list_num)
    
    first = 0
    last = len(list_num) - 1
    found = False
    
    while first <= last and not found:
        middle = (first + last) // 2
        if list_num[middle] == number:
            found = True
        else:
            if number < list_num[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

def main():
    
    list_num = input("\nEnter a list of numbers: ")
    number = input("\nEnter a number: ")
    
    result = element_search(list_num, number)
    
    print(result)
    
main()
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 09:30:23 2018

@author: kate
"""

#########################
#### Practice Python ####
#########################

### Exercise 17: Decode A Web Page ###

# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles 
# on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

all_titles = []

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
titles = soup.find_all(class_="story-heading")

for title in titles:
    all_titles.append(title.text)
    
print(all_titles)


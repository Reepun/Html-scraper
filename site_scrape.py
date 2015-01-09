'''
Created on Jan 9, 2015

@author: Fredrik Nilsson
'''
#Using lxml's html functions and requests http get.
from lxml import html
import requests
#Empty dictionary for the days and dishes. Is this the most optimal way?
farozon = {}

#Contact the page
page = requests.get("http://www.farozon.se/lunchmeny-20207064")
#Pull the raw html tree
tree = html.fromstring(page.content)

#Define days as the html "<tr>" tag, ranging from the first, to last (-1)
days = tree.cssselect("#block_82470858 table tr")[1:-1]
#Cycle the days from above
for item in days:
    #Assigning each cell (<td>) using findall() to locate them and their content.
    cells = item.findall('td')
    #Assigning the first, leftmost, cell as the day. Grabbig all the text using text_content and encoding it with latin-1
    day = cells[0].text_content().encode('latin-1')
    #Switching cells using -1, moving to the second cell, which contains the dish. Storing it in Dishes using text_content and encoding with latin-1. Also stripping away all html using strip()
    dishes = cells[-1].text_content().encode('latin-1').strip()
    #saving the dish in the dictionary with the day as it's key.
    #Some keys screw up due to some unicode characters being left in. Need to clean that. 
    farozon[day] = dishes
    
#bajs
print farozon

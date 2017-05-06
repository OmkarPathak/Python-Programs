# Author: OMKAR PATHAK
# This script helps us to enter a word and get precise meaning for that word from vocabulary.com

import urllib.request
from bs4 import BeautifulSoup

word = input('Enter the word of which you want to find the meaning: ')

# Get the meaning by scrapping www.vocabulary.com
url = "https://www.vocabulary.com/dictionary/" + word + ""
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, 'lxml')
soup1 = soup.find(class_="short")

# If certain word's meaning is not found
try:
    soup1 = soup1.get_text()
except AttributeError:
    print('Cannot find such word! Check spelling.')
    exit()

# Print short meaning
print ('-' * 25 + '->',word,"<-" + "-" * 25)
print ("SHORT MEANING: ",soup1)
print ('-' * 65)

# Print long meaning
soup2 = soup.find(class_="long")
soup2 = soup2.get_text()

print ('-' * 65)

# Print instances like Synonyms, Antonyms, etc.
soup3 = soup.find(class_="instances")
txt = soup3.get_text()
txt1 = txt.rstrip()

print (' '.join(txt1.split()))

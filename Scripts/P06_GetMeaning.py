# Author: OMKAR PATHAK
# This script helps us to enter a word and get precise meaning for that word from vocabulary.com

import urllib.request
from bs4 import BeautifulSoup

word = input('Enter the word of which you want to find the meaning: ')

url = "https://www.vocabulary.com/dictionary/"+word+""
htmlfile = urllib.request.urlopen(url)
soup = BeautifulSoup(htmlfile, 'lxml')
soup1 = soup.find(class_="short")

try:
    soup1 = soup1.get_text()
except AttributeError:
    print('Cannot find such word! Check spelling.')
    exit()

print ('-' * 30 + '->',word,"<-" + "-" * 30)
print ("SHORT MEANING: ",soup1)
print ('-' * 65)

soup2 = soup.find(class_="long")
soup2 = soup2.get_text()

print ('-' * 65)

soup3 = soup.find(class_="instances")
txt = soup3.get_text()
txt1 = txt.rstrip()

print (' '.join(txt1.split()))

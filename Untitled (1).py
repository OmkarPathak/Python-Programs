#!/usr/bin/env python
# coding: utf-8

# # File Handling using Python

# In[1]:


# open(filename, mode)

# r - reading
# w - writing
# a - appending


# In[7]:


file = open('social.txt', 'r')
data = file.read()

# if for

file.close()

print(file.closed)  


# In[11]:


# context manager

with open('social.txt', 'r') as file:
    data = file.read()
    
print(file.closed)


# In[15]:


with open('something.txt', 'a') as file:
    file.write('MMCOE - yethe bahutanche hith!')


# In[18]:


with open('social.txt', 'r') as fd:
    data = fd.read(6)   # how many bytes or characters you have to read
    
print(data)


# In[21]:


import os

print(os.getcwd())


# In[22]:


print('Original Directory:', os.getcwd())
os.chdir('/home/omkarpathak/Documents/Notebooks')
print('Current Directory:', os.getcwd())


# In[24]:


print(os.listdir())


# In[30]:


files = []

files = os.listdir()

# os.path.isfile(filename) # return True is it is a file, else it returns False

for file in files: 
    if os.path.isfile(os.path.abspath(file)):
        print('File:', file)
        
for file in files: 
    if os.path.isdir(os.path.abspath(file)):
        print('Dir:', file)


# In[68]:


os.chdir('/home/omkarpathak/Documents/PythonLecture/Naruto/Directory0')

for i in range(10):
    os.mkdir('Directory' + str(i) + str(i))   # creating a folder
    os.chdir('Directory' + str(i) + str(i))   # Directory0 -> Directory1
    with open('something.txt', 'w') as file:
        file.write('Text')
    os.chdir('/home/omkarpathak/Documents/PythonLecture/Naruto/Directory0')


# In[47]:


os.chdir('/home/omkarpathak/Documents/PythonLecture/')


# In[44]:


mylist = ['omkar', 1, 3, 4.0]
print(mylist)


# In[53]:


word_to_check = 'hilarious'

with open('social.txt', 'r') as file:
    data = file.read()
    
for line in data.split('\n'):
    if word_to_check in line:
        print('True')
        print(line)
        
print(len(data.split('\n')))


# In[72]:


os.chdir('/home/omkarpathak/Documents/PythonLecture')
with open('social.txt', 'r') as file:
    data = file.read()
    
char = 'M'
# print(data.lower())
print(data.lower().count(char.lower()))


# In[60]:


with open('social.txt', 'r') as file:
    data = file.read()
    
char = input('Enter a character of your choice:')

print(data.lower().count(char))


# In[76]:


string = 'My namename is Omkar'
print(string.count('name'))   # fuzzy search 


# In[ ]:


import numpy
import scipy
import matplotlib


#Author: OMKAR PATHAK
#This program gives examples about various list operations

#Syntax: list[start: end: step]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#index    0  1  2  3  4  5  6  7  8
#        -9 -8 -7 -6 -5 -4 -3 -2 -1

#List Slicing
print('Original List:',myList)
print('First Element:',myList[0]) #Prints the first element of the list or 0th element of the list
print('Element at 2nd Index position:',myList[2]) #Prints the 2nd element of the list
print('Elements from 0th Index to 4th Index:',myList[0: 5]) #Prints elements of the list from 0th index to 4th index. IT DOESN'T INCLUDE THE LAST INDEX
print('Element at -7th Index:',myList[-7]) #Prints the -7th or 3rd element of the list

#To append an element to a list
myList.append(10)
print('Append:',myList)

#To find the index of a particular element
print('Index of element \'6\':',myList.index(6)) #returns index of element '6'

#To sort the list
myList.sort()

#To pop last element
print('Poped Element:',myList.pop())

#To remove a particular element from the lsit BY NAME
myList.remove(6)
print('After removing \'6\':',myList)

#To insert an element at a specified Index
myList.insert(5, 6)
print('Inserting \'6\' at 5th index:',myList)

#To count number of occurences of a element in the list
print('No of Occurences of \'1\':',myList.count(1))

#To extend a list that is insert multiple elemets at once at the end of the list
myList.extend([11,0])
print('Extending list:',myList)

#To reverse a list
myList.reverse()
print('Reversed list:',myList)

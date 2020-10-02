# Author: OMKAR PATHAK

# Python program to reverse the words

userInput = input("Enter the words or numbers that needs to be reversed:")
#the above function displays the string "Enter the words that needs to be reversed:" and takes an input of words or numbers with a space between them.

userInput = userInput.split()
#.split() is an inbuild function that splits the given words or numbers.

print(' '.join(userInput[::-1]))
# the above line take the user defined function namely userInput prints the last letter or number group.
# the join function in the 11th line is used to join the reversed word or numbers with suceeding word with a space.

# OUTPUT:
# input-Computer Science
# output-Science Computer
#example input 2
#input-1234 2345
#output-2345 1234

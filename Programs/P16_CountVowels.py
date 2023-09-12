#Author: OMKAR PATHAK
#This program counts the vowels present in the user input

def countVowels(sentence):
    '''This function counts the vowels'''
    return sum(1 for i in sentence if i in ('a', 'e', 'i', 'o', 'u'))


if __name__ == '__main__':
    userInput = str(input("Enter the string to check for vowels: "))
    count = countVowels(userInput)
    print('Vowel Count: ',count)

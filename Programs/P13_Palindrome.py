#Author: OMKAR PATHAK
#This program checks for the palindrome

def palindrome(string):
    '''This function checks the string for palindrome'''
    revString = string[::-1]
    if string == revString:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

if __name__ == '__main__':
    userInput = str(input('Enter a string to check for Palindrome: '))
    palindrome(userInput)

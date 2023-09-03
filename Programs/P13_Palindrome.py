#Author: OMKAR PATHAK
#This program checks for the palindrome

def palindrome(string):
    '''This function checks the string for palindrome'''
    print(f"{string} is {'' if string == string[::-1] else 'not '}palindrome.")

if __name__ == '__main__':
    userInput = input('Enter a string to check for Palindrome: ')
    palindrome(userInput)

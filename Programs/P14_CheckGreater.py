#Author: OMKAR PATHAK
#This prpgram checks that the given number is greater than all those numbers in th list

def checkGreater(number):
    '''This function checks whether the entered number is greater than those in the list'''

    original = [1, 2, 3, 4, 5]
    print("{}, the entered number is {} than those in the list".format(*('yes', 'greater') if number > max(original) else ('no', 'less')))

if __name__ == '__main__':
    userInput = int(input('Enter the number to check: '))
    checkGreater(userInput)

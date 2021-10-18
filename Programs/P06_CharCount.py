#Author: OMKAR PATHAK
#This program checks for the character frequency in the given string

def charFrequency(userInput):
    '''This fuction helps to count the char frequency in the given string '''
    userInput = userInput.lower() #covert to lowercase
    count=0
    while userInput !='':
        count=userInput.count(userInput[0])
        print(userInput[0],": ",count )
        userInput=userInput.replace(userInput[0],'')

if __name__ == '__main__':
    userInput = str(input('Enter a string: '))
    print(charFrequency(userInput))

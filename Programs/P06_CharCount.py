#Author: OMKAR PATHAK
#This program checks for the character frequency in the given string

def CharacterFrequency(userInput):
    '''This fuction helps the user to count the character frequency in the given string '''
    userInput = userInput.lower() #Converts the string given by user into lowercase letters.
    dict = {}
    #defining an empty dictionary named dict.
    for char in userInput:
        keys = dict.keys()
        #stores the key value of the dictionary in keys variable
        if char in keys:
            dict[char] += 1
        #checks if the character is there in keys variable. if its available then increments the value by 1, else return value 1.
        else:
            dict[char] = 1
    return dict

if __name__ == '__main__':
    userInput = str(input('Enter a string: '))
    print(CharacterFrequency(userInput))

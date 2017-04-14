#Author: OMKAR PATHAK
#This program counts the vowels present in the user input

def countVowels(sentence):
    '''This function counts the vowels'''
    count = 0
    sentence = sentence.lower()
    for c in sentence:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


if __name__ == '__main__':
    userInput = str(input("Enter the string to check for vowels: "))
    count = countVowels(userInput)
    print('Vowel Count: ',count)

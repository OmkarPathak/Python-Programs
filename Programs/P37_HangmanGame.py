# Author: Omkar Pathak
# This is just an example of how we can use Python for some gaming problems.

import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        print('_', end = ' ')
    print()

    playing = True

    letterGuessed = ''

    try:
        while playing == True:
            print()
            guess = str(input('Enter a letter to guess: '))

            # If letter is guessed correcly
            if guess in word:
                letterGuessed += guess

            # Print the word
            for char in word:
                if char in letterGuessed:
                    print(char, end = ' ')
                else:
                    print('_', end = ' ')

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

        # print(letterGuessed)

# Author: Omkar Pathak
# This is just an example of how we can use Python for some gaming problems.

import random
from collections import Counter

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
    chances = len(word) + 2
    correct = 0

    try:
        while (chances != 0):
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue


            # If letter is guessed correcly
            if guess in word:
                letterGuessed += guess

            # Print the word
            for char in word:
                if char in letterGuessed:
                    print(char, end = ' ')
                    correct += 1
                else:
                    print('_', end = ' ')

            # If user has guessed all the letters
            if (Counter(letterGuessed) == Counter(word)):
                print()
                print('Congratulations, You won!')
                break

        # If user has used all of his chances
        if chances == 0:
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()

        # print(letterGuessed)

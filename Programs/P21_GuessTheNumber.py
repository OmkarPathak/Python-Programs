#Author: OMKAR PATHAK
#This program guesses the randomnly generated number


import random
import time
def guess():
    ''' This function guesses the randomnly generated number '''
    randomNumber = random.randint(0, 101)
    count = 0
    starttime = time.time()
    print('Game Starts now!')

    while True:
        count += 1
        number = int(input('Enter the number between 0 to 100: '))
        if number < randomNumber:
            print('Too small')
        elif number > randomNumber:
            print('Too large')
        else:
            endtime = time.time()
            print('Game over!')
            print('You have got it in', count, 'tries')
            print('Total Time:', round(endtime - starttime, 2),'secs')
            break

if __name__ == '__main__':
    guess()

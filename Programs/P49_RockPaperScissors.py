# Author: OMKAR PATHAK
# This program illustrates a game of Rock Paper Scissors.
# RULES:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random, time

def rockPaperScissors():
    # R => Rock, P => Paper, S => Scissors
    computerOptions = ['R', 'P', 'S']
    computer = computerOptions[random.randint(0, 2)]

    forOptions = {'R': 'Rock', 'P': 'Paper', 'S':'Scissors'}

    try:
        player = input('Enter your choice [R]ock [P]aper [S]cissors: ')
        player = player.upper()
        if player in computerOptions:
            if player == computer:
                print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                print('You both tied!')
            elif player == 'R':
                if computer == 'P':
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Sorry, you lose! Try again.')
                else:
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Congrats, you win!')
            elif player == 'S':
                if computer == 'R':
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Sorry, you lose! Try again.')
                else:
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Congrats, you win!')
            elif player == 'P':
                if computer == 'S':
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Sorry, you lose! Try again.')
                else:
                    print('Player:',forOptions.get(player),'Computer:',forOptions.get(computer))
                    print('Congrats, you win!')
            else:
                print('Please enter only R, P or S as your choice')
    except:
        exit()

if __name__ == '__main__':
    rockPaperScissors()

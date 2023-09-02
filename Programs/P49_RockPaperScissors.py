# Author: OMKAR PATHAK
# This program illustrates a game of Rock Paper Scissors.
# RULES:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

def rockPaperScissors() -> None:
    # R => Rock, P => Paper, S => Scissors
    COMPUTEROPTIONS = ('R', 'P', 'S')
    COMPUTER = random.choice(COMPUTEROPTIONS)

    OPTIONS = {'R': 'Rock', 'P': 'Paper', 'S':'Scissors'}

    player = input('Enter your choice [R]ock [P]aper [S]cissors: ').upper()

    if player not in COMPUTEROPTIONS:
        print('Please enter only R, P or S as your choice')
        return

    STATEMENT = ('You Won!', 'You Lost!', 'You both tied!')
    
    result = {
        'R': STATEMENT[0 if COMPUTER == 'S' else 1],
        'S': STATEMENT[0 if COMPUTER == 'P' else 1],
        'P': STATEMENT[0 if COMPUTER == 'R' else 1],
    }

    print('Player:',OPTIONS.get(player),'COMPUTER:',OPTIONS.get(COMPUTER))
    print(STATEMENT[2] if player == COMPUTER else result.get(player))

if __name__ == '__main__':
    rockPaperScissors()

#Author: OMKAR PATHAK
#This program gives a demo of how can you pass arguments while running python programs
#Run the program as: python P15_Arguments.py Omkar Pathak

import sys

def arguments():
    '''This function prints the argruments passed while running the python program'''
    try:
        print('This is the name of the script:', sys.argv[0])
        print('First argument:', sys.argv[1])
        print('Second argument:', sys.argv[2])
    except IndexError:
        print('Give only two arguments')

if __name__ == '__main__':
    arguments()

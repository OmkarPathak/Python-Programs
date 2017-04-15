#Author: OMKAR PATHAK
#In this example w will see the example for Python argument parser

import argparse

def argumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--slowbros', help = 'Names of Slowbros', action = 'store_true')
    arg = parser.parse_args()
    if(arg.slowbros):
        slowBros()
    else:
        print('Dude give some arguments! Type ArgumentParser -h for more details')


def slowBros():
    print('SLOWBROS MEMBERS: \nOmkar Pathak\nChinmaya Kaundanya\nAkash Nalawade\nSanket Parode')


if __name__ == '__main__':
    argumentParser()

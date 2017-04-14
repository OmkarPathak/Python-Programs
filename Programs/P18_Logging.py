#Author: OMKAR PATHAK
#This program illustrates a logging example
import logging

def log(number):
    ''' This function creates a log file if any error is reported '''
    logging.basicConfig(filename = 'P18-logfile.txt', level = logging.INFO)
    try:
        if int(number) % 2 == 0:
            print('Successful')
        else:
            print('Unsuccessful, this instance will be reported, check the log file')
            logging.info('Invalid Entry')
    except:
        print('Please enter a valid integer')

if __name__ == '__main__':
    try:
        userInput = int(input('Enter a number: '))
        log(userInput)
    except:
        print('Please enter a valid integer')

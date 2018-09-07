#!/usr/bin/python3.6
import sys, os, datetime

def create_file(file_name):
    '''
        Create a flat file based on underlying Operating System
    '''
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('touch ' + file_name)
    elif sys.platform == 'win32':
        os.system('echo . > ' + file_name)

def write_data_in_file(file_name):
    '''
        Write the metadata into the file
    '''
    if sys.argv[3]:
        if len(sys.argv[3]) <= 15:
            length = 15
        else:
            length = len(sys.argv[3])
    else:
        length = 15
    with open(file_name, 'w') as fd:
        fd.write('#' * (length + 16))
        fd.write('\n# Author: ' + sys.argv[2])
        fd.write('\n# Description: ' + sys.argv[3])
        fd.write('\n# Created at: ' + datetime.datetime.today().strftime('%d %b %Y') + '\n')
        fd.write('#' * (length + 16))

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print('You need to provide three arguments [File Name] [Author Name] [Description]')
        exit()
    create_file(sys.argv[1])
    write_data_in_file(sys.argv[1])
# Author: OMKAR PATHAK
# This script illustrates how to find if a file exists on the system with the specified name

import os

# Path IN which we have to search file
PATH = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'   # Give your path here

def searchFile(fileName):
    ''' This function searches for the specified file name in the given PATH '''
    for root, dirs, files in os.walk(PATH):
        print('Looking in:',root)
        for Files in files:
            try:
                found = Files.find(fileName)        # Returns -1 if NOT found else returns index
                # print(found)
                if found != -1:
                    print(fileName, 'Found')
                    break
            except:
                exit()

if __name__ == '__main__':
    searchFile('6-Folder.txt')

    # OUTPUT:
    # omkarpathak@omkarpathak-Inspiron-3542:~/Documents/GITs/Python-Programs/Scripts$ python P04_FindIfAFileExists.py
    # Looking in: /home/omkarpathak/Documents/GITs/Python-Programs/Scripts
    # Looking in: /home/omkarpathak/Documents/GITs/Python-Programs/Scripts/Tests
    # 6-Folder.txt Found

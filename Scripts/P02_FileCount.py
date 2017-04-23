# Author: OMKAR PATHAK
# This script illustrates how to count number of files and directories in a diectory recursively

import os

# Path IN which we have to count files and directories
PATH = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts'   # Give your path here

fileCount = 0
dirCount = 0

for root, dirs, files in os.walk(PATH):
    print('Looking in:',root)
    for directories in dirs:
        dirCount += 1
    for Files in files:
        fileCount += 1

print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total:',(dirCount + fileCount))

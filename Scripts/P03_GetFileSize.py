# Author        : Craig Richards
# Description   : This will scan the current directory and all subdirectories and display the size.

import os       # Load the library module
directory = '/home/omkarpathak/Documents/GITs/Python-Programs/Scripts' # Set the variable directory to be the current directory
dir_size = 0    # Set the size to 0

fsizedicr = {'Bytes': 1, 'Kilobytes': float(1)/1024, 'Megabytes': float(1)/(1024*1024), 'Gigabytes': float(1)/(1024*1024
                                                                                                               *
                                                                                                               1024)}

for (path, dirs, files) in os.walk(directory):      # Walk through all the directories. For each iteration, os.walk returns the folders, subfolders and files in the dir.
    for file in files:                              # Get all the files
        filename = os.path.join(path, file)
        dir_size += os.path.getsize(filename)       # Add the size of each file in the root dir to get the total size.

for key in fsizedicr:       #iterating through the dictionary
    print ("Folder Size: " + str(round(fsizedicr[key]*dir_size, 2)) + " " + key)        # round function example: round(4.2384, 2) ==> 4.23

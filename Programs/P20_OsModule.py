#Author: OMKAR PATHAK
#This program illustrates the example for os module in short

import os
import time

print(os.getcwd()) #Prints the current working directory

os.mkdir('newDir1')
for i in range(1,10):
    os.rename('newDir' + str(i),'newDir' + str(i + 1))
    print('newDir' + str(i),' is renamed to ','newDir' + str(i + 1)) #Prints the renaming 
    time.sleep(2)
    
#Output
#C:\Users\Vishal
#newDir1  is renamed to  newDir2
#newDir2  is renamed to  newDir3
#newDir3  is renamed to  newDir4
#newDir4  is renamed to  newDir5
#newDir5  is renamed to  newDir6
#newDir6  is renamed to  newDir7
#newDir7  is renamed to  newDir8
#newDir8  is renamed to  newDir9
#newDir9  is renamed to  newDir10

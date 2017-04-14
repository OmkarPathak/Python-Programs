#Author: OMKAR PATHAK
#This program illustrates the example for os module in short

import os
import time

print(os.getcwd()) #Prints the current working directory

os.mkdir('newDir1')
for i in range(1,10):
    print('Here i is',i)
    os.rename('newDir' + str(i),'newDir' + str(i + 1))
    time.sleep(2)

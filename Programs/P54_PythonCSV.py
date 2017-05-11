# Author: OMKAR PATHAK
# In this example we will see how to use CSV files with Python

# csv.QUOTE_ALL = Instructs writer objects to quote all fields.
# csv.QUOTE_MINIMAL = Instructs writer objects to only quote those fields which contain special characters such
#                     as delimiter, quotechar or any of the characters in lineterminator.
# csv.QUOTE_NONNUMERIC = Instructs writer objects to quote all non-numeric fields.
#                        Instructs the reader to convert all non-quoted fields to type float.
# csv.QUOTE_NONE = Instructs writer objects to never quote fields.

import csv

def csvRead(filePath):
    with open(filePath) as fd:
        reader = csv.reader(fd, delimiter = ',')
        for row in reader:
            print(row[0] + ' ' + row[1])

def csvWrite(filePath, data):
    with open(filePath, 'a') as fd:
        writer = csv.writer(fd, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(data)

if __name__ == '__main__':
    # data = ['Firstname', 'Lastname']
    # csvWrite('example.csv', data)
    userInput = input('What is your Fullname? ')
    userInput = userInput.split(' ')
    csvWrite('example.csv', userInput)
    csvRead('example.csv')

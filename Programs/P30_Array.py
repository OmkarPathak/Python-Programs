#Author: OMKAR PATHAK
#This example illustrates how an array can be implemened using Python

class Array(object):
    def __init__(self, size, defaultValue = None):
        '''
            size: indicates the static size of the Array
            defaultValue indicates the default value that Array takes while creation, you can also
            pass preinitialized list to set the values of the array elements
        '''
        if(defaultValue == None):
            self.items = list()
            for i in range(size):
                self.items.append(defaultValue)
        else:
            self.items = defaultValue

    def myLen(self):
        ''' This function returns the length of the created Array '''
        length = len(self.items)
        return length

    def getItem(self, index):
        ''' This function returns the value of the index specified '''
        return self.items[index]

    def setItem(self, index, value):
        ''' This function is used to set the value at the specified index '''
        self.items[index] = value


if __name__ == '__main__':
    myArray = Array(5)
    length = myArray.myLen()
    print(length)
    myArray.setItem(2, 12)
    print(myArray.items)

    for i in range(length):
        myArray.items[i] = i

    print(myArray.items)

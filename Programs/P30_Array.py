#Author: OMKAR PATHAK
#This example illustrates how an array can be implemened using Python

class Array(object):
    def __init__(self, size, defaultValue = None):
        '''
            size: indicates the static size of the Array
            defaultValue indicates the default value that Array takes while creation, you can also
            pass preinitialized list to set the values of the array elements
        '''
        self.size = size
        # If only array size is initialized then, initialize all the elements as None type
        if(defaultValue == None):
            self.items = list()
            for i in range(size):
                self.items.append(defaultValue)
        else:
            # If user has given the default values for the array
            self.items = list()

            if(len(defaultValue) == size or len(defaultValue) < size):
                for j in range(len(defaultValue)):
                    if(defaultValue[j]):
                        self.items.append(defaultValue[j])
                for i in range(len(defaultValue), size):
                    self.items.append(None)
            else:
                print('Elements are more than the size specified')

    def myLen(self):
        ''' This function returns the length of the Array (Only initialised number of elements)'''
        length = 0
        for i in self.items:
            if i == None:
                continue
            else:
                length += 1
        return length

    def insertFirst(self, element):
        ''' This function adds the element to the beginning of the array '''
        if (self.myLen() < self.size):
            for i in range(self.myLen(), 0, -1):
                self.items[i] = self.items[i - 1]
            self.items[0] = element
        else:
            print('Element index out of range')

    def insertAtIndex(self, index, element):
        ''' This function adds the element to the beginning of the array '''
        if (self.myLen() < self.size):
            for i in range(self.myLen(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = element
        else:
            print('Element index out of range')

    def insertAfterIndex(self, index, element):
        ''' This function adds the element to the beginning of the array '''
        if (self.myLen() < self.size):
            for i in range(self.myLen(), index + 1, -1):
                self.items[i] = self.items[i - 1]
            self.items[index + 1] = element
        else:
            print('Element index out of range')

    def insertBeforeIndex(self, index, element):
        ''' This function adds the element to the beginning of the array '''
        if (self.myLen() < self.size):
            for i in range(self.myLen(), index - 1, -1):
                self.items[i] = self.items[i - 1]
            self.items[index - 1] = element
        else:
            print('Element index out of range')

    def delete(self, element):
        if element in self.items:
            Index = self.items.index(element)
            self.items[Index] = None
        else:
            print('This element is not in the Array!')

    def search(self, element):
        if element in self.items:
            position = 0
            for i in range(self.myLen()):
                if(self.items[i] == element):
                    break
                else:
                    position += 1

            print('Element {} found at position {}'.format(element, position))
        else:
            print('This element is not in the Array!')

if __name__ == '__main__':
    myArray = Array(5, [1])
    print(myArray.items, myArray.myLen())       # [1, None, None, None, None] 1
    myArray.insertFirst(3)
    print(myArray.items, myArray.myLen())       # [3, 1, None, None, None] 2
    myArray.insertAfterIndex(1,4)
    print(myArray.items, myArray.myLen())       # [3, 1, 4, None, None] 3
    myArray.insertBeforeIndex(3,5)
    print(myArray.items, myArray.myLen())       # [3, 1, 5, 4, None] 4
    myArray.delete(5)
    print(myArray.items, myArray.myLen())       # [3, 1, None, 4, None] 3
    myArray.search(4)                           # Element 4 found at position 3

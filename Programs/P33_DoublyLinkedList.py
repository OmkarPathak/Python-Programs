#Author: OMKAR PATHAK
#This program illustrates an example of singly linked list

class Node(object):
    def __init__(self, data, Next = None, Previous = None):
        self.data = data
        self.next = Next
        self.previous = Previous

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        ''' This function checks whether the list is empty'''
        return self.head == None

    def insert(self, data):
        ''' This function inserts a new node in the Linked List '''
        newNode = Node(data)
        if self.head:
            self.head.setPrevious(newNode)
        newNode.setNext(self.head)
        self.head = newNode

    def getAllData(self):
        ''' This function displays the data elements of the Linked List '''
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return elements

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

if __name__ == '__main__':
    myList = LinkedList()
    myList.insert(1)
    myList.insert(12)
    myList.insert(32)
    myList.insert(22)
    myList.remove(12)
    for i in range(0, 10):
        myList.insert(i)
    print(myList.getAllData())

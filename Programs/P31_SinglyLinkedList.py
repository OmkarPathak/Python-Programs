#This program illustrates an example of singly linked list
#Linked lists do NOT support random access hence only sequential search can be carried out

class Node(object):
    def __init__(self, data, Next = None):
        self.data = data
        self.next = Next

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

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

    def getAllData(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.getData())
            current = current.getNext()

        return elements

if __name__ == '__main__':
    myList = LinkedList()

    print(myList.head)                  # None

    myList.add(12)
    myList.add(2)
    myList.add(22)
    myList.add(32)
    myList.add(42)

    print(myList.size())                # 5

    print(myList.search(93))            # False
    print(myList.search(12))            # True
    print(myList.getAllData())
    myList.remove(12)
    print(myList.getAllData())

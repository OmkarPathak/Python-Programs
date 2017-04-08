#This program illustrates an example of singly linked list
#Linked lists do NOT support random access hence only sequential search can be carried out

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found != False:
            if current.get_data() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class Node(object):
    ''' Class for creating a singly linked list '''
    def __init__(self, data, next = None):
        ''' This constructor initilizes the node with the data and the next item in the list'''
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, newNext):
        self.next = newNext

    def replace(self, targetItem, newItem):
        probe = self
        while probe != None and targetItem != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = newItem
            print('Target Updated')
            return True
        else:
            print('Target not found in the linked list')
            return False

if __name__ == '__main__':
    #node1 = Node("A", "B")
    #node2 = Node("B", "C")
    #node3 = Node("C")
    #print(node1.data,'=>', node1.next)
    #print(node2.data,'=>', node2.next)
    #print(node3.data,'=>', node3.next)

    #node = None
    #for i in range(6, 1, -1):
    #    node = Node(i, node)

    #print(node.data)
    #node.search(4)

    #node.replace(2, 5)
    #print(node.data)

    node = LinkedList(1)
    print(node.head)
    node.insert(2)
    print(node.head)
    print(node.size())

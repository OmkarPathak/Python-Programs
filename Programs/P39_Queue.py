# Author: OMKAR PATHAK

# This program illustrates an example of Queue implementation in Python
# Stack Operations: enqueue(), dequeue(), isFull(), isEmpty, peek()

class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.queue)
        return myString

    def enqueue(self, item):
        '''This function adds an item to the rear end of the queue '''
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        ''' This function removes an item from the front end of the queue '''
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        ''' This function checks if the queue is empty '''
        return self.queue == []

    def isFull(self):
        ''' This function checks if the queue is full '''
        return len(self.queue) == self.size

    def peek(self):
        ''' This function helps to see the first element at the fron end of the queue '''
        if(self.isEmpty() != True):
            return self.queue[-1]
        else:
            print('Queue is Empty!')

if __name__ == '__main__':
    myQueue = Queue(10)
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print(myQueue)
    myQueue.dequeue()
    print(myQueue)

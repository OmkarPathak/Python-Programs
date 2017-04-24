#Author: OMKAR PATHAK

#This program illustrates an example of Stack implementation
#Stack Operations: push(), pop(), isEmpty(), peek(), stackSize()

class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def __str__(self):
        myString = ' '.join(str(i) for i in self.index)
        return myString

    def push(self, data):
        ''' Pushes a element to top of the stack '''
        self.index.append(data)

    def pop(self):
        ''' Pops the top element '''
        return self.index.pop()

    def isEmpty(self):
        ''' Checks whether the stack is empty '''
        return len(self.index) == []

    def isFull(self):
        ''' Checks whether the stack if full '''
        return len(self.index) == self.size

    def peek(self):
        ''' Returns the top element of the stack '''
        return self.index[-1]

    def stackSize(self):
        ''' Returns the current stack size '''
        return len(self.index)

if __name__ == '__main__':
    myStack = Stack(10)
    for i in range(0, 10):
        myStack.push(i)
    print(myStack.isEmpty())        # False
    print(myStack.isFull())         # True
    print(myStack)                  # 0 1 2 3 4 5 6 7 8 9
    print(myStack.stackSize())      # 10
    print(myStack.pop())            # 9
    print(myStack)                  # 0 1 2 3 4 5 6 7 8
    print(myStack.peek())           # 8

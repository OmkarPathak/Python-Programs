# Author: OMKAR PATHAK
# This example illustrates an example for multiprocessing and synchronization using pipes

from multiprocessing import Process, Pipe

def parentData(parent):
    ''' This function sends the data for the child process '''
    parent.send(['Hello'])
    parent.close()

def childData(child):
    ''' This function sends the data for the parent process '''
    child.send(['Bye'])
    child.close()

if __name__ == '__main__':
    parent, child = Pipe()              # Create Pipe
    process1 = Process(target = parentData, args = (parent, ))      # Create a process for handling parent data
    process2 = Process(target = childData, args = (child, ))        # Create a process for handling child data
    process1.start()                    # Start the  parent process
    process2.start()                    # Start the child process
    print(parent.recv())                # Display data received from child (BYE)
    print(child.recv())                 # Display data received from parent (HELLO)
    process1.join()                     # Wait till the process completes its execution
    process2.join()

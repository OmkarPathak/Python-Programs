#Author: OMKAR PATHAK
#This program is an example for sequential search

def sequentialSearch(target, List):
    '''This function returns the position of the target if found else returns -1'''
    position = 0
    global iterations
    iterations = 0
    while position < len(List):
        iterations += 1
        if target == List[position]:
            return position
        position += 1
    return -1

if __name__ == '__main__':
    List = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 3
    ans = sequentialSearch(target, List)
    if ans != -1:
        print('Target found at position:',ans,'in',iterations,'iterations')
    else:
        print('Target not found in the list')

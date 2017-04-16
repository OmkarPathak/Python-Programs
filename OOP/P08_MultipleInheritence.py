#Author: OMKAR PATHAK
#This program shows the order in which the classes are accessed in case of multiple inheritance
#Python uses DEPTH FIRST SEARCH algorithm for lookups

class A(object):
    def doThis(self):
        print('Doing this in A')

class B(A):
    pass

#If class C was also eing derived from A then the lookup order would be D,B,C,A
class C(object):
    def doThis(self):
        print('Doing this in C')

class D(B, A):
    pass

if __name__ == '__main__':
    dObj = D()
    dObj.doThis() #A method gets called because order for lookup is D,B,A,C this is shown by function mro

    print(D.mro())

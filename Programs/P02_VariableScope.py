#Author: OMKAR PATHAK
#This programs shows the rules for variable scope

# LEGB Rule: Local, Enclosing, Global, Built-in

x = 'Global x'

def test():
    #global x
    y = 'Local y'
    x = 'Local x'
    print(x +', '+ y) #prints 'Local x' and  'Local y'

if __name__ == '__main__':
    test()
    print(x) #prints 'Global x'

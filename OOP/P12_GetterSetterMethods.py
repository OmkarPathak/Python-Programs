'''
Author: AMIT PATHAK 

In this example, we will the getter and setter methods in python class.
Private variables of a class cannot be accessed outside the class using the class object.
In order to access or manipulate these variables, we make use of getter and setter methods respectively.
'''

class CreditCard(object):

    def __init__(self, number, new_pin):
        self.card_number = number
        self.__pin       = new_pin     # Private Variable

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        self.__pin = new_pin


if __name__ == '__main__':

    cc = CreditCard(number=514235895214, new_pin=1234)

    print(cc.card_number)
    ### Output: 514235895214

    #print(cc.__pin)
    ### Output: AttributeError: 'CreditCard' object has no attribute '__pin'

    print(cc.get_pin())
    ### Output: 1234

    cc.set_pin(new_pin=8745)   # Set a new pin to 8745
    print(cc.get_pin())
    ### Output: 8745

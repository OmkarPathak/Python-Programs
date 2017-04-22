# Author: OMKAR PATHAK
# This program illustrates all the OOP concepts learned uptil now

class BankAccount(object):
    defaultAccNumber = 1        # Class Attribute

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    myObj = BankAccount('Omkar', 1000)
    myObj.deposit(1000)
    print(myObj.getBalance())
    myObj.withdraw(500)
    print(myObj.getBalance())

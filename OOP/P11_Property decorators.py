#This shows the usage of property decorators

#Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a way so that the users neeed not make any additional changes in their code.

#Without property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.total= self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

# Output: Tim cook
#         Elon Musk has 10000 dollars in the account


#With property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    @property
    def total(self):
        return self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

#Output: Tim cook
#        Tim cook has 10000 dollars in the account

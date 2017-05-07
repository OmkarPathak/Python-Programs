#Author: OMKAR PATHAK
#This program illustrates the concept of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and the
#from the base class

class Data(object):
    def getData(self):
        print('In data!')

class Time(Data):           #Inheriting from Data class
    def getTime(self):
        print('In Time!')

if __name__ == '__main__':
    data = Data()
    time = Time()

    data.getData()
    time.getTime()
    time.getData()          #Inherited Data method

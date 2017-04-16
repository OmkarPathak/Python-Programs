#Author: OMKAR PATHAK
#This program illustrates the advanced concepts of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and the
#from the base class
#mro: Method Resolution order

class Data(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print('Data:',self.data)

class Time(Data):           #Inhertiting from Data class
    def getTime(self):
        print('Time:',self.data)

if __name__ == '__main__':
    data = Data(10)
    time = Time(20)     #inherited Class -> Value passed to __init__of Data (Base class)

    time.getTime()
    data.getData()
    time.getData()

    print(Time.mro())

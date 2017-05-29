#!/usr/bin/env python

# Author: OMKAR PATHAK

# This is a small fun project which I have developed to get through all the concepts learned so far.

# For installing on Ubuntu:
# sudo apt install python3-tk 

from tkinter import *
from tkinter.messagebox import showerror
import pickle

class todoGUI(object):
    def __init__(self):
        self.mainWindow = Tk()
        self.mainWindow.title('TODO Application!')
        self.fieldnames = ('key', 'name', 'age', 'pay')

    def buildWidgets(self):
        global entries
        entries = {}
        self.mainFrame = Frame(self.mainWindow)
        self.mainFrame.pack()
        for(idx, label) in enumerate(self.fieldnames):
            labels = Label(self.mainFrame, text = label)
            ent = Entry(self.mainFrame, font=('Arial', 17))
            # ent.pack()
            labels.grid(row = idx, column = 0)
            ent.grid(row = idx, column = 1)
            entries[label] = ent
        Button(self.mainWindow, text="Fetch", command = self.fetchRecord).pack(side=LEFT)
        Button(self.mainWindow, text="Update", command = self.updateRecord).pack(side=LEFT)
        Button(self.mainWindow, text="Quit", command = self.mainWindow.quit).pack(side=RIGHT)

        return entries

    def fetchRecord(self):
        dbfile = open('examplePickle', 'rb')
        db = pickle.load(dbfile)
        try:
            key = entries['key'].get()
            record = db[key]
            # fetch by key, show in GUI
        except:
            showerror(title='Error', message='No such key!')
        else:
            for field in self.fieldnames:
                entries[field].delete(0, END)
                entries[field].insert(0, record[field])

        dbfile.close()
        return record

    def updateRecord(self):
        dbfile = open('examplePickle', 'rb')
        db = pickle.load(dbfile)
        dbfile.close()
        key = entries['key'].get()
        if key in db:
            record = db[key]
            # update existing record
        else:
            # make/store new one for key
            # db['name'] = entries['name'].get()
            # db[str(key)] = key
            dbfile = open('examplePickle', 'ab')
            temp = {}
            # temp['key'] = str(key)
            # for field in self.fieldnames[1:]:
            #     temp[field] = str(entries[field].get())
            #
            # print(temp)
            # db[str(key)] = temp
            # print(db)
            del db[key]
            for field in self.fieldnames:
                temp[field] = entries[field].get()

            pickle.dump(temp, dbfile)
            dbfile.close()

    def startGUI(self):
        self.mainWindow.mainloop()

if __name__ == '__main__':

    window = todoGUI()
    entries = window.buildWidgets()
    window.startGUI()

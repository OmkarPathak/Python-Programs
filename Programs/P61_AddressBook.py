# Author: OMKAR PATHAK

# In this small mini project we will be creating a simple address book application that will store, search and
# delete records

# TODO: seach,  modify function

import pickle, os

class AddressBook(object):
    # myFile = open('addressbook', 'wb')
    # pickle.dump(source, destination)
    # pickle.load(source)
    def __init__(self, name = None, address = None, email = None, phone = None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.contacts = {}
        self.filename = 'addressbook'

    def __str__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3}]'.format(self.name, self.address, self.email, self.phone)

    def __repr__(self):
        return '[Name: {0} | Address: {1} | Email: {2} | Phone: {3}]'.format(self.name, self.address, self.email, self.phone)

    # Adding details provided by the user in our Address Book
    def addContacts(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                myAddressBook = open(self.filename, 'rb')
                data = pickle.load(myAddressBook)
                myAddressBook.close()
            else:
                myAddressBook = open(self.filename, 'wb')
                data = {}

            contact = self.getDetailsFromUser()
            data[contact['Name']] = contact
            myAddressBook = open(self.filename, 'wb')
            pickle.dump(data, myAddressBook)
            myAddressBook.close()

        except EOFError as e:
            # print(e)
            print('There was an error! Contact was not added.')
        finally:
            myAddressBook.close()

    # Getting the details from the user to adding the Address Book
    def getDetailsFromUser(self):
        try:
            self.contacts['Name'] = str(input('Enter Contact\'s Full Name: '))
            self.contacts['Address'] = str(input('Enter Contact\'s Address: '))
            self.contacts['Email'] = str(input('Enter Contact\'s Email Address: '))
            self.contacts['Phone'] = int(input('Enter Contact\'s Phone Number: '))
            return self.contacts
        except KeyboardInterrupt as error:
            raise error

    # To display ALL the contact in our Address Book
    def displayContacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'rb')
            data = pickle.load(myAddressBook)
            myAddressBook.close()
            if data:
                for records in data.values():
                    print(records)
            myAddressBook.close()
        else:
            print('No Record in database.')

    # To serach for a specific contact in our Address Book
    def searchContacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'rb')
            data = pickle.load(myAddressBook)
            myAddressBook.close()
            try:
                contactToSearch = input('Enter the name of the contact to search: ')
                counter = 0
                for contact in data.values():
                    if contactToSearch in contact['Name']:
                        print(data[contact['Name']])
                        counter += 1
                if counter == 0:
                    print('No record found whose name is:', contactToSearch)
            except EOFError as e:
                print('Error occured!')
        else:
            print('No Record in database.')

    def modifyContacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            myAddressBook = open(self.filename, 'rb')
            data = pickle.load(myAddressBook)
            myAddressBook.close()
            try:
                contactToModify = input('Enter the name of the contact to modify (Only enter full name): ')
                # Search for the record to update
                for contact in data.values():
                    if contactToModify == contact['Name']:
                        contact = data[contactToModify]
                        break
                option = int(input('1. To modify name, 2. To modify address, 3. To modify email, 4. To modify email: '))
                if option == 1:
                    contact['Name'] = input('Enter Name to modify: ')
                    del data[contactToModify]
                    data[contact['Name']] = contact
                else:
                    print('Incorrect option selected.')
            except EOFError as e:
                print(e)
            finally:
                myAddressBook = open(self.filename, 'wb')
                pickle.dump(data, myAddressBook)
                myAddressBook.close()
        else:
            print('No Record in database.')

if __name__ == '__main__':
    myBook = AddressBook()
    # myBook.addContacts()
    myBook.displayContacts()
    myBook.searchContacts()
    # myBook.modifyContacts()

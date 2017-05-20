# Author: OMKAR PATHAK

# In this small mini project we will be creating a simple address book application that will store, search and
# delete records

import pickle, os

class AddressBook(object):
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
            print('Contact Added Successfully!')
        except:
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

    # To search for a specific contact in our Address Book
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
            except:
                print('Error occured!')
        else:
            print('No Record in database.')

    # For modifying contacts
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
                option = int(input('1. To modify name, 2. To modify address, 3. To modify email, 4. To modify phone: '))
                if option == 1:
                    contact['Name'] = input('Enter Name to modify: ')
                    del data[contactToModify]
                    data[contact['Name']] = contact
                    print('Successful')
                elif option == 2:
                     contact['Address'] = input('Enter Address to modify: ')
                     del data[contactToModify]
                     data[contactToModify] = contact
                     print('Successful')
                elif option == 3:
                    contact['Email'] = input('Enter Email to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                elif option == 4:
                    contact['Phone'] = input('Enter Phone to modify: ')
                    del data[contactToModify]
                    data[contactToModify] = contact
                    print('Successful')
                else:
                    print('Incorrect option selected.')
            except:
                print('Error occured. No such record found. Try Again!')
            finally:
                myAddressBook = open(self.filename, 'wb')
                pickle.dump(data, myAddressBook)
                myAddressBook.close()
        else:
            print('No Record in database.')

if __name__ == '__main__':
    myBook = AddressBook()
    print('Enter 1. To Add Contacts 2. For Searching a Contact 3. For Modifying a Contact 4. To Display Contacts 5. To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            myBook.addContacts()
        elif choice == 2:
            myBook.searchContacts()
        elif choice == 3:
            myBook.modifyContacts()
        elif choice == 4:
            myBook.displayContacts()
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')

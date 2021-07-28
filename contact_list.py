import os

# create a contact class
class Contact(object):
    '''
    create a contact entry
    '''

    def __init__(self, firstname:str, surname:str, mobile:str, email:str):
        self.firstname = firstname
        self.surname = surname
        self.mobile = mobile
        self.email = email

    def __str__(self) -> str:
        return self.firstname + self.surname + self.mobile + self.email

    def name(self,newFirstname):
        self.firstname = newFirstname

    def lastName(self,newSurname):
        self.surname = newSurname
    
    def mobilephone(self,newMobile):
        self.mobile = newMobile
    
    def emailaddress(self,newEmail):
        self.email = newEmail

entries = []

# create a file to save contacts to
def contactFile():
    '''
    to load the contacts list file
    '''
    try:
        with open('contactListFile.txt','r') as clf:
            for line in clf:
                entry = line.split()
                entries.append(Contact(entry[0], entry[1], entry[2], entry[3]))
    except FileNotFoundError:
        print('Contact file not found.')

# create a new entry
def addcontact():
    '''
    add a contact to the file
    '''
    print('Enter the following details: ')
    newFirstname = input("Firstname: ")
    newSurname = input("Surname: ")
    newMobile = input("Mobile: ")
    newEmail = input("Email: ")
    entries.append(Contact(newFirstname,newSurname,newMobile,newEmail))
    saveChanges()
    print('Contact added successfully.')
    menu()
    

def saveChanges():
    '''
    to save any file changes that have been made
    '''
    with open("contactListFile.txt", "w") as clf:
        for e in entries:
            clf.write(e.firstname + " " + e.surname + " " + e.mobile + " " + e.email + "\n")
            

# view all contacts in the list
def showContacts():
    '''
    to see all contacts in the list
    '''
    for e in entries:
        print(e.firstname + ";" + e.surname + ";" + e.mobile + ";" + e.email)
    print("--- end of list --- \n")
    menu()

# search a contact entry
def searchContacts():
    '''
    to search for a contact in the list
    '''
    with open('contactListFile.txt','r') as clf:
        search = input("Enter your search term: ")
        for e in entries:
            if search == e.firstname or search == e.surname or search == e.mobile or search == e.email:
                print('Contact entry found.')
                print(e.firstname + " - " + e.surname + " - " + e.mobile + " - " + e.email)
                menu()

# update a contact entry
def updateContact():
    '''
    to update a contact entry
    '''
    to_update = input("Which contact field would you like to update? \nFirstname, Surname, Mobile or Email? \n")
    if to_update.lower() == "firstname":
        contact_to_update = input("Which contact do you want to update? \n")
        for e in entries:
            if contact_to_update == e.firstname:
                newFirstname1 = input("Enter the new name: ")
                e.name(newFirstname1)
                saveChanges()
                print("Contact name has been updated.")  
                menu()

    if to_update.lower() == "surname":
        contact_to_update = input("Which contact do you want to update? \n")
        for e in entries:
            if contact_to_update == e.firstname:
                newSurname1 = input("Enter the new surname: ")
                e.lastName(newSurname1)
                saveChanges()
                print("Contact surname has been updated.")  
                menu()            
    if to_update.lower() == "mobile":
        contact_to_update = input("Which contact do you want to update? \n")
        for e in entries:
            if contact_to_update == e.firstname:
                newMobile1 = input("Enter the new number")
                e.mobilephone(newMobile1)
                saveChanges()
                print("Contact mobile has been updated.")  
                menu()
    if to_update.lower() == "email":
        contact_to_update = input("Which contact do you want to update? \n")
        for e in entries:
            if contact_to_update == e.firstname:
                newEmail1 = input("Enter the new email address: ")
                e.emailaddress(newEmail1)
                saveChanges()
                print("Contact email address has been updated.")
                menu() 
    else:
        print("Please enter a valid option to update: 'firstname', 'surname', 'mobile', 'email'\n")
        updateContact()

# delete a contact entry
def removeContact():
    '''
    to remove a contact from the list
    '''
    remove_who = input("Which contact would you like to remove? \n")
    with open('contactListFile.txt','r') as clf:
        for e in entries:
            if remove_who == e.firstname or remove_who == e.surname or remove_who == e.mobile or remove_who == e.email:
                print("Contact found: ")
                print(e.firstname + " - " + e.surname + " - " + e.mobile + " - " + e.email)
                confirm = input("proceed to remove? 'Y' or 'N' \n")
                if confirm.lower() == 'y':
                    entries.remove(e)
                    print("Contact entry has been removed.")
                    saveChanges()
                    showContacts()
                elif confirm.lower() == 'n':
                    menu()
                else:
                    print("Removal request could not be confirmed.")
                    menu()
                    


# menu for using the contacts list
def menu():
    print("What would you like to do? \n")
    action = input("a = add contact, l = show list of all contacts, s = seach contacts, u = update contact, d = delete a contact or x = quit this program. \nSelection: ")
    if action.lower() == 'a':
        addcontact()
    if action.lower() == 'l':
        showContacts()
    if action.lower() == 's':
        searchContacts()
    if action.lower() == 'u':
        updateContact()
    if action.lower() == 'd':
        removeContact()
    if action.lower() == 'x':
        print("Closing the program now. \nGood bye")
        quit()
    else:
        print('Please enter a valid menu option. \n')
        menu()

contactFile()
menu()
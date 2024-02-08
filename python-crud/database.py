import mysql.connector as mysql
import classes

contacts = []

DATABASE = mysql.connect (
    host = 'localhost',	
    user = 'root',
    password = 'adminadmin',
    database = 'my_database'
)

cursor = DATABASE.cursor()

cursor.execute('SELECT * FROM contact')
result = cursor.fetchall()
for x in result:
    contacts.append(classes.Contact(x))

def addContact(contact):
    sql = 'INSERT INTO contact (name, email, phoneNumber) VALUES ({}, {}, {})'.format(contact.name, contact.email, contact.phoneNumber)
    cursor.execute(sql)
    DATABASE.commit()
    cursor.execute(f'SELECT * FROM contact WHERE id = {classes.contact_counter}')
    contacts.append(classes.Contact(cursor.fetchone()))
    pass

def removeContact(index):
    sql = 'DELETE FROM contact WHERE id = {}'.format(contacts[index].id)
    cursor.execute(sql)
    DATABASE.commit()
    contacts.pop(index)
    pass

def updateContact(index, newContact):
    cursor.execute(f'UPDATE contact SET name = {newContact.name}, email = {newContact.email}, phoneNumber = {newContact.phoneNumber} WHERE id = {contacts[index].id}')
    DATABASE.commit()
    contacts[index].name = newContact.name
    contacts[index].email = newContact.email
    contacts[index].phoneNumber = newContact.phoneNumber
    pass

def getContact(atribute):
    for i in range(len(contacts)):
        if contacts[i].name == atribute:
            return i
        elif contacts[i].id == atribute:
            return i
        else:
            return None
    pass




#import pymysql.cursors

from fixture.db import DBFixture


db = DBFixture(host="lab", name="addressbook", user="root", password="")

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()


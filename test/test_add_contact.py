# -*- coding: utf-8 -*-
from model import Contact
# from model import ContactDate
# import pytest
# import random
# import string
# import calendar


# def random_string(prefix, maxlen):
#     sysmbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
#     return prefix + "".join([random.choice(sysmbols) for i in range(random.randrange(maxlen))])


# testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                        address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
#                        email3="", homepage="", bdate=ContactDate("-", "-", ""), adate=ContactDate("-", "-", ""),
#                        address2="", secondaryphone="", notes="")] +\
#            [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#                     lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
#                     title=random_string("name", 10), company=random_string("name", 10),
#                     address=random_string("address", 10), homephone=random_string("homephone", 10),
#                     mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
#                     fax=random_string("fax", 10), email=random_string("email", 10),
#                     email2=random_string("email2", 10), email3=random_string("email3", 10),
#                     homepage=random_string("homepage", 10),
#                     bdate=ContactDate(random.randint(1, 31), calendar.month_name[random.randint(1, 12)],
#                                       random.randint(1900, 2100)),
#                     adate=ContactDate(random.randint(1, 31), calendar.month_name[random.randint(1, 12)],
#                                       random.randint(1900, 2100)),
#                     address2=random_string("address2", 10), secondaryphone=random_string("secondaryphone", 10),
#                     notes=random_string("notes", 10))
#             for i in range(5)]


#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
#def test_add_contact(app, contact):

def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
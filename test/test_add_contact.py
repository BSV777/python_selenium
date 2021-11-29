# -*- coding: utf-8 -*-
from model import Contact
from model import ContactDate


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()

    contact = Contact(firstname="test", middlename="test", lastname="test",
                               nickname="test", title="test", company="test",
                               address="test", homephone="test", mobilephone="test",
                               workphone="test", fax="test", email="test", email2="test",
                               email3="test", homepage="test",
                               bdate=ContactDate(1, "January", 2001),
                               adate=ContactDate(2, "February", 2002),
                               address2="test", phone2="test", notes="test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


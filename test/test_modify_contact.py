from model import Contact
from model import ContactDate
from random import randrange


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="mod", middlename="mod", lastname="mod",
                                             nickname="test", title="test", company="test",
                                             address="test", homephone="test", mobilephone="test",
                                             workphone="test", fax="test", email="test", email2="test",
                                             email3="test", homepage="test",
                                             bdate=ContactDate(1, "January", 2001),
                                             adate=ContactDate(2, "February", 2002),
                                             address2="test", phone2="test", notes="test")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

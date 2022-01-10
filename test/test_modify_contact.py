from model import Contact
from model import ContactDate
import random


def test_modify_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()

    contact = random.choice(old_contacts)

    #index = randrange(len(old_contacts))

    contact.firstname = "mod"
    contact.middlename = "mod"
    contact.lastname = "mod" + str(contact.id)
    contact.nickname = "test"
    contact.title = "test"
    contact.company = "test"
    contact.address = "test"
    contact.homephone = "test"
    contact.mobilephone = "test"
    contact.workphone = "test"
    contact.fax = "test"
    contact.email = "test"
    contact.email2 = "test"
    contact.email3 = "test"
    contact.homepage = "test"
    contact.bdate = ContactDate(1, "January", 2001)
    contact.adate = ContactDate(2, "February", 2002)
    contact.address2 = "test"
    contact.secondaryphone = "test"
    contact.notes = "test"

    # contact = Contact(firstname="mod", middlename="mod", lastname="mod" + str(index),
    #                   nickname="test", title="test", company="test",
    #                   address="test", homephone="test", mobilephone="test",
    #                   workphone="test", fax="test", email="test", email2="test",
    #                   email3="test", homepage="test",
    #                   bdate=ContactDate(1, "January", 2001),
    #                   adate=ContactDate(2, "February", 2002),
    #                   address2="test", secondaryphone="test", notes="test")
    #contact.id = old_contacts[index].id


    app.contact.modify_contact_by_id(contact.id, contact)
    #assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    #old_contacts[index] = contact

    for c in old_contacts:
        if c.id == contact.id:
            c = contact
            break

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
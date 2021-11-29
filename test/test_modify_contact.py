from model import Contact
from model import ContactDate


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", middlename="test", lastname="test",
                                             nickname="test", title="test", company="test",
                                             address="test", homephone="test", mobilephone="test",
                                             workphone="test", fax="test", email="test", email2="test",
                                             email3="test", homepage="test",
                                             bdate=ContactDate(1, "January", 2001),
                                             adate=ContactDate(2, "February", 2002),
                                             address2="test", phone2="test", notes="test")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

from model import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)

    #index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_index(index)

    app.contact.delete_contact_by_id(contact.id)
    #assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()

    #old_contacts[index:index+1] = []
    old_contacts.remove(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
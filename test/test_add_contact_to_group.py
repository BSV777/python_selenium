from model import Contact
from model import Group
import random


def test_add_contact_to_group(app, db, orm):

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)

    app.contact.add_contact_to_group(contact.id, group.id)

    assert contact in orm.get_contacts_in_group(group)

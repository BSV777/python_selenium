from model import Contact
from model import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = orm.get_group_list()
    group = random.choice(groups)

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))

    contacts = orm.get_contacts_not_in_group(group)

    if len(contacts) == 0:
        contacts = orm.get_contacts_in_group(group)
        contact = random.choice(contacts)
        app.contact.remove_contact_from_group(contact.id, group.id)
        contacts = orm.get_contacts_not_in_group(group)

    contact = random.choice(contacts)

    app.contact.add_contact_to_group(contact.id, group.id)

    assert contact in orm.get_contacts_in_group(group)

from model import Contact
from model import Group
import random


def test_remove_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    groups = orm.get_groups_by_contact(contact)
    if len(groups) == 0:
        group = random.choice(orm.get_group_list())
        app.contact.add_contact_to_group(contact.id, group.id)
        groups = orm.get_groups_by_contact(contact)

    group = random.choice(groups)

    app.contact.remove_contact_from_group(contact.id, group.id)
    print("contact.id =", contact.id, "group.id =", group.id)
    assert contact in orm.get_contacts_not_in_group(group)
    #assert contact not in orm.get_contacts_in_group(group)
    #assert False

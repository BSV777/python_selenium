import re
#from random import randrange
from model.contact import Contact


def test_data_on_home_page(app, db):
    old_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)

    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    #index = randrange(len(old_contacts))

    for i, contact_from_db in enumerate(old_contacts):
        assert contacts_from_home_page[i].lastname == contact_from_db.lastname
        assert contacts_from_home_page[i].firstname == contact_from_db.firstname
        assert contacts_from_home_page[i].address == contact_from_db.address.strip()
        print("HP_email", contacts_from_home_page[i].all_emails_from_home_page)
        print("DB_email", merge_emails_like_on_homepage(contact_from_db))
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_homepage(contact_from_db)
        # print("HP_phone", contacts_from_home_page[i].all_phones_from_home_page)
        # print("DB_phone", merge_phones_like_on_homepage(contact_from_db))
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_homepage(contact_from_db)

        # contact_from_home_page = db.get_contact_list()[index]
        # contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        # assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        # assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        # assert contact_from_home_page.address == contact_from_edit_page.address.strip()
        # assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_homepage(contact_from_edit_page)
        # assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_homepage(contact_from_edit_page)

# def test_phones_on_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear_phone(s):
    s = re.sub(" ", "", s)
    return re.sub("[()-]/.", "", s)

def clear_email(s):
    s = re.sub(" ", "", s)
    return re.sub("[()]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

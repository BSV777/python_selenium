from model import Contact
from model import ContactDate


def test_modify_firsе_contact(app):
    app.contact.modify_first_contact(Contact(firstname="test", middlename="test", lastname="test",
                                             nickname="test", title="test", company="test",
                                             address="test", homephone="test", mobilephone="test",
                                             workphone="test", fax="test", email="test", email2="test",
                                             email3="test", homepage="test",
                                             bdate=ContactDate(1, "January", 2001),
                                             adate=ContactDate(2, "February", 2002),
                                             address2="test", phone2="test", notes="test"))


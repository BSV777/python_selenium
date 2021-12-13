from model import Contact
from model import ContactDate


testdata = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    title="title1", company="company1", address="address1", homephone="homephone1",
                    mobilephone="mobilephone1", workphone="workphone1", fax="fax1", email="email1",
                    email2="email21", email3="email31", homepage="homepage1", bdate=ContactDate("1", "January", "2021"),
                    adate=ContactDate("1", "January", "2021"), address2="address21",
                    secondaryphone="secondaryphone1", notes="notes1"),
            Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
                    title="title2", company="company2", address="address2", homephone="homephone2",
                    mobilephone="mobilephone2", workphone="workphone2", fax="fax2", email="email2",
                    email2="email22", email3="email32", homepage="homepage2", bdate=ContactDate("2", "January", "2022"),
                    adate=ContactDate("2", "January", "2022"), address2="address22",
                    secondaryphone="secondaryphone1", notes="notes2")
            ]

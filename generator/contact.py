from model import Contact
from model import ContactDate
import random
import string
import json
import os.path
import getopt
import sys
import jsonpickle
import calendar


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    sysmbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(sysmbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                       address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                       email3="", homepage="", bdate=ContactDate("-", "-", ""), adate=ContactDate("-", "-", ""),
                       address2="", secondaryphone="", notes="", all_phones_from_home_page="",
                       all_emails_from_home_page="")] +\
           [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("name", 10), company=random_string("name", 10),
                    address=random_string("address", 10), homephone=random_string("homephone", 10),
                    mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10),
                    email2=random_string("email2", 10), email3=random_string("email3", 10),
                    homepage=random_string("homepage", 10),
                    bdate=ContactDate(random.randint(1, 31), calendar.month_name[random.randint(1, 12)],
                                      random.randint(1900, 2100)),
                    adate=ContactDate(random.randint(1, 31), calendar.month_name[random.randint(1, 12)],
                                      random.randint(1900, 2100)),
                    address2=random_string("address2", 10), secondaryphone=random_string("secondaryphone", 10),
                    notes=random_string("notes", 10), all_phones_from_home_page="", all_emails_from_home_page="")
            for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


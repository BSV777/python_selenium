from model import Group
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    sysmbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(sysmbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + \
           [Group(name=random_string("name", 10), header=random_string("header", 20),
                  footer=random_string("footer", 20)) for i in range(n)]

# testdata = [Group(name=name, header=header, footer=footer)
#             for name in ["", random_string("name", 10)]
#             for header in ["", random_string("header", 10)]
#             for footer in ["", random_string("footer", 10)]]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

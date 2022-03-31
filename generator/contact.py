from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "../data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_email(prefix, max_len):
    email_suffix = ["@test.com", "@test.ru"]
    index = random.randrange(len(email_suffix))
    name = "".join(random.choice(string.ascii_letters + string.digits) for i in range(max_len))
    email = name + email_suffix[index]
    return prefix + email


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
            company="", address="", home_phone="", work_phone="", mobile_phone="",
            email1="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 8),
            lastname=random_string("lastname", 8),
            nickname=random_string("nickname", 5), title=random_string("title", 8),
            company=random_string("company", 10), address=random_string("address", 13),
            home_phone=random_string("23", 4), work_phone=random_string("38", 4),
            mobile_phone=random_string("+79", 9), email1=random_email("email1", 6),
            email2=random_email("email2", 6), email3=random_email("email3", 6))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

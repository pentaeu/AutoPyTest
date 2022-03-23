from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_email(prefix, max_len):
    email_suffix = ["@test.com", "@test.ru"]
    index = random.randrange(len(email_suffix))
    name = "".join(random.choice(string.ascii_letters + string.digits) for i in range(max_len))
    email = name + email_suffix[index]
    return prefix + email


testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address, email1=email1,mobile_phone=mobile_phone)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 5)]
    for address in ["", random_string("address", 7)]
    for email1 in ["", random_email("email1", 7)]
    for mobile_phone in ["", random_string("+79", 7)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

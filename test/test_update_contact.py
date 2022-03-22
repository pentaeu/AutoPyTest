from model.contact import Contact
from random import randrange


def test_update_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="adawd", lastname="Bybadad", mobile_phone="+7934123455",
                                   work_phone="306312", home_phone="342321", email1="email1@test.com",
                                   email2="email2@test.com", email3="email3@test.com", address="test_street"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="newname", lastname="new_lastname")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_update_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="forupdate"))
#     app.contact.edit_first_contact(Contact(email="email@email.com"))


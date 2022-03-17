from model.contact import Contact


def test_update_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="forupdate"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="2131")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_update_contact_email(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="forupdate"))
#     app.contact.edit_first_contact(Contact(email="email@email.com"))


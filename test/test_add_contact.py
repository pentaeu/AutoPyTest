from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="adawd", lastname="Bybadad", mobilephone="+7934123455", workphone="306312",
                      homephone="342321")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

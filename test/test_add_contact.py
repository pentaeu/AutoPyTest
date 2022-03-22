from model.contact import Contact

    
def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="ContactName", lastname="ContactLastName", mobile_phone="+7934123455",
                      work_phone="306312", home_phone="342321", email1="email1@test.com", email2="email2@test.com",
                      email3="email3@test.com", address="test_street")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

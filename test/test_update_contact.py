from model.contact import Contact


def test_update_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="2131"))


def test_update_contact_email(app):
    app.contact.edit_first_contact(Contact(email="email@email.com"))


from model.contact import Contact


def test_update_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="forupdate"))
    app.contact.edit_first_contact(Contact(firstname="2131"))


def test_update_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="forupdate"))
    app.contact.edit_first_contact(Contact(email="email@email.com"))


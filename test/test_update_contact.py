from model.contact import Contact


def test_update_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="2131"))
    app.session.logout()

def test_update_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email="email@email.com"))
    app.session.logout()

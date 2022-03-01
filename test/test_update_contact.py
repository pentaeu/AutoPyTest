
def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(firstname="123123123")
    app.session.logout()

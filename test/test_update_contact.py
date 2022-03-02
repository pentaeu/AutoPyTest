from model.contact import Contact


def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="2131", middlename="3123", lastname="1233", nickname="12334",
                                     company="333", address="awdf", email="awd@awdaw"))
    app.session.logout()

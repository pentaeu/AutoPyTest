# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="adawd", middlename="adaw", lastname="dfdfgfg", nickname="dfg",
                               company="adasda", address="fsdfsdf", email="adad@test.com"))
    app.session.logout()

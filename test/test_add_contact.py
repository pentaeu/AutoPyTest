# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application_contact import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.driver_quit)
    return fixture

    
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="adawd", middlename="adaw", lastname="dfdfgfg", nickname="dfg",
                                        company="adasda", address="fsdfsdf", email="adad@test.com"))
    app.logout()

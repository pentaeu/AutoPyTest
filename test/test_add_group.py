# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.driver_quit)
    return fixture

    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="awdawd", header="awda", footer="awdad"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

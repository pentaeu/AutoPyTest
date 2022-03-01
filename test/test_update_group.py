from model.group import Group


def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="a3123d", header="dddd", footer="dfggf"))
    app.session.logout()

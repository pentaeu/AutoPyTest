from model.group import Group


def test_update_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="a3123d"))
    app.session.logout()


def test_update_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="HEEEAADER"))
    app.session.logout()

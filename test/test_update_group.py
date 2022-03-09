from model.group import Group


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="updatefor"))
    app.group.edit_first_group(Group(name="a3123d"))


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="updatefor"))
    app.group.edit_first_group(Group(header="HEEEAADER"))


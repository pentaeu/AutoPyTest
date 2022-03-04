from model.group import Group


def test_update_group_name(app):
    app.group.edit_first_group(Group(name="a3123d"))


def test_update_group_header(app):
    app.group.edit_first_group(Group(header="HEEEAADER"))


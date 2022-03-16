from model.group import Group


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="updatefor"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="a3123d"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="updatefor"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="HEEEAADER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dellele"))
    app.group.delete_first_group()


from model.group import Group
from random import randrange


def test_update_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="SomeGroupForUpdate"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="UpdatedGroupName")
    group.group_id = old_groups[index].group_id
    app.group.edit_group_by_id(group.group_id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

from model.group import Group
from random import randrange
import allure


def test_update_group_name(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="SomeGroupForUpdate"))
    with allure.step('Given a random group from the list'):
        old_groups = db.get_group_list()
        index = randrange(len(old_groups))
        group = Group(name="UpdatedGroupName")
        group.id = old_groups[index].id
    with allure.step(f'When I edit group {group} from the list'):
        app.group.edit_group_by_id(group.id, group)
    with allure.step('Then the new group list is equal to the old list group with the edited group'):
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

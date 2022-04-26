from model.group import Group
import random
import allure


def test_del_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="SomeGroupForDelete"))
    with allure.step('Given a random group from the list'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step(f'When I delete group {group} from the list'):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list group without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

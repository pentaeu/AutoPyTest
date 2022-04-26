from model.contact import Contact
from model.group import Group
import random
import allure


def test_add_contact_to_group(app, db, orm):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="SomeGroupForContact"))
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="SomeContactForGroup"))
    with allure.step('Given a random group from the list'):
        group = random.choice(db.get_group_list())
    with allure.step(f'Given a contact not in group {group}'):
        if len(orm.get_contacts_not_in_group(group)) == 0:
            db.delete_all_contacts_from_group(group.id)
        contact = random.choice(orm.get_contacts_not_in_group(group))
    with allure.step(f'Then I add contact {contact} to the group {group}'):
        app.contact.add_contact_to_group_by_id(contact.id, group.id)
    with allure.step('Then the new contact list is equal to the new contact list with added contact to the group'):
        contacts_in_group = orm.get_contacts_in_group(group)
        assert contact in contacts_in_group

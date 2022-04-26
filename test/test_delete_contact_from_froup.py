from model.contact import Contact
from model.group import Group
import random
import allure


def test_del_contact_from_group(app, db, orm):
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="SomeGroupForContact"))
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="SomeContactForGroup"))
    with allure.step('Given a random group from the list'):
        group = random.choice(db.get_group_list())
    with allure.step('Given a random contact from the list'):
        contact = random.choice(db.get_contact_list())
    with allure.step(f'Then I delete contacts from the group {group}'):
        db.delete_contacts_from_groups()
    with allure.step(f'Then I add contact {contact} to the group {group}'):
        db.add_contact_to_group_by_id(contact.id, group.id)
    with allure.step(f'Then I delete contact {contact} from the group {group}'):
        app.contact.delete_contact_from_group(contact.id, group.id)
    with allure.step('Then the new contacts in group list is equal to the old contacts in group '
                     'list without the deleted contact'):
        assert orm.get_contacts_in_group(Group(id=group.id)) == []

from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="SomeGroupForContact"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="SomeContactForGroup"))
    groups = db.get_groups_with_contacts()
    group_id = random.choice(groups)
    contacts = orm.get_contacts_in_group(Group(id=group_id))
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(contact.id, group_id)
    assert contact in orm.get_contacts_not_in_group(Group(id=group_id))

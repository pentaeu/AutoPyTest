from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="SomeGroupForContact"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="SomeContactForGroup"))
    group = random.choice(db.get_group_list())
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group_by_id(contact.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group

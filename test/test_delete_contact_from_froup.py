from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="SomeGroupForContact"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="SomeContactForGroup"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    db.delete_contacts_from_groups()
    db.add_contact_to_group_by_id(contact.id, group.id)
    app.contact.delete_contact_from_group(contact.id, group.id)
    assert orm.get_contacts_in_group(Group(id=group.id)) == []

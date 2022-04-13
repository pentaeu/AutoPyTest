from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random
import re

db_orm = ORMFixture(host="127.0.0.1",
                    name="addressbook",
                    user="root",
                    password="")


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="SomeGroupForDelete"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="SomeContactForDelete"))
    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    db.add_contact_to_group_by_id(contact.id, group.group_id)
    app.contact.delete_contact_from_group(contact.id, group.group_id)
    assert clear(str(contact)) not in db_orm.get_contacts_in_group(Group(group_id=group.group_id))


def clear(s):
    return re.sub("[\[\]]", "", s)

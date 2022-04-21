from fixture.orm import ORMFixture
from model.group import Group

db1 = ORMFixture(host="127.0.0.1",
                name="addressbook",
                user="root",
                password="")

try:
    l = db1.get_contacts_in_group(Group(id='47'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()

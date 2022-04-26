import random
from model.contact import Contact
import allure


def test_del_contact(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="Some_contact_for_delete"))
    with allure.step('Given a random contact from the list'):
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with allure.step(f'When I delete contact {contact} from the list'):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step('Then the new contact list is equal to the old list contact without the deleted contact'):
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)




from model.contact import Contact
from random import randrange
import allure


def test_update_contact_by_index(app, db, check_ui):
    with allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="ContactName", lastname="ContactLastName", mobile_phone="+7934123455",
                                       work_phone="306312", home_phone="342321", email1="email1@test.com",
                                       email2="email2@test.com", email3="email3@test.com", address="test_street"))
    with allure.step('Given a random contact from the list'):
        old_contacts = db.get_contact_list()
        index = randrange(len(old_contacts))
        contact = Contact(firstname="UpdatedName", lastname="UpdatedLastName")
        contact.id = old_contacts[index].id
    with allure.step(f'When I edit contact {contact} from the list'):
        app.contact.edit_contact_by_id(contact.id, contact)
    with allure.step('Then the new contact list is equal to the old list contact with the edited contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)

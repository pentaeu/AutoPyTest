from model.contact import Contact
import re
import allure


# def test_all_data_on_home_page(app, db):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create(Contact(firstname="ContactName", lastname="ContactLastName", mobile_phone="+7934123455",
#                                    work_phone="306312", home_phone="342321", email1="email1@test.com",
#                                    email2="email2@test.com", email3="email3@test.com", address="test_street"))
#     all_data_on_page_home = app.contact.get_contact_list()
#     index = randrange(len(all_data_on_page_home))
#     contact_data_from_home_page = all_data_on_page_home[index]
#     contact_data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_data_from_home_page.id == contact_data_from_edit_page.id
#     assert contact_data_from_home_page.lastname == contact_data_from_edit_page.lastname
#     assert contact_data_from_home_page.firstname == contact_data_from_edit_page.firstname
#     assert contact_data_from_home_page.address == contact_data_from_edit_page.address
#     assert contact_data_from_home_page.all_phones_from_home_page == merge_phones(contact_data_from_edit_page)
#     assert contact_data_from_home_page.all_emails_from_home_page == merge_emails(contact_data_from_edit_page)


def test_all_contacts_on_home_page(app, db):
    with allure.step('Given a contacts data in DB'):
        contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Given a contacts data in UI'):
        contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    with allure.step('Then DB contact list is equal to the UI contact list'):
        assert len(contacts_ui) == len(contacts_db)
        for item in range(0, len(contacts_db)):
            contact_from_home_page = contacts_ui[item]
            contact_list_db = contacts_db[item]
            assert contact_from_home_page.id == contact_list_db.id
            assert contact_from_home_page.firstname == contact_list_db.firstname
            assert contact_from_home_page.lastname == contact_list_db.lastname
            assert contact_from_home_page.address == contact_list_db.address
            assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_list_db)
            assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_list_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))
